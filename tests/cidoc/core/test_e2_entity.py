# -*- coding: utf-8 -*-

"""Tests for E2TemporalEntity model;

"""


# pylint: disable=E0401,C0116,W0612


import re

import pytest

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E2TemporalEntity,
    E41Appellation,
    E42Identifier,
    E52TimeSpan,
    E55Type,
)


class TestE2TemporalEntityInheritance:
    """E2 Temporal Entity inheritance hierarchy tests;

    """

    def test_e2_inherits_from_e1(self) -> None:
        """Checks that E2TemporalEntity inherits from E1CRMEntity;"""
        assert issubclass(E2TemporalEntity, E1CRMEntity)

    # ------------------------- #

    def test_e2_inherits_e1_properties(self) -> None:
        """Checks that E2 inherits P1, P2, P3, P48, P137 from E1CRMEntity;"""
        entity = E2TemporalEntity()

        # E1 properties
        assert hasattr(entity, 'p1_is_identified_by')
        assert hasattr(entity, 'p2_has_type')
        assert hasattr(entity, 'p3_has_note')
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert hasattr(entity, 'p137_exemplifies')

    # ------------------------- #

    def test_e2_has_p4_has_timespan(self) -> None:
        """Checks that E2 has P4 has time-span property;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p4_has_timespan')

    # ------------------------- #

    def test_e2_has_temporal_primitive_properties(self) -> None:
        """Checks that E2 has all temporal primitive properties P173-P176, P182-P185;"""
        entity = E2TemporalEntity()

        # P173-P176: starts before/with properties;
        assert hasattr(entity, 'p173_starts_before_or_with_the_end_of')
        assert hasattr(entity, 'p174_starts_before_the_end_of')
        assert hasattr(entity, 'p175_starts_before_or_with_the_start_of')
        assert hasattr(entity, 'p176_starts_before_the_start_of')

        # P182-P185: ends before/with properties;
        assert hasattr(entity, 'p182_ends_before_or_with_start_of')
        assert hasattr(entity, 'p183_ends_before_the_start_of')
        assert hasattr(entity, 'p184_ends_before_or_with_the_end_of')
        assert hasattr(entity, 'p185_ends_before_the_end_of')

    # ------------------------- #

    def test_e2_mro_includes_property_mixins(self) -> None:
        """Checks that E2 MRO includes all expected property mixin classes;"""
        from pyheritage.cidoc.core.properties import (
            P1IsIdentifiedBy,
            P2HasType,
            P3HasNote,
            P4HasTimeSpan,
            P48HasPreferredIdentifier,
            P137Exemplifies,
            P173StartsBeforeOrWithTheEndOf,
            P174StartsBeforeTheEndOf,
            P175StartsBeforeOrWithTheStartOf,
            P176StartsBeforeTheStartOf,
            P182EndsBeforeOrWitheStartOf,
            P183EndsBeforeTheStartOf,
            P184EndsBeforeOrWithTheEndOf,
            P185EndsBeforeTheEndOf,
        )

        mro = E2TemporalEntity.__mro__

        assert P1IsIdentifiedBy in mro
        assert P2HasType in mro
        assert P3HasNote in mro
        assert P4HasTimeSpan in mro
        assert P48HasPreferredIdentifier in mro
        assert P137Exemplifies in mro
        assert P173StartsBeforeOrWithTheEndOf in mro
        assert P174StartsBeforeTheEndOf in mro
        assert P175StartsBeforeOrWithTheStartOf in mro
        assert P176StartsBeforeTheStartOf in mro
        assert P182EndsBeforeOrWitheStartOf in mro
        assert P183EndsBeforeTheStartOf in mro
        assert P184EndsBeforeOrWithTheEndOf in mro
        assert P185EndsBeforeTheEndOf in mro


# ******************************************************************************************************************* #


class TestE2TemporalEntityProperties:
    """E2 Temporal Entity property tests;

    """

    def test_p1_is_identified_by_field_exists(self) -> None:
        """Checks that P1 is identified by property field exists;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p1_is_identified_by')
        assert entity.p1_is_identified_by is None

    # ------------------------- #

    def test_p1_is_identified_by_accepts_appellation(self) -> None:
        """Checks that P1 property accepts E41 Appellation instances;"""
        entity = E2TemporalEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Bronze Age'),
            ],
        )
        assert len(entity.p1_is_identified_by) == 1
        assert isinstance(entity.p1_is_identified_by[0], E41Appellation)

    # ------------------------- #

    def test_p2_has_type_field_exists(self) -> None:
        """Checks that P2 has type property field exists;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p2_has_type')
        assert entity.p2_has_type == []

    # ------------------------- #

    def test_p2_has_type_accepts_type(self) -> None:
        """Checks that P2 property accepts E55 Type instances;"""
        entity = E2TemporalEntity(
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Historical Period')]),
            ],
        )
        assert len(entity.p2_has_type) == 1
        assert isinstance(entity.p2_has_type[0], E55Type)

    # ------------------------- #

    def test_p3_has_note_field_exists(self) -> None:
        """Checks that P3 has note property field exists;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p3_has_note')
        assert entity.p3_has_note is None

    # ------------------------- #

    def test_p3_has_note_accepts_string(self) -> None:
        """Checks that P3 property accepts string content;"""
        entity = E2TemporalEntity(
            p3_has_note=['A period of ancient history characterized by bronze metallurgy'],
        )
        assert entity.p3_has_note is not None
        assert len(entity.p3_has_note) == 1
        assert entity.p3_has_note[0].value == 'A period of ancient history characterized by bronze metallurgy'

    # ------------------------- #

    def test_p4_has_timespan_field_exists(self) -> None:
        """Checks that P4 has time-span property field exists;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p4_has_timespan')
        assert entity.p4_has_timespan is None

    # ------------------------- #

    def test_p4_has_timespan_accepts_e52(self) -> None:
        """Checks that P4 property accepts E52 Time-Span instances;"""
        time_span = E52TimeSpan(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='3300-1200 BCE')],
        )
        entity = E2TemporalEntity(p4_has_timespan=time_span)

        assert entity.p4_has_timespan is not None
        assert isinstance(entity.p4_has_timespan, E52TimeSpan)

    # ------------------------- #

    def test_p48_has_preferred_identifier_field_exists(self) -> None:
        """Checks that P48 has preferred identifier property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert entity.p48_has_preferred_identifier is None

    # ------------------------- #

    def test_p48_has_preferred_identifier_accepts_identifier(self) -> None:
        """Checks that P48 property accepts E42 Identifier instances;"""
        entity = E2TemporalEntity(
            p48_has_preferred_identifier=E42Identifier(
                p190_has_symbolic_content='PERIOD-001',
            ),
        )

        assert entity.p48_has_preferred_identifier is not None
        assert isinstance(entity.p48_has_preferred_identifier, E42Identifier)

    # ------------------------- #

    def test_p137_exemplifies_field_exists(self) -> None:
        """Checks that P137 exemplifies property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p137_exemplifies')
        assert entity.p137_exemplifies is None

    # ------------------------- #

    def test_p137_exemplifies_accepts_type(self) -> None:
        """Checks that P137 property accepts E55 Type instances;"""
        entity = E2TemporalEntity(
            p137_exemplifies=[E55Type(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Exemplary Period')],
            )],
        )

        assert entity.p137_exemplifies is not None
        assert isinstance(entity.p137_exemplifies[0], E55Type)

    # ------------------------- #

    def test_p173_field_exists(self) -> None:
        """Checks that P173 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p173_starts_before_or_with_the_end_of')
        assert entity.p173_starts_before_or_with_the_end_of is None

    # ------------------------- #

    def test_p173_accepts_e2_temporal_entity(self) -> None:
        """Checks that P173 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Reference Event')],
        )
        entity = E2TemporalEntity(
            p173_starts_before_or_with_the_end_of=[other_event],
        )

        assert entity.p173_starts_before_or_with_the_end_of is not None
        assert isinstance(entity.p173_starts_before_or_with_the_end_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p174_field_exists(self) -> None:
        """Checks that P174 property field exists;"""
        entity = E2TemporalEntity()
        assert hasattr(entity, 'p174_starts_before_the_end_of')
        assert entity.p174_starts_before_the_end_of is None

    # ------------------------- #

    def test_p174_accepts_e2_temporal_entity(self) -> None:
        """Checks that P174 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p174_starts_before_the_end_of=[other_event],
        )

        assert entity.p174_starts_before_the_end_of is not None
        assert isinstance(entity.p174_starts_before_the_end_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p175_field_exists(self) -> None:
        """Checks that P175 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p175_starts_before_or_with_the_start_of')
        assert entity.p175_starts_before_or_with_the_start_of is None

    # ------------------------- #

    def test_p175_accepts_e2_temporal_entity(self) -> None:
        """Checks that P175 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p175_starts_before_or_with_the_start_of=[other_event],
        )

        assert entity.p175_starts_before_or_with_the_start_of is not None
        assert isinstance(entity.p175_starts_before_or_with_the_start_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p176_field_exists(self) -> None:
        """Checks that P176 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p176_starts_before_the_start_of')
        assert entity.p176_starts_before_the_start_of is None

    # ------------------------- #

    def test_p176_accepts_e2_temporal_entity(self) -> None:
        """Checks that P176 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p176_starts_before_the_start_of=[other_event],
        )

        assert entity.p176_starts_before_the_start_of is not None
        assert isinstance(entity.p176_starts_before_the_start_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p182_field_exists(self) -> None:
        """Checks that P182 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p182_ends_before_or_with_start_of')
        assert entity.p182_ends_before_or_with_start_of is None

    # ------------------------- #

    def test_p182_accepts_e2_temporal_entity(self) -> None:
        """Checks that P182 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p182_ends_before_or_with_start_of=[other_event],
        )

        assert entity.p182_ends_before_or_with_start_of is not None
        assert isinstance(entity.p182_ends_before_or_with_start_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p183_field_exists(self) -> None:
        """Checks that P183 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p183_ends_before_the_start_of')
        assert entity.p183_ends_before_the_start_of is None

    # ------------------------- #

    def test_p183_accepts_e2_temporal_entity(self) -> None:
        """Checks that P183 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p183_ends_before_the_start_of=[other_event],
        )

        assert entity.p183_ends_before_the_start_of is not None
        assert isinstance(entity.p183_ends_before_the_start_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p184_field_exists(self) -> None:
        """Checks that P184 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p184_ends_before_or_with_the_end_of')
        assert entity.p184_ends_before_or_with_the_end_of is None

    # ------------------------- #

    def test_p184_accepts_e2_temporal_entity(self) -> None:
        """Checks that P184 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p184_ends_before_or_with_the_end_of=[other_event],
        )

        assert entity.p184_ends_before_or_with_the_end_of is not None
        assert isinstance(entity.p184_ends_before_or_with_the_end_of[0], E2TemporalEntity)

    # ------------------------- #

    def test_p185_field_exists(self) -> None:
        """Checks that P185 property field exists;"""
        entity = E2TemporalEntity()

        assert hasattr(entity, 'p185_ends_before_the_end_of')
        assert entity.p185_ends_before_the_end_of is None

    # ------------------------- #

    def test_p185_accepts_e2_temporal_entity(self) -> None:
        """Checks that P185 accepts E2TemporalEntity instances;"""
        other_event = E2TemporalEntity()
        entity = E2TemporalEntity(
            p185_ends_before_the_end_of=[other_event],
        )
        
        assert entity.p185_ends_before_the_end_of is not None
        assert isinstance(entity.p185_ends_before_the_end_of[0], E2TemporalEntity)


