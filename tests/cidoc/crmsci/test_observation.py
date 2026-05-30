# -*- coding: utf-8 -*-

"""Tests for CRMsci observation hierarchy entities: S4, S5, S6, S7, S8, S19, S21, S23;

"""


# pylint: disable=E0401,C0116,W0612


from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmsci.helpers import make_material, make_physical_thing, make_place, make_timespan, make_type

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E13AttributeAssignment,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E54Dimension,
    E55Type,
)
from pyheritage.cidoc.crmsci.entities import (
    S4Observation,
    S5InferenceMaking,
    S6DataEvaluation,
    S7SimulationOrPrediction,
    S8CategoricalHypothesisBuilding,
    S9PropertyType,
    S19EncounterEvent,
    S21Measurement,
    S23PositionDetermination,
)
from pyheritage.cidoc.crmsci.properties import (
    O8Observed,
    O9ObservedPropertyType,
    O10AssignedDimension,
    O11Described,
    O16ObservedValue,
    O19EncounteredObject,
    O21EncounteredAt,
    O24Measured,
    O30DeterminedPosition,
    O31HasValidityTimeSpan,
    O32DeterminedPositionOf,
)


def _event_places() -> list[E53Place]:
    return [make_place('Event Place')]


def _event_time() -> E52TimeSpan:
    return make_timespan('Event Time')


def _spatial_projection() -> list[E53Place]:
    return [make_place('Spatial Projection')]


def _assigned_types() -> list[E55Type]:
    return [make_type('Assigned Type')]


# ******************************************************************************************************************* #


