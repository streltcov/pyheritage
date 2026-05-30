# -*- coding: utf-8 -*-

"""Tests for CRMsci material hierarchy entities: S9, S10, S11-S14, S15;

"""

# pylint: disable=E0401,C0116,W0612


from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmsci.helpers import make_dimension, make_material, make_place, make_sample

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation, E54Dimension, E55Type, E70Thing
from pyheritage.cidoc.crmsci.entities import (
    S9PropertyType,
    S10MaterialSubstantial,
    S11AmountOfMatter,
    S12AmountOfFluid,
    S13Sample,
    S14FluidBody,
    S15ObservableEntity,
)
from pyheritage.cidoc.crmsci.properties import O6IsFormerOrCurrentPartOf, O12HasDimension, O15Occupied, O25Contains


class TestS9PropertyType:
    """S9 Property Type entity tests;

    S9 extends E55 Type — no additional CRMsci-specific properties;

    """

    def test_crm_code(self) -> None:
        """Verify S9 CRM code is 'S9';"""
        assert S9PropertyType.crm_code == 'S9'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S9 CRM label is 'S9 Property Type';"""
        assert S9PropertyType.crm_label == 'S9 Property Type'

    # ------------------------- #

    def test_inherits_from_e55(self) -> None:
        """Verify S9 inherits from E55 Type;"""
        assert issubclass(S9PropertyType, E55Type)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S9 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S9PropertyType, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S9 auto-generates a non-null string id;"""
        entity = S9PropertyType()

        assert hasattr(entity, 'id')
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S9 instance receives a unique id;"""
        entity1 = S9PropertyType()
        entity2 = S9PropertyType()

        assert entity1.id != entity2.id

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S9 can be created with a p1 appellation;"""
        entity = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='velocity')],
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'velocity'

    # ------------------------- #

    def test_model_dump_includes_id(self) -> None:
        """Verify model_dump includes id field;"""
        entity = S9PropertyType()
        dump = entity.model_dump()

        assert 'id' in dump

    # ------------------------- #

    def test_model_dump_by_alias_includes_at_id(self) -> None:
        """Verify model_dump with by_alias includes @id and excludes id;"""
        entity = S9PropertyType()
        dump = entity.model_dump(by_alias=True)

        assert '@id' in dump
        assert 'id' not in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id and appellation;"""
        entity = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='velocity')],
        )
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'velocity' in json_str


# ******************************************************************************************************************* #


class TestS10MaterialSubstantial:
    """S10 Material Substantial entity tests;

    Concrete entity — can be instantiated.
    Has required property O15 occupied (E53 Place).

    """

    def test_crm_code(self) -> None:
        """Verify S10 CRM code is 'S10';"""
        assert S10MaterialSubstantial.crm_code == 'S10'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S10 CRM label is 'S10 Material Substantial';"""
        assert S10MaterialSubstantial.crm_label == 'S10 Material Substantial'

    # ------------------------- #

    def test_inherits_from_e70_thing(self) -> None:
        """Verify S10 inherits from E70 Thing;"""
        assert issubclass(S10MaterialSubstantial, E70Thing)

    # ------------------------- #

    def test_inherits_from_s15_observable_entity(self) -> None:
        """Verify S10 inherits from S15 Observable Entity;"""
        assert issubclass(S10MaterialSubstantial, S15ObservableEntity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S10 inherits from E1 CRM Entity;"""
        assert issubclass(S10MaterialSubstantial, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o15_occupied(self) -> None:
        """Verify O15Occupied property mixin is present in S10 MRO;"""
        assert O15Occupied in S10MaterialSubstantial.__mro__

    # ------------------------- #

    def test_mro_includes_o25_contains(self) -> None:
        """Verify O25Contains property mixin is present in S10 MRO;"""
        assert O25Contains in S10MaterialSubstantial.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S10 auto-generates a non-null string id;"""
        entity = make_material()

        assert entity.id is not None

    # ------------------------- #

    def test_o15_occupied_field_exists(self) -> None:
        """Verify o15_occupied field is present and populated;"""
        entity = make_material()

        assert hasattr(entity, 'o15_occupied')

    # ------------------------- #

    def test_o15_occupied_is_required(self) -> None:
        """Verify S10 raises ValidationError without o15_occupied;"""
        with pytest.raises(ValidationError):
            S10MaterialSubstantial()

    # ------------------------- #

    def test_o15_occupied_accepts_place(self) -> None:
        """Verify o15_occupied accepts an E53Place;"""
        place = make_place('Sampling Location')
        entity = S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Groundwater')],
            o15_occupied=place,
        )

        assert entity.o15_occupied is not None
        assert entity.o15_occupied.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Sampling Location'

    # ------------------------- #

    def test_o15_occupied_rejects_invalid_type(self) -> None:
        """Verify o15_occupied raises ValidationError for non-place values;"""
        with pytest.raises(ValidationError):
            S10MaterialSubstantial(
                o15_occupied='invalid',  # type: ignore[arg-type]
            )

    # ------------------------- #

    def test_o12_has_dimension_field_exists(self) -> None:
        """Verify o12_has_dimension field is present and None by default;"""
        entity = make_material()

        assert hasattr(entity, 'o12_has_dimension')
        assert entity.o12_has_dimension is None

    # ------------------------- #

    def test_o12_has_dimension_accepts_dimension(self) -> None:
        """Verify o12_has_dimension accepts a list of E54Dimension;"""
        dim = make_dimension('Length', value=12.5, unit_label='cm')
        entity = S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test')],
            o15_occupied=make_place('Test Location'),
            o12_has_dimension=[dim],
        )

        assert entity.o12_has_dimension is not None
        assert isinstance(entity.o12_has_dimension[0], E54Dimension)

    # ------------------------- #

    def test_o12_rejects_invalid_type(self) -> None:
        """Verify o12_has_dimension raises ValueError for non-dimension values;"""
        with pytest.raises(ValueError):
            S10MaterialSubstantial(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test')],
                o15_occupied=make_place('Test Location'),
                o12_has_dimension=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, o15_occupied and p1_is_identified_by fields;"""
        entity = make_material('Groundwater')
        dump = entity.model_dump()

        assert 'id' in dump
        assert 'o15_occupied' in dump
        assert 'p1_is_identified_by' in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id and o15_occupied fields;"""
        entity = make_material('Groundwater')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Groundwater' in json_str
        assert 'o15_occupied' in json_str


# ******************************************************************************************************************* #


class TestS11AmountOfMatter:
    """S11 Amount of Matter entity tests;

    Abstract — cannot be instantiated directly;
    Tested through its concrete subclasses S12, S13;

    """

    def test_crm_code(self) -> None:
        """Verify S11 CRM code is 'S11';"""
        assert S11AmountOfMatter.crm_code == 'S11'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S11 CRM label is 'S11 Amount of Matter';"""
        assert S11AmountOfMatter.crm_label == 'S11 Amount of Matter'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S11 is abstract and cannot be instantiated;"""
        assert ABC in S11AmountOfMatter.__mro__

    # ------------------------- #

    def test_inherits_from_s10(self) -> None:
        """Verify S11 inherits from S10 Material Substantial;"""
        assert issubclass(S11AmountOfMatter, S10MaterialSubstantial)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S11 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S11AmountOfMatter, E1CRMEntity)


