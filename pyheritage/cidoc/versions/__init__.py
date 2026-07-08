# -*- coding: utf-8 -*-

"""CIDOC-CRM versioning package;

Provides version resolution for CIDOC CRM core and extensions;
Entry point: ``get_version_module(core_version)`` returns the versioned entities/properties module tree
for a given CRM core version;

Usage::

    from pyheritage.cidoc.versions import get_version_module
    mod = get_version_module("7.1.3")
    mod.entities.E1CRMEntity
    mod.properties.P1IsIdentifiedBy

The package also exports ``VersionMatrixResolver`` for resolving compatible extension versions
for a given core version;

"""


from pyheritage.cidoc.versions._registry import (
    get_version_module,
    VersionNotImplemented,
)
from pyheritage.cidoc.versions._resolver import (
    ExtensionNotAvailable,
    VersionMatrixResolver,
    VersionNotSupported,
)


__all__ = (
    'ExtensionNotAvailable',
    'VersionMatrixResolver',
    'VersionNotImplemented',
    'VersionNotSupported',
    'get_version_module',
)
