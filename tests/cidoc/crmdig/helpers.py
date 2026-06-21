"""Factory functions for CRMDig test entities;

All test data is based on examples from the CRMDig v5.0 spec;

"""


from pyheritage.cidoc.core.entities import (
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E55Type,
    E57Material,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmsci.entities import (
    S9PropertyType,
    S10MaterialSubstantial,
)


__all__ = [
    'make_stv',
    'make_e22_kwargs',
    'make_e7_kwargs',
    'make_s4_kwargs',
]


# ===================================================================== #
#                         Core CIDOC builders                           #
# ===================================================================== #


def make_stv(label: str = 'STV') -> E92SpaceTimeVolume:
    """Create minimal E92 Space-Time Volume with temporal/spatial projection;"""
    return E92SpaceTimeVolume(
        p160_has_temporal_projection=E52TimeSpan(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Time')],
        ),
        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
    )


# ===================================================================== #
#                      E22 / E7 kwargs builders                         #
# ===================================================================== #


def make_e22_kwargs() -> dict:
    """Return required kwargs for E22-derived entities (D8, D13);"""
    return {
        'p196_defines': make_stv(),
        'p53_has_former_or_current_location': [],
        'p45_consists_of': [E57Material()],
    }


# ******************************************************************************************************************* #


def make_e7_kwargs(label: str = 'E7') -> dict:
    """Return required kwargs for E7-derived entities (D7, D10, D11, D12, D2, D3, D30);"""
    return {
        'p7_took_place_at': [E53Place(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Place')],
            p157_is_at_rest_relative_to=[],
        )],
        'p160_has_temporal_projection': E52TimeSpan(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Time')],
        ),
        'p161_has_spatial_projection': [E53Place(p157_is_at_rest_relative_to=[])],
    }


# ******************************************************************************************************************* #


def make_s4_kwargs(label: str = 'S4') -> dict:
    """Return required kwargs for S4Observation-derived entities (D11, D2);"""
    thing = S10MaterialSubstantial(
        o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
    )
    kwargs = make_e7_kwargs(label)
    kwargs.update({
        'o24_measured': thing,
        'o8_observed': thing,
        'o9_observed_property_type': S9PropertyType(),
        'o16_observed_value': E55Type(),
        'p177_assigned_property_type': None,
    })
    return kwargs
