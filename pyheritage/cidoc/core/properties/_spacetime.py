# -*- coding: utf-8 -*-

"""Spatiotemporal framework properties;

(Mixin classes for entity models);

CIDOC-CRM v7.0

---------------------------------------------
Properties
---------------------------------------------
P79  beginning is qualified by     E52 -> E62
P80  end is qualified by           E52 -> E62
P81  ongoing throughout            E52 -> E61
P82  at some time within           E52 -> E61
P86  falls within                  E52 -> E52
P89  falls within                  E53 -> E53
P90  has value                     E54 -> E60
P91  has unit                      E54 -> E58
P121 overlaps with                 E53 -> E53
P122 borders with                  E53 -> E53
P132 spatiotemporally overlaps     E92 -> E92
P133 is spatiotemporally separated E92 -> E92
P157 is at rest relative to        E53 -> E18
P160 has temporal projection       E92 -> E52
P161 has spatial projection        E92 -> E53
P164 during                        E93 -> E52
P166 was a presence of             E93 -> E92
P167 at                            E93 -> E53
P168 place is defined by           E53 -> E94
P169 defines spacetime volume      E95 -> E92
P170 defines time                  E61 -> E52
P171 at some place within          E53 -> E94
P172 contains                      E53 -> E53
P180 has currency                  E97 -> E98
P181 has amount                    E97 -> E60
P189 approximates                  E53 -> E53
P191 had duration                  E52 -> E54
P195 was a presence of             E93 -> E18
P197 covered parts of              E93 -> E53

"""


from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (
        CoercedNumber,
        CoercedSpace,
        CoercedString,
        CoercedTime,
        E18PhysicalThing,
        E52TimeSpan,
        E53Place,
        E54Dimension,
        E58MeasurementUnit,
        E92SpaceTimeVolume,
        E98Currency,
    )


__all__ = ('P79BeginningIsQualifiedBy', 'P80EndIsQualifiedBy', 'P81OngoingThroughout', 'P82AtSomeTimeWithin',
           'P86FallsWithin', 'P89FallsWithin', 'P90HasValue', 'P91HasUnit', 'P121OverlapsWith', 'P122BordersWith',
           'P132SpatiotemporallyOverlaps', 'P133IsSpatiotemporallySeparated', 'P157IsAtRestRelativeTo',
           'P160HasTemporalProjection', 'P161HasSpatialProjection', 'P164During', 'P166WasAPresenceOf', 'P167At',
           'P168PlaceIsDefinedBy', 'P169DefinesSpacetimeVolume', 'P170DefinesTime', 'P171AtSomePlaceWithin',
           'P172Contains', 'P180HasCurrency', 'P181HasAmount', 'P189Approximates', 'P191HadDuration',
           'P195WasAPresenceOf', 'P197CoveredPartsOf', )


class P79BeginningIsQualifiedBy(PropertyMixin):
    """'P79 beginning is qualified by' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P79

    Domain:
        E52 Time-Span
    Range:
        E62 String
    SubProperty Of:
        E1 CRM Entity. P3 has note: E62 String
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of E52 Time-Span with a note detailing the scholarly or scientific
        opinions and justifications about the certainty, precision, sources etc of its beginning. Such notes may also
        be used to elaborate arguments about constraints or to give explanations of alternatives;

    Properties:
        -
    Examples:
        - the time-span of the Holocene (E52) beginning is qualified by “The formal definition and dating of
          the GSSP (GlobalStratotype Section and Point) for the base of theHolocene using
          the Greenland NGRIP ice core, and selected auxiliary records” (Walker et al 2009) (E62)
    In First Order Logic:
        P79 (x,y) ⊃ E52 (x)
        P79 (x,y) ⊃ E62(y)
        P79(x,y) ⊃ P3(x,y)

    """

    p79_beginning_is_qualified_by: Optional[CoercedString] = Field(
        default=None,
        description='P79 beginning is qualified by'
    )


# ******************************************************************************************************************* #


class P80EndIsQualifiedBy(PropertyMixin):
    """'P80 end is qualified by' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P80

    Domain:
        E52 Time-Span
    Range:
        E62 String
    SubProperty Of:
        E1 CRM Entity. P3 has note: E62 String
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of E52 Time-Span with a note detailing the scholarly or scientific
        opinions and justifications about the certainty, precision, sources etc of its end. Such notes may also
        be used to elaborate arguments about constraints or to give explanations of alternatives;

    Properties:
        -
    Examples:
        - the time-span of the Holocene (E52) end is qualified by “still ongoing” (E62)
    In First Order Logic:
        P80(x,y) ⊃ E52(x)
        P80(x,y) ⊃ E62(y)
        P80(x,y) ⊃ P3(x,y)

    """

    p80_end_is_qualified_by: Optional[CoercedString] = Field(default=None, description='P80 end is qualified by')


