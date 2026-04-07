# -*- coding: utf-8 -*-

"""Tests for CIDOC-CRM enums;

"""


# pylint: disable=E0401,C0116,W0612


from enum import Enum

import pytest

from pyheritage.cidoc.enums import SpatialFormat, TimePrecision


class TestTimePrecision:
    """TimePrecision enum tests;

    """

    def test_time_precision_is_str_enum(self) -> None:
        """Checks that TimePrecision inherits from str and Enum;"""
        assert issubclass(TimePrecision, str)
        assert issubclass(TimePrecision, Enum)

    # ------------------------- #

    def test_time_precision_millennium(self) -> None:
        """Checks MILLENNIUM precision value;"""
        assert TimePrecision.MILLENNIUM.value == "millennium"
        assert TimePrecision.MILLENNIUM == "millennium"

    # ------------------------- #

    def test_time_precision_century(self) -> None:
        """Checks CENTURY precision value;"""
        assert TimePrecision.CENTURY.value == "century"
        assert TimePrecision.CENTURY == "century"

    # ------------------------- #

    def test_time_precision_decade(self) -> None:
        """Checks DECADE precision value;"""
        assert TimePrecision.DECADE.value == "decade"
        assert TimePrecision.DECADE == "decade"

    # ------------------------- #

    def test_time_precision_year(self) -> None:
        """Checks YEAR precision value;"""
        assert TimePrecision.YEAR.value == "year"
        assert TimePrecision.YEAR == "year"

    # ------------------------- #

    def test_time_precision_month(self) -> None:
        """Checks MONTH precision value;"""
        assert TimePrecision.MONTH.value == "month"
        assert TimePrecision.MONTH == "month"

    # ------------------------- #

    def test_time_precision_day(self) -> None:
        """Checks DAY precision value;"""
        assert TimePrecision.DAY.value == "day"
        assert TimePrecision.DAY == "day"

    # ------------------------- #

    def test_time_precision_datetime(self) -> None:
        """Checks DATETIME precision value;"""
        assert TimePrecision.DATETIME.value == "datetime"
        assert TimePrecision.DATETIME == "datetime"

    # ------------------------- #

    def test_time_precision_unknown(self) -> None:
        """Checks UNKNOWN precision value;"""
        assert TimePrecision.UNKNOWN.value == "unknown"
        assert TimePrecision.UNKNOWN == "unknown"

    # ------------------------- #

    def test_time_precision_all_members(self) -> None:
        """Checks that all expected members exist in TimePrecision;"""
        expected_members = [
            'MILLENNIUM',
            'CENTURY',
            'DECADE',
            'YEAR',
            'MONTH',
            'DAY',
            'DATETIME',
            'UNKNOWN',
        ]
        for member in expected_members:
            assert hasattr(TimePrecision, member)

    # ------------------------- #

    def test_time_precision_iteration(self) -> None:
        """Checks that TimePrecision can be iterated;"""
        members = list(TimePrecision)
        assert len(members) == 8
        assert TimePrecision.MILLENNIUM in members
        assert TimePrecision.UNKNOWN in members

    # ------------------------- #

    def test_time_precision_from_string(self) -> None:
        """Checks creation from string value;"""
        assert TimePrecision("year") == TimePrecision.YEAR
        assert TimePrecision("datetime") == TimePrecision.DATETIME

    # ------------------------- #

    def test_time_precision_invalid_string_raises(self) -> None:
        """Checks that invalid string raises ValueError;"""
        with pytest.raises(ValueError):
            TimePrecision("invalid_precision")

    # ------------------------- #

    def test_time_precision_string_comparison(self) -> None:
        """Checks that TimePrecision members compare equal to their string values;"""
        assert TimePrecision.YEAR == "year"
        assert "year" == TimePrecision.YEAR
        assert TimePrecision.DAY != "month"

    # ------------------------- #

    def test_time_precision_name_attribute(self) -> None:
        """Checks that name attribute returns member name;"""
        assert TimePrecision.YEAR.name == "YEAR"
        assert TimePrecision.MILLENNIUM.name == "MILLENNIUM"

    # ------------------------- #

    def test_time_precision_in_collection(self) -> None:
        """Checks membership testing in collections;"""
        assert TimePrecision.YEAR in [TimePrecision.YEAR, TimePrecision.MONTH]
        assert "year" in [TimePrecision.YEAR, TimePrecision.MONTH]


