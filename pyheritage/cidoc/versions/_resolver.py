# -*- coding: utf-8 -*-

"""VersionMatrixResolver — compatibility matrix between CRM core versions and extensions;

"""


from typing import ClassVar


__all__ = ('ExtensionNotAvailable', 'VersionMatrixResolver', 'VersionNotSupported', )


class VersionNotSupported(LookupError):
    """Requested CRM core version is not supported;

    Raised when a CRM core version string is not present in the compatibility matrix;

    """


# ******************************************************************************************************************* #


class ExtensionNotAvailable(LookupError):
    """Extension is not available for the requested CRM core version;

    Raised when the compatibility matrix maps the extension to ``None``
    for the requested core version (e.g. CRMgeo on CRM 7.0);

    """


# ******************************************************************************************************************* #


class VersionMatrixResolver:
    """Matrix of compatible core-version → extension-version mappings;

    Maps each supported CRM core version to the compatible versions of each extension (archaeo, dig, sci, inf, geo);
    A value of None means the extension is not available for that core version;

    """

    _matrix: ClassVar[dict[str, dict[str, str | None]]] = {
        "7.0":   {"archaeo": None, "dig": None, "sci": None, "inf": None, "geo": None},
        "7.1.1": {"archaeo": None, "dig": None, "sci": None, "inf": None, "geo": None},
        "7.1.2": {"archaeo": "2.1.1", "dig": None, "sci": "2.0", "inf": None,
                  "geo": None, "tex": "2.0", "frbroo": "2.4"},
        "7.1.3": {"archaeo": None, "dig": "4.0", "sci": None, "inf": "1.0",
                  "geo": "1.2+2024", "lrmoo": "1.0", "act": "0.2",
                  "ba": "1.4", "presso": "1.3"},
    }