class TestS4Observation:
    """S4 Observation entity tests;

    S4 is ABC — no direct instantiation;

    """

    def test_crm_code(self) -> None:
        """Verify S4 CRM code is 'S4';"""
        assert S4Observation.crm_code == 'S4'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S4 CRM label is 'S4 Observation';"""
        assert S4Observation.crm_label == 'S4 Observation'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S4 is abstract and cannot be instantiated;"""
        assert ABC in S4Observation.__mro__

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S4 inherits from E13 Attribute Assignment;"""
        assert issubclass(S4Observation, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S4 inherits from E1 CRM Entity;"""
        assert issubclass(S4Observation, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o8_observed(self) -> None:
        """Verify O8Observed property mixin is present in S4 MRO;"""
        assert O8Observed in S4Observation.__mro__

    # ------------------------- #

    def test_mro_includes_o9_observed_property_type(self) -> None:
        """Verify O9ObservedPropertyType property mixin is present in S4 MRO;"""
        assert O9ObservedPropertyType in S4Observation.__mro__

    # ------------------------- #

    def test_mro_includes_o16_observed_value(self) -> None:
        """Verify O16ObservedValue property mixin is present in S4 MRO;"""
        assert O16ObservedValue in S4Observation.__mro__


# ******************************************************************************************************************* #


class TestS5InferenceMaking:
    """S5 Inference Making entity tests;

    S5 is ABC — no direct instantiation;

    """

    def test_crm_code(self) -> None:
        """Verify S5 CRM code is 'S5';"""
        assert S5InferenceMaking.crm_code == 'S5'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S5 CRM label is 'S5 Inference Making';"""
        assert S5InferenceMaking.crm_label == 'S5 Inference Making'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S5 is abstract and cannot be instantiated;"""
        assert ABC in S5InferenceMaking.__mro__

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S5 inherits from E13 Attribute Assignment;"""
        assert issubclass(S5InferenceMaking, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S5 inherits from E1 CRM Entity;"""
        assert issubclass(S5InferenceMaking, E1CRMEntity)

    # ------------------------- #

    def test_s4_is_subclass_of_s5(self) -> None:
        """Verify S4 Observation is NOT subclass of S5 — but S5 is NOT subclass of S4 either;"""
        assert not issubclass(S5InferenceMaking, S4Observation)

    # ------------------------- #

    def test_s6_is_subclass(self) -> None:
        """Verify S6 Data Evaluation is a subclass of S5;"""
        assert issubclass(S6DataEvaluation, S5InferenceMaking)

    # ------------------------- #

    def test_s7_is_subclass(self) -> None:
        """Verify S7 Simulation or Prediction is a subclass of S5;"""
        assert issubclass(S7SimulationOrPrediction, S5InferenceMaking)

    # ------------------------- #

    def test_s8_is_subclass(self) -> None:
        """Verify S8 Categorical Hypothesis Building is a subclass of S5;"""
        assert issubclass(S8CategoricalHypothesisBuilding, S5InferenceMaking)


# ******************************************************************************************************************* #


class TestS21Measurement:
    """S21 Measurement entity tests;

    S21 is ABC — no direct instantiation.

    """

    def test_crm_code(self) -> None:
        """Verify S21 CRM code is 'S21';"""
        assert S21Measurement.crm_code == 'S21'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S21 CRM label is 'S21 Measurement';"""
        assert S21Measurement.crm_label == 'S21 Measurement'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S21 is abstract and cannot be instantiated;"""
        assert ABC in S21Measurement.__mro__

    # ------------------------- #

    def test_inherits_from_s4(self) -> None:
        """Verify S21 inherits from S4 Observation;"""
        assert issubclass(S21Measurement, S4Observation)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S21 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S21Measurement, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S21 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S21Measurement, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o8(self) -> None:
        """Verify O8Observed property mixin is present in S21 MRO;"""
        assert O8Observed in S21Measurement.__mro__

    # ------------------------- #

    def test_mro_includes_o9(self) -> None:
        """Verify O9ObservedPropertyType property mixin is present in S21 MRO;"""
        assert O9ObservedPropertyType in S21Measurement.__mro__

    # ------------------------- #

    def test_mro_includes_o16(self) -> None:
        """Verify O16ObservedValue property mixin is present in S21 MRO;"""
        assert O16ObservedValue in S21Measurement.__mro__

    # ------------------------- #

    def test_mro_includes_o24(self) -> None:
        """Verify O24Measured property mixin is present in S21 MRO;"""
        assert O24Measured in S21Measurement.__mro__


# ******************************************************************************************************************* #


def _make_minimal_s6() -> S6DataEvaluation:
    return S6DataEvaluation(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
        o10_assigned_dimension=[E54Dimension(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Computed Dimension')],
        )],
        o11_described=[make_material('Described Entity')],
    )


class TestS6DataEvaluation:
    """S6 Data Evaluation entity tests;

    S6 is concrete — extends S5 Inference Making.
    Has O10 assigned dimension and O11 described.

    """

    def test_crm_code(self) -> None:
        """Verify S6 CRM code is 'S6';"""
        assert S6DataEvaluation.crm_code == 'S6'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S6 CRM label is 'S6 Data Evaluation';"""
        assert S6DataEvaluation.crm_label == 'S6 Data Evaluation'

    # ------------------------- #

    def test_inherits_from_s5(self) -> None:
        """Verify S6 inherits from S5 Inference Making;"""
        assert issubclass(S6DataEvaluation, S5InferenceMaking)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S6 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S6DataEvaluation, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S6 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S6DataEvaluation, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o10_assigned_dimension(self) -> None:
        """Verify O10AssignedDimension property mixin is present in S6 MRO;"""
        assert O10AssignedDimension in S6DataEvaluation.__mro__

    # ------------------------- #

    def test_mro_includes_o11_described(self) -> None:
        """Verify O11Described property mixin is present in S6 MRO;"""
        assert O11Described in S6DataEvaluation.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S6 auto-generates a non-null string id;"""
        entity = _make_minimal_s6()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S6 instance receives a unique id;"""
        a = _make_minimal_s6()
        b = _make_minimal_s6()

        assert a.id != b.id

    # ------------------------- #

    def test_o10_assigned_dimension_field_exists(self) -> None:
        """Verify o10_assigned_dimension field is present;"""
        entity = _make_minimal_s6()

        assert hasattr(entity, 'o10_assigned_dimension')

    # ------------------------- #

    def test_o10_assigned_dimension_accepts_dimension(self) -> None:
        """Verify o10_assigned_dimension accepts a list of E54Dimension;"""
        dim = E54Dimension(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Dimension')],
        )
        entity = S6DataEvaluation(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o10_assigned_dimension=[dim],
            o11_described=[make_material('Described')],
        )

        assert entity.o10_assigned_dimension is not None
        assert entity.o10_assigned_dimension[0] is dim

    # ------------------------- #

    def test_o10_assigned_dimension_rejects_invalid_type(self) -> None:
        """Verify o10_assigned_dimension raises ValidationError for non-dimension values;"""
        with pytest.raises(ValidationError):
            S6DataEvaluation(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o10_assigned_dimension=['invalid'],  # type: ignore[list-item]
                o11_described=[make_material('Described')],
            )

    # ------------------------- #

    def test_o11_described_field_exists(self) -> None:
        """Verify o11_described field is present;"""
        entity = _make_minimal_s6()

        assert hasattr(entity, 'o11_described')

    # ------------------------- #

    def test_o11_described_accepts_observable_entity(self) -> None:
        """Verify o11_described accepts a list of S15ObservableEntity;"""
        described = make_material('Described Entity')
        dim = E54Dimension(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Dimension')],
        )
        entity = S6DataEvaluation(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o10_assigned_dimension=[dim],
            o11_described=[described],
        )

        assert entity.o11_described is not None
        assert entity.o11_described[0] is described

    # ------------------------- #

    def test_o11_described_rejects_invalid_type(self) -> None:
        """Verify o11_described raises ValidationError for non-observable values;"""
        with pytest.raises(ValidationError):
            S6DataEvaluation(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o10_assigned_dimension=[E54Dimension(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='D')],
                )],
                o11_described=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes o10 and o11 fields;"""
        entity = _make_minimal_s6()
        data = entity.model_dump()

        assert 'o10_assigned_dimension' in data
        assert 'o11_described' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains property fields;"""
        entity = _make_minimal_s6()
        json_str = entity.model_dump_json()

        assert '"o10_assigned_dimension"' in json_str
        assert '"o11_described"' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S6 can be created with a p1 appellation;"""
        entity = S6DataEvaluation(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Evaluation Event')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o10_assigned_dimension=[E54Dimension(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Dim')],
            )],
            o11_described=[make_material('Described')],
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Evaluation Event'

    # ------------------------- #

    def test_complete_entity(self) -> None:
        """Verify S6 can be created with all optional fields populated;"""
        described = make_material('Described Entity')
        dim = E54Dimension(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Computed Value')],
            p90_has_value=42.0,
        )
        entity = S6DataEvaluation(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Complete Eval')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o10_assigned_dimension=[dim],
            o11_described=[described],
        )

        assert entity.o10_assigned_dimension is not None
        assert entity.o11_described is not None
        assert len(entity.o10_assigned_dimension) == 1
        assert entity.o10_assigned_dimension[0].p90_has_value.value == 42.0


