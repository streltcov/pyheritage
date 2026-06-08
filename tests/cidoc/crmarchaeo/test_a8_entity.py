# -*- coding: utf-8 -*-

"""Tests for A8 Stratigraphic Unit;

"""

# pylint: disable=E0401,C0116,W0612

from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a8, make_s20_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation, E55Type
from pyheritage.cidoc.crmarchaeo.entities import A8StratigraphicUnit
from pyheritage.cidoc.crmarchaeo.properties import AP11HasPhysicalRelationTo


class TestA8StratigraphicUnit:

    def test_crm_code(self) -> None:
        """Verify CRM code is A8;"""
        assert A8StratigraphicUnit.crm_code == 'A8'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A8 Stratigraphic Unit;"""
        assert A8StratigraphicUnit.crm_label == 'A8 Stratigraphic Unit'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify A8 is abstract (ABC in MRO);"""
        assert ABC in A8StratigraphicUnit.__mro__

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A8 inherits from E1 CRM Entity;"""
        assert issubclass(A8StratigraphicUnit, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap11(self) -> None:
        """Verify AP11 Has Physical Relation To mixin is in A8 MRO;"""
        assert AP11HasPhysicalRelationTo in A8StratigraphicUnit.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a8()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a8()
        b = make_a8()

        assert a.id != b.id

    # ------------------------- #

    def test_ap11_field_exists(self) -> None:
        """Verify ap11_has_physical_relation_to field exists with default None;"""
        entity = make_a8()

        assert hasattr(entity, 'ap11_has_physical_relation_to')
        assert entity.ap11_has_physical_relation_to is None

    # ------------------------- #

    def test_ap11_accepts_a8(self) -> None:
        """Verify AP11 accepts another A8 instance;"""
        other = make_a8('Related SU')
        entity = A8StratigraphicUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A8')],
            **make_s20_kwargs(),
            ap11_has_physical_relation_to=[other],
        )

        assert entity.ap11_has_physical_relation_to is not None
        assert len(entity.ap11_has_physical_relation_to) == 1
        assert isinstance(entity.ap11_has_physical_relation_to[0], A8StratigraphicUnit)

    # ------------------------- #

    def test_ap11_rejects_invalid_type(self) -> None:
        """Verify AP11 raises ValidationError for non-A8 values;"""
        with pytest.raises(ValidationError):
            A8StratigraphicUnit(
                ap11_has_physical_relation_to=['invalid'],
                **make_s20_kwargs(),
            )

    # ------------------------- #

    def test_ap11_1_has_type_field_exists(self) -> None:
        """Verify ap11_1_has_type sub-property field exists with default None;"""
        entity = make_a8()

        assert hasattr(entity, 'ap11_1_has_type')
        assert entity.ap11_1_has_type is None

    # ------------------------- #

    def test_ap11_1_has_type_accepts_e55(self) -> None:
        """Verify AP11.1 accepts E55 Type instances;"""
        entity = A8StratigraphicUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A8')],
            **make_s20_kwargs(),
            ap11_1_has_type=[E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='abuts')])],
        )

        assert entity.ap11_1_has_type is not None
        assert len(entity.ap11_1_has_type) == 1

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify A8 can be created with an E41 Appellation;"""
        entity = A8StratigraphicUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Layer Gamma')],
            **make_s20_kwargs(),
        )

        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Layer Gamma'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, AP11, and AP11.1 fields;"""
        entity = make_a8()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap11_has_physical_relation_to' in data
        assert 'ap11_1_has_type' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a8('Layer Gamma')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Layer Gamma' in json_str