# ******************************************************************************************************************* #


class P81OngoingThroughout(PropertyMixin):
    """'P81 ongoing throughout';

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P81

    Domain:
        E52 Time-Span
    Range:
        E61 Time Primitive
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of E52 Time-Span with an instance of E61 Time Primitive specifying
        a minimum period of time covered by it;

        Since Time-Spans may not have precisely known temporal extents, there may be multiple minimum periods
        of . Union of;

    Properties:
        -
    Examples:
        - the time-span of the development of the CIDOC CRM (E52) ongoing throughout 1996-2002 (E61)
    In First Order Logic:
        P81 (x,y) ⊃ E52(x)
        P81 (x,y) ⊃ E61(y)

    """

    p81_ongoing_throughout: CoercedTime = Field(default=None, description='P81 ongoing throughout')


# ******************************************************************************************************************* #


class P82AtSomeTimeWithin(PropertyMixin):
    """'P82 at some time within' CRM property;

    Domain:
        E52 Time-Span
    Range:
        E61 Time Primitive
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property describes the maximum period of time within which an E52 Time-Span falls;

        Since Time-Spans may not have precisely known temporal extents, the CIDOC CRM supports statements about
        the minimum and maximum temporal extents of Time-Spans. This property allows a Time-Span’s maximum temporal
        extent (i.e. its outer boundary) to be assigned an E61 Time Primitive value. Time Primitives are treated
        by the CIDOC CRM as application or system specific date intervals, and are not further analysed;

    Properties:
        -
    Examples:
        - the time-span of the development of the CIDOC CRM (E52) at some time within 1992-infinity (E61)
    In First Order Logic:
        - P82 (x,y) ⊃ E52(x)
        - P82 (x,y) ⊃ E61(y)

    """

    p82_at_some_time_within: CoercedTime = Field(default=None, description='P82 at some time within')


# ******************************************************************************************************************* #


class P86FallsWithin(PropertyMixin):
    """'P86 falls within (contains)' CRM property;

    Domain:
        - E52 Time-Span
    Range:
        - E52 Time-Span
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the inclusion relationship between two instances of E52 Time-Span;

        This property supports the notion that the temporal extent of an instance of E52 Time-Span falls within the
        temporal extent of another instance of E52 Time-Span. It addresses temporal containment only, and no
        contextual link between the two instances of E52 Time-Span is implied;

        This property is transitive;

    Properties:
        -
    Examples:
        - the time-span of the Apollo 11 moon mission (E52) falls within the time-span of the reign of
          Queen Elizabeth II (E52)
    In First Order Logic:
        - P86(x,y) ⊃ E52(x)
        - P86(x,y) ⊃ E52(y)

    """

    p86_falls_within: Optional[List[E52TimeSpan]] = Field(default=None, description='P86 falls within')


# ******************************************************************************************************************* #


class P89FallsWithin(PropertyMixin):
    """'P89 falls within (contains)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P89

    Domain:
        E53 Place
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of E53 Place that falls wholly within the extent of another instance
        of E53 Place;

        It addresses spatial containment only, and does not imply any relationship between things or phenomena
        occupying these places;

        This property is transitive;

    Properties:
        -
    Examples:
        - the area covered by the World Heritage Site of Stonehenge (E53) falls within the area
          of Salisbury Plain (E53)
    In First Order Logic:
        P89(x,y) ⊃ E53(x)
        P89(x,y) ⊃ E53(y)

    """

    p89_falls_within: Optional[List[E53Place]] = Field(default=None, description='P89 falls within (contains)')


# ******************************************************************************************************************* #


class P90HasValue(PropertyMixin):
    """'P90 has value' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P90

    Domain:
        - E54 Dimension
    Range:
        - E60 Number
    SubProperty Of:
        -
    SuperProperty Of:
        - E97 Monetary Amount. P181 has amount: E60 Number
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property allows an instance of E54 Dimension to be approximated by an instance of E60 Number primitive;

    Properties:
        -
    Examples:
        - height of silver cup 232 (E54) has value 226 (E60)
    In First Order Logic:
        - P90(x,y) ⊃ E54(x)
        - P90(x,y) ⊃ E60(y)

    """

    p90_has_value: CoercedNumber = Field(default=None, description='P90 has value')


# ******************************************************************************************************************* #


class P91HasUnit(PropertyMixin):
    """'P91 has unit (is unit of) CRM property';

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P91

    Domain:
        - E54 Dimension
    Range:
        - E58 Measurement Unit
    SubProperty Of:
        -
    SuperProperty Of:
        - E97 Monetary Amount. P180 has currency (was currency of): E98 Currency
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property shows the type of unit an instance of E54 Dimension was expressed in;

    Properties:
        -
    Examples:
        - height of silver cup 232 (E54) has unit mm (E58)
    In First Order Logic:
        - P91(x,y) ⊃ E54(x)
        - P91(x,y) ⊃ E58(y)

    """

    p91_has_unit: E58MeasurementUnit = Field(default=None, description='P91 has unit')


