# -*- coding: utf-8 -*-

"""Tests for E4 Period model;

"""


# pylint: disable=E0401,C0116,W0612


import pytest

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E2TemporalEntity,
    E4Period,
    E18PhysicalThing,
    E41Appellation,
    E42Identifier,
    E52TimeSpan,
    E53Place,
    E55Type,
    E57Material,
    E92SpaceTimeVolume,
)


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


class TestE4PeriodInheritance:
    """E4 Period inheritance hierarchy tests;

    """

    def test_e4_inherits_from_e2(self) -> None:
        """Checks that E4Period inherits from E2TemporalEntity;"""
        assert issubclass(E4Period, E2TemporalEntity)

    # ------------------------- #

    def test_e4_inherits_from_e92(self) -> None:
        """Checks that E4Period inherits from E92SpaceTimeVolume;"""
        assert issubclass(E4Period, E92SpaceTimeVolume)

    # ------------------------- #

    def test_e4_inherits_from_e1(self) -> None:
        """Checks that E4Period inherits from E1CRMEntity (via E2 Temporal Entity);"""
        assert issubclass(E4Period, E1CRMEntity)

    # ------------------------- #

    def test_e4_inherits_e1_properties(self) -> None:
        """Checks that E4 inherits all properties from E1CRMEntity via E2TemporalEntity;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
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

    # ------------------------- #

    def test_e4_mro_includes_property_mixins(self) -> None:
        """Checks that E4 MRO includes E4-specific property mixin classes;

        Inherited mixins (P1-P4, P48, P137, P173-P185) are verified in E3 tests.

        """
        from pyheritage.cidoc.core.properties import (
            P7TookPlaceAt,
            P8TookPlaceOnOrWithin,
            P9ConsistsOf,
            P10FallsWithin,
            P132SpatiotemporallyOverlaps,
            P160HasTemporalProjection,
            P161HasSpatialProjection,
        )

        mro = E4Period.__mro__

        assert P7TookPlaceAt in mro
        assert P8TookPlaceOnOrWithin in mro
        assert P9ConsistsOf in mro
        assert P10FallsWithin in mro
        assert P132SpatiotemporallyOverlaps in mro
        assert P160HasTemporalProjection in mro
        assert P161HasSpatialProjection in mro


# ******************************************************************************************************************* #


class TestE4PeriodProperties:
    """E4 Period property tests;

    Tests for all properties (inherited and E4-specific).
    Inherited properties are also tested in E3ConditionState tests.

    """

    # === Inherited properties (E1, E2) =====

    def test_p1_is_identified_by_field_exists(self) -> None:
        """Checks that P1 is identified by property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
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
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p185_ends_before_the_end_of')
        assert entity.p185_ends_before_the_end_of is None

    # === E4-specific properties =====

    # === P7 took place at =====

    def test_p7_took_place_at_field_exists(self) -> None:
        """Checks that P7 took place at property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p7_took_place_at')
        assert entity.p7_took_place_at == [place]

    # ------------------------- #

    def test_p7_took_place_at_accepts_e53_place(self) -> None:
        """Checks that P7 property accepts E53 Place instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
        )
        assert len(entity.p7_took_place_at) == 1
        assert isinstance(entity.p7_took_place_at[0], E53Place)

    # ------------------------- #

    def test_p7_took_place_at_accepts_multiple_places(self) -> None:
        """Checks that P7 property accepts multiple E53 Place instances;"""
        place1 = _create_minimal_place()
        place2 = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place1, place2],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place1],
        )
        assert len(entity.p7_took_place_at) == 2

    # ------------------------- #

    def test_p7_took_place_at_rejects_non_e53(self) -> None:
        """Checks that P7 rejects non-E53Place values;"""
        with pytest.raises(ValueError):
            E4Period(p7_took_place_at=["invalid"])  # type: ignore[list-item]

    # === P8 took place on or within =====

    def test_p8_took_place_on_or_within_field_exists(self) -> None:
        """Checks that P8 took place on or within property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p8_took_place_on_or_within')
        assert entity.p8_took_place_on_or_within is None

    # ------------------------- #

    def test_p8_took_place_on_or_within_accepts_e18(self) -> None:
        """Checks that P8 property accepts E18 Physical Thing instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        physical_thing = E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Westminster Abbey')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=E92SpaceTimeVolume(
                p160_has_temporal_projection=_create_minimal_timespan(),
                p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
            )
        )
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p8_took_place_on_or_within=[physical_thing],
        )
        assert len(entity.p8_took_place_on_or_within) == 1
        assert isinstance(entity.p8_took_place_on_or_within[0], E18PhysicalThing)

    # ------------------------- #

    def test_p8_took_place_on_or_within_rejects_non_e18(self) -> None:
        """Checks that P8 rejects non-E18PhysicalThing values;"""
        with pytest.raises(ValueError):
            E4Period(p8_took_place_on_or_within=["invalid"])  # type: ignore[list-item]

    # === P9 consists of =====

    def test_p9_consists_of_field_exists(self) -> None:
        """Checks that P9 consists of property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p9_consists_of')
        assert entity.p9_consists_of is None

    # ------------------------- #

    def test_p9_consists_of_accepts_e4_period(self) -> None:
        """Checks that P9 property accepts E4 Period instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        sub_period = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Middle Minoan')],
        )
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Cretan Bronze Age')],
            p9_consists_of=sub_period,
        )
        assert entity.p9_consists_of is not None
        assert isinstance(entity.p9_consists_of, E4Period)

    # ------------------------- #

    def test_p9_consists_of_rejects_non_e4(self) -> None:
        """Checks that P9 rejects non-E4Period values;"""
        with pytest.raises(ValueError):
            E4Period(p9_consists_of="invalid")  # type: ignore[arg-type]

    # === P10 falls within =====

    def test_p10_falls_within_field_exists(self) -> None:
        """Checks that P10 falls within property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p10_falls_within')
        assert entity.p10_falls_within is None

    # ------------------------- #

    def test_p10_falls_within_accepts_e92(self) -> None:
        """Checks that P10 property accepts E92 SpaceTime Volume instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        parent_period = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='European Bronze Age')],
        )
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Mycenaean Period')],
            p10_falls_within=[parent_period],
        )
        assert entity.p10_falls_within is not None
        assert len(entity.p10_falls_within) == 1
        assert isinstance(entity.p10_falls_within[0], E4Period)

    # ------------------------- #

    def test_p10_falls_within_rejects_non_e92(self) -> None:
        """Checks that P10 rejects non-E92SpaceTimeVolume values;"""
        with pytest.raises(ValueError):
            E4Period(p10_falls_within=["invalid"])  # type: ignore[list-item]

    # === P132 spatiotemporally overlaps =====

    def test_p132_spatiotemporally_overlaps_field_exists(self) -> None:
        """Checks that P132 spatiotemporally overlaps property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p132_spatiotemporally_overlaps')
        assert entity.p132_spatiotemporally_overlaps is None

    # ------------------------- #

    def test_p132_spatiotemporally_overlaps_accepts_e92(self) -> None:
        """Checks that P132 property accepts E92 SpaceTime Volume instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        other_period = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Hallstatt Period')],
        )
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Urnfield Period')],
            p132_spatiotemporally_overlaps=[other_period],
        )
        assert entity.p132_spatiotemporally_overlaps is not None
        assert len(entity.p132_spatiotemporally_overlaps) == 1
        assert isinstance(entity.p132_spatiotemporally_overlaps[0], E4Period)

    # ------------------------- #

    def test_p132_spatiotemporally_overlaps_rejects_non_e92(self) -> None:
        """Checks that P132 rejects non-E92SpaceTimeVolume values;"""
        with pytest.raises(ValueError):
            E4Period(p132_spatiotemporally_overlaps=["invalid"])  # type: ignore[list-item]

    # === P160 has temporal projection =====

    def test_p160_has_temporal_projection_field_exists(self) -> None:
        """Checks that P160 has temporal projection property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )
        assert hasattr(entity, 'p160_has_temporal_projection')
        assert entity.p160_has_temporal_projection is not None

    # ------------------------- #

    def test_p160_has_temporal_projection_accepts_e52(self) -> None:
        """Checks that P160 property accepts E52 Time-Span instances;"""
        place = _create_minimal_place()
        ts = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=ts,
            p161_has_spatial_projection=[place],
        )

        assert entity.p160_has_temporal_projection is not None
        assert isinstance(entity.p160_has_temporal_projection, E52TimeSpan)

    # ------------------------- #

    def test_p160_has_temporal_projection_rejects_non_e52(self) -> None:
        """Checks that P160 rejects non-E52TimeSpan values;"""
        with pytest.raises(ValueError):
            E4Period(p160_has_temporal_projection="invalid")  # type: ignore[arg-type]

    # === P161 has spatial projection =====

    def test_p161_has_spatial_projection_field_exists(self) -> None:
        """Checks that P161 has spatial projection property field exists;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place]
        )

        assert hasattr(entity, 'p161_has_spatial_projection')
        assert entity.p161_has_spatial_projection is not None

    # ------------------------- #

    def test_p161_has_spatial_projection_accepts_e53(self) -> None:
        """Checks that P161 property accepts E53 Place instances;"""
        place = _create_minimal_place()
        timespan = _create_minimal_timespan()
        entity = E4Period(
            p7_took_place_at=[place],
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[place],
        )
        assert entity.p161_has_spatial_projection is not None
        assert len(entity.p161_has_spatial_projection) == 1
        assert isinstance(entity.p161_has_spatial_projection[0], E53Place)

    # ------------------------- #

    def test_p161_has_spatial_projection_rejects_non_e53(self) -> None:
        """Checks that P161 rejects non-E53Place values;"""
        with pytest.raises(ValueError):
            E4Period(p161_has_spatial_projection=["invalid"])  # type: ignore[list-item]


