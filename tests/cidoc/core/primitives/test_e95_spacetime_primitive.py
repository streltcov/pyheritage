# -*- coding: utf-8 -*-

"""Tests for E95 SpaceTime Primitive CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


import re

import pytest

from pyheritage.cidoc.core.entities import E59PrimitiveValue, E61TimePrimitive, E94SpacePrimitive, E95SpaceTimePrimitive
from pyheritage.cidoc.core.properties import P169DefinesSpacetimeVolume
from pyheritage.cidoc.enums import TimePrecision


class TestE95Construction:
    """Test E95 SpaceTime Primitive construction scenarios;

    """

    def test_default_empty_construction(self) -> None:
        """Checks that E95 can be constructed with no arguments;"""
        entity = E95SpaceTimePrimitive()
        assert entity.spatial is None
        assert entity.temporal is None

    # ------------------------- #

    def test_construction_with_spatial_only(self) -> None:
        """Checks construction with spatial component only;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert entity.spatial is not None
        assert entity.temporal is None

    # ------------------------- #

    def test_construction_with_temporal_only(self) -> None:
        """Checks construction with temporal component only;"""
        temporal = E61TimePrimitive.from_year(1503)
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert entity.spatial is None
        assert entity.temporal is not None

    # ------------------------- #

    def test_construction_with_both_components(self) -> None:
        """Checks construction with both spatial and temporal components;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        temporal = E61TimePrimitive.from_year(1503)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.spatial is not None
        assert entity.temporal is not None

    # ------------------------- #

    def test_construction_via_dict_params(self) -> None:
        """Checks construction using dictionary-style parameters;"""
        entity = E95SpaceTimePrimitive(
            spatial={'value': 'POINT(2.3364 48.8606)'},
            temporal={'value': '1503'},
        )
        assert entity.spatial is not None
        assert entity.temporal is not None
        assert entity.spatial.value == 'POINT(2.3364 48.8606)'
        assert entity.temporal.value == '1503'


# ******************************************************************************************************************* #


class TestE95HasSpatial:
    """Test has_spatial property;

    """

    def test_has_spatial_true_when_defined_with_value(self) -> None:
        """Checks has_spatial returns True when spatial component has a value;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert entity.has_spatial is True

    # ------------------------- #

    def test_has_spatial_false_when_none(self) -> None:
        """Checks has_spatial returns False when spatial is None;"""
        entity = E95SpaceTimePrimitive()
        assert entity.has_spatial is False

    # ------------------------- #

    def test_has_spatial_false_when_empty_value(self) -> None:
        """Checks has_spatial returns False when spatial has empty value;"""
        spatial = E94SpacePrimitive(value='')
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert entity.has_spatial is False

    # ------------------------- #

    def test_has_spatial_true_with_polygon(self) -> None:
        """Checks has_spatial returns True for polygon geometry;"""
        spatial = E94SpacePrimitive.from_bbox(30, 31, 31, 32)
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert entity.has_spatial is True

    # ------------------------- #

    def test_has_spatial_true_with_complex_polygon(self) -> None:
        """Checks has_spatial returns True for complex polygon;"""
        spatial = E94SpacePrimitive.from_polygon([
            (30.4, 31.3), (30.5, 31.3),
            (30.5, 31.4), (30.4, 31.4),
            (30.4, 31.3),
        ])
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert entity.has_spatial is True


# ******************************************************************************************************************* #


class TestE95HasTemporal:
    """Test has_temporal property;

    """

    def test_has_temporal_true_when_defined_with_value(self) -> None:
        """Checks has_temporal returns True when temporal component has a value;"""
        temporal = E61TimePrimitive.from_year(1503)
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert entity.has_temporal is True

    # ------------------------- #

    def test_has_temporal_false_when_none(self) -> None:
        """Checks has_temporal returns False when temporal is None;"""
        entity = E95SpaceTimePrimitive()
        assert entity.has_temporal is False

    # ------------------------- #

    def test_has_temporal_false_when_empty_value(self) -> None:
        """Checks has_temporal returns False when temporal has empty value;"""
        temporal = E61TimePrimitive(value='')
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert entity.has_temporal is False

    # ------------------------- #

    def test_has_temporal_true_with_approximate_date(self) -> None:
        """Checks has_temporal returns True for approximate date;"""
        temporal = E61TimePrimitive(value='1503~')
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert entity.has_temporal is True

    # ------------------------- #

    def test_has_temporal_true_with_interval(self) -> None:
        """Checks has_temporal returns True for time interval;"""
        temporal = E61TimePrimitive.from_interval(1501, 1520)
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert entity.has_temporal is True