# ******************************************************************************************************************* #


def _make_minimal_s7() -> S7SimulationOrPrediction:
    return S7SimulationOrPrediction(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
    )


class TestS7SimulationOrPrediction:
    """S7 Simulation or Prediction entity tests;

    S7 is concrete — extends S5 Inference Making.
    No additional CRMsci-specific properties.

    """

    def test_crm_code(self) -> None:
        """Verify S7 CRM code is 'S7';"""
        assert S7SimulationOrPrediction.crm_code == 'S7'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S7 CRM label is 'S7 Simulation or Prediction';"""
        assert S7SimulationOrPrediction.crm_label == 'S7 Simulation or Prediction'

    # ------------------------- #

    def test_inherits_from_s5(self) -> None:
        """Verify S7 inherits from S5 Inference Making;"""
        assert issubclass(S7SimulationOrPrediction, S5InferenceMaking)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S7 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S7SimulationOrPrediction, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S7 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S7SimulationOrPrediction, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S7 auto-generates a non-null string id;"""
        entity = _make_minimal_s7()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S7 instance receives a unique id;"""
        a = _make_minimal_s7()
        b = _make_minimal_s7()

        assert a.id != b.id

    # ------------------------- #

    def test_model_dump_includes_id(self) -> None:
        """Verify model_dump includes id field;"""
        entity = _make_minimal_s7()
        dump = entity.model_dump()

        assert 'id' in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id;"""
        entity = _make_minimal_s7()
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S7 can be created with a p1 appellation;"""
        entity = S7SimulationOrPrediction(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Simulation Event')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Simulation Event'


# ******************************************************************************************************************* #


def _make_minimal_s8() -> S8CategoricalHypothesisBuilding:
    return S8CategoricalHypothesisBuilding(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
    )


class TestS8CategoricalHypothesisBuilding:
    """S8 Categorical Hypothesis Building entity tests;

    S8 is concrete — extends S5 Inference Making.
    No additional CRMsci-specific properties.

    """

    def test_crm_code(self) -> None:
        """Verify S8 CRM code is 'S8';"""
        assert S8CategoricalHypothesisBuilding.crm_code == 'S8'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S8 CRM label is 'S8 Categorical Hypothesis Building';"""
        assert S8CategoricalHypothesisBuilding.crm_label == 'S8 Categorical Hypothesis Building'

    # ------------------------- #

    def test_inherits_from_s5(self) -> None:
        """Verify S8 inherits from S5 Inference Making;"""
        assert issubclass(S8CategoricalHypothesisBuilding, S5InferenceMaking)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S8 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S8CategoricalHypothesisBuilding, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S8 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S8CategoricalHypothesisBuilding, E1CRMEntity)

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S8 auto-generates a non-null string id;"""
        entity = _make_minimal_s8()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S8 instance receives a unique id;"""
        a = _make_minimal_s8()
        b = _make_minimal_s8()

        assert a.id != b.id

    # ------------------------- #

    def test_model_dump_includes_id(self) -> None:
        """Verify model_dump includes id field;"""
        entity = _make_minimal_s8()
        dump = entity.model_dump()

        assert 'id' in dump

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains @id;"""
        entity = _make_minimal_s8()
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S8 can be created with a p1 appellation;"""
        entity = S8CategoricalHypothesisBuilding(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Hypothesis Event')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Hypothesis Event'


# ******************************************************************************************************************* #


def _make_minimal_s19() -> S19EncounterEvent:
    return S19EncounterEvent(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
        o8_observed=make_material('Observed Entity'),
        o9_observed_property_type=S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Observed Property')],
        ),
        o16_observed_value=E41Appellation(p190_has_symbolic_content='value'),
        o19_encountered_object=[make_physical_thing('Encountered Object')],
        o21_encountered_at=make_place('Encounter Place'),
    )


