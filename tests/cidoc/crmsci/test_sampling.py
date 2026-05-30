# -*- coding: utf-8 -*-

"""Tests for CRMsci sampling hierarchy entities: S1, S2, S3, S24;

"""


# pylint: disable=E0401,C0116,W0612


from abc import ABC

import pytest
from pydantic import ValidationError
from tests.cidoc.crmsci.helpers import make_material, make_place, make_sample, make_timespan, make_type

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E7Activity,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E54Dimension,
    E55Type,
)
from pyheritage.cidoc.crmsci.entities import (
    S1MatterRemoval,
    S2SampleTaking,
    S3MeasurementBySampling,
    S9PropertyType,
    S13Sample,
    S24SampleSplitting,
)
from pyheritage.cidoc.crmsci.properties import (
    O1Diminished,
    O2Removed,
    O3SampledFrom,
    O4SampledAt,
    O5Removed,
    O8Observed,
    O9ObservedPropertyType,
    O16ObservedValue,
    O20SampledFromTypeOfPart,
    O27Split,
    O29RemovedSubSample,
)


def _event_places() -> list[E53Place]:
    return [make_place('Event Place')]


def _event_time() -> E52TimeSpan:
    return make_timespan('Event Time')


def _spatial_projection() -> list[E53Place]:
    return [make_place('Spatial Projection')]


def _assigned_types() -> list[E55Type]:
    return [make_type('Assigned Type')]


def _make_minimal_s3() -> S3MeasurementBySampling:
    return S3MeasurementBySampling(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        p177_assigned_property_type=_assigned_types(),
        o3_sampled_from=[make_material('Source Material')],
        o4_sampled_at=make_place('Sampling Location'),
        o5_removed=[S13Sample(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
            o15_occupied=make_place('Sample Location'),
        )],
        o8_observed=make_material('Observed'),
        o9_observed_property_type=S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        ),
        o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
        o24_measured=make_material('Observed'),
    )


def _make_minimal_s24() -> S24SampleSplitting:
    return S24SampleSplitting(
        p7_took_place_at=_event_places(),
        p160_has_temporal_projection=_event_time(),
        p161_has_spatial_projection=_spatial_projection(),
        o3_sampled_from=[make_material('Source Material')],
        o4_sampled_at=make_place('Sampling Location'),
        o5_removed=[make_sample('Sample')],
    )


# ******************************************************************************************************************* #