# ******************************************************************************************************************* #


class P121OverlapsWith(PropertyMixin):
    """'P121 overlaps with' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P121

    Domain:
        E53 Place
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This symmetric property associates an instance of E53 Place with another instance of E53 Place
        geometrically overlapping it;

        It does not specify anything about the shared area. This property is purely spatial, in contrast to
        the temporal overlaps described by pxxx, pxxy or pxxz, and and, spatio temporal overlaps described
        by p132 spatiotemporally overlaps with;

    Properties:
        -
    Examples:
        - the territory of the United States (E53) overlaps with the Arctic (E53)
        - The maximal extent of the Greek Kingdom (E53) overlaps with the maximal extent of the Ottoman Empire(E53)
    In First Order Logic:
        P121(x,y) ⊃ E53(x)
        P121(x,y) ⊃ E53(y)
        P121(x,y) ⊃ P121(y,x)

    """

    p121_overlaps_with: Optional[List[E53Place]] = Field(default=None, description='P121 overlaps with')


# ******************************************************************************************************************* #


class P122BordersWith(PropertyMixin):
    """'P122 borders with' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#122

    Domain:
        E53 Place
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This symmetric property associates an instance of E53 Place with another instance of E53 Place which shares
        a part of its borders;

        This property is purely spatial, in contrast to time properties, which are purely temporal;

        This property is not transitive;

    Properties:
        -
    Examples:
        - Scotland (E53) borders with England (E53)
    In First Order Logic:
        P122(x,y) ⊃ E53(x)
        P122(x,y) ⊃ E53(y)
        P122(x,y) ⊃ P122(y,x)

    """

    p122_borders_with: Optional[List[E53Place]] = Field(default=None, description='P122 borders with')


# ******************************************************************************************************************* #


class P132SpatiotemporallyOverlaps(PropertyMixin):
    """'P132 spatiotemporally overlaps with' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#132

    Domain:
        E92 Spacetime Volume
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        -
    SuperProperty Of:
        E4 Period. P9 consists of (forms part of): E4 Period
        E92 Spacetime Volume. P10 falls within (contains): E92 Spacetime Volume
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This symmetric property associates two instances of E92 Spacetime Volume that have some of their extents
        in common. If only the fuzzy boundaries of the instances of E92 Spacetime Volume overlap, this property cannot
        be determined from observation alone and therefore should not be applied. However, there may be other forms
        of justification that the two instances of E92 Spacetime Volume must have some of their extents in common
        regardless of where and when precisely;

        If this property holds for two instances of E92 Spacetime Volume then it cannot be the case that P133 also
        holds for the same two instances. Furthermore, there are cases where neither P132 nor P133 holds between
        two instances of E92 Spacetime Volume. This would occur where only an overlap of the fuzzy boundaries of
        the two instances of E92 Spacetime Volume occurs and no other evidence is available;

    Properties:
        -
    Examples:
        - the “Urnfield” period (E4) spatiotemporally overlaps with the “Hallstatt” period (E4)
    In First Order Logic:
        P132(x,y) ⊃ E92(x)
        P132(x,y) ⊃ E92(y)
        P132(x,y) ⊃ P132(y,x)
        P132(x,y) ⊃ ¬P133(x,y)

    """

    p132_spatiotemporally_overlaps: Optional[List[E92SpaceTimeVolume]] = Field(
        default=None,
        description='P132 spatiotemporally overlaps with'
    )


# ******************************************************************************************************************* #


class P133IsSpatiotemporallySeparated(PropertyMixin):
    """'P133 is spatiotemporally separated from' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#133

    Domain:
        E92 Spacetime Volume
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This symmetric property associates two instances of E92 Spacetime Volume that have no extents in common. If
        only the fuzzy boundaries of the instances of E92 Spacetime Volume overlap, this property cannot be determined
        from observation alone and therefore should not be applied. However, there may be other forms of justification
        that the two instances of E92 Spacetime Volume must not have any of their extents in common regardless of
        where and when precisely;

        If this property holds for two instances of E92 Spacetime Volume then it cannot be the case that
        P132 spatiotemporally overlaps with also holds for the same two instances. Furthermore, there are cases
        where neither P132 nor P133 holds between two instances of E92 Spacetime Volume. This would occur where only
        an overlap of the fuzzy boundaries of the two instances of E92 Spacetime Volume occurs and no other evidence
        is available;

        This property is not transitive;

    Properties:
        -
    Examples:
        - the “Hallstatt” period (E4) is spatiotemporally separated from the “La Tène” era (E4)
        - Kingdom of Greece (1831-1924) (E92) is spatiotemporally separated from Ottoman Empire (1299-1922) (E92)
        - The path of the army of Alexander (335-323 B.C.) (E92) is spatiotemporally separated from
          the Mauryan Empire (E92)
    In First Order Logic:
        P133(x,y) ⊃ E92(x)
        P133(x,y) ⊃ E92(y)
        P133(x,y) ⊃ P133(y,x)
        P133(x,y) ⊃ ¬P132(x,y)

    """

    p133_is_spatiotemporally_separated: Optional[List[E92SpaceTimeVolume]] = Field(
        default=None,
        description='P133 is spatiotemporally separated from'
    )


