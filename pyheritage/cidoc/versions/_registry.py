# -*- coding: utf-8 -*-

"""Version registry — maps CRM core versions to their implementation modules;

Only known versions with a corresponding 'versions/v{xx}/' package are considered "implemented". All other
known versions raise 'VersionNotImplemented';

"""

import types

from pyheritage.cidoc.versions._resolver import VersionMatrixResolver


__all__ = ('VersionNotImplemented', 'get_version_module', )


_IMPLEMENTED_VERSIONS: frozenset[str] = frozenset({"7.0"})

_resolver = VersionMatrixResolver()


class VersionNotImplemented(LookupError):
    """CRM core version is recognised by the matrix but not yet implemented;

    Raised when a CRM core version (e.g. 7.1.2) is present in the compatibility matrix but there is
    no 'versions/v{xx}/' package with concrete entity/property classes yet;

    """


# ******************************************************************************************************************* #


def get_version_module(core_version: str) -> types.ModuleType:
    """Return the version module for *core_version*;

    Raises:
        VersionNotSupported if *core_version* is not in the compatibility matrix;
        VersionNotImplemented if *core_version* is known but not yet implemented;

    """
    if not _resolver.is_known(core_version):
        from pyheritage.cidoc.versions._resolver import VersionNotSupported
        raise VersionNotSupported(
            f"CRM version {core_version!r} is not supported"
        )

    if core_version not in _IMPLEMENTED_VERSIONS:
        formatted = ", ".join(sorted(_IMPLEMENTED_VERSIONS))
        raise VersionNotImplemented(
            f"CRM {core_version} is not implemented yet "
            f"(available: {formatted})"
        )

    from pyheritage.cidoc.versions import v70  # noqa: F811 — late import
    return v70
