# -*- coding: utf-8 -*-

"""VersionMatrixResolver — compatibility matrix between CRM core versions and extensions;

"""


__all__ = ('ExtensionNotAvailable', 'VersionNotSupported', )


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
