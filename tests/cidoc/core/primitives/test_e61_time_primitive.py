# -*- coding: utf-8 -*-

"""Tests for E61TimePrimitive CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


from typing import Any

import pytest

from pyheritage.cidoc.core.entities import E61TimePrimitive
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

    # ------------------------- #

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

    # === Year extraction =======

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

    def test_is_bce(self) -> None:
        """Checks that BCE is determined by the leading `-` in EDTF values;"""
        assert E61TimePrimitive(value="-0196").is_bce
        assert not E61TimePrimitive(value="1703").is_bce

    # ------------------------- #

    # === Comparison ============

    def test_equal(self) -> None:
        """Checks equality of time primitives via a normalized `sort_key`;"""
        assert E61TimePrimitive(value="1703") == E61TimePrimitive(value="1703")

    # ------------------------- #

    def test_approx_equals_exact(self) -> None:
        """Checks that an approximate date can compare equal to an exact one via `sort_key`;"""
        assert E61TimePrimitive(value="1703~") == E61TimePrimitive(value="1703")

    # ------------------------- #

    def test_less_than(self) -> None:
        """Checks `<` ordering for a BCE/CE pair;"""
        assert E61TimePrimitive(value="-0196") < E61TimePrimitive(value="1503")

    # ------------------------- #

    def test_greater_than(self) -> None:
        """Checks `>` ordering for a year comparison;"""
        assert E61TimePrimitive(value="1519") > E61TimePrimitive(value="1503")

    # ------------------------- #

    def test_compare_with_string(self) -> None:
        """Checks ordering of a time primitive against a plain EDTF string;"""
        assert E61TimePrimitive(value="1503") < "1519"

    # ------------------------- #

    def test_bce_ordering(self) -> None:
        """Checks correct ordering for two BCE values;"""
        assert E61TimePrimitive(value="-0500") < E61TimePrimitive(value="-0196")

    # ------------------------- #

    # === Coercion ==============

    def test_coercion_from_string(self) -> None:
        """Checks that `_coerce_e61` wraps an EDTF string into `E61TimePrimitive`;"""
        result = _coerce_e61("1503")
        assert isinstance(result, E61TimePrimitive)
        assert result.value == "1503"
