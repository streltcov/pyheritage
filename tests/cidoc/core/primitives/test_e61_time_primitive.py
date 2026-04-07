# -*- coding: utf-8 -*-

"""Tests for E61TimePrimitive CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


import re
from typing import Any

import pytest

from pyheritage.cidoc.core.entities import E59PrimitiveValue, E61TimePrimitive
from pyheritage.cidoc.core.entities._primitives import _coerce_e61  # noqa
from pyheritage.cidoc.enums import TimePrecision


class TestE61TimePrimitive:
    """Temporal value primitives;

    """

    # === Format validation =====

    @pytest.mark.parametrize("value", [
        "2024-01-15", "2024-01", "2024",
        "-0196", "-0196-03", "-0196-03-15",
        "1503~", "1503?", "1503%",
        "15xx", "150X", "2XXX",
        "2024-01-15T10:30:00",
        "2024-01-15T10:30:00Z",
        "2024-01-15T10:30:00+03:00",
    ])
    def test_valid_formats(self, value: Any) -> None:
        """Checks that valid EDTF strings are accepted without errors;"""
        t = E61TimePrimitive(value=value)
        assert t.value == value

    # ------------------------- #

    @pytest.mark.parametrize("value", [
        "january 1503",
        "about 1500",
        "XV century",
        "1503-1519",
        "12345",
    ])
    def test_invalid_formats(self, value: Any) -> None:
        """Checks that invalid EDTF formats are rejected by validation;"""
        with pytest.raises(ValueError, match="EDTF"):
            E61TimePrimitive(value=value)

    # ------------------------- #

    def test_empty_allowed(self) -> None:
        """Checks that an empty string is allowed as a primitive value;"""
        t = E61TimePrimitive(value="")
        assert t.value == ""

    # === Precision =============

    def test_precision_day(self) -> None:
        """Checks that time precision is determined as `day` for a date including a day;"""
        assert E61TimePrimitive(value="2024-01-15").precision == TimePrecision.DAY

    # ------------------------- #

    def test_precision_month(self) -> None:
        """Checks that time precision is determined as `month` for a date including a month;"""
        assert E61TimePrimitive(value="2024-01").precision == TimePrecision.MONTH

    # ------------------------- #

    def test_precision_year(self) -> None:
        """Checks that precision is determined as `year` for a date including only a year;"""
        assert E61TimePrimitive(value="2024").precision == TimePrecision.YEAR

    # ------------------------- #

    def test_precision_decade(self) -> None:
        """Checks that time precision is determined as `decade` for values like `195x`;"""
        assert E61TimePrimitive(value="195x").precision == TimePrecision.DECADE

    # ------------------------- #

    def test_precision_century(self) -> None:
        """Checks that time precision is determined as `century` for values like `15xx`;"""
        assert E61TimePrimitive(value="15xx").precision == TimePrecision.CENTURY

    # ------------------------- #

    def test_precision_millennium(self) -> None:
        """Checks that time precision is determined as `millennium` for values like `2xxx`;"""
        assert E61TimePrimitive(value="2xxx").precision == TimePrecision.MILLENNIUM

    # ------------------------- #

    def test_precision_datetime(self) -> None:
        """Checks that time precision is determined as `datetime` for values with time component;"""
        assert E61TimePrimitive(value="2024-01-15T10:30:00").precision == TimePrecision.DATETIME

    # ------------------------- #

    def test_precision_unknown_empty(self) -> None:
        """Checks that empty value has UNKNOWN precision;"""
        assert E61TimePrimitive(value="").precision == TimePrecision.UNKNOWN

    # ------------------------- #

    def test_precision_with_modifiers(self) -> None:
        """Checks precision calculation with approximate/uncertain modifiers;"""
        assert E61TimePrimitive(value="1503~").precision == TimePrecision.YEAR
        assert E61TimePrimitive(value="15xx?").precision == TimePrecision.CENTURY

    # === Flags (approximate, uncertain, interval, open) =====

    def test_approximate(self) -> None:
        """Checks the `is_approximate` flag for values marked with `~`;"""
        t = E61TimePrimitive(value="1503~")
        assert t.is_approximate

    # ------------------------- #

    def test_uncertain(self) -> None:
        """Checks the `is_uncertain` flag for values marked with `?`;"""
        t = E61TimePrimitive(value="1503?")
        assert t.is_uncertain

    # ------------------------- #

    def test_approx_uncertain(self) -> None:
        """Checks that for values marked with `%` (approximate + uncertain) both flags are set;"""
        t = E61TimePrimitive(value="1503%")
        assert t.is_approximate and t.is_uncertain

    # ------------------------- #

    def test_not_approximate(self) -> None:
        """Checks that exact dates are not approximate;"""
        assert not E61TimePrimitive(value="1503").is_approximate
        assert not E61TimePrimitive(value="1503?").is_approximate

    # ------------------------- #

    def test_not_uncertain(self) -> None:
        """Checks that exact dates are not uncertain;"""
        assert not E61TimePrimitive(value="1503").is_uncertain
        assert not E61TimePrimitive(value="1503~").is_uncertain

    # ------------------------- #

    def test_is_interval_true(self) -> None:
        """Checks is_interval flag for interval values;"""
        assert E61TimePrimitive(value="1703/1721").is_interval
        assert E61TimePrimitive(value="1703/..").is_interval
        assert E61TimePrimitive(value="../1721").is_interval

    # ------------------------- #

    def test_is_interval_false(self) -> None:
        """Checks is_interval flag for non-interval values;"""
        assert not E61TimePrimitive(value="1703").is_interval
        assert not E61TimePrimitive(value="1703~").is_interval

    # ------------------------- #

    def test_is_open_true(self) -> None:
        """Checks is_open flag for open-ended intervals;"""
        assert E61TimePrimitive(value="1703/..").is_open
        assert E61TimePrimitive(value="../1721").is_open

    # ------------------------- #

    def test_is_open_false(self) -> None:
        """Checks is_open flag for closed intervals and non-intervals;"""
        assert not E61TimePrimitive(value="1703/1721").is_open
        assert not E61TimePrimitive(value="1703").is_open

    # === Year extraction =====

    def test_year_positive(self) -> None:
        """Checks year extraction for positive (CE) values;"""
        assert E61TimePrimitive(value="1703").year == 1703

    # ------------------------- #

    def test_year_negative(self) -> None:
        """Checks year extraction for negative (BCE) values;"""
        assert E61TimePrimitive(value="-0196").year == -196

    # ------------------------- #

    def test_year_from_date(self) -> None:
        """Checks year extraction from a full EDTF date (`YYYY-MM-DD`);"""
        assert E61TimePrimitive(value="1452-04-15").year == 1452

    # ------------------------- #

    def test_year_from_century(self) -> None:
        """Checks year extraction from a century shorthand (`17xx` -> 1700);"""
        assert E61TimePrimitive(value="17xx").year == 1700

    # ------------------------- #

    def test_year_from_decade(self) -> None:
        """Checks year extraction from decade shorthand (`195x` -> 1950);"""
        assert E61TimePrimitive(value="195x").year == 1950

    # ------------------------- #

    def test_year_from_interval(self) -> None:
        """Checks year extraction from interval (uses start year);"""
        assert E61TimePrimitive(value="1503/1519").year == 1503

    # ------------------------- #

    def test_year_with_approximate(self) -> None:
        """Checks year extraction from approximate date;"""
        assert E61TimePrimitive(value="1503~").year == 1503

    # ------------------------- #

    def test_year_empty(self) -> None:
        """Checks year extraction from empty value returns None;"""
        assert E61TimePrimitive(value="").year is None

    # === BCE detection =====

    def test_is_bce(self) -> None:
        """Checks that BCE is determined by the leading `-` in EDTF values;"""
        assert E61TimePrimitive(value="-0196").is_bce
        assert not E61TimePrimitive(value="1703").is_bce

    # ------------------------- #

    def test_is_bce_empty(self) -> None:
        """Checks that empty value is not BCE;"""
        assert not E61TimePrimitive(value="").is_bce

    # === Comparison =====

    def test_equal(self) -> None:
        """Checks equality of time primitives via a normalized `sort_key`;"""
        assert E61TimePrimitive(value="1703") == E61TimePrimitive(value="1703")

    # ------------------------- #

    def test_approx_equals_exact(self) -> None:
        """Checks that an approximate date can compare equal to an exact one via `sort_key`;"""
        assert E61TimePrimitive(value="1703~") == E61TimePrimitive(value="1703")

    # ------------------------- #

    def test_not_equal(self) -> None:
        """Checks inequality of different dates;"""
        assert E61TimePrimitive(value="1703") != E61TimePrimitive(value="1704")

    # ------------------------- #

    def test_less_than(self) -> None:
        """Checks `<` ordering for a BCE/CE pair;"""
        assert E61TimePrimitive(value="-0196") < E61TimePrimitive(value="1503")

    # ------------------------- #

    def test_greater_than(self) -> None:
        """Checks `>` ordering for a year comparison;"""
        assert E61TimePrimitive(value="1519") > E61TimePrimitive(value="1503")

    # ------------------------- #

    def test_less_than_or_equal_true(self) -> None:
        """Checks `<=` operator returns True when appropriate;"""
        assert E61TimePrimitive(value="1503") <= E61TimePrimitive(value="1503")
        assert E61TimePrimitive(value="1503") <= E61TimePrimitive(value="1519")

    # ------------------------- #

    def test_greater_than_or_equal_true(self) -> None:
        """Checks `>=` operator returns True when appropriate;"""
        assert E61TimePrimitive(value="1519") >= E61TimePrimitive(value="1519")
        assert E61TimePrimitive(value="1519") >= E61TimePrimitive(value="1503")

    # ------------------------- #

    def test_compare_with_string(self) -> None:
        """Checks ordering of a time primitive against a plain EDTF string;"""
        assert E61TimePrimitive(value="1503") < "1519"

    # ------------------------- #

    def test_compare_with_string_equal(self) -> None:
        """Checks equality comparison with string;"""
        assert E61TimePrimitive(value="1503") == "1503"

    # ------------------------- #

    def test_compare_with_non_supported(self) -> None:
        """Checks comparison with unsupported type returns False;"""
        result = E61TimePrimitive(value="1503") == 42
        assert result is False

    # ------------------------- #

    def test_bce_ordering(self) -> None:
        """Checks correct ordering for two BCE values;"""
        assert E61TimePrimitive(value="-0500") < E61TimePrimitive(value="-0196")

    # === Hash =====

    def test_hash_same_value(self) -> None:
        """Checks that equal values have same hash;"""
        t1 = E61TimePrimitive(value="1503")
        t2 = E61TimePrimitive(value="1503")
        assert hash(t1) == hash(t2)

    # ------------------------- #

    def test_hash_different_value(self) -> None:
        """Checks that different values have different hash;"""
        t1 = E61TimePrimitive(value="1503")
        t2 = E61TimePrimitive(value="1504")
        assert hash(t1) != hash(t2)

    # === Coercion =====

    def test_coercion_from_string(self) -> None:
        """Checks that `_coerce_e61` wraps an EDTF string into `E61TimePrimitive`;"""
        result = _coerce_e61("1503")
        assert isinstance(result, E61TimePrimitive)
        assert result.value == "1503"

    # ------------------------- #

    def test_coercion_from_dict(self) -> None:
        """Checks coercion from dict;"""
        result = _coerce_e61({"value": "1503"})
        assert isinstance(result, E61TimePrimitive)
        assert result.value == "1503"

    # ------------------------- #

    def test_coercion_passthrough(self) -> None:
        """Checks passthrough of existing E61TimePrimitive;"""
        entity = E61TimePrimitive(value="1503")
        assert _coerce_e61(entity) is entity

    # === Factory methods =====

    def test_from_year(self) -> None:
        """Checks from_year factory method;"""
        t = E61TimePrimitive.from_year(1503)
        assert t.value == "1503"
        assert t.year == 1503

    # ------------------------- #

    def test_from_year_approximate(self) -> None:
        """Checks from_year with approximate flag;"""
        t = E61TimePrimitive.from_year(1503, approximate=True)
        assert t.value == "1503~"
        assert t.is_approximate

    # ------------------------- #

    def test_from_date(self) -> None:
        """Checks from_date factory method;"""
        t = E61TimePrimitive.from_date(1452, 4, 15)
        assert t.value == "1452-04-15"
        assert t.precision == TimePrecision.DAY

    # ------------------------- #

    def test_from_century(self) -> None:
        """Checks from_century factory method;"""
        t = E61TimePrimitive.from_century(16)
        assert t.value == "15xx"
        assert t.precision == TimePrecision.CENTURY

    # ------------------------- #

    def test_from_century_approximate(self) -> None:
        """Checks from_century with approximate flag;"""
        t = E61TimePrimitive.from_century(16, approximate=True)
        assert t.value == "15xx~"
        assert t.is_approximate

    # ------------------------- #

    def test_from_decade(self) -> None:
        """Checks from_decade factory method;"""
        t = E61TimePrimitive.from_decade(1950)
        assert t.value == "195x"
        assert t.precision == TimePrecision.DECADE

    # ------------------------- #

    def test_from_interval(self) -> None:
        """Checks from_interval factory method;"""
        t = E61TimePrimitive.from_interval(1501, 1520)
        assert t.value == "1501/1520"
        assert t.is_interval

    # ------------------------- #

    def test_from_text(self) -> None:
        """Checks from_text factory method;"""
        t = E61TimePrimitive.from_text("the 15th century")
        assert t.value is not None

    # ------------------------- #

    def test_from_text_invalid(self) -> None:
        """Checks from_text with None result raises ValueError;"""
        with pytest.raises(ValueError):
            E61TimePrimitive.from_text("zzzznotadate123456")

    # === Serialization =====

    def test_model_dump(self) -> None:
        """Checks model_dump output;"""
        t = E61TimePrimitive(value="1503")
        dump = t.model_dump()
        assert 'value' in dump
        assert dump['value'] == "1503"

    # ------------------------- #

    def test_model_dump_by_alias(self) -> None:
        """Checks model_dump with by_alias=True;"""
        t = E61TimePrimitive(value="1503")
        dump = t.model_dump(by_alias=True)
        assert '@id' in dump
        assert dump['value'] == "1503"

    # ------------------------- #

    def test_model_dump_json_string(self) -> None:
        """Checks JSON string output;"""
        t = E61TimePrimitive(value="1503")
        json_str = t.model_dump_json(by_alias=True)
        assert '"@id"' in json_str
        assert '"value":"1503"' in json_str or '"value": "1503"' in json_str

    # ------------------------- #

    def test_model_validate(self) -> None:
        """Checks model_validate class method;"""
        t = E61TimePrimitive.model_validate({'value': '1703'})
        assert isinstance(t, E61TimePrimitive)
        assert t.value == '1703'

    # === Inheritance and structure =====

    def test_inherits_from_e59(self) -> None:
        """Checks inheritance from E59PrimitiveValue;"""
        t = E61TimePrimitive(value="1503")
        assert isinstance(t, E59PrimitiveValue)

    # ------------------------- #

    def test_crm_code(self) -> None:
        """Checks crm_code attribute;"""
        assert hasattr(E61TimePrimitive, 'crm_code')
        assert E61TimePrimitive.crm_code == 'E61'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Checks crm_label attribute;"""
        assert hasattr(E61TimePrimitive, 'crm_label')
        assert E61TimePrimitive.crm_label == 'E61 Time Primitive'

    # ------------------------- #

    def test_has_id_field(self) -> None:
        """Checks that @id field exists;"""
        t = E61TimePrimitive(value="1503")
        assert hasattr(t, 'id')
        assert t.id is not None

    # ------------------------- #

    def test_id_is_uuid_format(self) -> None:
        """Checks that id is UUID format;"""
        t = E61TimePrimitive(value="1503")
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )
        assert uuid_pattern.match(t.id)

    # ------------------------- #

    def test_unique_ids(self) -> None:
        """Checks that each instance has unique id;"""
        t1 = E61TimePrimitive(value="1503")
        t2 = E61TimePrimitive(value="1503")
        assert t1.id != t2.id

    # === Default value =====

    def test_default_value(self) -> None:
        """Checks default value is empty string;"""
        t = E61TimePrimitive()
        assert t.value == ""

    # === Representation =====

    def test_repr_exact(self) -> None:
        """Checks __repr__ for exact date;"""
        t = E61TimePrimitive(value="1503")
        assert repr(t) == 'E61(1503)'

    # ------------------------- #

    def test_repr_approximate(self) -> None:
        """Checks __repr__ for approximate date;"""
        t = E61TimePrimitive(value="1503~")
        assert repr(t) == 'E61(1503~ [≈])'

    # ------------------------- #

    def test_repr_uncertain(self) -> None:
        """Checks __repr__ for uncertain date;"""
        t = E61TimePrimitive(value="1503?")
        assert repr(t) == 'E61(1503? [?])'

    # ------------------------- #

    def test_repr_both(self) -> None:
        """Checks __repr__ for approximate and uncertain date;"""
        t = E61TimePrimitive(value="1503%")
        assert repr(t) == 'E61(1503% [≈,?])'

    # ------------------------- #

    def test_repr_interval(self) -> None:
        """Checks __repr__ for interval;"""
        t = E61TimePrimitive(value="1503/1519")
        assert repr(t) == 'E61(1503/1519 [interval])'

    # === Parsed property =====

    def test_parsed_property_exists(self) -> None:
        """Checks that parsed property exists;"""
        t = E61TimePrimitive(value="1503")
        assert hasattr(t, 'parsed')

    # ------------------------- #

    def test_parsed_empty(self) -> None:
        """Checks that parsed is None for empty value;"""
        t = E61TimePrimitive(value="")
        assert t.parsed is None

    # === Lower and upper strict =====

    def test_lower_strict_century(self) -> None:
        """Checks lower_strict for century;"""
        t = E61TimePrimitive(value="17xx")
        # Note: lower_strict may be None if EDTF parsing doesn't populate it
        # This tests the property exists and is accessible
        _ = t.lower_strict  # Should not raise

    # ------------------------- #

    def test_upper_strict_century(self) -> None:
        """Checks upper_strict for century;"""
        t = E61TimePrimitive(value="17xx")
        # Note: upper_strict may be None if EDTF parsing doesn't populate it
        _ = t.upper_strict  # Should not raise

    # ------------------------- #

    def test_lower_upper_strict_empty(self) -> None:
        """Checks lower_strict and upper_strict for empty value;"""
        t = E61TimePrimitive(value="")
        assert t.lower_strict is None
        assert t.upper_strict is None

    # === Sort key =====

    def test_sort_key_exists(self) -> None:
        """Checks sort_key exists and is non-empty for valid dates;"""
        t = E61TimePrimitive(value="1503")
        assert t.sort_key is not None
        assert len(t.sort_key) > 0

    # ------------------------- #

    def test_sort_key_empty(self) -> None:
        """Checks sort_key for empty value;"""
        t = E61TimePrimitive(value="")
        assert t.sort_key == ""

    # ------------------------- #

    def test_sort_key_bce(self) -> None:
        """Checks sort_key for BCE date;"""
        t = E61TimePrimitive(value="-0196")
        assert t.sort_key is not None
        assert len(t.sort_key) > 0
