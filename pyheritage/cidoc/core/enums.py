# -*- coding: utf-8 -*-

"""CRM enums;

"""


from enum import Enum


__all__ = ('TimePrecision', 'SpatialFormat', )


class TimePrecision(str, Enum):
    """The accuracy level of the time primitive;

    It is determined by the python-edtf library or manually by the string format;

    """

    MILLENNIUM = "millennium"
    CENTURY = "century"
    DECADE = "decade"
    YEAR = "year"
    MONTH = "month"
    DAY = "day"
    DATETIME = "datetime"
    UNKNOWN = "unknown"


# ******************************************************************************************************************* #


class SpatialFormat(str, Enum):
    """Supported spatial formats;

    Used by E94SpatialPrimitive entity model;

    """

    WKT = "wkt"
    GEOJSON = "geojson"
    UNKNOWN = "unknown"