# ******************************************************************************************************************* #


class P157IsAtRestRelativeTo(PropertyMixin):
    """'P157 is at rest relative to (provides reference space for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#157

    Domain:
        E53 Place
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        E53 Place. P59i is located on or within (has section): E18 Physical Thing
        E53 Place. P156i is occupied by (occupies): E18 Physical Thing
    Quantification:
        many to many, necessary, dependent (1,n:0,n)

    Scope Note:
        This property associates an instance of E53 Place with the instance of E18 Physical Thing that determines
        a reference space for this instance of E53 Place by being at rest with respect to this reference space. The
        relative stability of form of an instance of E18 Physical Thing defines its default reference space. The
        reference space is not spatially limited to the referred thing. For example, a ship determines a reference
        space in terms of which other ships in its neighbourhood may be described. Larger constellations of matter,
        such as continental plates, may comprise many physical features that are at rest with them and define
        the same reference space;

    Properties:
        -
    Examples:
        - The spatial extent of the municipality of Athens in 2014 (E53) is at rest relative to The Royal Observatory
          in Greenwich (E25)
        - The place where Lord Nelson died on H.M.S. Victory (E53) is at rest relative to H.M.S. Victory (E22)
    In First Order Logic:
        P157(x,y) ⊃ E53(x)
        P157(x,y) ⊃ E18(y)

    """

    p157_is_at_rest_relative_to: List[E18PhysicalThing] = Field(
        description='P157 is at rest relative to (provides reference space for)'
    )


# ******************************************************************************************************************* #


class P160HasTemporalProjection(PropertyMixin):
    """'P160 has temporal projection (is temporal projection of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#160

    Domain:
        E92 Spacetime Volume
    Range:
        E52 Time-Span
    SubProperty Of:
        -
    SuperProperty Of:
        E93 Presence. P164 during (was time-span of): E52 Time-Span
    Quantification:
        one to one (1,1:1,1)

    Scope Note:
        This property describes the temporal projection of an instance of E92 Spacetime Volume. The property
        P4 has time-span is the same as P160 has temporal projection if it is used to document an instance
        of E4 Period or any subclass of it;

    Properties:
        -
    Examples:
        - the spatio-temporal trajectory of the H.M.S. Temeraire from its building in 1798 to its destruction
          in 1838 (E5) has temporal projection The Time-Span of the existence of H.M.S. Temeraire
          [P82 at some time within 1798-1838 (E61 Time Primitive)]
        - The Battle of Waterloo 1815 (E7) has temporal projection the time-span of The Battle of Waterloo
          [P82 at some time within Sunday, 18 June 1815 (E61 Time Primitive)]“
    In First Order Logic:
        P160(x,y) ⊃ E92(x)
        P160(x,y)⊃ E52(y)

    """

    p160_has_temporal_projection: Optional[E52TimeSpan] = Field(
        min_length=1,
        description='P160 has temporal projection (is temporal projection of)'
    )


# ******************************************************************************************************************* #


class P161HasSpatialProjection(PropertyMixin):
    """'P161 has spatial projection (is spatial projection of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#161

    Domain:
        E92 Spacetime Volume
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property associates an instance of an instance of E92 Spacetime Volume with an instance of
        E53 Place that is the result of the spatial projection of the instance of the E92 Spacetime Volume
        on a reference space;

        In general there can be more than one useful reference space (for reference space see p156 occupies and
        p157 is at rest relative to) to describe the spatial projection of a spacetime volume, for example,
        in describing a sea battle, the difference between the battle ship and the seafloor as reference spaces. Thus
        it can be seen that the projection is not unique;

        The spatial projection is the actual spatial coverage of a spacetime volume, which normally has fuzzy
        boundaries except for instances of E92 Spacetime Volumes which are geometrically defined in the same
        reference system as the range of this property are an exception to this and do not have fuzzy boundaries.
        Modelling explicitly fuzzy spatial projections serves therefore as a common topological reference of different
        spatial approximations rather than absolute geometric determination, for instance for relating outer or inner
        spatial boundaries for the respective spacetime volumes;

        In case the domain of an instance of P161 has spatial projection is an instance of E4 Period, the spatial
        projection describes all areas that period was ever present at, for instance, the Roman Empire;

        This property is part of the fully developed path from E18 Physical Thing through P196 defines,
        E92 Spacetime Volume, P161 has spatial projection, which in turn is implied by P156 occupies (is occupied by);

        This property is part of the fully developed path from E4 Period through P161 has spatial projection,
        E53 Place, P89 falls within (contains) to E53 Place, which in turn is shortcut
        by P7took place at (witnessed.)

    Properties:
        -
    Examples:
        - The Roman Empire has spatial projection all areas ever claimed by Rome
    In First Order Logic:
        P161(x,y) ⊃ E92(x)
        P161(x,y) ⊃ E53(y)

    """

    p161_has_spatial_projection: List[E53Place] = Field(
        min_length=1,
        description='P161 has spatial projection (is spatial projection of)'
    )


