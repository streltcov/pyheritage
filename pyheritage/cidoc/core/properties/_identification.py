# -*- coding: utf-8 -*-

"""Identification CRM properties (mixin classes for entity models);

CIDOC-CRM v7.0

"""


from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core._primitives import CoercedString


__all__ = ('P1IsIdentifiedBy', 'P2HasType', 'P3HasNote', 'P190HasSymbolicContent', )


class P1IsIdentifiedBy(PropertyMixin):
    """'P1 is identified by (identifies)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P1

    Domain:
        E1 CRM Entity
    Range:
        E41 Appellation
    SubProperty Of:
        -
    SuperProperty Of:
        E1 CRM Entity. P48 has preferred identifier (is preferred identifier of): E42 Identifier
        E71 Human-Made Thing. P102 has title (is title of): E35 Title
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the naming or identification of any real world item by a name or any other identifier;

        This property is intended for identifiers in general use, which form part of the world the model intends
        to describe, and not merely for internal database identifiers which are specific to a technical system,
        unless these latter also have a more general use outside the technical context. This property includes
        in particular identification by mathematical expressions such as coordinate systems used for the
        identification of instances of E53 Place. The property does not reveal anything about when, where and by
        whom this identifier was used. A more detailed representation can be made using the fully developed
        (i.e. indirect) path through E15 Identifier Assignment;

        P1 is identified by (identifies), is a shortcut for the path from ‘E1 CRM Entity’ through ‘P140i was
        attributed by’, ‘E15 Identifier Assignment’, ‘P37 assigned’,‘E42 Identifier’;

    Properties:
        -
    Examples:
        - the capital of Italy (E53) is identified by “Rome” (E41)
        - text 25014–32 (E33) is identified by “The Decline and Fall of the Roman Empire” (E35)
    In First Order Logic:
        P1(x,y) ⊃ E1(x)
        P1(x,y) ⊃ E41(y)

    """

    p1_is_identified_by: Optional[str] = Field(default=None, description='P1 is identified by'
                                                                                      ' (identifies)')


# ******************************************************************************************************************* #


class P2HasType(PropertyMixin):
    """'P2 has type (is type of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P2

    Domain:
        E1 CRM Entity
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        E1 CRM Entity. P137 exemplifies (is exemplified by): E55 Type
        E13 Attribute Assignment. P177 assigned property type: E55 Type
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property allows sub typing of CIDOC CRM entities - a form of specialisation – through the use of a
        terminological hierarchy, or thesaurus;

        The CIDOC CRM is intended to focus on the high-level entities and relationships needed to describe data
        structures. Consequently, it does not specialise entities any further than is required for this immediate
        purpose. However, entities in the isA hierarchy of the CIDOC CRM may by specialised into any number of sub
        entities, which can be defined in the E55 Type hierarchy. E41 Appellation, for example, may be specialised
        into “e-mail address”, “telephone number”, “post office box”, “URL” etc. none of which figures explicitly
        in the CIDOC CRM hierarchy. A comprehensive explanation about refining CIDOC CRM concepts by E55 Type is
        given in the section “About Types” in the section on “Specific Modelling Constructs” of this document;

    Properties:
        -
    Examples:
        - “enquiries@cidoc-crm.org” (E41) has type e-mail address (E55)
    In First Order Logic:
        P2(x,y) ⊃ E1(x)
        P2(x,y) ⊃ E55(y)

    """

    p2_has_type: list[Any] = Field(default_factory=list, description='P2 has type (is type of)')


# ******************************************************************************************************************* #


class P3HasNote(PropertyMixin):
    """'P3 has note' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P3

    Domain:
        E1 CRM Entity
    Range:
        E62 String
    SubProperty Of:
        -
    SuperProperty Of:
        E52 Time-Span. P79 beginning is qualified by: E62 String
        E52 Time-Span. P80 end is qualified by: E62 String
        E90 Symbolic Object. P190 has symbolic content: E62 String
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property is a container for all informal descriptions about an object that have not been expressed
        in terms of CIDOC CRM constructs;

        In particular it captures the characterisation of the item itself, its internal structures, appearance etc.;

        Like property P2 has type (is type of), this property is a consequence of the restricted focus of the
        CIDOC CRM. The aim is not to capture, in a structured form, everything that can be said about an item; indeed,
        the CIDOC CRM formalism is not regarded as sufficient to express everything that can be said. Good practice
        requires use of distinct note fields for different aspects of a characterisation. The P3.1 has type property
        of P3 has note allows differentiation of specific notes, e.g. “construction”, “decoration” etc.;

        An item may have many notes, but a note is attached to a specific item.

    Properties:
        P3.1 has type: E55 Type
    Examples:
        - coffee mug – OXCMS:1983.1.1 (E19) has note “chipped at edge of handle” (E62) has type Condition (E55)
    In First Order Logic:
        P3(x,y) ⊃ E1(x)
        P3(x,y) ⊃ E62(y)
        P3(x,y,z) ⊃ [P3(x,y) ∧ E55(z)]

    """

    p3_has_note: Optional[str] = Field(default=None, description='P3 has note')


# ******************************************************************************************************************* #


class P190HasSymbolicContent(PropertyMixin):
    """'P190 has symbolic content' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P190

    Domain:
        - E90 Symbolic Object
    Range:
        - E62 String
    SubProperty Of:
        - E1 CRM Entity. P3 has note: E62 String
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E90 Symbolic Object with a complete, identifying representation of its
        content in the form of an instance of E62 String;

        This property only applies to instances of E90 Symbolic Object that can be represented completely in this
        form. The representation may be more specific than the symbolic level defining the identity condition of the
        represented. This depends on the type of the symbolic object represented. For instance, if a name has type
        "Modern Greek character sequence", it may be represented in a loss-free Latin transcription, meaning however
        the sequence of Greek letters;

        As another example, if the represented object has type "English words sequence", American English or British
        English spelling variants may be chosen to represent the English word "colour" without defining a different
        symbolic object. If a name has type "European traditional name", no particular string may define its content;

    Properties:
        -
    Examples:
        - The materials description (E33) of the painting has symbolic content “Oil, French Watercolors on Paper,
          Graphite and Ink on Canvas, with an Oak frame.”
        - The title (E35) of Einstein’s 1915 text has symbolic content “Relativity, the Special and the General
          Theory“
        - The story of Little Red Riding Hood (E33) has symbolic content “Once upon a time there lived in a certain
          village …”
        - The inscription (E34) on Rijksmuseum object SK-A-1601 has symbolic content “B”
    In First Order Logic:
        P190(x,y) ⊃ E90(x)
        P190(x,y) ⊃ E62(y)

    """

    p190_has_symbolic_content: Optional[CoercedString] = Field(default=None)
