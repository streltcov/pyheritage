# -*- coding: utf-8 -*-

"""CRMtex entity models;

CRMtex v2.0 (June 2023)
https://cidoc-crm.org/extensions/crmtex

Entities
--------
TX1  Written Text
TX2  Writing
TX3  Writing System
TX4  Writing Field
TX5  Text Recognition
TX6  Transliteration
TX7  Written Text Segment
TX8  Grapheme
TX9  Glyph
TX10 Style
TX11 Grapheme Occurrence
TX12 Grapheme Sequence
TX13 Script
TX14 Reading

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core import entities as _core_entities
from pyheritage.cidoc.core.entities import (
    E25HumanMadeFeature,
    E29DesignOrProcedure,
    E55Type,
    E65Creation,
    E89PropositionalObject,
    E90SymbolicObject,
)
from pyheritage.cidoc.crminf import entities as _crminf_entities
from pyheritage.cidoc.crminf.entities import I1Argumentation
from pyheritage.cidoc.crmsci import entities as _crmsci_entities
from pyheritage.cidoc.crmsci.entities import S4Observation


__all__ = (
    'TX1WrittenText',
    'TX2Writing',
    'TX3WritingSystem',
    'TX4WritingField',
    'TX5TextRecognition',
    'TX6Transliteration',
    'TX7WrittenTextSegment',
    'TX8Grapheme',
    'TX9Glyph',
    'TX10Style',
    'TX11GraphemeOccurrence',
    'TX12GraphemeSequence',
    'TX13Script',
    'TX14Reading',
)


# ******************************************************************************************************************* #


@entity_register(label='TX8 Grapheme')
class TX8Grapheme(E55Type):
    """'TX8 Grapheme' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX8

    SubClass Of:
        E55 Type

    SuperClass Of:
        -

    Scope Note:
        This class comprises symbols used as atomic units with distinctive value in a
        writing system to represent linguistic units, such as phonemes, syllables, or
        words, and their diacritical marks. A grapheme is an abstract unit of a writing
        system, distinct from its physical manifestation.

    Examples:
        - The Latin letter 'a'
        - The Arabic numeral '1'
        - The Chinese character '中'
        - The ampersand '&'

    In First Order Logic:
        TX8(x) ⇒ E55(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX10 Style')
class TX10Style(E29DesignOrProcedure):
    """'TX10 Style' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX10

    SubClass Of:
        E29 Design or Procedure

    SuperClass Of:
        -

    Scope Note:
        This class comprises stylistic variations of texts, including local script
        styles, individual scribal hands, ductus, ligatures, writing angle, and other
        graphical features. An instance of TX10 Style can be associated with a particular
        script, period, geographical area, scribe, or workshop.

    Examples:
        - Carolingian minuscule
        - Roman square capitals
        - Uncial script
        - The scribal hand of the scribe who copied the Lindisfarne Gospels

    In First Order Logic:
        TX10(x) ⇒ E29(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX13 Script')
class TX13Script(E89PropositionalObject):
    """'TX13 Script' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX13

    SubClass Of:
        E89 Propositional Object

    SuperClass Of:
        -

    Scope Note:
        This class comprises functionally complete sets of mutually different graphemes
        employed by one or more languages, regardless of specific operating rules. A
        script defines the inventory of symbols used for writing a particular language
        or group of languages.

    Examples:
        - Latin script
        - Greek script
        - Cyrillic script
        - Arabic script
        - Devanagari script

    In First Order Logic:
        TX13(x) ⇒ E89(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX3 Writing System')
class TX3WritingSystem(E29DesignOrProcedure):
    """'TX3 Writing System' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX3

    SubClass Of:
        E29 Design or Procedure

    SuperClass Of:
        -

    Scope Note:
        This class comprises conventional symbolic systems designed to represent units
        of a natural language for recording and transmitting information. A writing
        system consists of a set of symbols (graphemes) and the syntactic rules
        governing their combination.

    Examples:
        - The Latin alphabet as used for English
        - The Greek alphabet
        - The Cyrillic alphabet as used for Russian
        - The Chinese writing system (logographic)
        - The Japanese syllabary (kana)

    In First Order Logic:
        TX3(x) ⇒ E29(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX12 Grapheme Sequence')
class TX12GraphemeSequence(E90SymbolicObject, ABC):
    """'TX12 Grapheme Sequence' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX12

    SubClass Of:
        E90 Symbolic Object

    SuperClass Of:
        TX11 Grapheme Occurrence

    Scope Note:
        This class comprises particular sequences of graphemes used for representing
        the abstract written form of a section of a text. A grapheme sequence is the
        ordered set of graphemes that constitutes the written form of a textual unit.

    Examples:
        - The sequence of Latin graphemes 'c', 'a', 't' forming the word "cat"
        - The sequence of Greek graphemes 'λ', 'ό', 'γ', 'ο', 'ς' forming the word "λόγος"

    In First Order Logic:
        TX12(x) ⇒ E90(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX1 Written Text')
class TX1WrittenText(E25HumanMadeFeature, ABC):
    """'TX1 Written Text' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX1

    SubClass Of:
        E25 Human-Made Feature

    SuperClass Of:
        TX7 Written Text Segment

    Scope Note:
        This class comprises visible or tactile marks (glyphs or graphs) that relate
        systematically to units of speech, intentionally traced on a physical support
        to convey a message. Written text is the result of a writing activity and may
        be studied independently of its physical carrier.

    Examples:
        - The inscription on the Rosetta Stone
        - The text of the Lindisfarne Gospels
        - A Roman curse tablet (tabella defixionis)
        - A medieval charter

    In First Order Logic:
        TX1(x) ⇒ E25(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX4 Writing Field')
class TX4WritingField(E25HumanMadeFeature):
    """'TX4 Writing Field' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX4

    SubClass Of:
        E25 Human-Made Feature

    SuperClass Of:
        -

    Scope Note:
        This class comprises the portion of the physical carrier arranged and reserved
        for accommodating a written text. The writing field defines the area within
        which the text is inscribed, such as the epigraphic field in inscriptions or
        the written area of a manuscript page.

    Examples:
        - The inscribed area of a Roman stele
        - The writing surface of a papyrus roll
        - A parchment page of a medieval codex

    In First Order Logic:
        TX4(x) ⇒ E25(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX2 Writing')
class TX2Writing(E65Creation):
    """'TX2 Writing' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX2

    SubClass Of:
        E65 Creation

    SuperClass Of:
        -

    Scope Note:
        This class comprises the activity of communicating information by means of
        permanent, visible marks in a non-mechanical way, using various techniques
        and tools on a given support. Writing encompasses the manual production of
        signs on a surface, including engraving, painting, inscribing, or any other
        technique that results in a handwritten text.

    Examples:
        - The writing of the Lindisfarne Gospels by Eadfrith in the early 8th century
        - The engraving of a Roman inscription on a marble slab
        - The writing of a medieval charter by a notary

    In First Order Logic:
        TX2(x) ⇒ E65(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX5 Text Recognition')
class TX5TextRecognition(E65Creation, S4Observation):
    """'TX5 Text Recognition' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX5

    SubClass Of:
        E65 Creation
        S4 Observation

    SuperClass Of:
        -

    Scope Note:
        This class comprises activities of recognizing physical features on a surface
        as an arrangement of glyphs of a known script. It includes scientific autoptic
        examination of the text, as well as the use of digital tools and representations
        for deciphering visible or faded inscriptions.

    Examples:
        - The reading of a carbonised papyrus scroll using multispectral imaging
        - The autoptic examination of a medieval manuscript by a palaeographer
        - The digital recognition of characters in an ancient inscription

    In First Order Logic:
        TX5(x) ⇒ E65(x)
        TX5(x) ⇒ S4(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX6 Transliteration')
class TX6Transliteration(E65Creation):
    """'TX6 Transliteration' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX6

    SubClass Of:
        E65 Creation

    SuperClass Of:
        -

    Scope Note:
        This class comprises activities of exactly re-writing (re-encoding) a grapheme
        sequence using a writing system different from the original, without changing
        the order of characters or words. Transliteration aims to represent the original
        graphemes as faithfully as possible in the target system.

    Examples:
        - The transliteration of a Greek inscription into the Latin alphabet
        - The transliteration of a Cyrillic text into roman characters
        - The conversion of a Chinese text into pinyin

    In First Order Logic:
        TX6(x) ⇒ E65(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX7 Written Text Segment')
class TX7WrittenTextSegment(TX1WrittenText, ABC):
    """'TX7 Written Text Segment' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX7

    SubClass Of:
        TX1 Written Text

    SuperClass Of:
        TX9 Glyph

    Scope Note:
        This class comprises portions of text considered of particular significance
        for the study of a handwritten document. Written text segments may correspond
        to columns, fragments, paragraphs, lines, words, or individual signs, depending
        on the analytical perspective.

    Examples:
        - A column of text in a papyrus roll
        - A paragraph in a medieval manuscript
        - A single word in an inscription
        - A fragment of a damaged text

    In First Order Logic:
        TX7(x) ⇒ TX1(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX9 Glyph')
class TX9Glyph(TX7WrittenTextSegment):
    """'TX9 Glyph' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX9

    SubClass Of:
        TX7 Written Text Segment

    SuperClass Of:
        -

    Scope Note:
        This class comprises physical, concrete features traced by a writer on a
        support. Glyphs are the material manifestations of graphemes — the actual
        marks visible on the surface, including their shape, size, and technical
        execution.

    Examples:
        - The specific shape of the letter 'a' as written by a particular scribe
        - A carved ligature in an inscription
        - A graffito scratched on a wall

    In First Order Logic:
        TX9(x) ⇒ TX7(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX11 Grapheme Occurrence')
class TX11GraphemeOccurrence(TX12GraphemeSequence):
    """'TX11 Grapheme Occurrence' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX11

    SubClass Of:
        TX12 Grapheme Sequence

    SuperClass Of:
        -

    Scope Note:
        This class comprises single occurrences of a grapheme used as an atomic unit
        at a particular position in the abstract form of a text. A grapheme occurrence
        is the instance of a grapheme at a specific location within a grapheme sequence.

    Examples:
        - The first occurrence of the letter 'a' in the word "cat"
        - The third grapheme in the sequence 'λόγος'

    In First Order Logic:
        TX11(x) ⇒ TX12(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='TX14 Reading')
class TX14Reading(I1Argumentation):
    """'TX14 Reading' CRMtex entity;

    https://cidoc-crm.org/extensions/crmtex/html/CRMtex_v2.0.html#TX14

    SubClass Of:
        I1 Argumentation

    SuperClass Of:
        -

    Scope Note:
        This class comprises the complete intellectual activity leading from text
        recognition to association with a complete linguistic meaning. Reading is
        the process of understanding and interpreting a written text, including the
        comprehension of its semantic content.

    Examples:
        - The reading of a damaged papyrus by a papyrologist
        - The interpretation of a medieval legal document by a historian
        - The decipherment of an ancient inscription by an epigraphist

    In First Order Logic:
        TX14(x) ⇒ I1(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


__crmtex_namespace__: dict[str, type] = {
    'TX1WrittenText': TX1WrittenText,
    'TX2Writing': TX2Writing,
    'TX3WritingSystem': TX3WritingSystem,
    'TX4WritingField': TX4WritingField,
    'TX5TextRecognition': TX5TextRecognition,
    'TX6Transliteration': TX6Transliteration,
    'TX7WrittenTextSegment': TX7WrittenTextSegment,
    'TX8Grapheme': TX8Grapheme,
    'TX9Glyph': TX9Glyph,
    'TX10Style': TX10Style,
    'TX11GraphemeOccurrence': TX11GraphemeOccurrence,
    'TX12GraphemeSequence': TX12GraphemeSequence,
    'TX13Script': TX13Script,
    'TX14Reading': TX14Reading,
}


__namespace__: dict[str, type] = {
    **_core_entities.__namespace__,
    **_crmsci_entities.__crmsci_namespace__,
    **_crminf_entities.__crminf_namespace__,
    **__crmtex_namespace__,
}


TX1WrittenText.model_rebuild(_types_namespace=__namespace__)
TX2Writing.model_rebuild(_types_namespace=__namespace__)
TX3WritingSystem.model_rebuild(_types_namespace=__namespace__)
TX4WritingField.model_rebuild(_types_namespace=__namespace__)
TX5TextRecognition.model_rebuild(_types_namespace=__namespace__)
TX6Transliteration.model_rebuild(_types_namespace=__namespace__)
TX7WrittenTextSegment.model_rebuild(_types_namespace=__namespace__)
TX8Grapheme.model_rebuild(_types_namespace=__namespace__)
TX9Glyph.model_rebuild(_types_namespace=__namespace__)
TX10Style.model_rebuild(_types_namespace=__namespace__)
TX11GraphemeOccurrence.model_rebuild(_types_namespace=__namespace__)
TX12GraphemeSequence.model_rebuild(_types_namespace=__namespace__)
TX13Script.model_rebuild(_types_namespace=__namespace__)
TX14Reading.model_rebuild(_types_namespace=__namespace__)