# ******************************************************************************************************************* #


class P164During(PropertyMixin):
    """'P164 during (was time-span of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#164

    Domain:
        E93 Presence
    Range:
        E52 Time-Span
    SubProperty Of:
        E92 Spacetime Volume. P160 has temporal projection (is temporal projection of): E52 Time-Span
    SuperProperty Of:
        -
    Quantification:
        (1,1 :0,n)

    Scope Note:
        This property relates an instance of E93 Presence with the chosen instance of E52 Time-Span that defines
        the time-slice of the spacetime volume that this instance of E93 Presence is related to by the property
        P166 was a presence of (had presence);

    Properties:
        -
    Examples:
        - 2016-02-09 (E52) was time-span of the last day of the 2016 Carnival in Cologne (E93)
        - Johann JoachimWinckelmann’s whereabouts in December 1755 (E93) during December 1755 (E52)
        - Johann Joachim Winkelmann’s whereabouts from November 19 1755 until April 9 1768 (E93) during
          November 19 1755 until April 9 1768 (E52)
    In First Order Logic:
        P164 (x,y) ⊃ E93(x)
        P164 (x,y) ⊃ E52(y)
        P164 (x,y) ⊃ P160(x,y)

    """

    p164_during: Optional[E52TimeSpan] = Field(default=None, description='P164 during (was time-span of)')


# ******************************************************************************************************************* #


class P166WasAPresenceOf(PropertyMixin):
    """'P166 was a presence of (had presence)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#166

    Domain:
        E93 Presence
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        E92 Spacetime Volume. P10 falls within (contains): E92 Spacetime Volume
    SuperProperty Of:
        -
    Quantification:
        (1,1 : 0,n)

    Scope Note:
        This property associates an instance of E93 Presence with the instance of E92 Spacetime Volume of which it
        represents a temporal restriction (i.e.: a time-slice). Instantiating this property constitutes a necessary
        part of the identity of the respective instance of E93 Presence;

    Properties:
        -
    Examples:
        - The Roman Empire on 19 August AD 14 (E93) was a presence of The Roman Empire (E4)
    In First Order Logic:
        P166(x,y) ⊃ E93(x),
        P166(x,y) ⊃ E92(y),
        P166(x,y) ⊃ P10(x,y)

    """

    p166_was_a_presence_of: Optional[E92SpaceTimeVolume] = Field(
        default=None,
        description='P166 was a presence of (had presence)'
    )


# ******************************************************************************************************************* #


class P167At(PropertyMixin):
    """'P167 at (was place of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#167

    Domain:
        E93 Presence
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (1,n ;0,n)

    Scope Note:
        This property associates an instance of E93 Presence with an instance of E53 Place that geometrically
        includes the spatial projection of the respective instance of E93 Presence. Besides others, this property
        may be used to state in which space an object has been for some known time, such as a room of a castle or in
        a drawer. It may also be used to describe a confinement of the spatial extent of some realm during a known
        time-span. It is a shortcut of the more fully developed path from E93 Presence through P161 has spatial
        projection, E53 Place, P89 falls within (contains) to E53 Place;

    Properties:
        -
    Examples:
        - Johann Joachim Winkelmann’s whereabouts in December 1755 (E93) at Rome (E53)
        - Johann Joachim Winkelmann’s whereabouts from November 19 1755 until April 9 1768 (E93) at Italy (E53)
    In First Order Logic:
        P167(x,y) ⊃ E93(x)
        P167(x,y) ⊃ E53(y)
        P167(x,y) ⊃ (∃z)[ E53(z) ∧ P161(x,z) ∧ P89(z,y)]

    """

    p167_at: Optional[E53Place] = Field(default=None, description='P167 at (was place of)')


# ******************************************************************************************************************* #


