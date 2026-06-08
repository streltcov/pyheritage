"""Factory functions for CRMarchaeo test entities;

All test data is based on the excavation of the West House at Akrotiri, Thera
(CRMarchaeo v2.0 spec examples), supplemented with consistent fictional detail;

"""


from pyheritage.cidoc.core.entities import (
    E18PhysicalThing,
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E55Type,
    E57Material,
    E92SpaceTimeVolume,
)
from pyheritage.cidoc.crmarchaeo.entities import (
    A2StratigraphicVolumeUnit,
    A3StratigraphicInterface,
    A4StratigraphicGenesis,
    A5StratigraphicModification,
    A6GroupDeclarationEvent,
    A7Embedding,
    A8StratigraphicUnit,
    A9ArchaeologicalExcavation,
    A10ExcavationInterface,
)
from pyheritage.cidoc.crmsci.entities import (
    S9PropertyType,
    S10MaterialSubstantial,
    S13Sample,
)


__all__ = [
    'make_stv',
    'make_s20_kwargs',
    'make_e13_kwargs',
    'make_s4_kwargs',
    'make_site',
    'make_a8',
    'make_a2',
    'make_a3',
    'make_a4',
    'make_a5',
    'make_a6',
    'make_a7',
    'make_a9',
    'make_a10',
    'make_s13',
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
#                      S20/S4 kwargs builders                           #
# ===================================================================== #


def make_s20_kwargs() -> dict:
    """Return the required kwargs common to S20-derived entities (A8, A2, A3, A7, A10);"""
    stv = make_stv()
    return {
        'p157_is_at_rest_relative_to': [],
        'p45_consists_of': [E57Material()],
        'p53_has_former_or_current_location': [],
        'p196_defines': stv,
        'o23_is_defined_by': stv,
    }


# ******************************************************************************************************************* #


def make_e13_kwargs(label: str = 'E13') -> dict:
    """Return the required kwargs for E13 Attribute Assignment (A6);"""
    return {
        'p7_took_place_at': [E53Place(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Place')],
            p157_is_at_rest_relative_to=[],
        )],
        'p160_has_temporal_projection': E52TimeSpan(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Time')],
        ),
        'p161_has_spatial_projection': [E53Place(p157_is_at_rest_relative_to=[])],
        'p177_assigned_property_type': [E55Type(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Type')],
        )],
    }


# ******************************************************************************************************************* #


def make_s4_kwargs(label: str = 'S4') -> dict:
    """Return the required kwargs for S4 Observation (A9);"""
    kwargs = make_e13_kwargs(label)
    kwargs.update({
        'o8_observed': S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Observed')],
            o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
        ),
        'o9_observed_property_type': S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Property')],
        ),
        'o16_observed_value': E41Appellation(p190_has_symbolic_content=label + ' Value'),
    })
    return kwargs


# ===================================================================== #
#                       E27 Site factory                               #
# ===================================================================== #


def make_site(label: str = 'Site') -> 'E27Site':
    """Create minimal E27 Site;"""
    from pyheritage.cidoc.core.entities import E27Site
    return E27Site(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        p45_consists_of=[E57Material()],
        p53_has_former_or_current_location=[],
        p196_defines=make_stv(label + ' STV'),
    )


# ===================================================================== #
#                   CRMarchaeo entity factories                         #
# ===================================================================== #


def make_a8(label: str = 'A8 Stratigraphic Unit') -> A8StratigraphicUnit:
    """Create minimal A8 Stratigraphic Unit;"""
    return A8StratigraphicUnit(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s20_kwargs(),
    )


# ******************************************************************************************************************* #


def make_a2(
    label: str = 'Layer A',
    contains: E18PhysicalThing | None = None,
) -> A2StratigraphicVolumeUnit:
    """Create A2 Stratigraphic Volume Unit with AP15 (remains) and AP21 (contains) populated;"""
    from pyheritage.cidoc.core.entities import E18PhysicalThing as E18
    from pyheritage.cidoc.crmsci.entities import S10MaterialSubstantial as S10

    remains = S10(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' remains')],
        o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
    )
    if contains is None:
        contains = E18(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' find')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=make_stv(label + ' STV'),
        )

    return A2StratigraphicVolumeUnit(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s20_kwargs(),
        ap15_is_or_contains_remains_of=[remains],
        ap21_contains=[contains],
    )


