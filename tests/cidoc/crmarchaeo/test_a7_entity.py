# -*- coding: utf-8 -*-

"""Tests for A7 Embedding;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import (
    make_a2,
    make_a7,
    make_a8,
    make_s20_kwargs,
)

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E18PhysicalThing,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E55Type,
    E57Material,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmarchaeo.entities import (
    A2StratigraphicVolumeUnit,
    A7Embedding,
    A8StratigraphicUnit,
)
from pyheritage.cidoc.crmarchaeo.properties import (
    AP11HasPhysicalRelationTo,
    AP17IsFoundBy,
    AP18IsEmbeddingOf,
    AP19IsEmbeddingIn,
)
from pyheritage.cidoc.crmsci.entities import (
    S9PropertyType,
    S10MaterialSubstantial,
    S19EncounterEvent,
)


class TestA7Embedding:

    def test_crm_code(self) -> None:
        """Verify CRM code is A7;"""
        assert A7Embedding.crm_code == 'A7'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A7 Embedding;"""
        assert A7Embedding.crm_label == 'A7 Embedding'

    # ------------------------- #

    def test_inherits_from_a8(self) -> None:
        """Verify A7 inherits from A8 Stratigraphic Unit;"""
        assert issubclass(A7Embedding, A8StratigraphicUnit)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A7 inherits from E1 CRM Entity;"""
        assert issubclass(A7Embedding, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap11(self) -> None:
        """Verify AP11 Has Physical Relation To mixin is in A7 MRO;"""
        assert AP11HasPhysicalRelationTo in A7Embedding.__mro__

    # ------------------------- #

    def test_mro_includes_ap17(self) -> None:
        """Verify AP17 Is Found By mixin is in A7 MRO;"""
        assert AP17IsFoundBy in A7Embedding.__mro__

    # ------------------------- #

    def test_mro_includes_ap18(self) -> None:
        """Verify AP18 Is Embedding Of mixin is in A7 MRO;"""
        assert AP18IsEmbeddingOf in A7Embedding.__mro__

    # ------------------------- #

    def test_mro_includes_ap19(self) -> None:
        """Verify AP19 Is Embedding In mixin is in A7 MRO;"""
        assert AP19IsEmbeddingIn in A7Embedding.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a7()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a7()
        b = make_a7()

        assert a.id != b.id

    # ------------------------- #

    def test_ap17_field_exists(self) -> None:
        """Verify ap17_is_found_by field exists;"""
        entity = make_a7()
        assert hasattr(entity, 'ap17_is_found_by')

    # ------------------------- #

    def test_ap17_accepts_s19(self) -> None:
        """Verify AP17 accepts S19 Encounter Event instances;"""
        stv = E92SpaceTimeVolume(
            p160_has_temporal_projection=E52TimeSpan(),
            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
        )
        obj = E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Pottery')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=stv,
        )
        encounter = S19EncounterEvent(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Encounter #145')],
            p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
            p160_has_temporal_projection=E52TimeSpan(),
            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
            p177_assigned_property_type=[E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='T')])],
            o8_observed=S10MaterialSubstantial(
                o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
            ),
            o9_observed_property_type=S9PropertyType(),
            o16_observed_value=E41Appellation(),
            o19_encountered_object=[obj],
            o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
        )
        entity = A7Embedding(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A7')],
            **make_s20_kwargs(),
            ap17_is_found_by=[encounter],
            ap18_is_embedding_of=[obj],
            ap19_is_embedding_in=[make_a2()],
        )

        assert entity.ap17_is_found_by is not None
        assert len(entity.ap17_is_found_by) == 1
        assert isinstance(entity.ap17_is_found_by[0], S19EncounterEvent)

    # ------------------------- #

    def test_ap17_rejects_invalid_type(self) -> None:
        """Verify AP17 raises ValidationError for non-S19 values;"""
        with pytest.raises(ValidationError):
            A7Embedding(
                ap17_is_found_by=['invalid'],
                **make_s20_kwargs(),
                ap18_is_embedding_of=[E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='X')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=E52TimeSpan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )],
                ap19_is_embedding_in=[make_a2()],
            )

    # ------------------------- #

    def test_ap18_field_exists(self) -> None:
        """Verify ap18_is_embedding_of field exists;"""
        entity = make_a7()
        assert hasattr(entity, 'ap18_is_embedding_of')

    # ------------------------- #

    def test_ap18_accepts_e18(self) -> None:
        """Verify AP18 accepts E18 Physical Thing instances;"""
        obj = E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Amphora')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=E92SpaceTimeVolume(
                p160_has_temporal_projection=E52TimeSpan(),
                p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
            ),
        )
        entity = A7Embedding(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A7')],
            **make_s20_kwargs(),
            ap17_is_found_by=[S19EncounterEvent(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='E')],
                p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
                p160_has_temporal_projection=E52TimeSpan(),
                p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                p177_assigned_property_type=[E55Type(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='T')],
                )],
                o8_observed=S10MaterialSubstantial(
                    o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
                ),
                o9_observed_property_type=S9PropertyType(),
                o16_observed_value=E41Appellation(),
                o19_encountered_object=[obj],
                o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
            )],
            ap18_is_embedding_of=[obj],
            ap19_is_embedding_in=[make_a2()],
        )

        assert entity.ap18_is_embedding_of is not None
        assert len(entity.ap18_is_embedding_of) == 1
        assert isinstance(entity.ap18_is_embedding_of[0], E18PhysicalThing)

    # ------------------------- #

    def test_ap18_rejects_invalid_type(self) -> None:
        """Verify AP18 raises ValidationError for non-E18 values;"""
        with pytest.raises(ValidationError):
            A7Embedding(
                ap18_is_embedding_of=['invalid'],
                **make_s20_kwargs(),
                ap17_is_found_by=[S19EncounterEvent(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='E')],
                    p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
                    p160_has_temporal_projection=E52TimeSpan(),
                    p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    p177_assigned_property_type=[E55Type()],
                    o8_observed=S10MaterialSubstantial(
                        o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
                    ),
                    o9_observed_property_type=S9PropertyType(),
                    o16_observed_value=E41Appellation(),
                    o19_encountered_object=[E18PhysicalThing(
                        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='O')],
                        p45_consists_of=[E57Material()],
                        p53_has_former_or_current_location=[],
                        p196_defines=E92SpaceTimeVolume(
                            p160_has_temporal_projection=E52TimeSpan(),
                            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                        ),
                    )],
                    o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
                )],
                ap19_is_embedding_in=[make_a2()],
            )

    # ------------------------- #

    def test_ap19_field_exists(self) -> None:
        """Verify ap19_is_embedding_in field exists;"""
        entity = make_a7()
        assert hasattr(entity, 'ap19_is_embedding_in')

    # ------------------------- #

    def test_ap19_accepts_a2(self) -> None:
        """Verify AP19 accepts A2 Stratigraphic Volume Unit instances;"""
        layer = make_a2('Containing layer')
        entity = A7Embedding(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test A7')],
            **make_s20_kwargs(),
            ap17_is_found_by=[S19EncounterEvent(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='E')],
                p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
                p160_has_temporal_projection=E52TimeSpan(),
                p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                p177_assigned_property_type=[E55Type()],
                o8_observed=S10MaterialSubstantial(
                    o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
                ),
                o9_observed_property_type=S9PropertyType(),
                o16_observed_value=E41Appellation(),
                o19_encountered_object=[E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='O')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=E52TimeSpan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )],
                o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
            )],
            ap18_is_embedding_of=[E18PhysicalThing(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Amphora')],
                p45_consists_of=[E57Material()],
                p53_has_former_or_current_location=[],
                p196_defines=E92SpaceTimeVolume(
                    p160_has_temporal_projection=E52TimeSpan(),
                    p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                ),
            )],
            ap19_is_embedding_in=[layer],
        )

        assert entity.ap19_is_embedding_in is not None
        assert len(entity.ap19_is_embedding_in) == 1
        assert isinstance(entity.ap19_is_embedding_in[0], A2StratigraphicVolumeUnit)

    # ------------------------- #

    def test_ap19_rejects_a8_not_a2(self) -> None:
        """Verify AP19 rejects A8 that is not an A2;"""
        plain_a8 = make_a8('Generic SU')

        with pytest.raises(ValidationError):
            A7Embedding(
                ap19_is_embedding_in=[plain_a8],
                **make_s20_kwargs(),
                ap17_is_found_by=[S19EncounterEvent(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='E')],
                    p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
                    p160_has_temporal_projection=E52TimeSpan(),
                    p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    p177_assigned_property_type=[E55Type()],
                    o8_observed=S10MaterialSubstantial(
                        o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
                    ),
                    o9_observed_property_type=S9PropertyType(),
                    o16_observed_value=E41Appellation(),
                    o19_encountered_object=[E18PhysicalThing(
                        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='O')],
                        p45_consists_of=[E57Material()],
                        p53_has_former_or_current_location=[],
                        p196_defines=E92SpaceTimeVolume(
                            p160_has_temporal_projection=E52TimeSpan(),
                            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                        ),
                    )],
                    o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
                )],
                ap18_is_embedding_of=[E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='X')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=E52TimeSpan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )],
            )

    # ------------------------- #

    def test_ap19_rejects_invalid_type(self) -> None:
        """Verify AP19 raises ValidationError for non-A2 values;"""
        with pytest.raises(ValidationError):
            A7Embedding(
                ap19_is_embedding_in=['invalid'],
                **make_s20_kwargs(),
                ap17_is_found_by=[S19EncounterEvent(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='E')],
                    p7_took_place_at=[E53Place(p157_is_at_rest_relative_to=[])],
                    p160_has_temporal_projection=E52TimeSpan(),
                    p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    p177_assigned_property_type=[E55Type()],
                    o8_observed=S10MaterialSubstantial(o15_occupied=E53Place(p157_is_at_rest_relative_to=[])),
                    o9_observed_property_type=S9PropertyType(),
                    o16_observed_value=E41Appellation(),
                    o19_encountered_object=[E18PhysicalThing(
                        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='O')],
                        p45_consists_of=[E57Material()],
                        p53_has_former_or_current_location=[],
                        p196_defines=E92SpaceTimeVolume(
                            p160_has_temporal_projection=E52TimeSpan(),
                            p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                        ),
                    )],
                    o21_encountered_at=E53Place(p157_is_at_rest_relative_to=[]),
                )],
                ap18_is_embedding_of=[E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='X')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=E52TimeSpan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )],
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, AP17, AP18, and AP19 fields;"""
        entity = make_a7()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap17_is_found_by' in data
        assert 'ap18_is_embedding_of' in data
        assert 'ap19_is_embedding_in' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a7('Amphora embedding')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Amphora' in json_str