# ******************************************************************************************************************* #


class TestE95Repr:
    """Test __repr__ method;

    """

    def test_repr_empty(self) -> None:
        """Checks __repr__ for empty E95 returns 'E95(empty)';"""
        entity = E95SpaceTimePrimitive()
        assert repr(entity) == 'E95(empty)'

    # ------------------------- #

    def test_repr_spatial_only(self) -> None:
        """Checks __repr__ with spatial component only;"""
        spatial = E94SpacePrimitive(value='POINT(2.3364 48.8606)')
        entity = E95SpaceTimePrimitive(spatial=spatial)
        assert repr(entity) == 'E95(POINT(2.3364 48.8606))'

    # ------------------------- #

    def test_repr_temporal_only(self) -> None:
        """Checks __repr__ with temporal component only;"""
        temporal = E61TimePrimitive(value='1503')
        entity = E95SpaceTimePrimitive(temporal=temporal)
        assert repr(entity) == 'E95(E61(1503))'

    # ------------------------- #

    def test_repr_both_components(self) -> None:
        """Checks __repr__ with both spatial and temporal components;"""
        spatial = E94SpacePrimitive(value='POINT(2.3364 48.8606)')
        temporal = E61TimePrimitive(value='1503')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert repr(entity) == 'E95(POINT(2.3364 48.8606), E61(1503))'

    # ------------------------- #

    def test_repr_with_approximate_temporal(self) -> None:
        """Checks __repr__ with approximate temporal component;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        temporal = E61TimePrimitive(value='1503~')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert repr(entity) == 'E95(POINT(2.3364 48.8606), E61(1503~ [≈]))'

    # ------------------------- #

    def test_repr_with_complex_spatial_and_interval(self) -> None:
        """Checks __repr__ with complex polygon and interval temporal;"""
        spatial = E94SpacePrimitive.from_bbox(30, 31, 31, 32)
        temporal = E61TimePrimitive.from_interval(1501, 1520)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        repr_str = repr(entity)
        assert repr_str.startswith('E95(')
        assert 'POLYGON' in repr_str
        assert '1501/1520' in repr_str


# ******************************************************************************************************************* #


class TestE95Serialization:
    """Test serialization methods;

    """

    def test_model_dump_empty(self) -> None:
        """Checks model_dump output for empty E95;"""
        entity = E95SpaceTimePrimitive()
        dump = entity.model_dump()
        assert 'spatial' in dump
        assert 'temporal' in dump
        assert dump['spatial'] is None
        assert dump['temporal'] is None

    # ------------------------- #

    def test_model_dump_with_components(self) -> None:
        """Checks model_dump output with both components;"""
        spatial = E94SpacePrimitive(value='POINT(2.3364 48.8606)')
        temporal = E61TimePrimitive(value='1503')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        dump = entity.model_dump()
        assert dump['spatial'] is not None
        assert dump['temporal'] is not None
        assert dump['spatial']['value'] == 'POINT(2.3364 48.8606)'
        assert dump['temporal']['value'] == '1503'

    # ------------------------- #

    def test_model_dump_by_alias(self) -> None:
        """Checks model_dump with by_alias=True includes @id field;"""
        entity = E95SpaceTimePrimitive()
        dump = entity.model_dump(by_alias=True)
        assert '@id' in dump
        assert dump['@id'] is not None

    # ------------------------- #

    def test_model_dump_by_alias_with_components(self) -> None:
        """Checks model_dump(by_alias=True) with components;"""
        spatial = E94SpacePrimitive(value='POINT(2.3364 48.8606)')
        temporal = E61TimePrimitive(value='1503')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        dump = entity.model_dump(by_alias=True)
        assert '@id' in dump
        assert dump['spatial']['value'] == 'POINT(2.3364 48.8606)'
        assert dump['temporal']['value'] == '1503'

    # ------------------------- #

    def test_model_dump_json_string(self) -> None:
        """Checks model_dump_json returns valid JSON string;"""
        spatial = E94SpacePrimitive(value='POINT(2.3364 48.8606)')
        temporal = E61TimePrimitive(value='1503')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        json_str = entity.model_dump_json(by_alias=True)
        assert '"@id"' in json_str
        assert 'POINT' in json_str
        assert '1503' in json_str

    # ------------------------- #

    def test_model_validate(self) -> None:
        """Checks model_validate class method;"""
        data = {
            'spatial': {'value': 'POINT(2.3364 48.8606)'},
            'temporal': {'value': '1503'},
        }
        entity = E95SpaceTimePrimitive.model_validate(data)
        assert isinstance(entity, E95SpaceTimePrimitive)
        assert entity.spatial is not None
        assert entity.temporal is not None

    # ------------------------- #

    def test_model_validate_empty(self) -> None:
        """Checks model_validate with empty data;"""
        entity = E95SpaceTimePrimitive.model_validate({})
        assert isinstance(entity, E95SpaceTimePrimitive)
        assert entity.spatial is None
        assert entity.temporal is None


# ******************************************************************************************************************* #


class TestE95Inheritance:
    """Test inheritance and CRM metadata;

    """

    def test_inherits_from_e59_primitive_value(self) -> None:
        """Checks inheritance from E59PrimitiveValue;"""
        entity = E95SpaceTimePrimitive()
        assert isinstance(entity, E59PrimitiveValue)

    # ------------------------- #

    def test_instance_of_p169_defines_spacetime_volume(self) -> None:
        """Checks that E95 is instance of P169DefinesSpacetimeVolume;"""
        entity = E95SpaceTimePrimitive()
        assert isinstance(entity, P169DefinesSpacetimeVolume)

    # ------------------------- #

    def test_crm_code(self) -> None:
        """Checks crm_code attribute equals 'E95';"""
        assert hasattr(E95SpaceTimePrimitive, 'crm_code')
        assert E95SpaceTimePrimitive.crm_code == 'E95'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Checks crm_label attribute;"""
        assert hasattr(E95SpaceTimePrimitive, 'crm_label')
        assert E95SpaceTimePrimitive.crm_label == 'E95 SpaceTime Primitive'

    # ------------------------- #

    def test_has_id_field(self) -> None:
        """Checks that @id field exists;"""
        entity = E95SpaceTimePrimitive()
        assert hasattr(entity, 'id')
        assert entity.id is not None

    # ------------------------- #

    def test_id_is_uuid_format(self) -> None:
        """Checks that id is UUID format;"""
        entity = E95SpaceTimePrimitive()
        uuid_pattern = re.compile(
            r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
            re.IGNORECASE,
        )
        assert uuid_pattern.match(entity.id)

    # ------------------------- #

    def test_unique_ids_per_instance(self) -> None:
        """Checks that each instance has unique id;"""
        e1 = E95SpaceTimePrimitive()
        e2 = E95SpaceTimePrimitive()
        assert e1.id != e2.id

    # ------------------------- #

    def test_has_p169_property(self) -> None:
        """Checks that p169_defines_spacetime_volume property exists from P169DefinesSpacetimeVolume;"""
        entity = E95SpaceTimePrimitive()
        assert hasattr(entity, 'p169_defines_spacetime_volume')


