"""
XMLAbstracts moved back to packtools.sps.models.v2.abstract.

PR #1180 (2026-05) moved it here believing it was used only by validation
code; that premise was wrong (scms-upload's TOC builder consumes it
directly for presentation data via packtools.sps.models.v2.abstract, not
for validation). Kept as a compatibility redirect only: this module
should not gain new logic, since the class itself carries no
validation-rule/expected-value concerns and doesn't belong here.
"""
import warnings as _warnings


def __getattr__(name):
    _moved = {
        "XMLAbstracts": "packtools.sps.models.v2.abstract",
    }
    if name in _moved:
        import importlib
        _warnings.warn(
            f"{name} has moved to {_moved[name]}. "
            f"Importing from packtools.sps.validation.models.abstract is deprecated.",
            DeprecationWarning,
            stacklevel=2,
        )
        mod = importlib.import_module(_moved[name])
        return getattr(mod, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
