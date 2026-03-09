# -*- coding: utf-8 -*-

"""Spacetime CRM properties (mixin classes for entity models);

CIDOC-CRM v7.0

"""


from typing import Any, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core._primitives import CoercedNumber


__all__ = ('P82AtSomeTimeWithin', 'P86FallsWithin', 'P90HasValue', 'P91HasUnit', 'P191HadDuration', )


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
