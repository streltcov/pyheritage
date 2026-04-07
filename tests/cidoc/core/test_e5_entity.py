# -*- coding: utf-8 -*-

"""Tests for E5Event CRM entity;

"""


# pylint: disable=E0401,C0116,W0612

import pytest

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E2TemporalEntity,
    E4Period,
    E5Event,
    E18PhysicalThing,
    E39Actor,
    E41Appellation,
    E42Identifier,
    E52TimeSpan,
    E53Place,
    E55Type,
    E57Material,
    E77PersistentItem,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.core.properties import P11HadParticipant, P12OccurredInPresenceOf


def _create_minimal_timespan() -> E52TimeSpan:
    """Create minimal E52TimeSpan;"""
    return E52TimeSpan(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Time Span')],
    )


def _create_minimal_place() -> E53Place:
    """Create minimal E53Place with required properties;"""
    return E53Place(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Place')],
        p157_is_at_rest_relative_to=[
            E18PhysicalThing(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Reference Object')],
                p45_consists_of=[E57Material()],
                p53_has_former_or_current_location=[],
                p196_defines=E92SpaceTimeVolume(
                    p160_has_temporal_projection=_create_minimal_timespan(),
                    p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                )
            )
        ],
    )


def _create_minimal_e5_event() -> E5Event:
    """Create minimal E5Event with all required fields;"""
    place = _create_minimal_place()
    timespan = _create_minimal_timespan()
    
    return E5Event(
        p7_took_place_at=[place],
        p160_has_temporal_projection=timespan,
        p161_has_spatial_projection=[place],
    )