# ******************************************************************************************************************* #


def make_a3(
    label: str = 'Interface [19]',
    confines: A2StratigraphicVolumeUnit | None = None,
) -> A3StratigraphicInterface:
    """Create A3 Stratigraphic Interface with AP12 (confines) pointing to an A2;"""
    if confines is None:
        confines = make_a2(label + ' volume')

    return A3StratigraphicInterface(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s20_kwargs(),
        ap12_confines=[confines],
    )


# ******************************************************************************************************************* #


def make_a7(
    label: str = 'Amphora embedding',
    embedding_of: E18PhysicalThing | None = None,
    embedding_in: A2StratigraphicVolumeUnit | None = None,
) -> A7Embedding:
    """Create A7 Embedding with AP17 (found by), AP18 (embedding of), AP19 (embedding in);"""
    from pyheritage.cidoc.core.entities import E18PhysicalThing as E18
    from pyheritage.cidoc.crmsci.entities import S19EncounterEvent

    if embedding_of is None:
        embedding_of = E18(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' object')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=make_stv(label + ' STV'),
        )
    if embedding_in is None:
        embedding_in = make_a2(label + ' layer')

    encounter = S19EncounterEvent(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' encounter')],
        p7_took_place_at=[E53Place(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Place')],
            p157_is_at_rest_relative_to=[],
        )],
        p160_has_temporal_projection=E52TimeSpan(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Time')],
        ),
        p161_has_spatial_projection=[E53Place(p157_is_at_rest_relative_to=[])],
        p177_assigned_property_type=[E55Type(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Type')],
        )],
        o8_observed=S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' matrix')],
            o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
        ),
        o9_observed_property_type=S9PropertyType(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Property')],
        ),
        o16_observed_value=E41Appellation(p190_has_symbolic_content=label + ' Value'),
        o19_encountered_object=[embedding_of],
        o21_encountered_at=E53Place(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' Spot')],
            p157_is_at_rest_relative_to=[],
        ),
    )

    return A7Embedding(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s20_kwargs(),
        ap17_is_found_by=[encounter],
        ap18_is_embedding_of=[embedding_of],
        ap19_is_embedding_in=[embedding_in],
    )


# ******************************************************************************************************************* #


def make_a10(label: str = 'Planum 6 of square I22') -> A10ExcavationInterface:
    """Create minimal A10 Excavation Interface;"""
    return A10ExcavationInterface(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s20_kwargs(),
    )


# ******************************************************************************************************************* #


def make_a5(label: str = 'Earthquake damage') -> A5StratigraphicModification:
    """Create A5 Stratigraphic Modification with AP8 (disturbed) and AP13 (relation) populated;"""
    return A5StratigraphicModification(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_e13_kwargs(label),
        o18_altered=[make_a8(label + ' disturbed SU')],
    )


# ******************************************************************************************************************* #


def make_a4(label: str = 'Pumice deposition') -> A4StratigraphicGenesis:
    """Create A4 Stratigraphic Genesis with AP7 (produced) and AP9 (took matter from) populated;"""
    return A4StratigraphicGenesis(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_e13_kwargs(label),
        o18_altered=[make_a8(label + ' altered SU')],
        o17_generated=[make_a8(label + ' generated SU')],
        ap7_produced=[make_a8(label + ' produced SU')],
        ap9_took_matter_from=[S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' source')],
            o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
        )],
    )


# ******************************************************************************************************************* #


def make_a6(label: str = 'Post hole grouping') -> A6GroupDeclarationEvent:
    """Create A6 Group Declaration Event with AP16 (assigned attribute to) populated;"""
    return A6GroupDeclarationEvent(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_e13_kwargs(label),
        ap16_assigned_attribute_to=[E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label + ' thing')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=make_stv(label + ' STV'),
        )],
    )


# ******************************************************************************************************************* #


def make_a9(label: str = 'West House excavation') -> A9ArchaeologicalExcavation:
    """Create A9 Archaeological Excavation with AP3 (investigated) populated;"""
    return A9ArchaeologicalExcavation(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        **make_s4_kwargs(label),
        ap3_investigated=[make_site(label + ' site')],
    )


# ******************************************************************************************************************* #


def make_s13(label: str = 'S13 Sample') -> S13Sample:
    """Create minimal S13 Sample (concrete subclass of S11);"""
    return S13Sample(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
    )
