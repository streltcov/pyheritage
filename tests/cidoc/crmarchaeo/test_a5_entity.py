# -*- coding: utf-8 -*-

"""Tests for A5 Stratigraphic Modification;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a5, make_a8, make_e13_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation, E55Type
from pyheritage.cidoc.crmarchaeo.entities import A5StratigraphicModification
from pyheritage.cidoc.crmarchaeo.properties import (
    AP8Disturbed,
    AP13HasStratigraphicRelationTo,
)
from pyheritage.cidoc.crmsci.entities import S18Alteration


class TestA5StratigraphicModification:

    def test_crm_code(self) -> None:
        """Verify CRM code is A5;"""
        assert A5StratigraphicModification.crm_code == 'A5'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A5 Stratigraphic Modification;"""
        assert A5StratigraphicModification.crm_label == 'A5 Stratigraphic Modification'

    # ------------------------- #

    def test_inherits_from_s18(self) -> None:
        """Verify A5 inherits from S18 Alteration;"""
        assert issubclass(A5StratigraphicModification, S18Alteration)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A5 inherits from E1 CRM Entity;"""
        assert issubclass(A5StratigraphicModification, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap8(self) -> None:
        """Verify AP8 Disturbed mixin is in A5 MRO;"""
        assert AP8Disturbed in A5StratigraphicModification.__mro__

    # ------------------------- #

    def test_mro_includes_ap13(self) -> None:
        """Verify AP13 Has Stratigraphic Relation To mixin is in A5 MRO;"""
        assert AP13HasStratigraphicRelationTo in A5StratigraphicModification.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a5()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a5()
        b = make_a5()

        assert a.id != b.id

    # ------------------------- #

    def test_ap8_field_exists(self) -> None:
        """Verify ap8_disturbed field exists with default None;"""
        entity = make_a5()

        assert hasattr(entity, 'ap8_disturbed')
        assert entity.ap8_disturbed is None

    # ------------------------- #

    def test_ap8_accepts_a8(self) -> None:
        """Verify AP8 accepts A8 Stratigraphic Unit instances;"""
        su = make_a8('Disturbed SU')
        entity = A5StratigraphicModification(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A5')],
            **make_e13_kwargs(),
            o18_altered=[make_a8()],
            ap8_disturbed=[su],
        )

        assert entity.ap8_disturbed is not None
        assert len(entity.ap8_disturbed) == 1
        assert isinstance(entity.ap8_disturbed[0], type(su))

    # ------------------------- #

    def test_ap8_rejects_invalid_type(self) -> None:
        """Verify AP8 raises ValidationError for non-A8 values;"""
        with pytest.raises(ValidationError):
            A5StratigraphicModification(
                ap8_disturbed=['invalid'],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
            )

    # ------------------------- #

    def test_ap13_field_exists(self) -> None:
        """Verify ap13_has_stratigraphic_relation_to field exists with default None;"""
        entity = make_a5()

        assert hasattr(entity, 'ap13_has_stratigraphic_relation_to')
        assert entity.ap13_has_stratigraphic_relation_to is None

    # ------------------------- #

    def test_ap13_accepts_a5(self) -> None:
        """Verify AP13 accepts another A5 instance;"""
        other = make_a5('Related modification')
        entity = A5StratigraphicModification(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A5')],
            **make_e13_kwargs(),
            o18_altered=[make_a8()],
            ap13_has_stratigraphic_relation_to=[other],
        )

        assert entity.ap13_has_stratigraphic_relation_to is not None
        assert len(entity.ap13_has_stratigraphic_relation_to) == 1
        assert isinstance(entity.ap13_has_stratigraphic_relation_to[0], A5StratigraphicModification)

    # ------------------------- #

    def test_ap13_rejects_invalid_type(self) -> None:
        """Verify AP13 raises ValidationError for non-A5 values;"""
        with pytest.raises(ValidationError):
            A5StratigraphicModification(
                ap13_has_stratigraphic_relation_to=['invalid'],
                **make_e13_kwargs(),
                o18_altered=[make_a8()],
            )

    # ------------------------- #

    def test_ap13_1_has_type_field_exists(self) -> None:
        """Verify ap13_1_has_type sub-property field exists with default None;"""
        entity = make_a5()

        assert hasattr(entity, 'ap13_1_has_type')
        assert entity.ap13_1_has_type is None

    # ------------------------- #

    def test_ap13_1_has_type_accepts_e55(self) -> None:
        """Verify AP13.1 accepts E55 Type instances;"""
        entity = A5StratigraphicModification(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A5')],
            **make_e13_kwargs(),
            o18_altered=[make_a8()],
            ap13_1_has_type=[E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='earlier than')])],
        )

        assert entity.ap13_1_has_type is not None

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes AP8 and AP13 fields;"""
        entity = make_a5()
        data = entity.model_dump()

        assert 'ap8_disturbed' in data
        assert 'ap13_has_stratigraphic_relation_to' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a5('Earthquake damage')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Earthquake damage' in json_str