# ******************************************************************************************************************* #


class TestE95EdgeCases:
    """Test edge cases and complex scenarios;

    """

    def test_complex_polygon_with_interval(self) -> None:
        """Checks E95 with complex polygon and time interval;"""
        spatial = E94SpacePrimitive.from_polygon([
            (30.4, 31.3), (30.5, 31.3),
            (30.5, 31.4), (30.4, 31.4),
            (30.4, 31.3),
        ])
        temporal = E61TimePrimitive.from_interval(1501, 1520)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is True
        assert entity.spatial.is_polygon is True
        assert entity.temporal.is_interval is True

    # ------------------------- #

    def test_point_with_approximate_date(self) -> None:
        """Checks E95 with point and approximate date;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        temporal = E61TimePrimitive(value='1503~')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is True
        assert entity.temporal.is_approximate is True

    # ------------------------- #

    def test_point_with_bce_date(self) -> None:
        """Checks E95 with point and BCE date;"""
        spatial = E94SpacePrimitive.from_lat_lon(30.04, 31.23)
        temporal = E61TimePrimitive(value='-0196')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is True
        assert entity.temporal.is_bce is True

    # ------------------------- #

    def test_multiple_independent_instances(self) -> None:
        """Checks that multiple E95 instances are independent;"""
        e1 = E95SpaceTimePrimitive(
            spatial=E94SpacePrimitive.from_lat_lon(48.8606, 2.3364),
            temporal=E61TimePrimitive.from_year(1503),
        )
        e2 = E95SpaceTimePrimitive(
            spatial=E94SpacePrimitive.from_lat_lon(51.5074, -0.1278),
            temporal=E61TimePrimitive.from_year(1703),
        )
        assert e1.id != e2.id
        assert e1.spatial.value != e2.spatial.value
        assert e1.temporal.value != e2.temporal.value
        assert e1.spatial.latitude == pytest.approx(48.8606)
        assert e2.spatial.latitude == pytest.approx(51.5074)

    # ------------------------- #

    def test_spatial_with_empty_temporal(self) -> None:
        """Checks E95 with spatial but explicitly empty temporal;"""
        spatial = E94SpacePrimitive.from_lat_lon(0, 0)
        temporal = E61TimePrimitive(value='')
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is False

    # ------------------------- #

    def test_temporal_with_empty_spatial(self) -> None:
        """Checks E95 with temporal but explicitly empty spatial;"""
        spatial = E94SpacePrimitive(value='')
        temporal = E61TimePrimitive.from_year(2024)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is False
        assert entity.has_temporal is True

    # ------------------------- #

    def test_bbox_with_century(self) -> None:
        """Checks E95 with bounding box and century temporal;"""
        spatial = E94SpacePrimitive.from_bbox(0, 0, 10, 10)
        temporal = E61TimePrimitive.from_century(16)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is True
        assert entity.spatial.is_polygon is True
        assert entity.temporal.precision == TimePrecision.CENTURY

    # ------------------------- #

    def test_linestring_with_decade(self) -> None:
        """Checks E95 with linestring and decade temporal;"""
        spatial = E94SpacePrimitive.from_linestring([
            (11.26, 43.77), (0.98, 47.41), (2.34, 48.86),
        ])
        temporal = E61TimePrimitive.from_decade(1950)
        entity = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        assert entity.has_spatial is True
        assert entity.has_temporal is True
        assert entity.spatial.is_line is True
        assert entity.temporal.precision == TimePrecision.DECADE

    # ------------------------- #

    def test_model_dump_json_roundtrip(self) -> None:
        """Checks that JSON can be used to recreate the entity;"""
        spatial = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        temporal = E61TimePrimitive.from_year(1503)
        original = E95SpaceTimePrimitive(spatial=spatial, temporal=temporal)
        json_str = original.model_dump_json()
        restored = E95SpaceTimePrimitive.model_validate_json(json_str)
        assert restored.spatial is not None
        assert restored.temporal is not None
        assert restored.spatial.value == original.spatial.value
        assert restored.temporal.value == original.temporal.value

    # ------------------------- #

    def test_p169_property_default_none(self) -> None:
        """Checks that p169_defines_spacetime_volume defaults to None;"""
        entity = E95SpaceTimePrimitive()
        assert entity.p169_defines_spacetime_volume is None
