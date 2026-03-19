# -*- coding: utf-8 -*-

"""Tests for E94 Space Primitive CRM entity;

"""


# pylint: disable=E0401,C0116,W0612


import pytest

from pyheritage.cidoc.core.entities import E94SpacePrimitive
from pyheritage.cidoc.core.entities._primitives import _coerce_e94  # noqa
from pyheritage.cidoc.core.enums import SpatialFormat


class TestE94EntityValidation:
    """Spatial data validation;

    """

    def test_valid_wkt_point(self) -> None:
        entity = E94SpacePrimitive(value='POINT(30 31)')
        assert entity.geometry is not None

    # ------------------------- #

    def test_valid_wkt_polygon(self) -> None:
        entity = E94SpacePrimitive(value='POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))')
        assert entity.geometry_type == 'Polygon'

    # ------------------------- #

    def test_valid_geojson(self) -> None:
        entity = E94SpacePrimitive(value='{"type": "Point", "coordinates": [30.0,31.0]}')
        assert entity.is_point

    # ------------------------- #

    def test_invalid_wkt(self) -> None:
        with pytest.raises(ValueError, match="Invalid WKT"):
            E94SpacePrimitive(value="POINT(abc def)")

    # ------------------------- #

    def test_invalid_geojson(self) -> None:
        with pytest.raises(ValueError, match="Invalid GeoJSON"):
            E94SpacePrimitive(value='{"not":"geometry"}')


# ******************************************************************************************************************* #


class TestE94SRS:
    """Test E94 Space Primitive SRS;

    """

    def test_default_srs(self) -> None:
        assert E94SpacePrimitive(value="POINT(0 0)").srs == "EPSG:4326"

    # ------------------------- #

    def test_custom_srs(self) -> None:
        sp = E94SpacePrimitive(
            value="POINT(500000 3500000)",
            srs="EPSG:32636",
        )
        assert sp.srs == "EPSG:32636"


# ******************************************************************************************************************* #


class TestE94Validation:
    """Test E94 Space Primitive with incorrect spatial values;

    """

    def test_random_string(self) -> None:
        with pytest.raises(ValueError, match="must be WKT or GeoJSON"):
            E94SpacePrimitive(value="somewhere in Egypt")

    # ------------------------- #

    def test_empty_allowed(self) -> None:
        entity = E94SpacePrimitive()
        assert entity.is_empty


# ******************************************************************************************************************* #


class TestE94Point:
    """Point geometry;

    """

    def test_from_lat_lon(self) -> None:
        sp = E94SpacePrimitive.from_lat_lon(48.8606, 2.3364)
        assert sp.latitude == pytest.approx(48.8606)
        assert sp.longitude == pytest.approx(2.3364)

    # ------------------------- #

    def test_from_lat_lon_with_altitude(self) -> None:
        sp = E94SpacePrimitive.from_lat_lon(45.83, 6.87, altitude=4808.0)
        assert sp.altitude == pytest.approx(4808.0)

    # ------------------------- #

    def test_is_point(self) -> None:
        sp = E94SpacePrimitive.from_lat_lon(0, 0)
        assert sp.is_point
        assert not sp.is_polygon
        assert not sp.is_line

    # ------------------------- #

    def test_coordinates(self) -> None:
        entity = E94SpacePrimitive(value="POINT(30.42 31.4)")
        coordinates = entity.coordinates
        assert coordinates[0] == pytest.approx(30.42)
        assert coordinates[1] == pytest.approx(31.4)

    # ------------------------- #

    def test_non_point_coordinates_none(self) -> None:
        entity = E94SpacePrimitive(value="LINESTRING(0 0, 1 1)")
        assert entity.coordinates is None
        assert entity.latitude is None


# ******************************************************************************************************************* #


class TestE94Polygon:
    """Polygon geometry;

    """

    def test_from_bbox(self) -> None:
        sp = E94SpacePrimitive.from_bbox(30, 31, 31, 32)
        assert sp.is_polygon
        assert sp.bounds == pytest.approx((30.0, 31.0, 31.0, 32.0))

    # ------------------------- #

    def test_from_polygon(self) -> None:
        sp = E94SpacePrimitive.from_polygon([
            (0, 0), (1, 0), (1, 1), (0, 1), (0, 0),
        ])
        assert sp.is_polygon

    # ------------------------- #

    def test_centroid(self) -> None:
        sp = E94SpacePrimitive.from_bbox(0, 0, 2, 2)
        assert sp.centroid == pytest.approx((1.0, 1.0))


# ******************************************************************************************************************* #


class TestE94Line:
    """Linestring geometry;

    """

    def test_from_linestring(self) -> None:
        entity = E94SpacePrimitive.from_linestring([
            (11.26, 43.77), (2.34, 48.86),
        ])
        assert entity.is_line
        assert entity.geometry_type == "LineString"

    # ------------------------- #

    def test_bounds(self) -> None:
        entity = E94SpacePrimitive.from_linestring([
            (0, 0), (10, 10),
        ])
        assert entity.bounds == pytest.approx((0, 0, 10, 10))


# ******************************************************************************************************************* #


class TestE94Format:
    """Test spatial formats;

    """

    def test_wkt_format(self) -> None:
        sp = E94SpacePrimitive(value="POINT(0 0)")
        assert sp.format == SpatialFormat.WKT

    # ------------------------- #

    def test_geojson_format(self) -> None:
        sp = E94SpacePrimitive(
            value='{"type":"Point","coordinates":[0,0]}'
        )
        assert sp.format == SpatialFormat.GEOJSON

    # ------------------------- #

    def test_wkt_to_geojson(self) -> None:
        entity = E94SpacePrimitive(value="POINT(30 31)")
        geo_json = entity.to_geojson()
        assert geo_json["type"] == "Point"
        assert geo_json["coordinates"] == pytest.approx([30.0, 31.0])

    # ------------------------- #

    def test_geojson_to_wkt(self) -> None:
        entity = E94SpacePrimitive(
            value='{"type":"Point","coordinates":[30,31]}'
        )
        wkt = entity.to_wkt()
        assert "POINT" in wkt
        assert "30" in wkt

    # ------------------------- #

    def test_polygon_to_geojson(self) -> None:
        sp = E94SpacePrimitive.from_bbox(0, 0, 1, 1)
        gj = sp.to_geojson()
        assert gj["type"] == "Polygon"
        assert "coordinates" in gj

    # ------------------------- #

    def test_to_geojson_feature(self) -> None:
        sp = E94SpacePrimitive.from_lat_lon(31.4, 30.42)
        feature = sp.to_geojson_feature(
            properties={"name": "Rosetta"}
        )
        assert feature["type"] == "Feature"
        assert feature["properties"]["name"] == "Rosetta"
        assert feature["geometry"]["type"] == "Point"


# ******************************************************************************************************************* #


class TestE94Coercion:
    """Automatic wrapping;

    """

    def test_string_to_e94_entity(self) -> None:
        entity = _coerce_e94('POINT(30 31)')
        assert isinstance(entity, E94SpacePrimitive)
        assert entity.is_point

    # ------------------------- #

    def test_passthrough(self) -> None:
        entity = E94SpacePrimitive(value='POINT(30 31)')
        assert _coerce_e94(entity) is entity
