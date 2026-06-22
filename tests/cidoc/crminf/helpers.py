"""Factory functions for CRMinf test entities;

"""


from pyheritage.cidoc.core.entities import (
    E41Appellation,
    E52TimeSpan,
    E53Place,
    E55Type,
    E70Thing,
    E73InformationObject,
)
from pyheritage.cidoc.crminf.entities import (
    I2Belief,
    I4PropositionSet,
    I6BeliefValue,
    I10ProvenanceStatement,
    I12AdoptedBelief,
    I13IntendedMeaningBelief,
    I14ProvenanceBelief,
)


__all__ = [
    'make_place',
    'make_timespan',
    'make_type',
    'make_activity_kwargs',
    'make_e13_kwargs',
    'make_belief_value',
    'make_proposition_set',
    'make_minimal_i2',
    'make_minimal_i10',
    'make_minimal_i12',
    'make_minimal_i13',
    'make_minimal_i14',
]


# ===================================================================== #
#                         Core CIDOC builders                           #
# ===================================================================== #


def make_place(label: str = 'Place') -> E53Place:
    """Create minimal E53 Place;"""
    return E53Place(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
        p157_is_at_rest_relative_to=[],
    )


# ******************************************************************************************************************* #


def make_timespan(label: str = 'Time') -> E52TimeSpan:
    """Create minimal E52 Time-Span;"""
    return E52TimeSpan(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
    )


# ******************************************************************************************************************* #


def make_type(label: str = 'Type') -> E55Type:
    """Create minimal E55 Type;"""
    return E55Type(
        p1_is_identified_by=[E41Appellation(p190_has_symbolic_content=label)],
    )


# ===================================================================== #
#                    Required kwargs builders                           #
# ===================================================================== #


def make_activity_kwargs(label: str = 'Activity') -> dict:
    """Return the required kwargs for E7 Activity (I1, I7, I15, I16);"""
    place = make_place(label + ' Place')
    return {
        'p161_has_spatial_projection': [place],
        'p160_has_temporal_projection': make_timespan(label + ' Time'),
        'p7_took_place_at': [place],
    }


# ******************************************************************************************************************* #


def make_e13_kwargs(label: str = 'E13') -> dict:
    """Return the required kwargs for E13 Attribute Assignment (I5, I17);"""
    kwargs = make_activity_kwargs(label)
    kwargs['p177_assigned_property_type'] = [make_type(label + ' Type')]
    return kwargs


# ===================================================================== #
#                       Belief value factory                           #
# ===================================================================== #


def make_belief_value(value: str = 'True') -> I6BeliefValue:
    """Create I6 Belief Value with given value;"""
    return I6BeliefValue(value=value)


# ===================================================================== #
#                       Proposition set factory                        #
# ===================================================================== #


def make_proposition_set() -> I4PropositionSet:
    """Create minimal I4 Proposition Set;"""
    return I4PropositionSet()


# ===================================================================== #
#                    CRMinf entity factories                           #
# ===================================================================== #


def make_minimal_i2() -> I2Belief:
    """Create minimal I2 Belief with J4 and J5;"""
    return I2Belief(
        j4_that=[make_proposition_set()],
        j5_holds_to_be=make_belief_value('True'),
    )


# ******************************************************************************************************************* #


def make_minimal_i10() -> I10ProvenanceStatement:
    """Create minimal I10 Provenance Statement with J20;"""
    return I10ProvenanceStatement(
        j20_is_about_the_provenance_of=[E70Thing()],
    )


# ******************************************************************************************************************* #


def make_minimal_i12() -> I12AdoptedBelief:
    """Create minimal I12 Adopted Belief with J4, J5, and J14;"""
    return I12AdoptedBelief(
        j14_adopted_interpretation_of=[E73InformationObject()],
        j4_that=[make_proposition_set()],
        j5_holds_to_be=make_belief_value('True'),
    )


# ******************************************************************************************************************* #


def make_minimal_i13() -> I13IntendedMeaningBelief:
    """Create minimal I13 Intended Meaning Belief with J4, J5, J16, J17;"""
    return I13IntendedMeaningBelief(
        j16_assumed_meaning=[make_proposition_set()],
        j17_about=[E73InformationObject()],
        j4_that=[make_proposition_set()],
        j5_holds_to_be=make_belief_value('True'),
    )


# ******************************************************************************************************************* #


def make_minimal_i14() -> I14ProvenanceBelief:
    """Create minimal I14 Provenance Belief with J4, J5, and J19;"""
    return I14ProvenanceBelief(
        j19_that=[make_minimal_i10()],
        j4_that=[make_proposition_set()],
        j5_holds_to_be=make_belief_value('True'),
    )
