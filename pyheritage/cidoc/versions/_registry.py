# -*- coding: utf-8 -*-

"""Version registry — maps CRM core versions to their implementation modules;

"""

import types

from pyheritage.cidoc.versions._resolver import VersionMatrixResolver


__all__ = ('VersionNotImplemented', )


_IMPLEMENTED_VERSIONS: frozenset[str] = frozenset({"7.0"})

_resolver = VersionMatrixResolver()


class VersionNotImplemented(LookupError):
    """CRM core version is recognised by the matrix but not yet implemented;

    Raised when a CRM core version (e.g. 7.1.2) is present in the compatibility matrix but there is
    no ``versions/v{xx}/`` package with concrete entity/property classes yet;

    """
