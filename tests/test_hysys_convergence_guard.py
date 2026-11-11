from __future__ import annotations

import sys
import json
import unittest
from unittest.mock import Mock, patch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from hysys_convergence_guard import (  # noqa: E402
    ConvergenceObservation,
    ConvergencePolicy,
    run_convergence_loop,
)


def passing_observation() -> ConvergenceObservation:
    return ConvergenceObservation(
        checks={
            "solver_idle": True,
            "required_recycles_active": True,
            "tear_residuals_within_approved_tolerance": True,
            "mass_energy_closure": True,
            "required_kpis_valid": True,
        },
        metrics={"sample_residual": 0.0},
        state_key="pass",
    )


class ConvergenceGuardTests(unittest.TestCase):
    def test_one_pass_is_not_enough(self) -> None:
        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=tuple(passing_observation().checks)),
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: passing_observation(),
            reopen_and_wait=lambda: None,
            observe_reopened=passing_observation,
        )

        self.assertTrue(result.accepted)
        self.assertEqual(len(result.iterations), 3)
        self.assertEqual(result.iterations[0].action, "confirm_stability")
        self.assertEqual(result.iterations[1].action, "accept")
        self.assertEqual(result.iterations[2].action, "accept_reopened")

    def test_failed_readback_adjusts_then_requires_two_passes(self) -> None:
        observations = iter(
            [
                ConvergenceObservation(
                    checks={
                        "solver_idle": True,
                        "required_recycles_active": False,
                        "tear_residuals_within_approved_tolerance": False,
                    },
                    state_key="recycle-not-closed",
                ),
                passing_observation(),
                passing_observation(),
            ]
        )
        adjustments: list[int] = []

        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=tuple(passing_observation().checks)),
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: next(observations),
            adjust=lambda iteration, _observation: not adjustments.append(iteration),
            reopen_and_wait=lambda: None,
            observe_reopened=passing_observation,
        )

        self.assertTrue(result.accepted)
        self.assertEqual(adjustments, [1])
        self.assertEqual(len(result.iterations), 4)

    def test_consecutive_passes_without_reopen_are_not_accepted(self) -> None:
        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=tuple(passing_observation().checks)),
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: passing_observation(),
        )

        self.assertFalse(result.accepted)
        self.assertEqual(result.stop_reason, "reopen_verification_required")

    def test_missing_check_fails_closed(self) -> None:
        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=("solver_idle", "tear_residuals_within_approved_tolerance")),
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: ConvergenceObservation(
                checks={
                    "solver_idle": True,
                    "tear_residuals_within_approved_tolerance": None,
                }
            ),
        )

        self.assertFalse(result.accepted)
        self.assertEqual(result.stop_reason, "failed_checks_without_adjustment")

    def test_repeated_failed_state_stops_without_false_success(self) -> None:
        policy = ConvergencePolicy(
            required_checks=("required_recycles_active",),
            max_iterations=10,
            max_repeated_failed_state=2,
        )
        result = run_convergence_loop(
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: ConvergenceObservation(
                checks={"required_recycles_active": False},
                state_key="same-failed-state",
            ),
            adjust=lambda _iteration, _observation: True,
            policy=policy,
        )

        self.assertFalse(result.accepted)
        self.assertEqual(result.stop_reason, "repeated_failed_state_without_progress")
        self.assertEqual(len(result.iterations), 2)

    def test_callback_error_is_a_failed_terminal_state(self) -> None:
        def fail_cycle(_iteration: int) -> None:
            raise TimeoutError("solver did not become idle")

        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=("solver_idle",)),
            cycle_and_wait=fail_cycle,
            observe=lambda _iteration: passing_observation(),
        )

        self.assertFalse(result.accepted)
        self.assertEqual(result.stop_reason, "cycle_or_wait_error")
        self.assertIn("TimeoutError", result.error or "")

    def test_audit_result_is_json_serializable(self) -> None:
        result = run_convergence_loop(
            policy=ConvergencePolicy(required_checks=("approved_contract",)),
            cycle_and_wait=lambda _iteration: None,
            observe=lambda _iteration: ConvergenceObservation(
                checks={"approved_contract": True},
                metrics={"opaque_runtime_value": object()},
            ),
            reopen_and_wait=lambda: None,
            observe_reopened=lambda: ConvergenceObservation(
                checks={"approved_contract": True}
            ),
        )

        payload = json.dumps(result.to_dict())
        self.assertIn("opaque_runtime_value", payload)

    def run_fixture(self, **overrides):
        args = dict(
            policy=ConvergencePolicy(required_checks=("solver_idle", "closure")),
            cycle_and_wait=lambda _: None,
            observe=lambda _: ConvergenceObservation(checks={"solver_idle": True, "closure": True}),
            reopen_and_wait=lambda: None,
            observe_reopened=lambda: ConvergenceObservation(checks={"solver_idle": True, "closure": True}),
        )
        args.update(overrides)
        return run_convergence_loop(**args)

    def test_missing_contract_stops_before_solver(self):
        cycle = Mock()
        result = self.run_fixture(policy=ConvergencePolicy(), cycle_and_wait=cycle)
        self.assertEqual(result.stop_reason, "acceptance_contract_required")
        cycle.assert_not_called()

    def test_omitted_required_check_is_audited_as_missing(self):
        result = self.run_fixture(observe=lambda _: ConvergenceObservation(checks={"solver_idle": True}))
        self.assertFalse(result.accepted)
        self.assertIsNone(result.iterations[0].checks["closure"])

    def test_reopened_contract_cannot_shrink(self):
        result = self.run_fixture(observe_reopened=lambda: ConvergenceObservation(checks={"solver_idle": True}))
        self.assertEqual(result.stop_reason, "reopened_checks_failed")
        self.assertIsNone(result.iterations[-1].checks["closure"])

    def test_reopen_cannot_be_disabled_for_acceptance(self):
        cycle = Mock()
        result = self.run_fixture(policy=ConvergencePolicy(
            required_checks=("solver_idle",), require_reopen_verification=False), cycle_and_wait=cycle)
        self.assertFalse(result.accepted)
        self.assertEqual(result.stop_reason, "reopen_verification_required")
        cycle.assert_not_called()

    def test_expired_callbacks_cannot_result_in_acceptance(self):
        for phase in ("cycle", "observe", "reopen", "observe_reopened"):
            now = [0.0]
            def expire(result=None):
                now[0] = 2.0
                return result
            good = ConvergenceObservation(checks={"solver_idle": True, "closure": True})
            replacements = {
                "cycle": {"cycle_and_wait": lambda _: expire()},
                "observe": {"observe": lambda _: expire(good)},
                "reopen": {"reopen_and_wait": expire},
                "observe_reopened": {"observe_reopened": lambda: expire(good)},
            }
            with self.subTest(phase=phase), patch("hysys_convergence_guard.time.monotonic", side_effect=lambda: now[0]):
                result = self.run_fixture(policy=ConvergencePolicy(
                    required_checks=("solver_idle", "closure"), max_wall_time_s=1), **replacements[phase])
                self.assertFalse(result.accepted)
                self.assertEqual(result.stop_reason, "wall_time_limit")

    def test_final_failed_iteration_does_not_write_an_unchecked_adjustment(self):
        adjust = Mock(return_value=True)
        result = self.run_fixture(policy=ConvergencePolicy(required_checks=("closure",), max_iterations=1),
            observe=lambda _: ConvergenceObservation(checks={"closure": False}), adjust=adjust)
        self.assertEqual(result.stop_reason, "iteration_limit")
        adjust.assert_not_called()

    def test_invalid_contract_and_limits_are_rejected(self):
        for kwargs in ({"max_iterations": True}, {"max_wall_time_s": float("nan")},
                       {"max_wall_time_s": float("inf")}, {"required_checks": "closure"},
                       {"required_checks": ("closure", "closure")}, {"required_checks": ("",)}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                ConvergencePolicy(**kwargs)


if __name__ == "__main__":
    unittest.main()