class P168PlaceIsDefinedBy(PropertyMixin):
    """'P168 place is defined by (defines place)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#168

    Domain:
        E53 Place
    Range:
        E94 Space Primitive
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (0,n:1,1)

    Scope Note:
        This property associates an instance of E53 Place with an instance of E94 Space Primitive that defines it.
        Syntactic variants or use of different scripts may result in multiple instances of E94 Space Primitive
        defining exactly the same place. Transformations between different reference systems always result in new
        definitions of places approximating each other and not in alternative definitions;

    Properties:
        -
    Examples:
        - the centroid from https://sws.geonames.org/735927 (E53) place is defined by 40°31'17.9"N 21°15'48.3"E
          (E94) [a single point for approximating the centre of the city of Kastoria, Greece]
        - Martin’s coordinates for Kastoria (E53) place is defined by 40°30'23"N 21°14'53"E, 40°31'40"N 21°16'43"E
          (E94) [a square covering the built settlement structure of Kastoria, Greece]
        - Martin’s centroid for Kastoria (E53) place is defined by 40°31'01.5"N 21°15'48"E (E94) [a point in the lake
          of Kastoria in the centre of the area covered by the city
        - the position measured by Alexander von Humboldt for the Plaza Mayor in Cumaná, Sucre,Venezuela 1799-1800AD
          (E53) place is defined by 10°27'52"N 66°30'02"W (E94) [actually 260km west of Cumaná]
    In First Order Logic:
        P168(x,y) ⊃ E53(x)
        P168(x,y) ⊃ E94(y)

    """

    p168_place_defined_by: Optional[CoercedSpace] = Field(
        default=None,
        description='P168 place is defined by (defines place)'
    )


# ******************************************************************************************************************* #


class P169DefinesSpacetimeVolume(PropertyMixin):
    """'P169 defines spacetime volume (spacetime volume is defined by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#169

    Domain:
        E95 Spacetime Primitive
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (1,1:0,n)

    Scope Note:
        This property associates an instance of E95 Spacetime Primitive with the instance of E92 Spacetime Volume
        it defines;

    Properties:
        -
    Examples:
        - {40°30'23"N 21°14'53"E, 40°31'40"N 21°16'43"E, 200BC-2020AD} (E95) defines spacetime volume Martin’s
          spatiotemporal enclosure 2020 for the evolution of the settlement of today’s city of Kastoria, Greece, since
          its conquest by the Romans (E92) [a square covering the current built settlement structure of Kastoria,
          Greece, through the years 200BC to 2020AD, which includes the extents of earlier phases of the city]
    In First Order Logic:
        P169(x,y) ⊃ E95(x)
        P169(x,y) ⊃ E92(y)

    """

    p169_defines_spacetime_volume: Optional[E92SpaceTimeVolume] = Field(
        default=None,
        description='P169 defines spacetime volume (spacetime volume is defined by)'
    )


# ******************************************************************************************************************* #


class P170DefinesTime(PropertyMixin):
    """'P170 defines time (time is defined by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#170

    Domain:
        E61 Time Primitive
    Range:
        E52 Time-Span
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of E61 Time Primitive with the instance of E52 Time-Span that constitutes
        the interpretation of the terms of the time primitive as an extent in absolute, real time;

    Properties:
        -
    Examples:
        - (1800/1/1 0:00:00 – 1899/31/12 23:59:59)(E61) defines time The 19th century (E52)
        - (1968/1/1 – 2018/1/1)(E61) defines time “1968/1/1 – 2018/1/1” (E52) [an arbitrary time-span during which
          the Saint Titus reliquary was present in the Saint Titus Church in Heraklion, Crete]
    In First Order Logic:
        P170(x,y) ⊃ E61(x)
        P170(x,y) ⊃ E52(y)

    """

    p170_defines_time: Optional[E52TimeSpan] = Field(
        default=None,
        description='P170 defines time (time is defined by)'
    )


# ******************************************************************************************************************* #


class P171AtSomePlaceWithin(PropertyMixin):
    """'P171 at some place within' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#171

    Domain:
        E53 Place
    Range:
        E94 Space Primitive
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (0,n:0,n)

    Scope Note:
        This property describes the maximum spatial extent within which an instance of E53 Place falls. Since
        instances of E53 Places may not have precisely known spatial extents, the CIDOC CRM supports statements about
        maximum spatial extents of instances of E53 Place. This property allows an instance of an instance of
        E53 Places’s maximum spatial extent (i.e. its outer boundary) to be assigned an instance of
        E94 Space Primitive value;

        P171 at some place within is a shortcut of the fully developed path E53 Place, P89 falls within, E53 Place,
        P168 place is defined by, E94 Space Primitive through a declarative Place that is not explicitly documented,
        to a Space Primitive: declarative places are defined in CRMgeo (Doerr and Hiebel 2013);

    Properties:
        -
    Examples:
        - the spatial extent of the Acropolis of Athens (E53) is at some place within POLYGON ((37.969172 23.720787,
          37.973122 23.721495 37.972741 23.728994, 37.969299 23.729735, 37.969172 23.720787)) (E94)
    In First Order Logic:
        P171(x,y) ⊃ E53(x)
        P171(x,y) ⊃ E94(y)

    """

    p171_at_some_place_within: Optional[CoercedSpace] = Field(default=None, description='P171 at some place within')


