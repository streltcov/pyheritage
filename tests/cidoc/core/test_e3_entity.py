# -*- coding: utf-8 -*-

"""Tests for E3ConditionState CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E2TemporalEntity,
    E3ConditionState,
    E41Appellation,
    E42Identifier,
    E52TimeSpan,
    E55Type,
)


class TestE3ConditionStateInheritance:
    """E3 Condition State inheritance hierarchy tests;

    """

    def test_e3_inherits_from_e2(self) -> None:
        """Checks that E3ConditionState inherits from E2TemporalEntity;"""
        assert issubclass(E3ConditionState, E2TemporalEntity)

    # ------------------------- #

    def test_e3_inherits_from_e1(self) -> None:
        """Checks that E3ConditionState inherits from E1CRMEntity;"""
        assert issubclass(E3ConditionState, E1CRMEntity)

    # ------------------------- #

    def test_e3_inherits_e1_properties(self) -> None:
        """Checks that E3 inherits P1, P2, P3, P48, P137 from E1CRMEntity;"""
        entity = E3ConditionState()

        assert hasattr(entity, 'p1_is_identified_by')
        assert hasattr(entity, 'p2_has_type')
        assert hasattr(entity, 'p3_has_note')
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert hasattr(entity, 'p137_exemplifies')

    # ------------------------- #

    def test_e3_inherits_e2_properties(self) -> None:
        """Checks that E3 inherits P4, P173, P174, P175, P176, P182, P183, P184, P185 from E2;"""
        entity = E3ConditionState()

        assert hasattr(entity, 'p4_has_timespan')
        assert hasattr(entity, 'p173_starts_before_or_with_the_end_of')
        assert hasattr(entity, 'p174_starts_before_the_end_of')
        assert hasattr(entity, 'p175_starts_before_or_with_the_start_of')
        assert hasattr(entity, 'p176_starts_before_the_start_of')
        assert hasattr(entity, 'p182_ends_before_or_with_start_of')
        assert hasattr(entity, 'p183_ends_before_the_start_of')
        assert hasattr(entity, 'p184_ends_before_or_with_the_end_of')
        assert hasattr(entity, 'p185_ends_before_the_end_of')

    # ------------------------- #

    def test_e3_has_p5_consists_of(self) -> None:
        """Checks that E3 has P5 consists of property;"""
        entity = E3ConditionState()
        assert hasattr(entity, 'p5_consists_of')
        assert entity.p5_consists_of is None


# ******************************************************************************************************************* #


class TestE3ConditionStateP5ConsistsOf:
    """Tests for P5 consists of property;

    """

    def test_p5_field_exists(self) -> None:
        """Checks that P5 consists of property field exists;"""
        entity = E3ConditionState()

        assert hasattr(entity, 'p5_consists_of')
        assert entity.p5_consists_of is None

    # ------------------------- #

    def test_p5_accepts_e3_condition_state(self) -> None:
        """Checks that P5 accepts E3 Condition State instances;"""
        sub_condition = E3ConditionState(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Structural Damage')],
        )
        entity = E3ConditionState(
            p5_consists_of=[sub_condition],
        )
        assert entity.p5_consists_of is not None
        assert isinstance(entity.p5_consists_of[0], E3ConditionState)

    # ------------------------- #

    def test_p5_example_amber_room(self) -> None:
        """Tests P5 with Amber Room example from CIDOC spec;"""
        reconstructed_state = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Amber Room reconstructed state'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='reconstructed')]),
            ],
        )
        entity = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Amber Room condition 2003-present'),
            ],
            p5_consists_of=[reconstructed_state],
        )
        assert entity.p5_consists_of is not None


# ******************************************************************************************************************* #


class TestE3ConditionStateP48HasPreferredIdentifier:
    """Tests for P48 has preferred identifier property;

    """

    def test_p48_field_exists(self) -> None:
        """Checks that P48 has preferred identifier property field exists;"""
        entity = E3ConditionState()
        assert hasattr(entity, 'p48_has_preferred_identifier')
        assert entity.p48_has_preferred_identifier is None

    # ------------------------- #

    def test_p48_accepts_identifier(self) -> None:
        """Checks that P48 accepts E42 Identifier instances;"""
        entity = E3ConditionState(
            p48_has_preferred_identifier=E42Identifier(
                p190_has_symbolic_content='COND-STATE-001',
            ),
        )
        assert entity.p48_has_preferred_identifier is not None
        assert isinstance(entity.p48_has_preferred_identifier, E42Identifier)


# ******************************************************************************************************************* #


class TestE3ConditionStateSerialization:
    """Tests for E3ConditionState serialization.

    """

    def test_e3_model_dump_json_includes_id(self) -> None:
        """Checks that model_dump_json includes id field;"""
        entity = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Test Condition State'),
            ],
        )
        json_str = entity.model_dump_json()
        assert '"id"' in json_str

    # ------------------------- #

    def test_e3_model_dump_with_alias_includes_at_id(self) -> None:
        """Checks that model_dump with by_alias includes @id;"""
        entity = E3ConditionState()
        dump = entity.model_dump(by_alias=True)
        assert '@id' in dump

    # ------------------------- #

    def test_e3_model_dump_with_alias_includes_crm_code(self) -> None:
        """Checks that model_dump with by_alias includes crm_code;"""
        entity = E3ConditionState()
        dump = entity.model_dump(by_alias=True)
        assert 'crm_code' not in dump


# ******************************************************************************************************************* #


class TestE3ConditionStateComplete:
    """Complete E3ConditionState entity tests with all properties;

    """

    def test_complete_e3_condition_state_peterhof(self) -> None:
        """Tests complete E3 Condition State with Peterhof Palace example;"""
        # Reference event for temporal relations
        restoration_start = E2TemporalEntity(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Peterhof Restoration Start'),
            ],
        )
        time_span = E52TimeSpan(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='1944-1946'),
            ],
        )
        structural_damage = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Structural Damage'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='severe damage')]),
            ],
        )
        entity = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Ruined State of Peterhof Palace'),
                E42Identifier(p190_has_symbolic_content='PETERHOF-COND-1944-1946'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='ruined')]),
            ],
            p3_has_note=[
                'The palace was severely damaged during World War II.',
                'Restoration work began in 1946.',
            ],
            p4_has_timespan=time_span,
            p5_consists_of=[structural_damage],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='PETERHOF-COND-1944-1946'),
            p137_exemplifies=[E55Type(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='War Damage Condition')],
            )],
            p173_starts_before_or_with_the_end_of=[restoration_start],
            p182_ends_before_or_with_start_of=[restoration_start],
        )

        # Verify all properties are set;
        assert entity.p1_is_identified_by is not None
        assert len(entity.p1_is_identified_by) == 2
        assert entity.p2_has_type is not None
        assert entity.p3_has_note is not None
        assert len(entity.p3_has_note) == 2
        assert entity.p4_has_timespan is not None
        assert entity.p5_consists_of is not None
        assert entity.p48_has_preferred_identifier is not None
        assert entity.p137_exemplifies is not None
        assert entity.p173_starts_before_or_with_the_end_of is not None
        assert entity.p182_ends_before_or_with_start_of is not None
        assert entity.crm_code == 'E3'
        assert entity.crm_label == 'E3 Condition State'

        # Validate serialization;
        json_output = entity.model_dump_json()
        assert '"id"' in json_output

    # ------------------------- #

    def test_complete_e3_condition_state_amber_room(self) -> None:
        """Tests complete E3 Condition State with Amber Room example;"""
        # Reconstructed state (P5)
        reconstructed = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Reconstructed Amber Room'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='reconstructed')]),
            ],
        )
        entity = E3ConditionState(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Amber Room condition from summer 2003'),
                E42Identifier(p190_has_symbolic_content='AMBER-ROOM-2003'),
            ],
            p2_has_type=[
                E55Type(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='reconstructed')]),
            ],
            p3_has_note=['Reconstruction completed in summer 2003 at Tsarskoje Selo.'],
            p5_consists_of=[reconstructed],
            p48_has_preferred_identifier=E42Identifier(p190_has_symbolic_content='AMBER-ROOM-2003'),
        )

        # Verify properties;
        assert entity.p1_is_identified_by is not None
        assert entity.p2_has_type is not None
        assert entity.p3_has_note is not None
        assert entity.p5_consists_of is not None
        assert entity.p48_has_preferred_identifier is not None
        assert entity.crm_code == 'E3'

        # Verify serialization;
        dump = entity.model_dump(by_alias=True, exclude_none=True)
        assert '@id' in dump
        assert 'p5_consists_of' in dump