# ******************************************************************************************************************* #


class TestE4PeriodValidation:
    """E4 Period validation tests — only E4-specific properties;

    """

    def test_p7_took_place_at_rejects_non_e53(self) -> None:
        """Checks that P7 rejects non-E53Place values;"""
        with pytest.raises(ValueError):
            E4Period(p7_took_place_at=["invalid"])  # type: ignore[list-item]

    # ------------------------- #

    def test_p8_took_place_on_or_within_rejects_non_e18(self) -> None:
        """Checks that P8 rejects non-E18PhysicalThing values;"""
        with pytest.raises(ValueError):
            E4Period(p8_took_place_on_or_within=["invalid"])  # type: ignore[list-item]

    # ------------------------- #

    def test_p9_consists_of_rejects_non_e4(self) -> None:
        """Checks that P9 rejects non-E4Period values;"""
        with pytest.raises(ValueError):
            E4Period(p9_consists_of="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p10_falls_within_rejects_non_e92(self) -> None:
        """Checks that P10 rejects non-E92SpaceTimeVolume values;"""
        with pytest.raises(ValueError):
            E4Period(p10_falls_within=["invalid"])  # type: ignore[list-item]

    # ------------------------- #

    def test_p132_spatiotemporally_overlaps_rejects_non_e92(self) -> None:
        """Checks that P132 rejects non-E92SpaceTimeVolume values;"""
        with pytest.raises(ValueError):
            E4Period(p132_spatiotemporally_overlaps=["invalid"])  # type: ignore[list-item]

    # ------------------------- #

    def test_p160_has_temporal_projection_rejects_non_e52(self) -> None:
        """Checks that P160 rejects non-E52TimeSpan values;"""
        with pytest.raises(ValueError):
            E4Period(p160_has_temporal_projection="invalid")  # type: ignore[arg-type]

    # ------------------------- #

    def test_p161_has_spatial_projection_rejects_non_e53(self) -> None:
        """Checks that P161 rejects non-E53Place values;"""
        with pytest.raises(ValueError):
            E4Period(p161_has_spatial_projection=["invalid"])  # type: ignore[list-item]


# ******************************************************************************************************************* #


class TestE4PeriodComplete:
    """Complete E4 Period test with all properties;

    """

    def test_complete_e4_period(self) -> None:
        """Tests complete E4Period with all properties populated;"""
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

        # Create place for P7 and P161
        place = _create_minimal_place()

        # Create physical thing for P8
        physical_thing = E18PhysicalThing(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Westminster Abbey'),
            ],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=E92SpaceTimeVolume(
                p160_has_temporal_projection=_create_minimal_timespan(),
                p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
            )
        )

        # Create sub-period for P9 (requires E92 fields)
        sub_period = E4Period(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Middle Minoan'),
            ],
            p7_took_place_at=[place],
            p160_has_temporal_projection=time_span,
            p161_has_spatial_projection=[place],
        )

        # Create parent period for P10 (requires E92 fields)
        parent_period = E4Period(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='European Bronze Age'),
            ],
            p7_took_place_at=[place],
            p160_has_temporal_projection=time_span,
            p161_has_spatial_projection=[place],
        )

        # Create the main entity with all properties
        entity = E4Period(
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
            # E4 specific properties
            p7_took_place_at=[place],
            p8_took_place_on_or_within=[physical_thing],
            p9_consists_of=sub_period,
            p10_falls_within=[parent_period],
            p132_spatiotemporally_overlaps=[parent_period],
            p160_has_temporal_projection=time_span,
            p161_has_spatial_projection=[place],
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

        # Verify E4 properties;
        assert entity.p7_took_place_at is not None
        assert len(entity.p7_took_place_at) == 1
        assert isinstance(entity.p7_took_place_at[0], E53Place)

        assert entity.p8_took_place_on_or_within is not None
        assert len(entity.p8_took_place_on_or_within) == 1
        assert isinstance(entity.p8_took_place_on_or_within[0], E18PhysicalThing)

        assert entity.p9_consists_of is not None
        assert isinstance(entity.p9_consists_of, E4Period)

        assert entity.p10_falls_within is not None
        assert len(entity.p10_falls_within) == 1
        assert isinstance(entity.p10_falls_within[0], E4Period)

        assert entity.p132_spatiotemporally_overlaps is not None
        assert len(entity.p132_spatiotemporally_overlaps) == 1
        assert isinstance(entity.p132_spatiotemporally_overlaps[0], E4Period)

        assert entity.p160_has_temporal_projection is not None
        assert isinstance(entity.p160_has_temporal_projection, E52TimeSpan)

        assert entity.p161_has_spatial_projection is not None
        assert len(entity.p161_has_spatial_projection) == 1
        assert isinstance(entity.p161_has_spatial_projection[0], E53Place)

    # ------------------------- #

    def test_complete_e4_serialization(self) -> None:
        """Tests complete E4Period serialization to JSON;"""
        time_span = E52TimeSpan(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='3300-1200 BCE'),
            ],
        )
        place = E53Place(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Mesopotamia'),
            ],
            p157_is_at_rest_relative_to=[E18PhysicalThing(
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

        entity = E4Period(
            p1_is_identified_by=[
                E41Appellation(p190_has_symbolic_content='Bronze Age'),
            ],
            p4_has_timespan=time_span,
            p7_took_place_at=[place],
            p160_has_temporal_projection=time_span,
            p161_has_spatial_projection=[place],
        )
        # Test model_dump;
        dump = entity.model_dump()
        assert 'p1_is_identified_by' in dump
        assert 'p4_has_timespan' in dump
        assert 'p7_took_place_at' in dump
        assert 'p160_has_temporal_projection' in dump
        assert 'p161_has_spatial_projection' in dump
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
        assert 'Mesopotamia' in json_str

    # ------------------------- #

    def test_e4_crm_code_attribute(self) -> None:
        """Checks that E4Period has crm_code attribute;"""
        assert hasattr(E4Period, 'crm_code')
        assert E4Period.crm_code == 'E4'

    # ------------------------- #

    def test_e4_crm_label_attribute(self) -> None:
        """Checks that E4Period has crm_label attribute;"""
        assert hasattr(E4Period, 'crm_label')
        assert E4Period.crm_label == 'E4 Period'