# ******************************************************************************************************************* #


class P172Contains(PropertyMixin):
    """'P172 contains' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#172

    Domain:
        E53 Place
    Range:
        E94 Space Primitive
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (0,n:0,n)

    Scope Note:
        This property describes a minimum spatial extent which is contained within an instance of E53 Place. Since
        instances of E53 Place may not have precisely known spatial extents, the CIDOC CRM supports statements about
        minimum spatial extents of instances of E53 Place. This property allows an instance of E53 Places’s minimum
        spatial extent (i.e. its inner boundary or a point being within a Place) to be assigned an instance
        of E94 Space Primitive value;

        This property is a shortcut of the fully developed path: E53 Place, P89i contains, E53 Place,
        P168 place is defined by, E94 Space Primitive

    Properties:
        -
    Examples:
        - the spatial extent of the Acropolis of Athens (E53) contains POINT (37.971431 23.725947) (E94)
    In First Order Logic:
        P172(x,y) ⊃ E53(x)
        P172(x,y) ⊃ E94(y)

    """

    p172_contains: Optional[CoercedSpace] = Field(default=None, description='P172 contains')


# ******************************************************************************************************************* #


class P180HasCurrency(PropertyMixin):
    """'P180 has currency (was currency of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#180

    Domain:
        E97 Monetary Amount
    Range:
        E98 Currency
    SubProperty Of:
        E54 Dimension. P91 has unit (is unit of): E58 Measurement Unit
    SuperProperty Of:
        -
    Quantification:
        (1,1; 0,n)

    Scope Note:
        This property establishes the relationship between an instance of E97 Monetary Amount and the instance
        of E98 Currency that it is measured in;

    Properties:
        -
    Examples:
        - Christies’ hammer price for “Vase with Fifteen Sunflowers” (E97) has currency British Pounds (E98);
    In First Order Logic:
        P180(x,y) ⊃ E97(x)
        P180(x,y) ⊃ E98(y)
        P180(x,y) ⊃ P91(x,y)

    """

    p180_has_currency: Optional[E98Currency] = Field(default=None, description='P180 has currency (was currency of)')


# ******************************************************************************************************************* #


class P181HasAmount(PropertyMixin):
    """'P181 has amount' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#181

    Domain:
        E97 Monetary Amount
    Range:
        E60 Number
    SubProperty Of:
        E54 Dimension. P90 has value: E60 Number
    SuperProperty Of:
        -
    Quantification:
        -
    Scope Note:
        This property establishes the relationship between an instance of E97 Monetary Amount and the amount
        of currency, an instance of E60 Number, that it consists of;

    Properties:
        -
    Examples:
        - Christies hammer price for “Vase with Fifteen Sunflowers” (E97) has amount 24,750,000 (E60);
    In First Order Logic:
        P181(x,y) ⊃ E97(x)
        P181(x,y) ⊃ E60(y)
        P181(x,y) ⊃ P90(x,y)

    """

    p181_has_amount: Optional[CoercedNumber] = Field(default=None, description='P181 has amount')


# ******************************************************************************************************************* #


class P189Approximates(PropertyMixin):
    """'P189 approximates (is approximated by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#189

    Domain:
        -
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property associates an instance of E53 Place with another instance of E53 Place, which is defined in
        the same reference space, and which is used to approximate the former. The property does not necessarily state
        the quality or accuracy of this approximation, but rather indicates the use of the first instance of place
        to approximate the second;

        In common documentation practice, find or encounter spots e.g. in archaeology, botany or zoology are often
        related to the closest village, river or other named place without detailing the relation, e.g. if it is
        located within the village or in a certain distance of the specified place. In this case the stated
        “phenomenal” place found in the documentation can be seen as approximation of the actual encounter spot
        without more specific knowledge;

        In more recent documentation often point coordinate information is provided that originates from GPS
        measurements or georeferencing from a map. This point coordinate information does not state the actual place
        of the encounter spot but tries to approximate it with a “declarative” place. The accuracy depends on the
        methodology used when creating the coordinates. It may be dependent on technical limitations like GPS accuracy
        but also on the method where the GPS location is taken in relation to the measured feature. If the methodology
        is known a maximum deviation from the measured point can be calculated and the encounter spot or feature may
        be related to the resulting circle using an instance of P171 at some place within;

        This property is not transitive;

    Properties:
        P189.1 has type: E55 Type
    Examples:
        - [40°31'17.9"N 21°15'48.3"E] approximates Kastoria, Greece, TGN ID: 7010880
          (coordinates from https://sws.geonames.org/735927)
        - [40°31'00.1"N 21°16'00.1"E] approximates Kastoria, Greece, TGN ID: 7010880
          (coordinates from http://vocab.getty.edu/page/tgn/7010880)
        - [40°04'60.0"N 22°21'00.0"E] approximates Mount Olympus National Park, Greece
          (coordinates from https://www.geonames.org/6941814)
    In First Order Logic:
        P189(x,y) ⊃ E53(x)
        P189(x,y) ⊃ E53 (y)
        P189 (x,y,z) ⊃ [P189 (x,y) ∧ E55(z)]

    """

    p189_approximates: Optional[E53Place] = Field(default=None, description='P189 approximates (is approximated by)')