class TestSpatialFormat:
    """SpatialFormat enum tests;

    """

    def test_spatial_format_is_str_enum(self) -> None:
        """Checks that SpatialFormat inherits from str and Enum;"""
        assert issubclass(SpatialFormat, str)
        assert issubclass(SpatialFormat, Enum)

    # ------------------------- #

    def test_spatial_format_wkt(self) -> None:
        """Checks WKT format value;"""
        assert SpatialFormat.WKT.value == "wkt"
        assert SpatialFormat.WKT == "wkt"

    # ------------------------- #

    def test_spatial_format_geojson(self) -> None:
        """Checks GEOJSON format value;"""
        assert SpatialFormat.GEOJSON.value == "geojson"
        assert SpatialFormat.GEOJSON == "geojson"

    # ------------------------- #

    def test_spatial_format_unknown(self) -> None:
        """Checks UNKNOWN format value;"""
        assert SpatialFormat.UNKNOWN.value == "unknown"
        assert SpatialFormat.UNKNOWN == "unknown"

    # ------------------------- #

    def test_spatial_format_all_members(self) -> None:
        """Checks that all expected members exist in SpatialFormat;"""
        expected_members = [
            'WKT',
            'GEOJSON',
            'UNKNOWN',
        ]
        for member in expected_members:
            assert hasattr(SpatialFormat, member)

    # ------------------------- #

    def test_spatial_format_iteration(self) -> None:
        """Checks that SpatialFormat can be iterated;"""
        members = list(SpatialFormat)
        assert len(members) == 3
        assert SpatialFormat.WKT in members
        assert SpatialFormat.GEOJSON in members
        assert SpatialFormat.UNKNOWN in members

    # ------------------------- #

    def test_spatial_format_from_string(self) -> None:
        """Checks creation from string value;"""
        assert SpatialFormat("wkt") == SpatialFormat.WKT
        assert SpatialFormat("geojson") == SpatialFormat.GEOJSON

    # ------------------------- #

    def test_spatial_format_invalid_string_raises(self) -> None:
        """Checks that invalid string raises ValueError;"""
        with pytest.raises(ValueError):
            SpatialFormat("invalid_format")

    # ------------------------- #

    def test_spatial_format_string_comparison(self) -> None:
        """Checks that SpatialFormat members compare equal to their string values;"""
        assert SpatialFormat.WKT == "wkt"
        assert "wkt" == SpatialFormat.WKT
        assert SpatialFormat.GEOJSON != "wkt"

    # ------------------------- #

    def test_spatial_format_name_attribute(self) -> None:
        """Checks that name attribute returns member name;"""
        assert SpatialFormat.WKT.name == "WKT"
        assert SpatialFormat.GEOJSON.name == "GEOJSON"

    # ------------------------- #

    def test_spatial_format_in_collection(self) -> None:
        """Checks membership testing in collections;"""
        assert SpatialFormat.WKT in [SpatialFormat.WKT, SpatialFormat.GEOJSON]
        assert "wkt" in [SpatialFormat.WKT, SpatialFormat.GEOJSON]


class TestEnumsModule:
    """Tests for the enums module structure;

    """

    def test_enums_exported_in_all(self) -> None:
        """Checks that enums are exported in __all__;"""
        from pyheritage.cidoc import enums
        assert 'TimePrecision' in enums.__all__
        assert 'SpatialFormat' in enums.__all__
        assert len(enums.__all__) == 2

    # ------------------------- #

    def test_enums_importable_from_module(self) -> None:
        """Checks that enums can be imported from pyheritage.cidoc.enums;"""
        from pyheritage.cidoc import enums
        assert hasattr(enums, 'TimePrecision')
        assert hasattr(enums, 'SpatialFormat')
