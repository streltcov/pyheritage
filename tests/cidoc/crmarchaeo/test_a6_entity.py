"""Tests for A6 Group Declaration Event;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a6, make_e13_kwargs

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E13AttributeAssignment,
    E18PhysicalThing,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E57Material,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmarchaeo.entities import A6GroupDeclarationEvent
from pyheritage.cidoc.crmarchaeo.properties import AP16AssignedAttributeTo


class TestA6GroupDeclarationEvent:

    def test_crm_code(self) -> None:
        """Verify CRM code is A6;"""
        assert A6GroupDeclarationEvent.crm_code == 'A6'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A6 Group Declaration Event;"""
        assert A6GroupDeclarationEvent.crm_label == 'A6 Group Declaration Event'

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify A6 inherits from E13 Attribute Assignment;"""
        assert issubclass(A6GroupDeclarationEvent, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A6 inherits from E1 CRM Entity;"""
        assert issubclass(A6GroupDeclarationEvent, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap16(self) -> None:
        """Verify AP16 Assigned Attribute To mixin is in A6 MRO;"""
        assert AP16AssignedAttributeTo in A6GroupDeclarationEvent.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a6()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a6()
        b = make_a6()

        assert a.id != b.id

    # ------------------------- #

    def test_ap16_field_exists(self) -> None:
        """Verify ap16_assigned_attribute_to field exists;"""
        entity = make_a6()
        assert hasattr(entity, 'ap16_assigned_attribute_to')

    # ------------------------- #

    def test_ap16_accepts_e18(self) -> None:
        """Verify AP16 accepts E18 Physical Thing instances;"""
        stv = E92SpaceTimeVolume(
            p160_has_temporal_projection=E52TimeSpan(),
            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
        )
        thing = E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Post hole [7]')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=stv,
        )
        entity = A6GroupDeclarationEvent(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Group declaration')],
            **make_e13_kwargs(),
            ap16_assigned_attribute_to=[thing],
        )

        assert entity.ap16_assigned_attribute_to is not None
        assert len(entity.ap16_assigned_attribute_to) == 1
        assert isinstance(entity.ap16_assigned_attribute_to[0], E18PhysicalThing)

    # ------------------------- #

    def test_ap16_rejects_invalid_type(self) -> None:
        """Verify AP16 raises ValidationError for non-E18 values;"""
        with pytest.raises(ValidationError):
            A6GroupDeclarationEvent(
                ap16_assigned_attribute_to=['invalid'],
                **make_e13_kwargs(),
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id and AP16 fields;"""
        entity = make_a6()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap16_assigned_attribute_to' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a6('Post hole grouping')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Post hole' in json_str
