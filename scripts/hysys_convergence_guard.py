from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Callable, Mapping


def _json_safe(value: object) -> object:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Mapping):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(item) for item in value]
    return repr(value)


@dataclass(frozen=True, slots=True)
class ConvergencePolicy:
    """Execution limits for a project-defined HYSYS convergence contract."""

    max_iterations: int = 12
    required_consecutive_passes: int = 2
    max_wall_time_s: float = 900.0
    max_repeated_failed_state: int = 3
    require_reopen_verification: bool = True

    def __post_init__(self) -> None:
        if self.max_iterations < 1:
            raise ValueError("max_iterations must be at least 1.")
        if self.required_consecutive_passes < 2:
            raise ValueError("required_consecutive_passes must be at least 2.")
        if self.max_wall_time_s <= 0:
            raise ValueError("max_wall_time_s must be positive.")
        if self.max_repeated_failed_state < 1:
            raise ValueError("max_repeated_failed_state must be at least 1.")


@dataclass(frozen=True, slots=True)
class ConvergenceObservation:
    """One fail-closed readback against an approved acceptance contract.

    Each required check must be True to pass. False means failed; None means
    missing or ambiguous and therefore also fails. The caller owns the
    engineering definitions and tolerances behind these checks.
    """

    checks: Mapping[str, bool | None]
    metrics: Mapping[str, object] = field(default_factory=dict)
    note: str = ""
    state_key: str | None = None

    def __post_init__(self) -> None:
        if not self.checks:
            raise ValueError("At least one project-defined convergence check is required.")
        invalid = [
            name
            for name, value in self.checks.items()
            if not isinstance(name, str)
            or not name.strip()
            or not (value is True or value is False or value is None)
        ]
        if invalid:
            raise ValueError(f"Invalid convergence checks: {invalid}")

    @property
    def passed(self) -> bool:
        return all(value is True for value in self.checks.values())

    @property
    def failed_checks(self) -> tuple[str, ...]:
        return tuple(name for name, value in self.checks.items() if value is not True)


@dataclass(frozen=True, slots=True)
class ConvergenceIteration:
    iteration: int
    passed: bool
    consecutive_passes: int
    checks: dict[str, bool | None]
    metrics: dict[str, object]
    note: str
    state_key: str | None
    action: str
    elapsed_s: float

    def to_dict(self) -> dict[str, object]:
        return {
            "iteration": self.iteration,
            "passed": self.passed,
            "consecutive_passes": self.consecutive_passes,
            "checks": _json_safe(self.checks),
            "metrics": _json_safe(self.metrics),
            "note": self.note,
            "state_key": self.state_key,
            "action": self.action,
            "elapsed_s": self.elapsed_s,
        }


@dataclass(frozen=True, slots=True)
class ConvergenceResult:
    accepted: bool
    stop_reason: str
    iterations: tuple[ConvergenceIteration, ...]
    error: str | None = None

    def require_accepted(self) -> "ConvergenceResult":
        if not self.accepted:
            raise RuntimeError(
                f"HYSYS convergence was not accepted: {self.stop_reason}"
            )
        return self

    def to_dict(self) -> dict[str, object]:
        return {
            "accepted": self.accepted,
            "stop_reason": self.stop_reason,
            "error": self.error,
            "iterations": [item.to_dict() for item in self.iterations],
        }


CycleCallback = Callable[[int], None]
ObserveCallback = Callable[[int], ConvergenceObservation]
AdjustCallback = Callable[[int, ConvergenceObservation], bool]
ReopenCallback = Callable[[], None]
ReopenObserveCallback = Callable[[], ConvergenceObservation]


