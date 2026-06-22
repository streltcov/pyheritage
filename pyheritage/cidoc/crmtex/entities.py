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


from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core import entities as _core_entities
from pyheritage.cidoc.core.entities import (
    E29DesignOrProcedure,
    E55Type,
    E89PropositionalObject,
)


__all__ = (
    'TX8Grapheme',
    'TX10Style',
    'TX13Script',
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


__crmtex_namespace__: dict[str, type] = {
    'TX10Style': TX10Style,
    'TX13Script': TX13Script,
    'TX8Grapheme': TX8Grapheme,
}

__namespace__: dict[str, type] = {
    **_core_entities.__namespace__,
    **__crmtex_namespace__,
}

TX8Grapheme.model_rebuild(_types_namespace=__namespace__)
TX10Style.model_rebuild(_types_namespace=__namespace__)
TX13Script.model_rebuild(_types_namespace=__namespace__)
