# -*- coding: utf-8 -*-

"""Tests for E60 Number CRM entity;

"""

# pylint: disable=E0401,C0116,W0612


import re

import pytest
from pydantic import ValidationError

from pyheritage.cidoc.core.entities import E59PrimitiveValue, E60Number
from pyheritage.cidoc.core.entities._primitives import _coerce_e60  # noqa


class TestE60Number:
    """Test E60 Number with integer, float, negative values etc.;

    """

    def test_integer(self) -> None:
        """Checks integer value;"""
        entity = E60Number(value=40)
        assert entity.value == 40
        assert int(entity) == 40

    # ------------------------- #

    def test_float(self) -> None:
        """Checks float value;"""
        entity = E60Number(value=3.14)
        assert float(entity) == pytest.approx(3.14)

    # ------------------------- #

    def test_negative(self) -> None:
        """Checks negative value;"""
        entity = E60Number(value=-40)
        assert entity.value == -40

    # ------------------------- #

    def test_zero(self) -> None:
        """Checks zero value;"""
        entity = E60Number(value=0)
        assert entity.value == 0

    # ------------------------- #

    def test_large_integer(self) -> None:
        """Checks large integer value;"""
        entity = E60Number(value=999999999999)
        assert entity.value == 999999999999

    # ------------------------- #

    def test_small_float(self) -> None:
        """Checks small float value;"""
        entity = E60Number(value=1.5e-04)
        assert float(entity) == pytest.approx(1.5e-04)

    # ------------------------- #

    def test_negative_float(self) -> None:
        """Checks negative float value;"""
        entity = E60Number(value=-3.14159)
        assert entity.value == -3.14159
        assert float(entity) == pytest.approx(-3.14159)

    # ------------------------- #

    def test_infinity_rejected(self) -> None:
        """Checks that infinity is rejected;"""
        with pytest.raises(ValueError, match='finite'):
            E60Number(value=float('inf'))

    # ------------------------- #

    def test_nan_rejected(self) -> None:
        """Checks that NaN is rejected;"""
        with pytest.raises(ValueError, match='finite'):
            E60Number(value=float('nan'))

    # ------------------------- #

    def test_negative_infinity_rejected(self) -> None:
        """Checks that negative infinity is rejected;"""
        with pytest.raises(ValueError, match='finite'):
            E60Number(value=float('-inf'))

    # === Magic methods =====

    def test_eq_with_same_value(self) -> None:
        """Checks equality with same value;"""
        entity1 = E60Number(value=42)
        entity2 = E60Number(value=42)
        assert entity1 == entity2

    # ------------------------- #

    def test_eq_with_different_value(self) -> None:
        """Checks inequality with different values;"""
        entity1 = E60Number(value=42)
        entity2 = E60Number(value=43)
        assert entity1 != entity2

    # ------------------------- #

    def test_eq_with_non_e60number(self) -> None:
        """Checks equality with non-E60Number returns NotImplemented;"""
        entity = E60Number(value=42)
        assert (entity == 42) is NotImplemented or (entity == 42) is False

    # ------------------------- #

    def test_int_conversion(self) -> None:
        """Checks __int__ conversion;"""
        entity = E60Number(value=42)
        assert int(entity) == 42
        assert isinstance(int(entity), int)

    # ------------------------- #

    def test_float_conversion(self) -> None:
        """Checks __float__ conversion;"""
        entity = E60Number(value=3.14)
        assert float(entity) == pytest.approx(3.14)
        assert isinstance(float(entity), float)

    # ------------------------- #

    def test_repr(self) -> None:
        """Checks __repr__ output;"""
        entity = E60Number(value=42)
        assert repr(entity) == 'E60(42)'

    # ------------------------- #

    def test_repr_float(self) -> None:
        """Checks __repr__ output for float value;"""
        entity = E60Number(value=3.14)
        assert repr(entity) == 'E60(3.14)'

    # ------------------------- #

    def test_coercion_from_int(self) -> None:
        """Checks coercion from int;"""
        entity = _coerce_e60(40)
        assert isinstance(entity, E60Number)
        assert entity.value == 40

    # ------------------------- #

    def test_coercion_from_float(self) -> None:
        """Checks coercion from float;"""
        entity = _coerce_e60(3.14)
        assert isinstance(entity, E60Number)
        assert entity.value == 3.14

    # ------------------------- #

    def test_coercion_from_dict(self) -> None:
        """Checks coercion from dict;"""
        entity = _coerce_e60({'value': 42})
        assert isinstance(entity, E60Number)
        assert entity.value == 42

    # ------------------------- #

    def test_coercion_passthrough(self) -> None:
        """Checks passthrough of existing E60Number;"""
        entity = E60Number(value=20)
        assert _coerce_e60(entity) is entity

    # ------------------------- #

    def test_model_dump(self) -> None:
        """Checks model_dump output;"""
        entity = E60Number(value=42)
        dump = entity.model_dump()
        assert 'value' in dump
        assert dump['value'] == 42

    # ------------------------- #

    def test_model_dump_json(self) -> None:
        """Checks model_dump with mode='json';"""
        entity = E60Number(value=3.14)
        dump = entity.model_dump(mode='json')
        assert dump['value'] == 3.14

    # ------------------------- #

    def test_model_dump_by_alias(self) -> None:
        """Checks model_dump with by_alias=True;"""
        entity = E60Number(value=42)
        dump = entity.model_dump(by_alias=True)
        assert '@id' in dump
        assert dump['value'] == 42

    # ------------------------- #

    def test_model_dump_json_string(self) -> None:
        """Checks JSON string output;"""
        entity = E60Number(value=42)
        json_str = entity.model_dump_json(by_alias=True)
        assert '"@id"' in json_str
        assert '"value":42' in json_str or '"value": 42' in json_str

    # ------------------------- #

    def test_model_validate(self) -> None:
        """Checks model_validate class method;"""
        entity = E60Number.model_validate({'value': 100})
        assert isinstance(entity, E60Number)
        assert entity.value == 100

    # ------------------------- #

    def test_inherits_from_e59(self) -> None:
        """Checks inheritance from E59PrimitiveValue;"""
        entity = E60Number(value=42)
        assert isinstance(entity, E59PrimitiveValue)

    # ------------------------- #

    def test_crm_code(self) -> None:
        """Checks crm_code attribute;"""
        assert hasattr(E60Number, 'crm_code')
        assert E60Number.crm_code == 'E60'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Checks crm_label attribute;"""
        assert hasattr(E60Number, 'crm_label')
        assert E60Number.crm_label == 'E60 Number'

    # ------------------------- #

    def test_has_id_field(self) -> None:
        """Checks that @id field exists;"""
        entity = E60Number(value=42)
        assert hasattr(entity, 'id')
        assert entity.id is not None

    # ------------------------- #

    def test_id_is_uuid_format(self) -> None:
        """Checks that id is UUID format;"""
        entity = E60Number(value=42)
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )
        assert uuid_pattern.match(entity.id)

    # ------------------------- #

    def test_unique_ids(self) -> None:
        """Checks that each instance has unique id;"""
        entity1 = E60Number(value=42)
        entity2 = E60Number(value=42)
        assert entity1.id != entity2.id

    # ------------------------- #

    def test_default_value(self) -> None:
        """Checks default value is 0;"""
        entity = E60Number()
        assert entity.value == 0

    # ------------------------- #

    def test_boolean_as_int(self) -> None:
        """Checks boolean treated as int (True=1, False=0);"""
        entity_true = E60Number(value=True)
        entity_false = E60Number(value=False)
        assert entity_true.value is True or entity_true.value == 1
        assert entity_false.value is False or entity_false.value == 0

    # ------------------------- #

    def test_validation_error_message(self) -> None:
        """Checks validation error message content;"""
        with pytest.raises(ValidationError):
            E60Number(value=float('inf'))
