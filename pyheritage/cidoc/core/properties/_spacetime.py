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

from typing import Any, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core._primitives import CoercedNumber


__all__ = ('P79BeginningIsQualifiedBy', 'P80EndIsQualifiedBy', 'P81OngoingThroughout', 'P82AtSomeTimeWithin',
           'P86FallsWithin', 'P89FallsWithin', 'P90HasValue', 'P91HasUnit', 'P121OverlapsWith', 'P122BordersWith',
           'P132SpatiotemporallyOverlaps', 'P133IsSpatiotemporallySeparated', 'P157IsAtRestRelativeTo',
           'P191HadDuration', 'P195WasAPresenceOf', 'P197CoveredPartsOf', )


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

    p79_beginning_is_qualified_by: Optional[str] = Field(default=None, description='P79 beginning is qualified by')


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

    p80_end_is_qualified_by: Optional[str] = Field(default=None, description='P80 end is qualified by')


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

    p81_ongoing_throughout: Optional[str] = Field(default=None, description='P81 ongoing throughout')


# ******************************************************************************************************************* #


class P82AtSomeTimeWithin(PropertyMixin):
    """'P82 at some time within' CRM property;

    Domain:
        - E52 Time-Span
    Range:
        - E61 Time Primitive
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

    p82_at_some_time_within: Optional[Any] = Field(default=None)


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

        This property supports the notion that a the temporal extent of an instance of E52 Time-Span falls within the
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

    p86_falls_within: Optional[Any] = Field(default=None)


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

    p89_falls_within: Optional[str] = Field(default=None, description='P89 falls within (contains)')


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

    p90_has_value: Optional[CoercedNumber] = Field(default=None)


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

    p91_has_unit: Optional[Any] = Field(default=None)


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

    p121_overlaps_with: Optional[str] = Field(default=None, description='P121 overlaps with')


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

    p122_borders_with: Optional[str] = Field(default=None, description='P122 borders with')


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

    p132_spatiotemporally_overlaps: Optional[str] = Field(
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

    p133_is_spatiotemporally_separated: Optional[str] = Field(
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

    p157_is_at_rest_relative_to: Optional[str] = Field(
        default=None,
        description='P157 is at rest relative to (provides reference space for)'
    )


# ******************************************************************************************************************* #


class P191HadDuration(PropertyMixin):
    """'P191 had duration (was duration of)' CRM property;

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

    p191_had_duration: Optional[Any] = Field(default=None)


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

    p195_was_a_presence_of: Optional[str] = Field(default=None, description='P195 was a presence of (had presence)')


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

    p197_covered_parts_of: Optional[str] = Field(
        default=None,
        description='P197 covered parts of (was partially covered by)'
    )