class TestS19EncounterEvent:
    """S19 Encounter Event entity tests;

    S19 is concrete — extends S4 Observation.
    Has O19 encountered object and O21 encountered at.

    """

    def test_crm_code(self) -> None:
        """Verify S19 CRM code is 'S19';"""
        assert S19EncounterEvent.crm_code == 'S19'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S19 CRM label is 'S19 Encounter Event';"""
        assert S19EncounterEvent.crm_label == 'S19 Encounter Event'

    # ------------------------- #

    def test_inherits_from_s4(self) -> None:
        """Verify S19 inherits from S4 Observation;"""
        assert issubclass(S19EncounterEvent, S4Observation)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S19 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S19EncounterEvent, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S19 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S19EncounterEvent, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o19_encountered_object(self) -> None:
        """Verify O19EncounteredObject property mixin is present in S19 MRO;"""
        assert O19EncounteredObject in S19EncounterEvent.__mro__

    # ------------------------- #

    def test_mro_includes_o21_encountered_at(self) -> None:
        """Verify O21EncounteredAt property mixin is present in S19 MRO;"""
        assert O21EncounteredAt in S19EncounterEvent.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S19 auto-generates a non-null string id;"""
        entity = _make_minimal_s19()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S19 instance receives a unique id;"""
        a = _make_minimal_s19()
        b = _make_minimal_s19()

        assert a.id != b.id

    # ------------------------- #

    def test_o19_encountered_object_field_exists(self) -> None:
        """Verify o19_encountered_object field is present;"""
        entity = _make_minimal_s19()

        assert hasattr(entity, 'o19_encountered_object')

    # ------------------------- #

    def test_o19_encountered_object_accepts_physical_thing(self) -> None:
        """Verify o19_encountered_object accepts a list of E18PhysicalThing;"""
        obj = make_physical_thing('Encountered Object')
        entity = S19EncounterEvent(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o19_encountered_object=[obj],
            o21_encountered_at=make_place('Encounter Place'),
        )

        assert entity.o19_encountered_object is not None
        assert entity.o19_encountered_object[0] is obj

    # ------------------------- #

    def test_o19_encountered_object_rejects_invalid_type(self) -> None:
        """Verify o19_encountered_object raises ValidationError for non-thing values;"""
        with pytest.raises(ValidationError):
            S19EncounterEvent(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o8_observed=make_material('Observed'),
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
                o19_encountered_object=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_o21_encountered_at_field_exists(self) -> None:
        """Verify o21_encountered_at field is present;"""
        entity = _make_minimal_s19()

        assert hasattr(entity, 'o21_encountered_at')

    # ------------------------- #

    def test_o21_encountered_at_accepts_place(self) -> None:
        """Verify o21_encountered_at accepts an E53Place;"""
        place = make_place('Encounter Place')
        entity = S19EncounterEvent(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o19_encountered_object=[make_physical_thing('Object')],
            o21_encountered_at=place,
        )

        assert entity.o21_encountered_at is place

    # ------------------------- #

    def test_o21_encountered_at_rejects_invalid_type(self) -> None:
        """Verify o21_encountered_at raises ValidationError for non-place values;"""
        with pytest.raises(ValidationError):
            S19EncounterEvent(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o8_observed=make_material('Observed'),
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
                o19_encountered_object=[make_physical_thing('Object')],
                o21_encountered_at='invalid',  # type: ignore[arg-type]
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes property fields;"""
        entity = _make_minimal_s19()
        data = entity.model_dump()

        assert 'o8_observed' in data
        assert 'o9_observed_property_type' in data
        assert 'o16_observed_value' in data
        assert 'o19_encountered_object' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains property fields;"""
        entity = _make_minimal_s19()
        json_str = entity.model_dump_json()

        assert '"o19_encountered_object"' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S19 can be created with a p1 appellation;"""
        entity = S19EncounterEvent(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Encounter Event')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o19_encountered_object=[make_physical_thing('Object')],
            o21_encountered_at=make_place('Encounter Place'),
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Encounter Event'

    # ------------------------- #

    def test_complete_entity(self) -> None:
        """Verify S19 can be created with all optional fields populated;"""
        obj = make_physical_thing('Fossil')
        entity = S19EncounterEvent(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Fossil Encounter')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed Material'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Species')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='Homo neanderthalensis'),
            o19_encountered_object=[obj],
            o21_encountered_at=make_place('Encounter Place'),
        )

        assert entity.o19_encountered_object is not None
        assert entity.o19_encountered_object[0] is obj

    # ------------------------- #

    def test_o8_observed_field_exists(self) -> None:
        """Verify o8_observed field is present;"""
        entity = _make_minimal_s19()

        assert hasattr(entity, 'o8_observed')

    # ------------------------- #

    def test_o8_observed_accepts_observable_entity(self) -> None:
        """Verify o8_observed accepts an S15ObservableEntity;"""
        observed = make_material('Observed Material')
        entity = S19EncounterEvent(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=observed,
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o19_encountered_object=[make_physical_thing('Object')],
            o21_encountered_at=make_place('Encounter Place'),
        )

        assert entity.o8_observed is observed

    # ------------------------- #

    def test_o9_observed_property_type_field_exists(self) -> None:
        """Verify o9_observed_property_type field is present;"""
        entity = _make_minimal_s19()

        assert hasattr(entity, 'o9_observed_property_type')

    # ------------------------- #

    def test_o16_observed_value_field_exists(self) -> None:
        """Verify o16_observed_value field is present;"""
        entity = _make_minimal_s19()

        assert hasattr(entity, 'o16_observed_value')


# ******************************************************************************************************************* #


def _make_minimal_s23() -> S23PositionDetermination:
    return S23PositionDetermination(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
        o8_observed=make_material('Observed Entity'),
        o9_observed_property_type=S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Position Property')],
        ),
        o16_observed_value=E41Appellation(p190_has_symbolic_content='position value'),
        o31_has_validity_time_span=_event_time(),
        o32_determined_position_of=make_material('Observed Entity'),
    )