# ******************************************************************************************************************* #


class TestE2TemporalEntityValidation:
    """E2 Temporal Entity validation tests for reject of invalid values;

    """

    def test_p4_has_timespan_rejects_non_e52(self) -> None:
        """Checks that P4 rejects non-E52TimeSpan values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p4_has_timespan="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p173_rejects_non_e2(self) -> None:
        """Checks that P173 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p173_starts_before_or_with_the_end_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p174_rejects_non_e2(self) -> None:
        """Checks that P174 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p174_starts_before_the_end_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p175_rejects_non_e2(self) -> None:
        """Checks that P175 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p175_starts_before_or_with_the_start_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p176_rejects_non_e2(self) -> None:
        """Checks that P176 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p176_starts_before_the_start_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p182_rejects_non_e2(self) -> None:
        """Checks that P182 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p182_ends_before_or_with_start_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p183_rejects_non_e2(self) -> None:
        """Checks that P183 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p183_ends_before_the_start_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p184_rejects_non_e2(self) -> None:
        """Checks that P184 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p184_ends_before_or_with_the_end_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p185_rejects_non_e2(self) -> None:
        """Checks that P185 rejects non-E2TemporalEntity values;"""
        with pytest.raises(ValueError):
            E2TemporalEntity(p185_ends_before_the_end_of="invalid")  # type: ignore[arg-type]


