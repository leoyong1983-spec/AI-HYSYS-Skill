"""Resolve one HYSYS version before any COM activation (no COM dependency)."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable


SUPPORTED_PROG_IDS = {
    "14": "HYSYS.Application.V14.0",
    "15": "HYSYS.Application.V15.0",
}


class HysysVersionError(RuntimeError):
    pass


@dataclass(frozen=True)
class HysysTarget:
    major: str
    prog_id: str
    clsid: str


def registry_value(path: str) -> str:
    import winreg

    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, path) as key:
        return str(winreg.QueryValueEx(key, "")[0])


def resolve_hysys_target(
    version: str = "auto",
    *,
    prog_id: str | None = None,
    registered_prog_id: str | None = None,
    read_registry: Callable[[str], str] = registry_value,
) -> HysysTarget:
    if version not in ("auto", *SUPPORTED_PROG_IDS):
        raise HysysVersionError("Supported HYSYS versions are auto, 14, and 15.")

    requested = set() if version == "auto" else {version}
    for override in (prog_id, registered_prog_id):
        if override in (None, "HYSYS.Application"):
            continue
        matches = [v for v, name in SUPPORTED_PROG_IDS.items() if name.lower() == override.lower()]
        if not matches:
            raise HysysVersionError(f"Unsupported HYSYS ProgID: {override}")
        requested.add(matches[0])
    if len(requested) > 1:
        raise HysysVersionError("Conflicting HYSYS version and ProgID selections.")

    installed = {}
    for major, name in SUPPORTED_PROG_IDS.items():
        try:
            clsid = read_registry(name + r"\CLSID").strip()
        except OSError:
            continue
        if clsid:
            installed[major] = HysysTarget(major, name, clsid)

    if requested:
        major = requested.pop()
        if major not in installed:
            raise HysysVersionError(f"HYSYS V{major} is not registered; no other version will be used.")
        return installed[major]

    try:
        default_clsid = read_registry(r"HYSYS.Application\CLSID").strip().lower()
    except OSError:
        default_clsid = ""
    matches = [target for target in installed.values() if target.clsid.lower() == default_clsid]
    if len(matches) == 1:
        return matches[0]
    if len(installed) == 1:
        return next(iter(installed.values()))
    if not installed:
        raise HysysVersionError("Neither HYSYS V14 nor V15 is registered.")
    raise HysysVersionError("Multiple HYSYS versions without a unique default; choose --hysys-version 14 or 15.")


def verify_reported_version(reported: str, target: HysysTarget) -> None:
    """Check the product major, retaining the full build string in run reports."""
    match = re.match(r"\s*(?:Aspen\s+)?(?:HYSYS\s+)?(?:Version\s+)?V?(14|15)(?=[.\s(]|$)", reported, re.IGNORECASE)
    if match is None:
        raise HysysVersionError(f"Cannot verify HYSYS product version from {reported!r}.")
    if match.group(1) != target.major:
        raise HysysVersionError(f"Requested HYSYS V{target.major}, but attached application reports {reported!r}.")