class TestS23PositionDetermination:
    """S23 Position Determination entity tests;

    S23 is concrete — extends S4 Observation.
    Has O30 determined position, O31 has validity time-span,
    and O32 determined position of.

    """

    def test_crm_code(self) -> None:
        """Verify S23 CRM code is 'S23';"""
        assert S23PositionDetermination.crm_code == 'S23'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S23 CRM label is 'S23 Position Determination';"""
        assert S23PositionDetermination.crm_label == 'S23 Position Determination'

    # ------------------------- #

    def test_inherits_from_s4(self) -> None:
        """Verify S23 inherits from S4 Observation;"""
        assert issubclass(S23PositionDetermination, S4Observation)

    # ------------------------- #

    def test_inherits_from_e13(self) -> None:
        """Verify S23 inherits from E13 Attribute Assignment (through chain);"""
        assert issubclass(S23PositionDetermination, E13AttributeAssignment)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S23 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S23PositionDetermination, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o30_determined_position(self) -> None:
        """Verify O30DeterminedPosition property mixin is present in S23 MRO;"""
        assert O30DeterminedPosition in S23PositionDetermination.__mro__

    # ------------------------- #

    def test_mro_includes_o31_has_validity_time_span(self) -> None:
        """Verify O31HasValidityTimeSpan property mixin is present in S23 MRO;"""
        assert O31HasValidityTimeSpan in S23PositionDetermination.__mro__

    # ------------------------- #

    def test_mro_includes_o32_determined_position_of(self) -> None:
        """Verify O32DeterminedPositionOf property mixin is present in S23 MRO;"""
        assert O32DeterminedPositionOf in S23PositionDetermination.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S23 auto-generates a non-null string id;"""
        entity = _make_minimal_s23()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S23 instance receives a unique id;"""
        a = _make_minimal_s23()
        b = _make_minimal_s23()

        assert a.id != b.id

    # ------------------------- #

    def test_o8_observed_field_exists(self) -> None:
        """Verify o8_observed field is present;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o8_observed')

    # ------------------------- #

    def test_o8_observed_accepts_observable_entity(self) -> None:
        """Verify o8_observed accepts an S15ObservableEntity;"""
        observed = make_material('Observed Material')
        entity = S23PositionDetermination(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=observed,
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o31_has_validity_time_span=_event_time(),
            o32_determined_position_of=observed,
        )

        assert entity.o8_observed is observed

    # ------------------------- #

    def test_o9_observed_property_type_field_exists(self) -> None:
        """Verify o9_observed_property_type field is present;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o9_observed_property_type')

    # ------------------------- #

    def test_o16_observed_value_field_exists(self) -> None:
        """Verify o16_observed_value field is present;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o16_observed_value')

    # ------------------------- #

    def test_o30_determined_position_field_exists(self) -> None:
        """Verify o30_determined_position field is present and None by default;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o30_determined_position')
        assert entity.o30_determined_position is None

    # ------------------------- #

    def test_o30_determined_position_accepts_space_primitive(self) -> None:
        """Verify o30_determined_position accepts a list of E94SpacePrimitive;"""
        from pyheritage.cidoc.core.entities import E94SpacePrimitive
        sp = E94SpacePrimitive(value='POINT(1 2 3)')
        entity = S23PositionDetermination(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o31_has_validity_time_span=_event_time(),
            o32_determined_position_of=make_material('Observed'),
            o30_determined_position=[sp],
        )

        assert entity.o30_determined_position is not None
        assert entity.o30_determined_position[0] is sp

    # ------------------------- #

    def test_o31_has_validity_time_span_field_exists(self) -> None:
        """Verify o31_has_validity_time_span field is present;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o31_has_validity_time_span')

    # ------------------------- #

    def test_o31_has_validity_time_span_accepts_timespan(self) -> None:
        """Verify o31_has_validity_time_span accepts an E52TimeSpan;"""
        ts = make_timespan('Validity')
        entity = S23PositionDetermination(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o31_has_validity_time_span=ts,
            o32_determined_position_of=make_material('Observed'),
        )

        assert entity.o31_has_validity_time_span is ts

    # ------------------------- #

    def test_o32_determined_position_of_field_exists(self) -> None:
        """Verify o32_determined_position_of field is present;"""
        entity = _make_minimal_s23()

        assert hasattr(entity, 'o32_determined_position_of')

    # ------------------------- #

    def test_o32_determined_position_of_accepts_observable(self) -> None:
        """Verify o32_determined_position_of accepts an S15ObservableEntity;"""
        observed = make_material('Observed Target')
        entity = S23PositionDetermination(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=observed,
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o31_has_validity_time_span=_event_time(),
            o32_determined_position_of=observed,
        )

        assert entity.o32_determined_position_of is observed

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes property fields;"""
        entity = _make_minimal_s23()
        data = entity.model_dump()

        assert 'o8_observed' in data
        assert 'o9_observed_property_type' in data
        assert 'o16_observed_value' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains property fields;"""
        entity = _make_minimal_s23()
        json_str = entity.model_dump_json()

        assert '"o8_observed"' in json_str
        assert '"o9_observed_property_type"' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S23 can be created with a p1 appellation;"""
        entity = S23PositionDetermination(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Position Fix')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o8_observed=make_material('Observed'),
            o9_observed_property_type=S9PropertyType(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Prop')],
            ),
            o16_observed_value=E41Appellation(p190_has_symbolic_content='v'),
            o31_has_validity_time_span=_event_time(),
            o32_determined_position_of=make_material('Observed'),
        )
        
        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Position Fix'
