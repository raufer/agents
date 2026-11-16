"""Native companion packages that may have no build for the running Python.

``livekit-blingfire`` and ``livekit-local-inference`` ship compiled wheels
only. On a Python they have no wheel for yet, they are not installed, the
modules that wrap them still import, and using them raises :func:`missing`'s
error instead.
"""

from __future__ import annotations

import sys


def missing(package: str) -> RuntimeError:
    """The error raised when ``package`` is used but has no build for this Python."""
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    return RuntimeError(f"{package} is not installed: it has no build for Python {version} yet")