# ******************************************************************************************************************* #


class TestE2TemporalEntityComplete:
    """Complete E2 Temporal Entity test with all properties;

    """

    def test_complete_e2_entity(self) -> None:
        """Tests complete E2TemporalEntity with all properties populated;"""
        # Create reference temporal entity for temporal relations
        reference_event = E2TemporalEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Reference Event'),
            ],
        )

        # Create time-span
        time_span = E52TimeSpan(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='3300-1200 BCE'),
            ],
            p3_has_note=['Bronze Age time-span'],
        )

        # Create the main entity with all properties
        entity = E2TemporalEntity(
            # E1 properties
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Bronze Age'),
                E42Identifier(p190_has_symbolic_content='PERIOD-BRONZE-001'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Historical Period')]),
            ],
            p3_has_note=['A period of ancient history characterized by bronze metallurgy'],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='PERIOD-BRONZE-001'),
            p137_exemplifies=[E55Type(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Exemplary Bronze Age Site')],
            )],
            # E2 specific properties
            p4_has_timespan=time_span,
            p173_starts_before_or_with_the_end_of=[reference_event],
            p174_starts_before_the_end_of=[reference_event],
            p175_starts_before_or_with_the_start_of=[reference_event],
            p176_starts_before_the_start_of=[reference_event],
            p182_ends_before_or_with_start_of=[reference_event],
            p183_ends_before_the_start_of=[reference_event],
            p184_ends_before_or_with_the_end_of=[reference_event],
            p185_ends_before_the_end_of=[reference_event],
        )

        # Verify E1 properties;
        assert entity.p1_is_identified_by is not None
        assert len(entity.p1_is_identified_by) == 2
        assert entity.p2_has_type is not None
        assert len(entity.p2_has_type) == 1
        assert entity.p3_has_note is not None
        assert len(entity.p3_has_note) == 1
        assert entity.p3_has_note[0].value == 'A period of ancient history characterized by bronze metallurgy'
        assert entity.p48_has_preferred_identifier is not None
        assert entity.p137_exemplifies is not None

        # Verify E2 properties;
        assert entity.p4_has_timespan is not None
        assert isinstance(entity.p4_has_timespan, E52TimeSpan)

        # Verify temporal relations;
        assert entity.p173_starts_before_or_with_the_end_of is not None
        assert entity.p174_starts_before_the_end_of is not None
        assert entity.p175_starts_before_or_with_the_start_of is not None
        assert entity.p176_starts_before_the_start_of is not None
        assert entity.p182_ends_before_or_with_start_of is not None
        assert entity.p183_ends_before_the_start_of is not None
        assert entity.p184_ends_before_or_with_the_end_of is not None
        assert entity.p185_ends_before_the_end_of is not None

        # All temporal relations should be E2TemporalEntity instances;
        for prop in [
            entity.p173_starts_before_or_with_the_end_of,
            entity.p174_starts_before_the_end_of,
            entity.p175_starts_before_or_with_the_start_of,
            entity.p176_starts_before_the_start_of,
            entity.p182_ends_before_or_with_start_of,
            entity.p183_ends_before_the_start_of,
            entity.p184_ends_before_or_with_the_end_of,
            entity.p185_ends_before_the_end_of,
        ]:
            assert isinstance(prop[0], E2TemporalEntity)

    # ------------------------- #

    def test_complete_e2_serialization(self) -> None:
        """Tests complete E2TemporalEntity serialization to JSON;"""
        time_span = E52TimeSpan(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='3300-1200 BCE'),
            ],
        )

        entity = E2TemporalEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Bronze Age'),
            ],
            p4_has_timespan=time_span,
        )

        # Test model_dump;
        dump = entity.model_dump()
        assert 'p1_is_identified_by' in dump
        assert 'p4_has_timespan' in dump
        assert '@id' not in dump  # Without by_alias, should be 'id'
        assert 'id' in dump

        # Test model_dump with by_alias;
        dump_alias = entity.model_dump(by_alias=True)
        assert '@id' in dump_alias
        assert 'id' not in dump_alias

        # Test JSON serialization;
        json_str = entity.model_dump_json(by_alias=True, indent=2)
        assert '@id' in json_str
        assert 'Bronze Age' in json_str
        assert '3300-1200 BCE' in json_str

    # ------------------------- #

    def test_e2_uuid_generation(self) -> None:
        """Checks that E2 entities get unique UUID identifiers;"""
        entity1 = E2TemporalEntity()
        entity2 = E2TemporalEntity()

        assert entity1.id != entity2.id
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )
        assert uuid_pattern.match(entity1.id)
        assert uuid_pattern.match(entity2.id)