# ******************************************************************************************************************* #


class TestS13Sample:
    """S13 Sample entity tests;

    Concrete entity. Subclass of S11 Amount of Matter - no additional CRMsci-specific properties;

    """

    def test_crm_code(self) -> None:
        """Verify S13 CRM code is 'S13';"""
        assert S13Sample.crm_code == 'S13'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S13 CRM label is 'S13 Sample';"""
        assert S13Sample.crm_label == 'S13 Sample'

    # ------------------------- #

    def test_inherits_from_s11(self) -> None:
        """Verify S13 inherits from S11 Amount of Matter;"""
        assert issubclass(S13Sample, S11AmountOfMatter)

    # ------------------------- #

    def test_inherits_from_s10(self) -> None:
        """Verify S13 inherits from S10 Material Substantial (through chain);"""
        assert issubclass(S13Sample, S10MaterialSubstantial)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S13 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S13Sample, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S13 auto-generates a non-null string id;"""
        entity = make_sample()

        assert entity.id is not None

    # ------------------------- #

    def test_has_o15_occupied_from_s10(self) -> None:
        """Verify S13 inherits o15_occupied from S10;"""
        entity = make_sample()

        assert hasattr(entity, 'o15_occupied')
        assert entity.o15_occupied is not None

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S13 can be created with a p1 appellation;"""
        entity = make_sample('Water Sample')

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Water Sample'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, o15_occupied and p1_is_identified_by;"""
        entity = make_sample('Soil Sample')
        dump = entity.model_dump()

        assert 'id' in dump
        assert 'o15_occupied' in dump
        assert 'p1_is_identified_by' in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id and appellation;"""
        entity = make_sample('Soil Sample')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Soil Sample' in json_str


# ******************************************************************************************************************* #


class TestS14FluidBody:
    """S14 Fluid Body entity tests;

    Abstract — cannot be instantiated directly;
    Tested through its concrete subclass S12;

    """

    def test_crm_code(self) -> None:
        """Verify S14 CRM code is 'S14';"""
        assert S14FluidBody.crm_code == 'S14'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S14 CRM label is 'S14 Fluid Body';"""
        assert S14FluidBody.crm_label == 'S14 Fluid Body'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S14 is abstract and cannot be instantiated;"""
        assert ABC in S14FluidBody.__mro__

    # ------------------------- #

    def test_inherits_from_s10(self) -> None:
        """Verify S14 inherits from S10 Material Substantial;"""
        assert issubclass(S14FluidBody, S10MaterialSubstantial)


# ******************************************************************************************************************* #


class TestS12AmountOfFluid:
    """S12 Amount of Fluid entity tests;

    Concrete entity. Multiple inheritance from S11 + S14;
    Has optional property O6 is former or current part of;

    """

    def test_crm_code(self) -> None:
        """Verify S12 CRM code is 'S12';"""
        assert S12AmountOfFluid.crm_code == 'S12'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S12 CRM label is 'S12 Amount of Fluid';"""
        assert S12AmountOfFluid.crm_label == 'S12 Amount of Fluid'

    # ------------------------- #

    def test_inherits_from_s11(self) -> None:
        """Verify S12 inherits from S11 Amount of Matter;"""
        assert issubclass(S12AmountOfFluid, S11AmountOfMatter)

    # ------------------------- #

    def test_inherits_from_s14(self) -> None:
        """Verify S12 inherits from S14 Fluid Body;"""
        assert issubclass(S12AmountOfFluid, S14FluidBody)

    # ------------------------- #

    def test_inherits_from_s10(self) -> None:
        """Verify S12 inherits from S10 Material Substantial (through chain);"""
        assert issubclass(S12AmountOfFluid, S10MaterialSubstantial)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S12 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S12AmountOfFluid, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o6(self) -> None:
        """Verify O6IsFormerOrCurrentPartOf property mixin is present in S12 MRO;"""
        assert O6IsFormerOrCurrentPartOf in S12AmountOfFluid.__mro__

    # ------------------------- #

    def test_mro_includes_o15(self) -> None:
        """Verify O15Occupied property mixin is present in S12 MRO;"""
        assert O15Occupied in S12AmountOfFluid.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S12 auto-generates a non-null string id;"""
        place = make_place()
        entity = S12AmountOfFluid(o15_occupied=place)

        assert entity.id is not None

    # ------------------------- #

    def test_o6_field_exists(self) -> None:
        """Verify o6_is_former_or_current_part_of field is present and None by default;"""
        place = make_place()
        entity = S12AmountOfFluid(o15_occupied=place)

        assert hasattr(entity, 'o6_is_former_or_current_part_of')
        assert entity.o6_is_former_or_current_part_of is None

    # ------------------------- #

    def test_o6_accepts_s12(self) -> None:
        """Verify o6_is_former_or_current_part_of accepts a list of S12AmountOfFluid;"""
        place = make_place('Fluid Location')
        other = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Blood Sample')],
            o15_occupied=make_place('Blood Location'),
        )
        entity = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Test Fluid')],
            o15_occupied=place,
            o6_is_former_or_current_part_of=[other],
        )

        assert entity.o6_is_former_or_current_part_of is not None
        assert len(entity.o6_is_former_or_current_part_of) == 1
        assert isinstance(entity.o6_is_former_or_current_part_of[0], S12AmountOfFluid)

    # ------------------------- #

    def test_o6_rejects_invalid_type(self) -> None:
        """Verify o6_is_former_or_current_part_of raises ValidationError for non-fluid values;"""
        place = make_place()
        with pytest.raises(ValidationError):
            S12AmountOfFluid(
                o15_occupied=place,
                o6_is_former_or_current_part_of=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_o15_occupied_is_required(self) -> None:
        """Verify S12 raises ValidationError without o15_occupied;"""
        with pytest.raises(ValidationError):
            S12AmountOfFluid()

    # ------------------------- #

    def test_o15_occupied_accepts_place(self) -> None:
        """Verify o15_occupied accepts an E53Place;"""
        place = make_place('River Location')
        entity = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Rhine Water')],
            o15_occupied=place,
        )

        assert entity.o15_occupied is not None

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, o15_occupied and o6 fields;"""
        place = make_place()
        entity = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Blood Sample')],
            o15_occupied=place,
        )
        dump = entity.model_dump()

        assert 'id' in dump
        assert 'o15_occupied' in dump
        assert 'o6_is_former_or_current_part_of' in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id and appellation;"""
        place = make_place()
        entity = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Blood Sample')],
            o15_occupied=place,
        )
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Blood Sample' in json_str

    # ------------------------- #

    def test_complete_entity(self) -> None:
        """Verify S12 can be created with all optional fields populated;"""
        place = make_place('Lab Location')
        other = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Main Fluid Body')],
            o15_occupied=make_place('Source Location'),
        )
        entity = S12AmountOfFluid(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='J.K. Blood Sample 0019FCF5')],
            p3_has_note=['Sample for cholesterol measurement'],
            o15_occupied=place,
            o6_is_former_or_current_part_of=[other],
        )

        assert entity.crm_code == 'S12'
        assert entity.p1_is_identified_by is not None
        assert len(entity.p1_is_identified_by) == 1
        assert entity.p3_has_note is not None
        assert len(entity.p3_has_note) == 1
        assert entity.p3_has_note[0].value == 'Sample for cholesterol measurement'
        assert entity.o15_occupied is not None
        assert entity.o6_is_former_or_current_part_of is not None
        assert len(entity.o6_is_former_or_current_part_of) == 1

        dump = entity.model_dump(by_alias=True, mode='json')
        assert '@id' in dump
        assert 'o15_occupied' in dump
        assert 'o6_is_former_or_current_part_of' in dump
        assert 'p3_has_note' in dump


# ******************************************************************************************************************* #


class TestS15ObservableEntity:
    """S15 Observable Entity tests;

    Abstract — cannot be instantiated directly;
    Tested through its concrete subclass S10;

    """

    def test_crm_code(self) -> None:
        """Verify S15 CRM code is 'S15';"""
        assert S15ObservableEntity.crm_code == 'S15'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S15 CRM label is 'S15 Observable Entity';"""
        assert S15ObservableEntity.crm_label == 'S15 Observable Entity'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S15 is abstract and cannot be instantiated;"""
        assert ABC in S15ObservableEntity.__mro__

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S15 inherits from E1 CRM Entity;"""
        assert issubclass(S15ObservableEntity, E1CRMEntity)

    # ------------------------- #

    def test_s10_is_subclass(self) -> None:
        """Verify S10MaterialSubstantial is a subclass of S15;"""
        assert issubclass(S10MaterialSubstantial, S15ObservableEntity)

    # ------------------------- #

    def test_mro_includes_o12(self) -> None:
        """Verify O12HasDimension property mixin is present in S15 MRO;"""
        assert O12HasDimension in S15ObservableEntity.__mro__
