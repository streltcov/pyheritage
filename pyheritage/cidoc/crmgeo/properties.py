# -*- coding: utf-8 -*-

"""CRMgeo property models;

(Mixin classes for entity models);

CRMgeo v2.0 (2026)

------------------------------------------------
Properties
------------------------------------------------
Q2  occupied                             E18 -> SP1
Q3  has temporal projection              SP1 -> SP13
Q4  has spatial projection               SP1 -> SP2
Q5  defined in                           E53 -> SP3
Q6  is at rest in relation to            SP3 -> E18
Q7  describes                            SP4 -> SP3
Q8  is fixed on                          SP4 -> E26
Q9  place is expressed in terms of       SP6 -> SP4
Q10 place is defined by                  SP6 -> E94
Q11 approximates place                   SP6 -> SP2
Q12 approximates spacetime               SP7 -> SP1
Q13 approximates time                    SP10 -> SP13
Q14 defines time                         E61 -> SP10
Q15 time is expressed in terms of        SP10 -> SP11
Q16 defines spacetime volume             E95 -> SP7
Q17 time is expressed in terms of        SP7 -> SP11
Q18 place is expressed in terms of       SP7 -> SP4
Q19 has reference event                  SP11 -> E5

"""


from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (  # noqa: F401 – used in docstrings
        E5Event,
        E18PhysicalThing,
        E26PhysicalFeature,
        E53Place,
        E61TimePrimitive,
        E94SpacePrimitive,
        E95SpaceTimePrimitive,
    )
    from pyheritage.cidoc.crmgeo.entities import (  # noqa: F401 – used in docstrings
        SP1PhenomenalSpacetimeVolume,
        SP2PhenomenalPlace,
        SP3ReferenceSpace,
        SP4SpatialCoordinateReferenceSystem,
        SP6DeclarativePlace,
        SP7DeclarativeSpacetimeVolume,
        SP10DeclarativeTimeSpan,
        SP11TemporalReferenceSystem,
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
    'Q9PlaceIsExpressedInTermsOf',
    'Q10PlaceIsDefinedBy',
    'Q11ApproximatesPlace',
    'Q12ApproximatesSpacetime',
    'Q13ApproximatesTime',
    'Q14DefinesTime',
    'Q15TimeIsExpressedInTermsOf',
    'Q16DefinesSpacetimeVolume',
    'Q17TimeIsExpressedInTermsOf',
    'Q18PlaceIsExpressedInTermsOf',
    'Q19HasReferenceEvent',
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


class Q9PlaceIsExpressedInTermsOf(PropertyMixin):
    """'Q9 place is expressed in terms of (expresses place)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q9

    Domain:
        SP6 Declarative Place
    Range:
        SP4 Spatial Coordinate Reference System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property defines the coordinate reference system in terms of which
        a Space Primitive is formulated.

    Properties:
        -
    Examples:
        - The declarative place in terms of WGS 84 (SP4)

    In First Order Logic:
        Q9(x,y) ⊃ SP6(x)
        Q9(x,y) ⊃ SP4(y)

    """

    q9_place_is_expressed_in_terms_of: SP4SpatialCoordinateReferenceSystem = Field(
        description='Q9 place is expressed in terms of',
    )


# ******************************************************************************************************************* #


class Q10PlaceIsDefinedBy(PropertyMixin):
    """'Q10 place is defined by (defines place)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q10

    Domain:
        SP6 Declarative Place
    Range:
        E94 Space Primitive
    SubProperty Of:
        E53 Place. P168 place is defined by (defines place): E94 Space Primitive
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property associates an instance of SP6 Declarative Place with the
        instance of E94 Space Primitive that defines it. Syntactic variants or
        use of different scripts may result in multiple instances of E94 Space
        Primitive defining exactly the same place. Transformations between
        different reference systems always result in new definitions of places
        approximating each other and not in alternative definitions.

    Properties:
        -
    Examples:
        - The centroid from https://sws.geonames.org/735927 (SP6) place is
          defined by 40°31'17.9"N 21°15'48.3"E (E94)

    In First Order Logic:
        Q10(x,y) ⊃ SP6(x)
        Q10(x,y) ⊃ E94(y)
        Q10(x,y) ⇔ P168(x,y)

    """

    q10_place_is_defined_by: List[E94SpacePrimitive] = Field(
        default=None,
        description='Q10 place is defined by (defines place)',
    )


# ******************************************************************************************************************* #


class Q11ApproximatesPlace(PropertyMixin):
    """'Q11 approximates place (place is approximated by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q11

    Domain:
        SP6 Declarative Place
    Range:
        SP2 Phenomenal Place
    SubProperty Of:
        E53 Place. P189 approximates (is approximated by): E53 Place
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property approximates a SP2 Phenomenal Place which is defined in
        the same reference space. The property does not state the quality or
        accuracy of the approximation, but states the intention to approximate
        the place.

    Properties:
        -
    Examples:
        - The declarative place with point shape which is defined in terms of
          coordinates taken from https://sws.geonames.org/735927 (SP6)
          approximates place Kastoria, Greece (SP2)

    In First Order Logic:
        Q11(x,y) ⊃ SP6(x)
        Q11(x,y) ⊃ SP2(y)

    """

    q11_approximates_place: List[SP2PhenomenalPlace] = Field(
        default=None,
        description='Q11 approximates place (place is approximated by)',
    )


# ******************************************************************************************************************* #


class Q12ApproximatesSpacetime(PropertyMixin):
    """'Q12 approximates spacetime (spacetime is approximated by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q12

    Domain:
        SP7 Declarative Spacetime Volume
    Range:
        SP1 Phenomenal Spacetime Volume
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property approximates an E53 Place which is defined in the same
        reference space. The property does not state the quality or accuracy of
        the approximation, but states the intention to approximate the place.

    Properties:
        -
    Examples:
        - The declared maximum extent of the Byzantine Empire (SP7) approximates
          spacetime the phenomenal maximum extent of the Byzantine Empire (SP1)

    In First Order Logic:
        Q12(x,y) ⊃ SP7(x)
        Q12(x,y) ⊃ SP1(y)

    """

    q12_approximates_spacetime: List[SP1PhenomenalSpacetimeVolume] = Field(
        default=None,
        description='Q12 approximates spacetime (spacetime is approximated by)',
    )


# ******************************************************************************************************************* #


class Q13ApproximatesTime(PropertyMixin):
    """'Q13 approximates time (time is approximated by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q13

    Domain:
        SP10 Declarative Time-Span
    Range:
        SP13 Phenomenal Time-Span
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property approximates a E52 Time-Span. The property does not state
        the quality or accuracy of the approximation, but states the intention
        to approximate the time span.

    Properties:
        -
    Examples:
        - September 1939 - September 1945 (SP10) approximates time the
          phenomenal duration of the Second World War (SP13)

    In First Order Logic:
        Q13(x,y) ⊃ SP10(x)
        Q13(x,y) ⊃ SP13(y)

    """

    q13_approximates_time: List[SP13PhenomenalTimeSpan] = Field(
        default=None,
        description='Q13 approximates time (time is approximated by)',
    )


# ******************************************************************************************************************* #


class Q14DefinesTime(PropertyMixin):
    """'Q14 defines time (time is defined by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q14

    Domain:
        E61 Time Primitive
    Range:
        SP10 Declarative Time-Span
    SubProperty Of:
        E61 Time Primitive. P170 defines time (time is defined by): E52 Time-Span
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of E61 Time Primitive with the
        instance of SP10 Declarative Time Span it defines. Syntactic variants
        or use of different scripts may result in multiple instances of E61
        Time Primitive defining exactly the same time span. Transformations
        between different temporal reference systems in general result in new
        definitions of time spans approximating each other.

    Properties:
        -
    Examples:
        - "1800/1/1 0:00:00 - 1899/31/12 23:59:59" (E61) defines time the
          19th century (SP10)

    In First Order Logic:
        Q14(x,y) ⊃ E61(x)
        Q14(x,y) ⊃ SP10(y)
        Q14(x,y) ⇔ P170(x,y)

    Note:
        Defined as a standalone mixin — domain E61 is a core CRM entity, so
        this mixin is NOT applied to E61TimePrimitive (would create circular
        dependency). Consumers may subclass E61TimePrimitive with this mixin
        if needed.

    """

    q14_defines_time: Optional[SP10DeclarativeTimeSpan] = Field(
        default=None,
        description='Q14 defines time (time is defined by)',
    )


# ******************************************************************************************************************* #


class Q15TimeIsExpressedInTermsOf(PropertyMixin):
    """'Q15 time is expressed in terms of (expresses time)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q15

    Domain:
        SP10 Declarative Time-Span
    Range:
        SP11 Temporal Reference System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property defines the temporal reference system in terms of which
        a SP10 Declarative Time-Span is formulated.

    Properties:
        -
    Examples:
        - The declarative time span (SP10) defined by "1800/1/1 0:00:00 -
          1899/31/12 23:59:59" (E61) time is expressed in terms of the
          Gregorian Calendar (SP11)

    In First Order Logic:
        Q15(x,y) ⊃ SP10(x)
        Q15(x,y) ⊃ SP11(y)

    """

    q15_time_is_expressed_in_terms_of: List[SP11TemporalReferenceSystem] = Field(
        default=None,
        description='Q15 time is expressed in terms of (expresses time)',
    )


# ******************************************************************************************************************* #


class Q16DefinesSpacetimeVolume(PropertyMixin):
    """'Q16 defines spacetime volume (spacetime volume is defined by)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q16

    Domain:
        E95 Spacetime Primitive
    Range:
        SP7 Declarative Spacetime Volume
    SubProperty Of:
        E95 Spacetime Primitive. P169 defines spacetime volume
        (spacetime volume is defined by): E92 Spacetime Volume
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of E95 Spacetime Primitive with the
        instance of SP7 Declarative Spacetime Volume it defines. Syntactic
        variants or use of different scripts may result in multiple instances of
        E95 Spacetime Primitive defining exactly the same SP7 Declarative
        Spacetime Volume. Transformations between different temporal or spatial
        reference systems in general result in new definitions of Spacetime
        Volumes approximating each other.

    Properties:
        -
    Examples:
        - The KML Placemark defining the Byzantine Empire maximum extent (E95)
          defines spacetime volume the declared maximum extent of the Byzantine
          Empire between 555 and 565 (SP7)

    In First Order Logic:
        Q16(x,y) ⊃ E95(x)
        Q16(x,y) ⊃ SP7(y)
        Q16(x,y) ⇔ P169(x,y)

    Note:
        Defined as a standalone mixin — domain E95 is a core CRM entity, so
        this mixin is NOT applied to E95SpaceTimePrimitive (would create
        circular dependency). Consumers may subclass E95SpaceTimePrimitive
        with this mixin if needed.

    """

    q16_defines_spacetime_volume: SP7DeclarativeSpacetimeVolume = Field(
        description='Q16 defines spacetime volume (spacetime volume is defined by)',
    )


# ******************************************************************************************************************* #


class Q17TimeIsExpressedInTermsOf(PropertyMixin):
    """'Q17 time is expressed in terms of (expresses time)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q17

    Domain:
        SP7 Declarative Spacetime Volume
    Range:
        SP11 Temporal Reference System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property defines the temporal reference system in terms of which
        a SP7 Declarative Spacetime Volume is formulated.

    Properties:
        -
    Examples:
        - The declared maximum extent of the Byzantine Empire (SP7) time is
          expressed in terms of the proleptic Gregorian Calendar (SP11)

    In First Order Logic:
        Q17(x,y) ⊃ SP7(x)
        Q17(x,y) ⊃ SP11(y)

    """

    q17_time_is_expressed_in_terms_of: List[SP11TemporalReferenceSystem] = Field(
        default=None,
        description='Q17 time is expressed in terms of (expresses time)',
    )


# ******************************************************************************************************************* #


class Q18PlaceIsExpressedInTermsOf(PropertyMixin):
    """'Q18 place is expressed in terms of (expresses place)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q18

    Domain:
        SP7 Declarative Spacetime Volume
    Range:
        SP4 Spatial Coordinate Reference System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property defines the spatial coordinate reference system in terms
        of which a SP7 Declarative Spacetime Volume is formulated.

    Properties:
        -
    Examples:
        - The declared maximum extent of the Byzantine Empire (SP7) place is
          expressed in terms of Longitude-Latitude in WGS84 (SP4)

    In First Order Logic:
        Q18(x,y) ⊃ SP7(x)
        Q18(x,y) ⊃ SP4(y)

    """

    q18_place_is_expressed_in_terms_of: List[SP4SpatialCoordinateReferenceSystem] = Field(
        default=None,
        description='Q18 place is expressed in terms of (expresses place)',
    )


# ******************************************************************************************************************* #


class Q19HasReferenceEvent(PropertyMixin):
    """'Q19 has reference event (is reference event of)' CRMgeo property;

    https://cidoc-crm.org/extensions/crmgeo/html/CRMgeo_v2.0.html#Q19

    Domain:
        SP11 Temporal Reference System
    Range:
        E5 Event
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property defines the reference event for a SP11 Temporal Reference
        System. The origin for a Temporal Reference System is fixed on a
        reference event.

    Properties:
        -
    Examples:
        - The Gregorian Calendar (SP11) has reference event Birth of Christ (E67)

    In First Order Logic:
        Q19(x,y) ⊃ SP11(x)
        Q19(x,y) ⊃ E5(y)

    """

    q19_has_reference_event: E5Event = Field(
        description='Q19 has reference event (is reference event of)',
    )
