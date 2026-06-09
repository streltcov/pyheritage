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

from typing import List, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (  # noqa: F401 – used in docstrings
        E18PhysicalThing,
        E26PhysicalFeature,
        E53Place,
    )
    from pyheritage.cidoc.crmgeo.entities import (  # noqa: F401 – SP5 used in docstrings only
        SP1PhenomenalSpacetimeVolume,
        SP2PhenomenalPlace,
        SP3ReferenceSpace,
        SP4SpatialCoordinateReferenceSystem,
        SP5GeometricPlaceExpression,
        SP6DeclarativePlace,
        SP13PhenomenalTimeSpan,
    )


__all__ = (
    'Q2Occupied',
    'Q3HasTemporalProjection',
    'Q4HasSpatialProjection',
    'Q5DefinedIn',
    'Q6IsAtRestRelativeTo',
    'Q7Describes',
    'Q8IsFixedOn',
    'Q9IsExpressedInTermsOf',
    'Q10DefinesPlace',
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


# ******************************************************************************************************************* #


class Q6IsAtRestRelativeTo(PropertyMixin):
    """'Q6 is at rest relative to (is reference space for)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q6

    Domain:
        SP3 Reference Space
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of SP3 Reference Space with an instance
        of E18 Physical Thing that is at rest in it, i.e., no part moves relative to
        the reference space. The reference space is valid as long as the reference
        object exists. The fact that some things are at rest in a reference space is
        essential for the determination of relative positions to earth-bound features.

    Properties:
        -
    Examples:
        - The Space inside and around H.M.S. Victory (SP3) is at rest relative to
          H.M.S. Victory (E22)

    In First Order Logic:
        Q6(x,y) ⊃ SP3(x)
        Q6(x,y) ⊃ E18(y)

    """

    q6_is_at_rest_relative_to: List[E18PhysicalThing] = Field(
        default=None,
        description='Q6 is at rest relative to (is reference space for)',
    )


# ******************************************************************************************************************* #


class Q7Describes(PropertyMixin):
    """'Q7 describes (is described by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q7

    Domain:
        SP4 Spatial Coordinate Reference System
    Range:
        SP3 Reference Space
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary, dependent (1,1:0,n)

    Scope Note:
        This property associates an instance of SP4 Spatial Coordinate Reference
        System with an instance of SP3 Reference Space it describes by relating a
        Coordinate System to fixed real world features of that reference space.

    Properties:
        -
    Examples:
        - The Coordinate Reference System WGS 84 (SP4) describes the earth-bound
          reference space (SP3)

    In First Order Logic:
        Q7(x,y) ⊃ SP4(x)
        Q7(x,y) ⊃ SP3(y)

    """

    q7_describes: SP3ReferenceSpace = Field(
        description='Q7 describes (is described by)',
    )


# ******************************************************************************************************************* #


class Q8IsFixedOn(PropertyMixin):
    """'Q8 is fixed on (fixes)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q8

    Domain:
        SP4 Spatial Coordinate Reference System
    Range:
        E26 Physical Feature
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of SP4 Spatial Coordinate Reference
        System with the instance of E26 Physical Feature on which the origin of
        its coordinate system is, or was, fixed with respect to the SP3 Reference
        Space it describes.

    Properties:
        -
    Examples:
        - The Coordinate Reference System (SP4) of the Space inside and around
          H.M.S. Victory (SP3) is fixed on the middle mast of the H.M.S. Victory
          (E26)

    In First Order Logic:
        Q8(x,y) ⊃ SP4(x)
        Q8(x,y) ⊃ E26(y)

    """

    q8_is_fixed_on: Optional[E26PhysicalFeature] = Field(
        default=None,
        description='Q8 is fixed on (fixes)',
    )


# ******************************************************************************************************************* #


class Q9IsExpressedInTermsOf(PropertyMixin):
    """'Q9 is expressed in terms of' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q9

    Domain:
        SP5 Geometric Place Expression
    Range:
        SP4 Spatial Coordinate Reference System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary, dependent (1,1:0,n)

    Scope Note:
        This property associates an instance of SP5 Geometric Place Expression
        with the instance of SP4 Spatial Coordinate Reference System in terms of
        which its coordinates are expressed.

    Properties:
        -
    Examples:
        - The geometric place expression "45.67, 88.56" (SP5) is expressed in terms
          of WGS 84 (SP4)

    In First Order Logic:
        Q9(x,y) ⊃ SP5(x)
        Q9(x,y) ⊃ SP4(y)

    """

    q9_is_expressed_in_terms_of: SP4SpatialCoordinateReferenceSystem = Field(
        description='Q9 is expressed in terms of',
    )


# ******************************************************************************************************************* #


class Q10DefinesPlace(PropertyMixin):
    """'Q10 defines place (is defined by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v1.2.html#Q10

    Domain:
        SP5 Geometric Place Expression
    Range:
        SP6 Declarative Place
    SubProperty Of:
        E53 Place. P168 place is defined by (defines place): E94 Space Primitive
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of SP5 Geometric Place Expression
        with an instance of SP6 Declarative Place that it defines. The same
        geometric place expression may define several places over time, if the
        reference features related to the SP4 Spatial Coordinate Reference System
        move with respect to the SP3 Reference Space, e.g., due to continental
        drift. However, during normal documentation practice and for the time
        span relevant to the documented context, this effect can be neglected.

    Properties:
        -
    Examples:
        - The GML point with coordinates 45.67, 88.56 in WGS84 (SP5) defines
          the declarative place of the Orinoco river in the map of Diego Ribeiro
          (SP6)

    In First Order Logic:
        Q10(x,y) ⊃ SP5(x)
        Q10(x,y) ⊃ SP6(y)
        Q10(x,y) ⇒ P168(x,y)

    """

    q10_defines_place: List[SP6DeclarativePlace] = Field(
        default=None,
        description='Q10 defines place (is defined by)',
    )
