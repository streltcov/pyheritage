# -*- coding: utf-8 -*-

"""Factory functions for CRMsci test entities;

"""


from pyheritage.cidoc.core.entities import (
    E18PhysicalThing,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E54Dimension,
    E55Type,
    E57Material,
    E58MeasurementUnit,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmsci.entities import S10MaterialSubstantial, S13Sample


__all__ = [
    'make_timespan',
    'make_place',
    'make_physical_thing',
    'make_dimension',
    'make_type',
    'make_material',
    'make_sample',
]


def make_timespan(label: str = 'Time Span') -> E52TimeSpan:
    """Create minimal E52TimeSpan with an appellation identified by label."""
    return E52TimeSpan(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
    )


# ******************************************************************************************************************* #


def _make_inner_place() -> E53Place:
    """Minimal E53Place with only the required p157_is_at_rest_relative_to."""
    return E53Place(p157_is_at_rest_relative_to=[])


# ******************************************************************************************************************* #


def make_place(label: str = 'Place') -> E53Place:
    """Create E53Place with appellation and p157_is_at_rest_relative_to referencing an E18PhysicalThing."""
    timespan = make_timespan('Reference Time')
    inner_place = _make_inner_place()
    return E53Place(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        p157_is_at_rest_relative_to=[
            E18PhysicalThing(
                p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Reference Object')],
                p45_consists_of=[E57Material()],
                p53_has_former_or_current_location=[],
                p196_defines=E92SpaceTimeVolume(
                    p160_has_temporal_projection=timespan,
                    p161_has_spatial_projection=[inner_place],
                ),
            )
        ],
    )


# ******************************************************************************************************************* #


def make_physical_thing(label: str = 'Physical Thing') -> E18PhysicalThing:
    """Create E18PhysicalThing with all required fields including nested E92SpaceTimeVolume and E53Place."""
    timespan = make_timespan('Reference Time')
    inner_place = _make_inner_place()
    return E18PhysicalThing(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        p45_consists_of=[E57Material()],
        p53_has_former_or_current_location=[],
        p196_defines=E92SpaceTimeVolume(
            p160_has_temporal_projection=timespan,
            p161_has_spatial_projection=[inner_place],
        ),
    )


# ******************************************************************************************************************* #


def make_dimension(
    label: str = 'Dimension',
    value: float | None = None,
    unit_label: str | None = None,
) -> E54Dimension:
    """Create E54Dimension; value and unit_label are optional."""
    kwargs: dict = {
        'p1_is_identified_by': [E41Appellation(p190_has_symbolic_content=label)],
    }
    if value is not None:
        kwargs['p90_has_value'] = value
    if unit_label is not None:
        kwargs['p91_has_unit'] = E58MeasurementUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=unit_label)],
        )
    return E54Dimension(**kwargs)


# ******************************************************************************************************************* #


def make_type(label: str = 'Type') -> E55Type:
    """Create minimal E55Type with an appellation identified by label."""
    return E55Type(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
    )


# ******************************************************************************************************************* #


def make_material(label: str = 'Material Substantial') -> S10MaterialSubstantial:
    """Create S10MaterialSubstantial with appellation and o15_occupied place."""
    return S10MaterialSubstantial(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        o15_occupied=make_place(f'Location of {label}'),
    )


# ******************************************************************************************************************* #


def make_sample(label: str = 'Sample') -> S13Sample:
    """Create S13Sample with appellation and o15_occupied place."""
    return S13Sample(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        o15_occupied=make_place(f'Location of {label}'),
    )
