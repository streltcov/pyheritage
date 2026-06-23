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
    from pyheritage.cidoc.core.entities import (
        E24PhysicalHumanMadeObject,
        E36VisualItem,
        E56Language,
    )
    from pyheritage.cidoc.crmtex.entities import (
        TX1WrittenText,
        TX3WritingSystem,
        TX7WrittenTextSegment,
        TX8Grapheme,
        TX9Glyph,
        TX10Style,
        TX12GraphemeSequence,
        TX13Script,
    )


__all__ = (
    'TXP1UsedWritingSystem',
    'TXP2Includes',
    'TXP4HasSegment',
    'TXP5Wrote',
    'TXP6Encodes',
    'TXP7HasItem',
    'TXP8HasComponent',
    'TXP9IsEncodedUsing',
    'TXP10DecipheredText',
    'TXP11Transcribed',
    'TXP12HasStyle',
    'TXP13DecipheredViaRepresentation',
    'TXP14UsedCopyOrRepresentationOf',
    'TXP15RecordedCorrespondence',
    'TXP16EmploysScript',
    'TXP17HasPart',
    'TXP18Read',
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


# ******************************************************************************************************************* #


class TXP7HasItem(PropertyMixin):
    """'TXP7 has item (is item of)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP7

    Domain:
        TX13 Script
    Range:
        TX8 Grapheme
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of TX13 Script with an instance of TX8
        Grapheme that is employed by that script. A script consists of a set of
        graphemes used for writing;

    Properties:
        -
    Examples:
        - The Latin script (TX13) *has item* the grapheme 'a' (TX8)
        - The Greek script (TX13) *has item* the grapheme 'α' (TX8)

    In First Order Logic:
        TXP7(x,y) ⇒ TX13(x)
        TXP7(x,y) ⇒ TX8(y)
        TXP7(x,y) ⇒ P67(x,y)

    """

    txp7_has_item: List[TX8Grapheme] = Field(
        default=None,
        description='TXP7 has item (is item of)',
    )


# ******************************************************************************************************************* #


class TXP8HasComponent(PropertyMixin):
    """'TXP8 has component (is component of)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP8

    Domain:
        TX1 Written Text
    Range:
        TX9 Glyph
    SubProperty Of:
        E1 CRM Entity. P46 is composed of (forms part of): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property states the physical belonging of an instance of TX9 Glyph to an
        instance of TX1 Written Text. It links a written text to the concrete glyphs
        that constitute its visible manifestation;

    Properties:
        -
    Examples:
        - The text of the Rosetta Stone (TX1) *has component* the carved hieroglyphic glyphs (TX9)
        - The text of a papyrus letter (TX1) *has component* the ink strokes forming each character (TX9)

    In First Order Logic:
        TXP8(x,y) ⇒ TX1(x)
        TXP8(x,y) ⇒ TX9(y)
        TXP8(x,y) ⇒ P46(x,y)

    """

    txp8_has_component: List[TX9Glyph] = Field(
        default=None,
        description='TXP8 has component (is component of)',
    )


# ******************************************************************************************************************* #


class TXP9IsEncodedUsing(PropertyMixin):
    """'TXP9 is encoded using (encodes)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP9

    Domain:
        TX1 Written Text
    Range:
        TX3 Writing System
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property is a shortcut associating an instance of TX1 Written Text directly
        with the instance of TX3 Writing System that was used to encode it, without
        requiring the explicit documentation of the writing activity;

    Properties:
        -
    Examples:
        - The text of the Codex Sinaiticus (TX1) *is encoded using* the Greek alphabet (TX3)
        - The Vindolanda tablet text (TX1) *is encoded using* the Latin cursive (TX3)

    In First Order Logic:
        TXP9(x,y) ⇒ TX1(x)
        TXP9(x,y) ⇒ TX3(y)

    """

    txp9_is_encoded_using: List[TX3WritingSystem] = Field(
        default=None,
        description='TXP9 is encoded using (encodes)',
    )


# ******************************************************************************************************************* #


class TXP10DecipheredText(PropertyMixin):
    """'TXP10 deciphered text (was deciphered by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP10

    Domain:
        TX5 Text Recognition
    Range:
        E24 Physical Human-Made Object
    SubProperty Of:
        S4 Observation. O8 observed (was observed by): S15 Observable Entity
    SuperProperty Of:
        -
    Quantification:
        one to one (0,1:0,n)

    Scope Note:
        This property associates an instance of TX5 Text Recognition with the instance
        of E24 Physical Human-Made Object carrying the glyphs that were recognised
        during the text recognition activity;

    Properties:
        -
    Examples:
        - The multispectral imaging of a carbonised papyrus (TX5) *deciphered text* the papyrus roll (E24)
        - The autoptic examination of a marble inscription (TX5) *deciphered text* the inscribed stele (E24)

    In First Order Logic:
        TXP10(x,y) ⇒ TX5(x)
        TXP10(x,y) ⇒ E24(y)
        TXP10(x,y) ⇒ O8(x,y)

    """

    txp10_deciphered_text: E24PhysicalHumanMadeObject | None = Field(
        default=None,
        description='TXP10 deciphered text (was deciphered by)',
    )


# ******************************************************************************************************************* #


class TXP11Transcribed(PropertyMixin):
    """'TXP11 transcribed (was transcribed by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP11

    Domain:
        TX6 Transliteration
    Range:
        TX12 Grapheme Sequence
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property relates an instance of TX6 Transliteration to the instance of
        TX12 Grapheme Sequence that it produced. The transliteration activity creates
        a grapheme sequence that re-encodes the original text in a different writing
        system;

    Properties:
        -
    Examples:
        - The transliteration of a Greek epigraph into Latin characters (TX6) *transcribed* the grapheme sequence
          'logos' (TX12)
        - The transliteration of a Russian text into the Latin alphabet (TX6) *transcribed* the grapheme sequence
          'russkij' (TX12)

    In First Order Logic:
        TXP11(x,y) ⇒ TX6(x)
        TXP11(x,y) ⇒ TX12(y)
        TXP11(x,y) ⇒ P16(x,y)

    """

    txp11_transcribed: List[TX12GraphemeSequence] = Field(
        default=None,
        description='TXP11 transcribed (was transcribed by)',
    )


# ******************************************************************************************************************* #


class TXP12HasStyle(PropertyMixin):
    """'TXP12 has style (is style of)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP12

    Domain:
        TX1 Written Text
    Range:
        TX10 Style
    SubProperty Of:
        E7 Activity. P33 used specific technique (was used for): E29 Design or Procedure
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the style of an instance of TX1 Written Text. It
        associates a written text with the instance of TX10 Style that characterises
        its graphic appearance;

    Properties:
        -
    Examples:
        - The text of the Lindisfarne Gospels (TX1) *has style* Insular majuscule (TX10)
        - A Roman square capital inscription (TX1) *has style* Roman square capitals (TX10)
        - A Carolingian manuscript (TX1) *has style* Carolingian minuscule (TX10)

    In First Order Logic:
        TXP12(x,y) ⇒ TX1(x)
        TXP12(x,y) ⇒ TX10(y)
        TXP12(x,y) ⇒ P33(x,y)

    """

    txp12_has_style: List[TX10Style] = Field(
        default=None,
        description='TXP12 has style (is style of)',
    )


# ******************************************************************************************************************* #


class TXP13DecipheredViaRepresentation(PropertyMixin):
    """'TXP13 deciphered via the representation (was representation for)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP13

    Domain:
        TX5 Text Recognition
    Range:
        E36 Visual Item
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        one to one (0,1:0,n)

    Scope Note:
        This property associates an instance of TX5 Text Recognition with an instance
        of E36 Visual Item, such as a digital image or a facsimile, that was used as
        the basis for deciphering the text;

    Properties:
        -
    Examples:
        - The multispectral imaging of a palimpsest (TX5) *deciphered via the representation*
          the digital image processed with spectral filters (E36)
        - The reading of a faded inscription (TX5) *deciphered via the representation*
          a UV photograph of the stone (E36)

    In First Order Logic:
        TXP13(x,y) ⇒ TX5(x)
        TXP13(x,y) ⇒ E36(y)
        TXP13(x,y) ⇒ P16(x,y)

    """

    txp13_deciphered_via_the_representation: E36VisualItem | None = Field(
        default=None,
        description='TXP13 deciphered via the representation (was representation for)',
    )


# ******************************************************************************************************************* #


class TXP14UsedCopyOrRepresentationOf(PropertyMixin):
    """'TXP14 used copy or representation of (was represented by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP14

    Domain:
        TX5 Text Recognition
    Range:
        TX1 Written Text
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates a non-autoptic instance of TX5 Text Recognition with
        an instance of TX1 Written Text via a copy or surrogate of the original text,
        rather than through direct examination of the physical carrier;

    Properties:
        -
    Examples:
        - The remote reading of a carbonised scroll (TX5) *used copy or representation of*
          the text of the scroll as published in a digital edition (TX1)
        - The study of an inscription from a squeeze (TX5) *used copy or representation of*
          the text as reproduced on the paper squeeze (TX1)

    In First Order Logic:
        TXP14(x,y) ⇒ TX5(x)
        TXP14(x,y) ⇒ TX1(y)
        TXP14(x,y) ⇒ P16(x,y)

    """

    txp14_used_copy_or_representation_of: List[TX1WrittenText] = Field(
        default=None,
        description='TXP14 used copy or representation of (was represented by)',
    )


# ******************************************************************************************************************* #


class TXP15RecordedCorrespondence(PropertyMixin):
    """'TXP15 recorded correspondence (was recorded by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP15

    Domain:
        TX5 Text Recognition
    Range:
        TX12 Grapheme Sequence
    SubProperty Of:
        E65 Creation. P94 has created (was created by): E28 Conceptual Object
    SuperProperty Of:
        -
    Quantification:
        one to one (0,1:1,1)

    Scope Note:
        This property associates an instance of TX5 Text Recognition with the instance
        of TX12 Grapheme Sequence that was created to record the correspondence between
        the recognised glyphs and the graphemes of the identified script;

    Properties:
        -
    Examples:
        - The close reading of an Ancient Greek inscription (TX5) *recorded correspondence*
          the grapheme sequence 'ΑΘΗΝΑ' (TX12)
        - The digital recognition of a Latin inscription (TX5) *recorded correspondence*
          the grapheme sequence 'SPQR' (TX12)

    In First Order Logic:
        TXP15(x,y) ⇒ TX5(x)
        TXP15(x,y) ⇒ TX12(y)
        TXP15(x,y) ⇒ P94(x,y)

    """

    txp15_recorded_correspondence: TX12GraphemeSequence | None = Field(
        default=None,
        description='TXP15 recorded correspondence (was recorded by)',
    )


# ******************************************************************************************************************* #


class TXP16EmploysScript(PropertyMixin):
    """'TXP16 employs script (is script employed by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP16

    Domain:
        TX3 Writing System
    Range:
        TX13 Script
    SubProperty Of:
        E89 Propositional Object. P148 has component (is component of): E89 Propositional Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of TX3 Writing System with the instance
        of TX13 Script that it employs. A writing system implements a particular script
        to represent a language;

    Properties:
        -
    Examples:
        - The English writing system (TX3) *employs script* the Latin script (TX13)
        - The Russian writing system (TX3) *employs script* the Cyrillic script (TX13)

    In First Order Logic:
        TXP16(x,y) ⇒ TX3(x)
        TXP16(x,y) ⇒ TX13(y)
        TXP16(x,y) ⇒ P148(x,y)

    """

    txp16_employs_script: List[TX13Script] = Field(
        default=None,
        description='TXP16 employs script (is script employed by)',
    )


# ******************************************************************************************************************* #


class TXP17HasPart(PropertyMixin):
    """'TXP17 has part (is part of)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP17

    Domain:
        TX12 Grapheme Sequence
    Range:
        TX12 Grapheme Sequence
    SubProperty Of:
        E90 Symbolic Object. P106 is composed of (forms part of): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property associates an instance of TX12 Grapheme Sequence with another
        instance of TX12 Grapheme Sequence that is a part of it at a particular position.
        A grapheme sequence may be composed of subsequences corresponding to smaller
        textual units;

    Properties:
        -
    Examples:
        - The grapheme sequence 'catalogue' (TX12) *has part* the subsequence 'cat' (TX12)
        - The grapheme sequence 'λόγος' (TX12) *has part* the subsequence 'λό' (TX12)

    In First Order Logic:
        TXP17(x,y) ⇒ TX12(x)
        TXP17(x,y) ⇒ TX12(y)
        TXP17(x,y) ⇒ P106(x,y)

    """

    txp17_has_part: List[TX12GraphemeSequence] = Field(
        default=None,
        description='TXP17 has part (is part of)',
    )


# ******************************************************************************************************************* #


class TXP18Read(PropertyMixin):
    """'TXP18 read (was read by)' CRMtex property;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TXP18

    Domain:
        TX14 Reading
    Range:
        TX1 Written Text
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of TX14 Reading with an instance of TX1
        Written Text whose meaning was interpreted during the reading activity;

    Properties:
        -
    Examples:
        - The reading of the Rosetta Stone by Jean-François Champollion (TX14) *read*
          the hieroglyphic text of the Rosetta Stone (TX1)
        - The palaeographic analysis of a medieval charter (TX14) *read*
          the text of the charter (TX1)

    In First Order Logic:
        TXP18(x,y) ⇒ TX14(x)
        TXP18(x,y) ⇒ TX1(y)
        TXP18(x,y) ⇒ P16(x,y)

    """

    txp18_read: List[TX1WrittenText] = Field(
        default=None,
        description='TXP18 read (was read by)',
    )
