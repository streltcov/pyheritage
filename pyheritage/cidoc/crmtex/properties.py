# -*- coding: utf-8 -*-

"""CRMtex property models;

(Mixin classes for entity models);

CRMtex v2.0 (June 2023)
https://cidoc-crm.org/extensions/crmtex

------------------------------------------------------
Properties
------------------------------------------------------
TXP1  used writing system                  TX2  -> TX3
TXP2  includes                             TX4  -> TX1
TXP4  has segment                          TX1  -> TX7
TXP5  wrote                                TX2  -> TX1
TXP6  encodes                              TX3  -> E56
TXP7  has item                             TX13 -> TX8
TXP8  has component                        TX1  -> TX9
TXP9  is encoded using                     TX1  -> TX3
TXP10 deciphered text                      TX5  -> E24
TXP11 transcribed                          TX6  -> TX12
TXP12 has style                            TX1  -> TX10
TXP13 deciphered via the representation    TX5  -> E36
TXP14 used copy or representation of       TX5  -> TX1
TXP15 recorded correspondence              TX5  -> TX12
TXP16 employs script                       TX3  -> TX13
TXP17 has part                             TX12 -> TX12
TXP18 read                                 TX14 -> TX1

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E56Language
    from pyheritage.cidoc.crmtex.entities import (
        TX1WrittenText,
        TX3WritingSystem,
        TX7WrittenTextSegment,
    )


__all__ = (
    'TXP1UsedWritingSystem',
    'TXP2Includes',
    'TXP4HasSegment',
    'TXP5Wrote',
    'TXP6Encodes',
)


# ******************************************************************************************************************* #


class TXP1UsedWritingSystem(PropertyMixin):
    """'TXP1 used writing system (was used by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP1

    Domain:
        TX2 Writing
    Range:
        TX3 Writing System
    SubProperty Of:
        E7 Activity. P33 used specific technique (was used for): E29 Design or Procedure
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the writing system employed during a writing event.
        It associates an instance of TX2 Writing with the instance of TX3 Writing
        System that was used to produce the written text;

    Properties:
        -
    Examples:
        - The writing of the Codex Sinaiticus (TX2) *used writing system* Greek alphabet (TX3)
        - The writing of the Vindolanda tablets (TX2) *used writing system* Latin cursive (TX3)

    In First Order Logic:
        TXP1(x,y) ⇒ TX2(x)
        TXP1(x,y) ⇒ TX3(y)
        TXP1(x,y) ⇒ P33(x,y)

    """

    txp1_used_writing_system: List[TX3WritingSystem] = Field(
        default=None,
        description='TXP1 used writing system (was used by)',
    )


# ******************************************************************************************************************* #


class TXP2Includes(PropertyMixin):
    """'TXP2 includes (is included in)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP2

    Domain:
        TX4 Writing Field
    Range:
        TX1 Written Text
    SubProperty Of:
        E25 Human-Made Feature. P56 bears feature (is found on): E26 Physical Feature
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property relates an instance of TX4 Writing Field to an instance of TX1
        Written Text that it contains. A writing field is the area of the physical
        carrier that has been arranged and reserved to accommodate the written text;

    Properties:
        -
    Examples:
        - The epigraphic field of the Rosetta Stone (TX4) *includes* the hieroglyphic text (TX1)
        - The writing field of a papyrus column (TX4) *includes* a column of text (TX1)

    In First Order Logic:
        TXP2(x,y) ⇒ TX4(x)
        TXP2(x,y) ⇒ TX1(y)
        TXP2(x,y) ⇒ P56(x,y)

    """

    txp2_includes: List[TX1WrittenText] = Field(
        default=None,
        description='TXP2 includes (is included in)',
    )


# ******************************************************************************************************************* #


class TXP4HasSegment(PropertyMixin):
    """'TXP4 has segment (is segment of)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP4

    Domain:
        TX1 Written Text
    Range:
        TX7 Written Text Segment
    SubProperty Of:
        E1 CRM Entity. P46 is composed of (forms part of): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property correlates an instance of TX1 Written Text with an instance of
        TX7 Written Text Segment that composes it. A written text may be composed of
        multiple segments, such as columns, paragraphs, lines, or words;

    Properties:
        -
    Examples:
        - The text of the Lindisfarne Gospels (TX1) *has segment* the first column of folio 27r (TX7)
        - The text of a Roman inscription (TX1) *has segment* line 5 (TX7)

    In First Order Logic:
        TXP4(x,y) ⇒ TX1(x)
        TXP4(x,y) ⇒ TX7(y)
        TXP4(x,y) ⇒ P46(x,y)

    """

    txp4_has_segment: List[TX7WrittenTextSegment] = Field(
        default=None,
        description='TXP4 has segment (is segment of)',
    )


# ******************************************************************************************************************* #


class TXP5Wrote(PropertyMixin):
    """'TXP5 wrote (was written by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP5

    Domain:
        TX2 Writing
    Range:
        TX1 Written Text
    SubProperty Of:
        E12 Production. P108 has produced (was produced by): E24 Physical Human-Made Object
    SuperProperty Of:
        -
    Quantification:
        one to one (0,1:1,1)

    Scope Note:
        This property links an instance of TX2 Writing to the instance of TX1 Written
        Text that it produced. Each writing activity may produce at most one written
        text, and each written text is produced by exactly one writing activity;

    Properties:
        -
    Examples:
        - The writing of the Book of Kells by the monks of Iona (TX2) *wrote* the text of the Book of Kells (TX1)
        - Eadfrith's writing activity (TX2) *wrote* the text of the Lindisfarne Gospels (TX1)

    In First Order Logic:
        TXP5(x,y) ⇒ TX2(x)
        TXP5(x,y) ⇒ TX1(y)
        TXP5(x,y) ⇒ P108(x,y)

    """

    txp5_wrote: TX1WrittenText | None = Field(
        default=None,
        description='TXP5 wrote (was written by)',
    )


# ******************************************************************************************************************* #


class TXP6Encodes(PropertyMixin):
    """'TXP6 encodes (is encoded by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP6

    Domain:
        TX3 Writing System
    Range:
        E56 Language
    SubProperty Of:
        E1 CRM Entity. P2 has type (is type of): E55 Type
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property indicates the language that is encoded by an instance of TX3
        Writing System. A writing system may encode one or more natural languages;

    Properties:
        -
    Examples:
        - The Latin alphabet as used for English (TX3) *encodes* English (E56)
        - The Greek alphabet (TX3) *encodes* Greek (E56)
        - The Cyrillic alphabet as used for Russian (TX3) *encodes* Russian (E56)

    In First Order Logic:
        TXP6(x,y) ⇒ TX3(x)
        TXP6(x,y) ⇒ E56(y)
        TXP6(x,y) ⇒ P2(x,y)

    """

    txp6_encodes: List[E56Language] = Field(
        default=None,
        description='TXP6 encodes (is encoded by)',
    )