def run_convergence_loop(
    *,
    cycle_and_wait: CycleCallback,
    observe: ObserveCallback,
    adjust: AdjustCallback | None = None,
    reopen_and_wait: ReopenCallback | None = None,
    observe_reopened: ReopenObserveCallback | None = None,
    policy: ConvergencePolicy | None = None,
) -> ConvergenceResult:
    """Run solve/read/evaluate/adjust cycles until a verified terminal state.

    ``cycle_and_wait`` may trigger a solve or continuation step, but reaching
    solver idle is never treated as convergence. ``observe`` must read the
    project-approved checks after every cycle. ``adjust`` may change only
    approved variables and returns True only when it actually applied a safe
    bounded change. Callback errors and missing evidence fail closed.
    """

    active_policy = policy or ConvergencePolicy()
    started = time.monotonic()
    history: list[ConvergenceIteration] = []
    consecutive_passes = 0
    repeated_failed_state = 0
    previous_failed_state: str | None = None

    def failure(reason: str, error: Exception | None = None) -> ConvergenceResult:
        return ConvergenceResult(
            accepted=False,
            stop_reason=reason,
            iterations=tuple(history),
            error=None if error is None else f"{type(error).__name__}: {error}",
        )

    for iteration in range(1, active_policy.max_iterations + 1):
        elapsed = time.monotonic() - started
        if elapsed > active_policy.max_wall_time_s:
            return failure("wall_time_limit")

        try:
            cycle_and_wait(iteration)
        except Exception as exc:
            return failure("cycle_or_wait_error", exc)

        try:
            observation = observe(iteration)
        except Exception as exc:
            return failure("readback_or_evaluation_error", exc)

        if not isinstance(observation, ConvergenceObservation):
            return failure("invalid_observation_type")

        if observation.passed:
            consecutive_passes += 1
            previous_failed_state = None
            repeated_failed_state = 0
            action = (
                "accept"
                if consecutive_passes >= active_policy.required_consecutive_passes
                else "confirm_stability"
            )
        else:
            consecutive_passes = 0
            action = "adjust_or_stop"
            if observation.state_key is not None:
                if observation.state_key == previous_failed_state:
                    repeated_failed_state += 1
                else:
                    previous_failed_state = observation.state_key
                    repeated_failed_state = 1

        history.append(
            ConvergenceIteration(
                iteration=iteration,
                passed=observation.passed,
                consecutive_passes=consecutive_passes,
                checks=dict(observation.checks),
                metrics=dict(observation.metrics),
                note=observation.note,
                state_key=observation.state_key,
                action=action,
                elapsed_s=round(time.monotonic() - started, 6),
            )
        )

        if observation.passed:
            if consecutive_passes >= active_policy.required_consecutive_passes:
                if not active_policy.require_reopen_verification:
                    return ConvergenceResult(
                        accepted=True,
                        stop_reason="required_consecutive_passes_reached",
                        iterations=tuple(history),
                    )
                if reopen_and_wait is None or observe_reopened is None:
                    return failure("reopen_verification_required")
                try:
                    reopen_and_wait()
                except Exception as exc:
                    return failure("reopen_error", exc)
                try:
                    reopened = observe_reopened()
                except Exception as exc:
                    return failure("reopened_readback_or_evaluation_error", exc)
                if not isinstance(reopened, ConvergenceObservation):
                    return failure("invalid_reopened_observation_type")
                history.append(
                    ConvergenceIteration(
                        iteration=iteration + 1,
                        passed=reopened.passed,
                        consecutive_passes=(
                            consecutive_passes + 1 if reopened.passed else 0
                        ),
                        checks=dict(reopened.checks),
                        metrics=dict(reopened.metrics),
                        note=reopened.note,
                        state_key=reopened.state_key,
                        action="accept_reopened" if reopened.passed else "reject_reopened",
                        elapsed_s=round(time.monotonic() - started, 6),
                    )
                )
                if not reopened.passed:
                    return failure("reopened_checks_failed")
                return ConvergenceResult(
                    accepted=True,
                    stop_reason="reopened_contract_passed",
                    iterations=tuple(history),
                )
            continue

        if repeated_failed_state >= active_policy.max_repeated_failed_state:
            return failure("repeated_failed_state_without_progress")

        if adjust is None:
            return failure("failed_checks_without_adjustment")

        try:
            changed = bool(adjust(iteration, observation))
        except Exception as exc:
            return failure("adjustment_error", exc)
        if not changed:
            return failure("adjustment_declined_or_no_change")

    return failure("iteration_limit")