class TestS1MatterRemoval:
    """S1 Matter Removal entity tests;

    S1 is ABC — no direct instantiation.

    """

    def test_crm_code(self) -> None:
        """Verify S1 CRM code is 'S1';"""
        assert S1MatterRemoval.crm_code == 'S1'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S1 CRM label is 'S1 Matter Removal';"""
        assert S1MatterRemoval.crm_label == 'S1 Matter Removal'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S1 is abstract and cannot be instantiated;"""
        assert ABC in S1MatterRemoval.__mro__

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Verify S1 inherits from E7 Activity;"""
        assert issubclass(S1MatterRemoval, E7Activity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S1 inherits from E1 CRM Entity;"""
        assert issubclass(S1MatterRemoval, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o1_diminished(self) -> None:
        """Verify O1Diminished property mixin is present in S1 MRO;"""
        assert O1Diminished in S1MatterRemoval.__mro__

    # ------------------------- #

    def test_mro_includes_o2_removed(self) -> None:
        """Verify O2Removed property mixin is present in S1 MRO;"""
        assert O2Removed in S1MatterRemoval.__mro__


# ******************************************************************************************************************* #


class TestS2SampleTaking:
    """S2 Sample Taking entity tests;

    S2 is ABC — no direct instantiation.

    """

    def test_crm_code(self) -> None:
        """Verify S2 CRM code is 'S2';"""
        assert S2SampleTaking.crm_code == 'S2'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S2 CRM label is 'S2 Sample Taking';"""
        assert S2SampleTaking.crm_label == 'S2 Sample Taking'

    # ------------------------- #

    def test_is_abstract(self) -> None:
        """Verify S2 is abstract and cannot be instantiated;"""
        assert ABC in S2SampleTaking.__mro__

    # ------------------------- #

    def test_inherits_from_s1(self) -> None:
        """Verify S2 inherits from S1 Matter Removal;"""
        assert issubclass(S2SampleTaking, S1MatterRemoval)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Verify S2 inherits from E7 Activity (through chain);"""
        assert issubclass(S2SampleTaking, E7Activity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S2 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S2SampleTaking, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o3_sampled_from(self) -> None:
        """Verify O3SampledFrom property mixin is present in S2 MRO;"""
        assert O3SampledFrom in S2SampleTaking.__mro__

    # ------------------------- #

    def test_mro_includes_o4_sampled_at(self) -> None:
        """Verify O4SampledAt property mixin is present in S2 MRO;"""
        assert O4SampledAt in S2SampleTaking.__mro__

    # ------------------------- #

    def test_mro_includes_o5_removed(self) -> None:
        """Verify O5Removed property mixin is present in S2 MRO;"""
        assert O5Removed in S2SampleTaking.__mro__

    # ------------------------- #

    def test_mro_includes_o20_sampled_from_type_of_part(self) -> None:
        """Verify O20SampledFromTypeOfPart property mixin is present in S2 MRO;"""
        assert O20SampledFromTypeOfPart in S2SampleTaking.__mro__


# ******************************************************************************************************************* #


class TestS3MeasurementBySampling:
    """S3 Measurement by Sampling entity tests;

    S3 is concrete — inherits from S2 Sample Taking and S21 Measurement;

    """

    def test_crm_code(self) -> None:
        """Verify S3 CRM code is 'S3';"""
        assert S3MeasurementBySampling.crm_code == 'S3'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S3 CRM label is 'S3 Measurement by Sampling';"""
        assert S3MeasurementBySampling.crm_label == 'S3 Measurement by Sampling'

    # ------------------------- #

    def test_inherits_from_s2(self) -> None:
        """Verify S3 inherits from S2 Sample Taking;"""
        assert issubclass(S3MeasurementBySampling, S2SampleTaking)

    # ------------------------- #

    def test_inherits_from_s1(self) -> None:
        """Verify S3 inherits from S1 Matter Removal (through chain);"""
        assert issubclass(S3MeasurementBySampling, S1MatterRemoval)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Verify S3 inherits from E7 Activity (through chain);"""
        assert issubclass(S3MeasurementBySampling, E7Activity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S3 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S3MeasurementBySampling, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o1_diminished(self) -> None:
        """Verify O1Diminished property mixin is present in S3 MRO;"""
        assert O1Diminished in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o3_sampled_from(self) -> None:
        """Verify O3SampledFrom property mixin is present in S3 MRO;"""
        assert O3SampledFrom in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o4_sampled_at(self) -> None:
        """Verify O4SampledAt property mixin is present in S3 MRO;"""
        assert O4SampledAt in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o5_removed(self) -> None:
        """Verify O5Removed property mixin is present in S3 MRO;"""
        assert O5Removed in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o8_observed(self) -> None:
        """Verify O8Observed property mixin is present in S3 MRO;"""
        assert O8Observed in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o9_observed_property_type(self) -> None:
        """Verify O9ObservedPropertyType property mixin is present in S3 MRO;"""
        assert O9ObservedPropertyType in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o16_observed_value(self) -> None:
        """Verify O16ObservedValue property mixin is present in S3 MRO;"""
        assert O16ObservedValue in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_mro_includes_o20_sampled_from_type_of_part(self) -> None:
        """Verify O20SampledFromTypeOfPart property mixin is present in S3 MRO;"""
        assert O20SampledFromTypeOfPart in S3MeasurementBySampling.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S3 auto-generates a non-null string id;"""
        entity = _make_minimal_s3()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S3 instance receives a unique id;"""
        a = _make_minimal_s3()
        b = _make_minimal_s3()

        assert a.id != b.id

    # ------------------------- #

    def test_o3_sampled_from_field_exists(self) -> None:
        """Verify o3_sampled_from field is present and populated;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o3_sampled_from')

    # ------------------------- #

    def test_o3_sampled_from_accepts_material(self) -> None:
        """Verify o3_sampled_from accepts a list of S10MaterialSubstantial;"""
        source = make_material('Source Material')
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[source],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[S13Sample(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                o15_occupied=make_place('Sample Location'),
            )],
            o8_observed=source,
            o9_observed_property_type=s9,
            o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            o24_measured=source,
        )

        assert entity.o3_sampled_from is not None
        assert entity.o3_sampled_from[0] is source

    # ------------------------- #

    def test_o3_sampled_from_rejects_invalid_type(self) -> None:
        """Verify o3_sampled_from raises ValidationError for non-material values;"""
        with pytest.raises(ValidationError):
            S3MeasurementBySampling(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o3_sampled_from=['invalid'],  # type: ignore[list-item]
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=[S13Sample(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                    o15_occupied=make_place('Sample Location'),
                )],
                o8_observed=make_material('Observed'),
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            )

    # ------------------------- #

    def test_o4_sampled_at_field_exists(self) -> None:
        """Verify o4_sampled_at field is present and populated;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o4_sampled_at')

    # ------------------------- #

    def test_o4_sampled_at_accepts_place(self) -> None:
        """Verify o4_sampled_at accepts an E53Place;"""
        place = make_place('Sampling Location')
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=place,
            o5_removed=[S13Sample(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                o15_occupied=make_place('Sample Location'),
            )],
            o8_observed=make_material('Observed'),
            o9_observed_property_type=s9,
            o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            o24_measured=make_material('Observed'),
        )

        assert entity.o4_sampled_at is place

    # ------------------------- #

    def test_o4_sampled_at_rejects_invalid_type(self) -> None:
        """Verify o4_sampled_at raises ValidationError for non-place values;"""
        with pytest.raises(ValidationError):
            S3MeasurementBySampling(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at='invalid',  # type: ignore[arg-type]
                o5_removed=[S13Sample(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                    o15_occupied=make_place('Sample Location'),
                )],
                o8_observed=make_material('Observed'),
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            )

    # ------------------------- #

    def test_o5_removed_field_exists(self) -> None:
        """Verify o5_removed field is present and populated;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o5_removed')

    # ------------------------- #

    def test_o5_removed_accepts_sample(self) -> None:
        """Verify o5_removed accepts a list of S13Sample;"""
        sample = S13Sample(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
            o15_occupied=make_place('Sample Location'),
        )
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[sample],
            o8_observed=make_material('Observed'),
            o9_observed_property_type=s9,
            o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            o24_measured=make_material('Observed'),
        )

        assert entity.o5_removed is not None
        assert entity.o5_removed[0] is sample

    # ------------------------- #

    def test_o5_removed_rejects_invalid_type(self) -> None:
        """Verify o5_removed raises ValidationError for non-sample values;"""
        with pytest.raises(ValidationError):
            S3MeasurementBySampling(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=['invalid'],  # type: ignore[list-item]
                o8_observed=make_material('Observed'),
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            )

    # ------------------------- #

    def test_o8_observed_field_exists(self) -> None:
        """Verify o8_observed field is present and populated;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o8_observed')

    # ------------------------- #

    def test_o8_observed_accepts_observable_entity(self) -> None:
        """Verify o8_observed accepts an S15ObservableEntity;"""
        observed = make_material('Observed Material')
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[S13Sample(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                o15_occupied=make_place('Sample Location'),
            )],
            o8_observed=observed,
            o9_observed_property_type=s9,
            o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            o24_measured=observed,
        )

        assert entity.o8_observed is observed

    # ------------------------- #

    def test_o8_observed_rejects_invalid_type(self) -> None:
        """Verify o8_observed raises ValidationError for non-observable values;"""
        with pytest.raises(ValidationError):
            S3MeasurementBySampling(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                p177_assigned_property_type=_assigned_types(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=[S13Sample(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                    o15_occupied=make_place('Sample Location'),
                )],
                o8_observed='invalid',  # type: ignore[arg-type]
                o9_observed_property_type=S9PropertyType(
                    p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
                ),
                o16_observed_value=E41Appellation(p190_has_symbolic_content='observed value'),
            )

    # ------------------------- #

    def test_o9_observed_property_type_field_exists(self) -> None:
        """Verify o9_observed_property_type field is present;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o9_observed_property_type')

    # ------------------------- #

    def test_o16_observed_value_field_exists(self) -> None:
        """Verify o16_observed_value field is present;"""
        entity = _make_minimal_s3()

        assert hasattr(entity, 'o16_observed_value')

    # ------------------------- #

    def test_o16_observed_value_accepts_appellation(self) -> None:
        """Verify o16_observed_value accepts an E41Appellation as value;"""
        value = E41Appellation(p190_has_symbolic_content='a value')
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[S13Sample(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                o15_occupied=make_place('Sample Location'),
            )],
            o8_observed=make_material('Observed'),
            o9_observed_property_type=s9,
            o16_observed_value=value,
            o24_measured=make_material('Observed'),
        )

        assert entity.o16_observed_value is value

    # ------------------------- #

    def test_o16_observed_value_accepts_dimension(self) -> None:
        """Verify o16_observed_value accepts an E54Dimension as value;"""
        value = E54Dimension(p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='dim')])
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[S13Sample(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
                o15_occupied=make_place('Sample Location'),
            )],
            o8_observed=make_material('Observed'),
            o9_observed_property_type=s9,
            o16_observed_value=value,
            o24_measured=make_material('Observed'),
        )

        assert entity.o16_observed_value is value

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes property fields;"""
        entity = _make_minimal_s3()
        data = entity.model_dump()

        assert 'o3_sampled_from' in data
        assert 'o4_sampled_at' in data
        assert 'o5_removed' in data
        assert 'o8_observed' in data
        assert 'o9_observed_property_type' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains property fields;"""
        entity = _make_minimal_s3()
        json_str = entity.model_dump_json()

        assert '"o3_sampled_from"' in json_str
        assert '"o4_sampled_at"' in json_str
        assert '"o5_removed"' in json_str

    # ------------------------- #

    def test_complete_entity(self) -> None:
        """Verify S3 can be created with all optional fields populated;"""
        source = make_material('Source Material')
        sample = S13Sample(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Sample')],
            o15_occupied=make_place('Sample Location'),
        )
        s9 = S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Property Type')],
        )
        entity = S3MeasurementBySampling(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            p177_assigned_property_type=_assigned_types(),
            o1_diminished=[source],
            o2_removed=[sample],
            o3_sampled_from=[source],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[sample],
            o8_observed=source,
            o9_observed_property_type=s9,
            o16_observed_value=E54Dimension(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Value')],
            ),
            o20_sampled_from_type_of_part=[make_type('Part Type')],
            o24_measured=source,
        )

        assert entity.o1_diminished is not None
        assert entity.o2_removed is not None
        assert entity.o3_sampled_from is not None
        assert entity.o4_sampled_at is not None
        assert entity.o5_removed is not None
        assert entity.o8_observed is not None
        assert entity.o9_observed_property_type is not None
        assert entity.o20_sampled_from_type_of_part is not None


# ******************************************************************************************************************* #


class TestS24SampleSplitting:
    """S24 Sample Splitting entity tests;

    S24 is concrete — inherits from S2 Sample Taking.

    """

    def test_crm_code(self) -> None:
        """Verify S24 CRM code is 'S24';"""
        assert S24SampleSplitting.crm_code == 'S24'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify S24 CRM label is 'S24 Sample Splitting';"""
        assert S24SampleSplitting.crm_label == 'S24 Sample Splitting'

    # ------------------------- #

    def test_inherits_from_s2(self) -> None:
        """Verify S24 inherits from S2 Sample Taking;"""
        assert issubclass(S24SampleSplitting, S2SampleTaking)

    # ------------------------- #

    def test_inherits_from_s1(self) -> None:
        """Verify S24 inherits from S1 Matter Removal (through chain);"""
        assert issubclass(S24SampleSplitting, S1MatterRemoval)

    # ------------------------- #

    def test_inherits_from_e7(self) -> None:
        """Verify S24 inherits from E7 Activity (through chain);"""
        assert issubclass(S24SampleSplitting, E7Activity)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify S24 inherits from E1 CRM Entity (through chain);"""
        assert issubclass(S24SampleSplitting, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_o3_sampled_from(self) -> None:
        """Verify O3SampledFrom property mixin is present in S24 MRO;"""
        assert O3SampledFrom in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_mro_includes_o4_sampled_at(self) -> None:
        """Verify O4SampledAt property mixin is present in S24 MRO;"""
        assert O4SampledAt in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_mro_includes_o5_removed(self) -> None:
        """Verify O5Removed property mixin is present in S24 MRO;"""
        assert O5Removed in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_mro_includes_o20_sampled_from_type_of_part(self) -> None:
        """Verify O20SampledFromTypeOfPart property mixin is present in S24 MRO;"""
        assert O20SampledFromTypeOfPart in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_mro_includes_o27_split(self) -> None:
        """Verify O27Split property mixin is present in S24 MRO;"""
        assert O27Split in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_mro_includes_o29_removed_sub_sample(self) -> None:
        """Verify O29RemovedSubSample property mixin is present in S24 MRO;"""
        assert O29RemovedSubSample in S24SampleSplitting.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify S24 auto-generates a non-null string id;"""
        entity = _make_minimal_s24()

        assert entity.id is not None
        assert isinstance(entity.id, str)

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each S24 instance receives a unique id;"""
        a = _make_minimal_s24()
        b = _make_minimal_s24()

        assert a.id != b.id

    # ------------------------- #

    def test_o3_sampled_from_field_exists(self) -> None:
        """Verify o3_sampled_from field is present;"""
        entity = _make_minimal_s24()

        assert hasattr(entity, 'o3_sampled_from')

    # ------------------------- #

    def test_o3_sampled_from_accepts_material(self) -> None:
        """Verify o3_sampled_from accepts a list of S10MaterialSubstantial;"""
        source = make_material('Source Material')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[source],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[make_sample('Sample')],
        )

        assert entity.o3_sampled_from is not None
        assert entity.o3_sampled_from[0] is source

    # ------------------------- #

    def test_o3_sampled_from_rejects_invalid(self) -> None:
        """Verify o3_sampled_from raises ValidationError for non-material values;"""
        with pytest.raises(ValidationError):
            S24SampleSplitting(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                o3_sampled_from=['invalid'],  # type: ignore[list-item]
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=[make_sample('Sample')],
            )

    # ------------------------- #

    def test_o4_sampled_at_field_exists(self) -> None:
        """Verify o4_sampled_at field is present;"""
        entity = _make_minimal_s24()

        assert hasattr(entity, 'o4_sampled_at')

    # ------------------------- #

    def test_o4_sampled_at_accepts_place(self) -> None:
        """Verify o4_sampled_at accepts an E53Place;"""
        place = make_place('Sampling Location')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=place,
            o5_removed=[make_sample('Sample')],
        )

        assert entity.o4_sampled_at is place

    # ------------------------- #

    def test_o4_sampled_at_rejects_invalid(self) -> None:
        """Verify o4_sampled_at raises ValidationError for non-place values;"""
        with pytest.raises(ValidationError):
            S24SampleSplitting(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at='invalid',  # type: ignore[arg-type]
                o5_removed=[make_sample('Sample')],
            )

    # ------------------------- #

    def test_o5_removed_field_exists(self) -> None:
        """Verify o5_removed field is present;"""
        entity = _make_minimal_s24()

        assert hasattr(entity, 'o5_removed')

    # ------------------------- #

    def test_o5_removed_accepts_sample(self) -> None:
        """Verify o5_removed accepts a list of S13Sample;"""
        sample = make_sample('Sample')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[sample],
        )

        assert entity.o5_removed is not None
        assert entity.o5_removed[0] is sample

    # ------------------------- #

    def test_o5_removed_rejects_invalid(self) -> None:
        """Verify o5_removed raises ValidationError for non-sample values;"""
        with pytest.raises(ValidationError):
            S24SampleSplitting(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_o20_sampled_from_type_of_part_accepts_type(self) -> None:
        """Verify o20_sampled_from_type_of_part accepts a list of E55Type;"""
        etype = make_type('Part Type')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[make_sample('Sample')],
            o20_sampled_from_type_of_part=[etype],
        )

        assert entity.o20_sampled_from_type_of_part is not None
        assert entity.o20_sampled_from_type_of_part[0] is etype

    # ------------------------- #

    def test_o27_split_field_exists(self) -> None:
        """Verify o27_split field is present and None by default;"""
        entity = _make_minimal_s24()

        assert hasattr(entity, 'o27_split')
        assert entity.o27_split is None

    # ------------------------- #

    def test_o27_split_accepts_sample(self) -> None:
        """Verify o27_split accepts a list of S13Sample;"""
        source = make_sample('Source Sample')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[make_sample('Result Sample')],
            o27_split=[source],
        )

        assert entity.o27_split is not None
        assert entity.o27_split[0] is source

    # ------------------------- #

    def test_o27_split_rejects_invalid_type(self) -> None:
        """Verify o27_split raises ValidationError for non-sample values;"""
        with pytest.raises(ValidationError):
            S24SampleSplitting(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=[make_sample('Sample')],
                o27_split=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_o29_removed_sub_sample_field_exists(self) -> None:
        """Verify o29_removed_sub_sample field is present and None by default;"""
        entity = _make_minimal_s24()

        assert hasattr(entity, 'o29_removed_sub_sample')
        assert entity.o29_removed_sub_sample is None

    # ------------------------- #

    def test_o29_removed_sub_sample_accepts_sample(self) -> None:
        """Verify o29_removed_sub_sample accepts a list of S13Sample;"""
        sub = make_sample('Sub Sample')
        entity = S24SampleSplitting(
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[make_sample('Result Sample')],
            o29_removed_sub_sample=[sub],
        )

        assert entity.o29_removed_sub_sample is not None
        assert entity.o29_removed_sub_sample[0] is sub

    # ------------------------- #

    def test_o29_removed_sub_sample_rejects_invalid_type(self) -> None:
        """Verify o29_removed_sub_sample raises ValidationError for non-sample values;"""
        with pytest.raises(ValidationError):
            S24SampleSplitting(
                p7_took_place_at=_event_places(),
                p160_has_temporal_projection=_event_time(),
                p161_has_spatial_projection=_spatial_projection(),
                o3_sampled_from=[make_material('Source Material')],
                o4_sampled_at=make_place('Sampling Location'),
                o5_removed=[make_sample('Sample')],
                o29_removed_sub_sample=['invalid'],  # type: ignore[list-item]
            )

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes property fields;"""
        entity = _make_minimal_s24()
        data = entity.model_dump()

        assert 'o3_sampled_from' in data
        assert 'o4_sampled_at' in data
        assert 'o5_removed' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization contains property fields;"""
        entity = _make_minimal_s24()
        json_str = entity.model_dump_json()

        assert '"o3_sampled_from"' in json_str
        assert '"o4_sampled_at"' in json_str

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify S24 can be created with a p1 appellation;"""
        entity = S24SampleSplitting(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Splitting Event')],
            p7_took_place_at=_event_places(),
            p160_has_temporal_projection=_event_time(),
            p161_has_spatial_projection=_spatial_projection(),
            o3_sampled_from=[make_material('Source Material')],
            o4_sampled_at=make_place('Sampling Location'),
            o5_removed=[make_sample('Sample')],
        )

        assert entity.p1_is_identified_by is not None
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Splitting Event'