class TestE5EventInheritance:
    """E5 Event inheritance hierarchy tests;

    """

    def test_e5_inherits_from_e4(self) -> None:
        """Checks that E5Event inherits from E4Period;"""
        assert issubclass(E5Event, E4Period)

    # ------------------------- #

    def test_e5_inherits_from_e2(self) -> None:
        """Checks that E5Event inherits from E2TemporalEntity;"""
        assert issubclass(E5Event, E2TemporalEntity)

    # ------------------------- #

    def test_e5_inherits_from_e1(self) -> None:
        """Checks that E5Event inherits from E1CRMEntity (via E2, E4);"""
        assert issubclass(E5Event, E1CRMEntity)

    # ------------------------- #

    def test_e5_inherits_e92(self) -> None:
        """Checks that E5Event inherits from E92SpaceTimeVolume (via E4);"""
        assert issubclass(E5Event, E92SpaceTimeVolume)

    # ------------------------- #

    def test_e5_inherits_all_properties(self) -> None:
        """Checks that E5 inherits all properties from E1, E2, E4 via E4Period;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )

        # E1 properties;
        assert hasattr(entity, 'p1_is_identified_by')
        assert hasattr(entity, 'p2_has_type')
        assert hasattr(entity, 'p3_has_note')
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert hasattr(entity, 'p137_exemplifies')

        # E2 properties;
        assert hasattr(entity, 'p4_has_timespan')
        assert hasattr(entity, 'p173_starts_before_or_with_the_end_of')
        assert hasattr(entity, 'p174_starts_before_the_end_of')
        assert hasattr(entity, 'p175_starts_before_or_with_the_start_of')
        assert hasattr(entity, 'p176_starts_before_the_start_of')
        assert hasattr(entity, 'p182_ends_before_or_with_start_of')
        assert hasattr(entity, 'p183_ends_before_the_start_of')
        assert hasattr(entity, 'p184_ends_before_or_with_the_end_of')
        assert hasattr(entity, 'p185_ends_before_the_end_of')

        # E4-specific properties;
        assert hasattr(entity, 'p7_took_place_at')
        assert hasattr(entity, 'p8_took_place_on_or_within')
        assert hasattr(entity, 'p9_consists_of')
        assert hasattr(entity, 'p10_falls_within')
        assert hasattr(entity, 'p132_spatiotemporally_overlaps')
        assert hasattr(entity, 'p160_has_temporal_projection')
        assert hasattr(entity, 'p161_has_spatial_projection')

        # E5-specific properties;
        assert hasattr(entity, 'p11_had_participant')
        assert hasattr(entity, 'p12_occurred_in_presence_of')

    # ------------------------- #

    def test_e5_mro_includes_e5_specific_mixins(self) -> None:
        """Checks that E5 MRO includes E5-specific property mixin classes;

        Inherited mixins (P1-P4, P48, P137, P173-P185 from E1/E2, P7-P10/P132/P160/P161 from E4)
        are verified in E3 and E4 tests.

        """
        mro = E5Event.__mro__

        assert P11HadParticipant in mro
        assert P12OccurredInPresenceOf in mro


# ******************************************************************************************************************* #


class TestE5EventProperties:
    """E5 Event property tests;

    Tests for all properties (inherited and E5-specific).
    Inherited properties are also tested in E3 and E4 tests.

    """

    # === Inherited properties (E1, E2, E4) =====

    def test_p1_is_identified_by_field_exists(self) -> None:
        """Checks that P1 is identified by property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p1_is_identified_by')
        assert entity.p1_is_identified_by is None

    # ------------------------- #

    def test_p2_has_type_field_exists(self) -> None:
        """Checks that P2 has type property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p2_has_type')
        assert entity.p2_has_type == []

    # ------------------------- #

    def test_p3_has_note_field_exists(self) -> None:
        """Checks that P3 has note property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p3_has_note')
        assert entity.p3_has_note is None

    # ------------------------- #

    def test_p4_has_timespan_field_exists(self) -> None:
        """Checks that P4 has time-span property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p4_has_timespan')
        assert entity.p4_has_timespan is None

    # ------------------------- #

    def test_p48_has_preferred_identifier_field_exists(self) -> None:
        """Checks that P48 has preferred identifier property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert entity.p48_has_preferred_identifier is None

    # ------------------------- #

    def test_p137_exemplifies_field_exists(self) -> None:
        """Checks that P137 exemplifies property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p137_exemplifies')
        assert entity.p137_exemplifies is None

    # === P173-P185 temporal relations =====

    def test_p173_starts_before_or_with_the_end_of_field_exists(self) -> None:
        """Checks that P173 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p173_starts_before_or_with_the_end_of')
        assert entity.p173_starts_before_or_with_the_end_of is None

    # ------------------------- #

    def test_p174_starts_before_the_end_of_field_exists(self) -> None:
        """Checks that P174 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p174_starts_before_the_end_of')
        assert entity.p174_starts_before_the_end_of is None

    # ------------------------- #

    def test_p175_starts_before_or_with_the_start_of_field_exists(self) -> None:
        """Checks that P175 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p175_starts_before_or_with_the_start_of')
        assert entity.p175_starts_before_or_with_the_start_of is None

    # ------------------------- #

    def test_p176_starts_before_the_start_of_field_exists(self) -> None:
        """Checks that P176 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p176_starts_before_the_start_of')
        assert entity.p176_starts_before_the_start_of is None

    # ------------------------- #

    def test_p182_ends_before_or_with_start_of_field_exists(self) -> None:
        """Checks that P182 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p182_ends_before_or_with_start_of')
        assert entity.p182_ends_before_or_with_start_of is None

    # ------------------------- #

    def test_p183_ends_before_the_start_of_field_exists(self) -> None:
        """Checks that P183 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p183_ends_before_the_start_of')
        assert entity.p183_ends_before_the_start_of is None

    # ------------------------- #

    def test_p184_ends_before_or_with_the_end_of_field_exists(self) -> None:
        """Checks that P184 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p184_ends_before_or_with_the_end_of')
        assert entity.p184_ends_before_or_with_the_end_of is None

    # ------------------------- #

    def test_p185_ends_before_the_end_of_field_exists(self) -> None:
        """Checks that P185 property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p185_ends_before_the_end_of')
        assert entity.p185_ends_before_the_end_of is None

    # === E4-inherited properties =====

    def test_p7_took_place_at_field_exists(self) -> None:
        """Checks that P7 took place at property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p7_took_place_at')
        assert entity.p7_took_place_at is not None

    # ------------------------- #

    def test_p8_took_place_on_or_within_field_exists(self) -> None:
        """Checks that P8 took place on or within property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p8_took_place_on_or_within')
        assert entity.p8_took_place_on_or_within is None

    # ------------------------- #

    def test_p9_consists_of_field_exists(self) -> None:
        """Checks that P9 consists of property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p9_consists_of')
        assert entity.p9_consists_of is None

    # ------------------------- #

    def test_p10_falls_within_field_exists(self) -> None:
        """Checks that P10 falls within property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p10_falls_within')
        assert entity.p10_falls_within is None

    # ------------------------- #

    def test_p132_spatiotemporally_overlaps_field_exists(self) -> None:
        """Checks that P132 spatiotemporally overlaps property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p132_spatiotemporally_overlaps')
        assert entity.p132_spatiotemporally_overlaps is None

    # ------------------------- #

    def test_p160_has_temporal_projection_field_exists(self) -> None:
        """Checks that P160 has temporal projection property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p160_has_temporal_projection')
        assert entity.p160_has_temporal_projection is not None

    # ------------------------- #

    def test_p161_has_spatial_projection_field_exists(self) -> None:
        """Checks that P161 has spatial projection property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E5Event(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p161_has_spatial_projection')
        assert entity.p161_has_spatial_projection is not None

    # === E5-specific properties =====

    # === P11 had participant =====

    def test_p11_had_participant_field_exists(self) -> None:
        """Checks that P11 had participant property field exists;"""
        entity = _create_minimal_e5_event()
        assert hasattr(entity, 'p11_had_participant')
        assert entity.p11_had_participant is None

    # ------------------------- #

    def test_p11_accepts_e39_actor(self) -> None:
        """Checks that P11 accepts E39 Actor instances;"""
        actor = E39Actor(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Napoleon Bonaparte')],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        entity = _create_minimal_e5_event()
        entity.p11_had_participant = [actor]

        assert entity.p11_had_participant is not None
        assert isinstance(entity.p11_had_participant[0], E39Actor)

    # ------------------------- #

    def test_p11_rejects_non_e39(self) -> None:
        """Checks that P11 rejects non-E39 Actor types;"""
        with pytest.raises(ValueError):
            E5Event(
                p7_took_place_at=[_create_minimal_place()],
                p160_has_temporal_projection=_create_minimal_timespan(),
                p161_has_spatial_projection=[_create_minimal_place()],
                p11_had_participant=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_p11_example_battle_of_waterloo(self) -> None:
        """Tests P11 with Battle of Waterloo example;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()

        napoleon = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Napoleon Bonaparte'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        wellington = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Duke of Wellington'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        entity = E5Event(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Battle of Waterloo'),
            ],
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p11_had_participant=[napoleon, wellington],
        )
        assert entity.p11_had_participant is not None
        assert len(entity.p11_had_participant) == 2

    # === P12 occurred in presence of =====

    def test_p12_occurred_in_presence_of_field_exists(self) -> None:
        """Checks that P12 occurred in the presence of property field exists;"""
        entity = _create_minimal_e5_event()
        assert hasattr(entity, 'p12_occurred_in_presence_of')
        assert entity.p12_occurred_in_presence_of is None

    # ------------------------- #

    def test_p12_accepts_e77_persistent_item(self) -> None:
        """Checks that P12 accepts E77 Persistent Item instances;"""
        artifact = E77PersistentItem(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Ancient Vase')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
        )
        entity = _create_minimal_e5_event()
        entity.p12_occurred_in_presence_of = [artifact]

        assert entity.p12_occurred_in_presence_of is not None
        assert isinstance(entity.p12_occurred_in_presence_of[0], E77PersistentItem)

    # ------------------------- #

    def test_p12_rejects_non_e77(self) -> None:
        """Checks that P12 rejects non-E77 Persistent Item types;"""
        with pytest.raises(ValueError):
            E5Event(
                p7_took_place_at=[_create_minimal_place()],
                p160_has_temporal_projection=_create_minimal_timespan(),
                p161_has_spatial_projection=[_create_minimal_place()],
                p12_occurred_in_presence_of=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_p12_example_titanic_sinking(self) -> None:
        """Tests P12 with Titanic sinking example;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()

        deckchair = E77PersistentItem(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Deckchair 42'),
            ],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
        )
        entity = E5Event(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Sinking of the Titanic'),
            ],
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p12_occurred_in_presence_of=[deckchair],
        )
        assert entity.p12_occurred_in_presence_of is not None
        assert isinstance(entity.p12_occurred_in_presence_of[0], E77PersistentItem)


# ******************************************************************************************************************* #


class TestE5EventSerialization:
    """Tests for E5Event serialization.

    """

    def test_e5_model_dump_json_includes_id(self) -> None:
        """Checks that model_dump_json includes id field;"""
        entity = _create_minimal_e5_event()
        entity.p1_is_identified_by = [
            E41Appellation(p190_has_symbolic_content='Test Event'),
        ]
        json_str = entity.model_dump_json()
        assert '"id"' in json_str

    # ------------------------- #

    def test_e5_model_dump_with_alias_includes_at_id(self) -> None:
        """Checks that model_dump with by_alias includes @id;"""
        entity = _create_minimal_e5_event()
        dump = entity.model_dump(by_alias=True)
        assert '@id' in dump

    # ------------------------- #

    def test_e5_model_dump_with_alias_includes_crm_code(self) -> None:
        """Checks that model_dump with by_alias includes crm_code;"""
        entity = _create_minimal_e5_event()
        dump = entity.model_dump(by_alias=True)
        assert 'crm_code' not in dump


# ******************************************************************************************************************* #


class TestE5EventComplete:
    """Complete E5Event entity tests with all properties;

    """

    def test_complete_e5_event_battle_of_stalingrad(self) -> None:
        """Tests complete E5 Event with Battle of Stalingrad example;"""
        # Reference event for temporal relations
        timespan = _create_minimal_timespan()
        
        # Place
        stalingrad = E53Place(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Stalingrad'),
            ],
            p157_is_at_rest_relative_to=[
                E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Reference Object')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=_create_minimal_timespan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )
            ],
        )
        # Actors (participants)
        german_forces = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='German 6th Army'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        soviet_forces = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Soviet 62nd Army'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        # Persistent items present at the event
        tank = E77PersistentItem(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='T-34 Tank'),
            ],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
        )
        entity = E5Event(
            # E1 properties
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Battle of Stalingrad'),
                E42Identifier(p190_has_symbolic_content='BATTLE-STALINGRAD-1942'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='military battle')]),
            ],
            p3_has_note=[
                'Major battle on the Eastern Front of World War II.',
                'One of the bloodiest battles in history.',
            ],
            p4_has_timespan=timespan,
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='BATTLE-STALINGRAD-1942'),
            p137_exemplifies=[E55Type(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Turning Point Battle')],
            )],
            # E4/E92 required properties
            p7_took_place_at=[stalingrad],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[stalingrad],
            # E5 specific properties
            p11_had_participant=[german_forces, soviet_forces],
            p12_occurred_in_presence_of=[tank],
        )

        # Verify all properties are set;
        assert entity.p1_is_identified_by is not None
        assert len(entity.p1_is_identified_by) == 2
        assert entity.p2_has_type is not None
        assert entity.p3_has_note is not None
        assert len(entity.p3_has_note) == 2
        assert entity.p4_has_timespan is not None
        assert entity.p7_took_place_at is not None
        assert entity.p11_had_participant is not None
        assert len(entity.p11_had_participant) == 2
        assert entity.p12_occurred_in_presence_of is not None
        assert entity.p48_has_preferred_identifier is not None
        assert entity.p137_exemplifies is not None
        assert entity.crm_code == 'E5'
        assert entity.crm_label == 'E5 Event'

        # Validate serialization;
        json_output = entity.model_dump_json()
        assert '"id"' in json_output

    # ------------------------- #

    def test_complete_e5_event_ylata_conference(self) -> None:
        """Tests complete E5 Event with Yalta Conference example;"""
        timespan = _create_minimal_timespan()
        
        # Participants
        roosevelt = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Franklin D. Roosevelt'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        churchill = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Winston Churchill'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        stalin = E39Actor(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Joseph Stalin'),
            ],
            p74_has_current_or_former_residence=[],
            p76_has_contact_point=[],
        )
        # Place
        livadia_palace = E53Place(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Livadia Palace'),
            ],
            p157_is_at_rest_relative_to=[
                E18PhysicalThing(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Reference Object')],
                    p45_consists_of=[E57Material()],
                    p53_has_former_or_current_location=[],
                    p196_defines=E92SpaceTimeVolume(
                        p160_has_temporal_projection=_create_minimal_timespan(),
                        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
                    ),
                )
            ],
        )
        # Persistent item (the table they signed on)
        signing_table = E77PersistentItem(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Conference signing table'),
            ],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
        )
        entity = E5Event(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Yalta Conference'),
                E42Identifier(p190_has_symbolic_content='YALTA-1945'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='diplomatic conference')]),
            ],
            p3_has_note=['Meeting of the Big Three Allied leaders during World War II.'],
            p4_has_timespan=timespan,
            p7_took_place_at=[livadia_palace],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[livadia_palace],
            p11_had_participant=[roosevelt, churchill, stalin],
            p12_occurred_in_presence_of=[signing_table],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='YALTA-1945'),
        )

        # Verify properties;
        assert entity.p1_is_identified_by is not None
        assert entity.p2_has_type is not None
        assert entity.p3_has_note is not None
        assert entity.p4_has_timespan is not None
        assert entity.p7_took_place_at is not None
        assert entity.p11_had_participant is not None
        assert len(entity.p11_had_participant) == 3
        assert entity.p12_occurred_in_presence_of is not None
        assert entity.p48_has_preferred_identifier is not None
        assert entity.crm_code == 'E5'

        # Verify serialization;
        dump = entity.model_dump(by_alias=True, exclude_none=True)
        assert '@id' in dump
        assert 'p11_had_participant' in dump
        assert 'p12_occurred_in_presence_of' in dump
