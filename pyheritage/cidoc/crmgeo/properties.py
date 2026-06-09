# -*- coding: utf-8 -*-

"""CRMgeo property models;

(Mixin classes for entity models);

CRMgeo v1.2 (original 2015)

------------------------------------------------
Properties
------------------------------------------------
Q2  occupied                         E18 -> SP1
Q3  has temporal projection          SP1 -> SP13
Q4  has spatial projection           SP1 -> SP2
Q5  defined in                       E53 -> SP3
Q6  is at rest in relation to        SP3 -> E18
Q7  describes                        SP4 -> SP3
Q8  is fixed on                      SP4 -> E26
Q9  is expressed in terms of         SP5 -> SP4
Q10 defines place                    SP5 -> SP6
Q11 approximates                     SP6 -> SP2
Q12 approximates                     SP7 -> SP1
Q13 approximates                     SP10 -> SP13
Q14 defines time                     SP14 -> SP10
Q15 is expressed in terms of         SP14 -> SP11
Q16 defines spacetime volume         SP12 -> SP7
Q17 is expressed in terms of         SP12 -> SP11
Q18 is expressed in terms of         SP12 -> SP4
Q19 has reference event              SP11 -> E5

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (  # noqa: F401 – used in docstrings
        E18PhysicalThing,
        E53Place,
    )
    from pyheritage.cidoc.crmgeo.entities import (
        SP1PhenomenalSpacetimeVolume,
        SP2PhenomenalPlace,
        SP3ReferenceSpace,
        SP13PhenomenalTimeSpan,
    )


__all__ = (
    'Q2Occupied',
    'Q3HasTemporalProjection',
    'Q4HasSpatialProjection',
    'Q5DefinedIn',
)


class Q2Occupied(PropertyMixin):
    """'Q2 occupied (is occupied by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q2

    Domain:
        E18 Physical Thing
    Range:
        SP1 Phenomenal Spacetime Volume
    SubProperty Of:
        E18 Physical Thing. P196 defines (is defined by): E92 Spacetime Volume
    SuperProperty Of:
        -
    Quantification:
        one to one, necessary (1,1:0,1)

    Scope Note:
        This property describes the 4 dimensional point sets (volumes) in spacetime
        that the trajectory of an instance of E18 Physical Thing occupies in the
        course of its existence. We include in the occupied space the space filled
        by the matter of the physical thing and all inner spaces not accessible in
        regular function.

    Properties:
        -
    Examples:
        - H.M.S. Victory (E22) occupied a spatio-temporal trajectory (SP1) from
          its launching (E12) to its actual location (E9)

    In First Order Logic:
        Q2(x,y) ⊃ E18(x)
        Q2(x,y) ⊃ SP1(y)
        Q2(x,y) ⇔ P196(x,y)

    Note:
        Defined as a standalone mixin — domain E18 is a core CRM entity, so this
        mixin is NOT applied to E18PhysicalThing (would create circular dependency).
        Consumers may subclass E18PhysicalThing with this mixin if needed.

    """

    q2_occupied: List[SP1PhenomenalSpacetimeVolume] = Field(
        default=None,
        min_length=1,
        description='Q2 occupied (is occupied by)',
    )


# ******************************************************************************************************************* #


class Q3HasTemporalProjection(PropertyMixin):
    """'Q3 has temporal projection (is temporal projection of)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q3

    Domain:
        SP1 Phenomenal Spacetime Volume
    Range:
        SP13 Phenomenal Time-Span
    SubProperty Of:
        E92 Spacetime Volume. P160 has temporal projection (is temporal projection of):
        E52 Time-Span
    SuperProperty Of:
        -
    Quantification:
        one to one, necessary, dependent (1,1:1,1)

    Scope Note:
        This property describes the temporal projection of an instance of SP1
        Phenomenal Spacetime Volume. This property can be extended in a future
        model to a ternary (3-ary) relationship describing the temporal projection
        under a spatial constraint.

    Properties:
        -
    Examples:
        - The spatio-temporal trajectory (SP1) of the H.M.S. Victory (E22) has
          temporal projection the phenomenal temporal extent from its launching
          to its actual location (SP13)

    In First Order Logic:
        Q3(x,y) ⊃ SP1(x)
        Q3(x,y) ⊃ SP13(y)

    """

    q3_has_temporal_projection: SP13PhenomenalTimeSpan = Field(
        description='Q3 has temporal projection (is temporal projection of)',
    )


# ******************************************************************************************************************* #


class Q4HasSpatialProjection(PropertyMixin):
    """'Q4 has spatial projection (is spatial projection of)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q4

    Domain:
        SP1 Phenomenal Spacetime Volume
    Range:
        SP2 Phenomenal Place
    SubProperty Of:
        E92 Spacetime Volume. P161 has spatial projection (is spatial projection of):
        E53 Place
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property describes the spatial projection of an instance of SP1
        Phenomenal Spacetime Volume on an instance of SP2 Phenomenal Place. Even
        though the projection of a spacetime volume to one instance of SP3 Reference
        Space is unique, each reference space gives rise to another projection. The
        projections overlap at the time of the spacetime volume, the respective
        instances of SP2 Phenomenal Place may later drift apart, or earlier be yet
        apart. This property can be extended in a future model to a ternary (3-ary)
        relationship describing the spatial projection under a temporal constraint.

    Properties:
        -
    Examples:
        - The spatio-temporal trajectory (SP1) of the H.M.S. Victory (E22) has
          spatial projection the phenomenal spatial extent from its building to
          its actual location (SP2)

    In First Order Logic:
        Q4(x,y) ⊃ SP1(x)
        Q4(x,y) ⊃ SP2(y)

    """

    q4_has_spatial_projection: List[SP2PhenomenalPlace] = Field(
        default=None,
        min_length=1,
        description='Q4 has spatial projection (is spatial projection of)',
    )


# ******************************************************************************************************************* #


class Q5DefinedIn(PropertyMixin):
    """'Q5 defined in (is reference space for)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q5

    Domain:
        E53 Place
    Range:
        SP3 Reference Space
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of E53 Place with the instance of
        SP3 Reference Space it is defined in.

    Properties:
        -
    Examples:
        - The location of Lord Nelson when he died (E53) defined in the Reference
          Space (SP3) inside and around the H.M.S. Victory (E22)

    In First Order Logic:
        Q5(x,y) ⊃ E53(x)
        Q5(x,y) ⊃ SP3(y)

    Note:
        Defined as a standalone mixin — domain E53 is a core CRM entity, so this
        mixin is NOT applied to E53Place (would create circular dependency).
        Consumers may subclass E53Place with this mixin if needed.

    """

    q5_defined_in: SP3ReferenceSpace = Field(
        description='Q5 defined in (is reference space for)',
    )