# ******************************************************************************************************************* #


class P191HadDuration(PropertyMixin):
    """'P191 had duration (was duration of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#191

    Domain:
        - E52 Time-Span
    Range:
        - E54 Dimension
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to one (1,1:1,1)

    Scope Note:
        This property describes the length of time covered by an instance of E52 Time-Span. It allows an instance of
        E52 Time-Span to be associated with an instance of E54 Dimension representing duration independent from the
        actual beginning and end. Indeterminacy of the duration value can be expressed by assigning a numerical
        interval to the property P90 has value of E54 Dimension;

    Properties:
        -
    Examples:
        - the time span of the Battle of Issos 333 B.C.E. (E52) had duration Battle of Issos duration (E54)
    In First Order Logic:
        - P191(x,y) ⊃ E52(x)
        - P191(x,y) ⊃ E54(y)

    """

    p191_had_duration: Optional[E54Dimension] = Field(default=None, description='P191 had duration')


# ******************************************************************************************************************* #


class P195WasAPresenceOf(PropertyMixin):
    """'P195 was a presence of (had presence)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#195

    Domain:
        E93 Presence
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (1,1 : 0,n)

    Scope Note:
        This property associates an instance of E93 Presence with the instance of E18 Physical Thing of which
        it represents a temporal restriction (i.e.: a time-slice) of the thing’s trajectory through spacetime. In
        other words, it describes where the instance of E18 Physical Thing were or moved around within
        a given time-span. Instantiating this property constitutes a necessary part of the identity of the
        respective instance of E93 Presence;

        This property is a shortcut of the fully developed path from E18 Physical Thing through P196 defines,
        E92 Spacetime Volume, P166 was a presence of (had presence), E93 Presence;

    Properties:
        -
    Examples:
        - Johann Joachim Winckelmann’s whereabouts in December 1755 (E93) was a presence
          of Johann Joachim Winckelmann (E21)
        - Johann Joachim Winckelmann’s whereabouts from November 19 1755 until April 9 1768 (E93) was a presence
          of Johann Joachim Winckelmann (E21)
    In First Order Logic:
        P195(x,y) ⊃ E93(x),
        P195(x,y) ⊃ E18(y),
        P195(x,y) = (∃z)[E9(z) ∧ P196 (y,z) ∧ P166(z,x)]

    """

    p195_was_a_presence_of: Optional[E18PhysicalThing] = Field(
        default=None,
        description='P195 was a presence of (had presence)'
    )


# ******************************************************************************************************************* #


class P197CoveredPartsOf(PropertyMixin):
    """'P197 covered parts of (was partially covered by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#197

    Domain:
        E93 Presence
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        -
    Scope Note:
        This property associates an instance of E93 Presence with an instance of E53 Place that geometrically overlaps
        with the spatial projection of the respective instance of E93 Presence. A use case of this property is to
        state through which places an object or an instance of E21 Person has or was moved within a given time-span.
        It may also be used to describe a partial or complete, temporary or permanent extension of the spatial extent
        of some realm into a neighboring region during a known time-span. It may also be used to describe a partial
        or complete, temporary or permanent extension of the spatial extent of some realm into a neighboring region
        during a known time-span. It is a shortcut of the more fully developed path from E93 Presence through
        P161 has spatial projection, E53 Place, P121 overlaps with to E53 Place;

    Properties:
        -
    Examples:
        - Johann Joachim Winckelmann’s whereabouts from November 19 1755 until April 9 1768 (E93) covered parts
          of Paestum, Italy (E53)
        - The Byzantine Empire 1013 AD (E93) covered parts of The Italian Peninsula (E53)
    In First Order Logic:
        -

    """

    p197_covered_parts_of: Optional[E53Place] = Field(
        default=None,
        description='P197 covered parts of (was partially covered by)'
    )
