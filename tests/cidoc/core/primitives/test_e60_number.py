# -*- coding: utf-8 -*-

"""Tests for E60 Number CRM entity;

"""

# pylint: disable=E0401,C0116,W0612


import pytest

from pyheritage.cidoc.core.entities import E60Number
from pyheritage.cidoc.core.entities._primitives import _coerce_e60  # noqa


class TestE60Number:
    """Test E60 Number with integer, float, negative values etc.;

    """

    def test_integer(self) -> None:
        entity = E60Number(value=40)
        assert entity.value == 40
        assert int(entity) == 40

    # ------------------------- #

    def test_float(self) -> None:
        entity = E60Number(value=3.14)
        assert float(entity) == pytest.approx(3.14)

    # ------------------------- #

    def test_negative(self) -> None:
        entity = E60Number(value=-40)
        assert entity.value == -40

    # ------------------------- #

    def test_zero(self) -> None:
        entity = E60Number(value=0)
        assert entity.value == 0

    # ------------------------- #

    def test_infinity_rejected(self) -> None:
        with pytest.raises(ValueError, match='finite'):
            E60Number(value=float('inf'))

    # ------------------------- #

    def test_nan_rejected(self) -> None:
        with pytest.raises(ValueError, match='finite'):
            E60Number(value=float('nan'))

    # ------------------------- #

    def test_coercion_from_int(self) -> None:
        entity = _coerce_e60(40)
        assert isinstance(entity, E60Number)
        assert entity.value == 40

    # ------------------------- #

    def test_passthrough(self) -> None:
        entity = E60Number(value=20)
        assert _coerce_e60(20) == entity
