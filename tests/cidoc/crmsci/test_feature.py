# -*- coding: utf-8 -*-

"""Tests for CRMsci feature hierarchy entities: S20, S22;

"""


# pylint: disable=E0401,C0116,W0612


import pytest
from pydantic import ValidationError
from tests.cidoc.crmsci.helpers import make_material, make_timespan

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E18PhysicalThing,
    E26PhysicalFeature,
    E41Appellation,
    E53Place,
    E57Material,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmsci.entities import S20RigidPhysicalFeature, S22SegmentOfMatter
from pyheritage.cidoc.crmsci.properties import O7Confines, O23IsDefinedBy


def _inner_place() -> E53Place:
    return E53Place(p157_is_at_rest_relative_to=[])


def _required_kwargs() -> dict:
    timespan = make_timespan('Reference Time')
    inner = _inner_place()
    stv = E92SpaceTimeVolume(
        p160_has_temporal_projection=timespan,
        p161_has_spatial_projection=[inner],
    )
    return {
        'p157_is_at_rest_relative_to': [],
        'p45_consists_of': [E57Material()],
        'p53_has_former_or_current_location': [],
        'p196_defines': stv,
        'o23_is_defined_by': stv,
    }


# ******************************************************************************************************************* #


class TestS20RigidPhysicalFeature:
    """S20 Rigid Physical Feature entity tests;

    S20 is concrete — extends E26 Physical Feature and E53 Place;
    Has optional property O7 confines;

    """

    def test_crm_code(self) -> None:
        """Verify S20 CRM code is 'S20';"""
        assert S20RigidPhysicalFeature.crm_code == 'S20'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S20 CRM label is 'S20 Rigid Physical Feature';"""
        assert S20RigidPhysicalFeature.crm_label == 'S20 Rigid Physical Feature'

    # ------------------------- #

    def test_inherits_from_e26(self) -> None:
        """Verify S20 inherits from E26 Physical Feature;"""
        assert issubclass(S20RigidPhysicalFeature, E26PhysicalFeature)

    # ------------------------- #

    def test_inherits_from_e53(self) -> None:
        """Verify S20 inherits from E53 Place;"""
        assert issubclass(S20RigidPhysicalFeature, E53Place)

    # ------------------------- #

    def test_inherits_from_e18(self) -> None:
        """Verify S20 inherits from E18 Physical Thing;"""
        assert issubclass(S20RigidPhysicalFeature, E18PhysicalThing)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S20 inherits from E1 CRM Entity;"""
        assert issubclass(S20RigidPhysicalFeature, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o7_confines(self) -> None:
        """Verify O7Confines property mixin is present in S20 MRO;"""
        assert O7Confines in S20RigidPhysicalFeature.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S20 auto-generates a non-null string id;"""
        entity = S20RigidPhysicalFeature(**_required_kwargs())

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S20 instance receives a unique id;"""
        a = S20RigidPhysicalFeature(**_required_kwargs())
        b = S20RigidPhysicalFeature(**_required_kwargs())

        assert a.id != b.id

    # ------------------------- #

    def test_o7_confines_field_exists(self) -> None:
        """Verify o7_confines field is present and None by default;"""
        entity = S20RigidPhysicalFeature(**_required_kwargs())

        assert hasattr(entity, 'o7_confines')
        assert entity.o7_confines is None

    # ------------------------- #

    def test_o7_confines_accepts_material(self) -> None:
        """Verify o7_confines accepts a list with S10MaterialSubstantial;"""
        mat = make_material('Confined Material')
        entity = S20RigidPhysicalFeature(
            o7_confines=[mat],
            **_required_kwargs(),
        )

        assert entity.o7_confines is not None
        assert entity.o7_confines[0] is mat

    # ------------------------- #

    def test_o7_confines_rejects_invalid_type(self) -> None:
        """Verify o7_confines raises ValidationError for non-material values;"""
        with pytest.raises(ValidationError):
            S20RigidPhysicalFeature(
                o7_confines=['invalid'],  # type: ignore[list-item]
                **_required_kwargs(),
            )

    # ------------------------- #

    def test_mro_includes_o23_is_defined_by(self) -> None:
        """Verify O23IsDefinedBy property mixin is present in S20 MRO;"""
        assert O23IsDefinedBy in S20RigidPhysicalFeature.__mro__

    # ------------------------- #

    def test_o23_is_defined_by_field_exists(self) -> None:
        """Verify o23_is_defined_by field is present in S20;"""
        entity = S20RigidPhysicalFeature(**_required_kwargs())
        assert hasattr(entity, 'o23_is_defined_by')

    # ------------------------- #

    def test_o23_is_defined_by_accepts_spacetime_volume(self) -> None:
        """Verify o23_is_defined_by accepts an E92SpaceTimeVolume;"""
        timespan = make_timespan('Ref Time')
        inner = _inner_place()
        stv = E92SpaceTimeVolume(
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[inner],
        )
        entity = S20RigidPhysicalFeature(
            p157_is_at_rest_relative_to=[],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=stv,
            o23_is_defined_by=stv,
        )
        assert entity.o23_is_defined_by is stv

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S20 can be created with a p1 appellation;"""
        entity = S20RigidPhysicalFeature(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Fault Line')],
            **_required_kwargs(),
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Fault Line'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id and o7_confines fields;"""
        entity = S20RigidPhysicalFeature(**_required_kwargs())
        data = entity.model_dump()

        assert 'id' in data
        assert 'o7_confines' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id;"""
        entity = S20RigidPhysicalFeature(**_required_kwargs())
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str

    # ------------------------- #

    def test_complete_entity(self) -> None:
        """Verify S20 can be created with all optional fields populated;"""
        mat = make_material('Rock Layer')
        entity = S20RigidPhysicalFeature(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Fault S20')],
            p3_has_note=['A visible fault line'],
            o7_confines=[mat],
            **_required_kwargs(),
        )

        assert entity.o7_confines is not None
        assert entity.o7_confines[0] is mat
        assert entity.p3_has_note is not None
        assert entity.p3_has_note[0].value == 'A visible fault line'


# ******************************************************************************************************************* #


class TestS22SegmentOfMatter:
    """S22 Segment of Matter entity tests;

    S22 is concrete — extends S20 Rigid Physical Feature;
    No additional CRMsci-specific properties;

    """

    def test_crm_code(self) -> None:
        """Verify S22 CRM code is 'S22';"""
        assert S22SegmentOfMatter.crm_code == 'S22'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S22 CRM label is 'S22 Segment of Matter';"""
        assert S22SegmentOfMatter.crm_label == 'S22 Segment of Matter'

    # ------------------------- #

    def test_inherits_from_s20(self) -> None:
        """Verify S22 inherits from S20 Rigid Physical Feature;"""
        assert issubclass(S22SegmentOfMatter, S20RigidPhysicalFeature)

    # ------------------------- #

    def test_inherits_from_e26(self) -> None:
        """Verify S22 inherits from E26 Physical Feature (through chain);"""
        assert issubclass(S22SegmentOfMatter, E26PhysicalFeature)

    # ------------------------- #

    def test_inherits_from_e53(self) -> None:
        """Verify S22 inherits from E53 Place (through chain);"""
        assert issubclass(S22SegmentOfMatter, E53Place)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S22 inherits from E1 CRM Entity;"""
        assert issubclass(S22SegmentOfMatter, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o7_confines(self) -> None:
        """Verify O7Confines property mixin is present in S22 MRO;"""
        assert O7Confines in S22SegmentOfMatter.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S22 auto-generates a non-null string id;"""
        entity = S22SegmentOfMatter(**_required_kwargs())

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S22 instance receives a unique id;"""
        a = S22SegmentOfMatter(**_required_kwargs())
        b = S22SegmentOfMatter(**_required_kwargs())

        assert a.id != b.id

    # ------------------------- #

    def test_o7_confines_accepts_material(self) -> None:
        """Verify o7_confines accepts a list with S10MaterialSubstantial;"""
        mat = make_material('Confined Material')
        entity = S22SegmentOfMatter(
            o7_confines=[mat],
            **_required_kwargs(),
        )

        assert entity.o7_confines is not None
        assert entity.o7_confines[0] is mat

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id field;"""
        entity = S22SegmentOfMatter(**_required_kwargs())
        data = entity.model_dump()

        assert 'id' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id;"""
        entity = S22SegmentOfMatter(**_required_kwargs())
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S22 can be created with a p1 appellation;"""
        entity = S22SegmentOfMatter(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Clay Layer A11')],
            **_required_kwargs(),
        )
        
        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Clay Layer A11'
