# -*- coding: utf-8 -*-

"""Identification, naming, and typing properties;

(Mixin classes for CRM entities);

CIDOC-CRM v7.0

---------------------------------------------
Properties
---------------------------------------------
P1   is identified by              E1  -> E41
P2   has type                      E1  -> E55
P3   has note                      E1  -> E62
P48  has preferred identifier      E1  -> E42
P102 has title                     E71 -> E35
P127 has broader term              E55 -> E55
P137 exemplifies                   E55 -> E55
P139 has alternative form          E41 -> E41
P150 defines typical parts of      E55 -> E55
P190 has symbolic content          E90 -> E62

"""


from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import CoercedString, E35Title, E41Appellation, E42Identifier, E55Type


__all__ = ('P1IsIdentifiedBy', 'P2HasType', 'P3HasNote', 'P48HasPreferredIdentifier', 'P102HasTitle',
           'P127HasBroaderTerm', 'P137Exemplifies', 'P139HasAlternativeForm', 'P150DefinesTypicalPartsOf',
           'P190HasSymbolicContent', )


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

    p1_is_identified_by: Optional[List[E41Appellation]] = Field(
        default=None,
        description='P1 is identified by (identifies)'
    )


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

    p2_has_type: list[E55Type] = Field(default_factory=list, description='P2 has type (is type of)')


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

    p3_has_note: Optional[List[CoercedString]] = Field(default=None, description='P3 has note')


# ******************************************************************************************************************* #


class P48HasPreferredIdentifier(PropertyMixin):
    """'P48 has preferred identifier (is preferred identifier of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P48

    Domain:
        E1 CRM Entity
    Range:
        E42 Identifier
    SubProperty Of:
        E1 CRM Entity. P1 is identified by (identifies): E41 Appellation
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property records the preferred instance of E42 Identifier that was used to identify an instance of
        E1 CRM Entity at the time this property was recorded;

        More than one preferred identifier may have been assigned to an item over time;

        Use of this property requires an external mechanism for assigning temporal validity to the respective
        CIDOC CRM instance;

        The fact that an identifier is a preferred one for an organisation can be better expressed in a context
        independent form by assigning a suitable instance of E55 Type to the respective instance of
        E15 Identifier Assignment using the P2 has type property;

    Properties:
        -
    Examples:
        - the pair of Lederhosen donated by Dr Martin Doerr (E22) has preferred identifier “OXCMS:2001.1.32” (E42)
    In First Order Logic:
        P48(x,y) ⊃ E1(x)
        P48(x,y) ⊃ E42(y)
        P48(x,y) ⊃ P1(x,y)

    """

    p48_has_preferred_identifier: Optional[E42Identifier] = Field(
        default=None,
        description='P48 has preferred identifier (is preferred identifier of)'
    )


# ******************************************************************************************************************* #


class P102HasTitle(PropertyMixin):
    """'P102 has title (is title of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P102

    Domain:
        E71 Human-Made Thing
    Range:
        E35 Title
    SubProperty Of:
        E1 CRM Entity. P1 is identified by (identifies): E41 Appellation
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E35 Title has been applied to an instance of E71 Human-Made Thing;

        The P102.1 has type property of the P102 has title (is title of) property enables the relationship between the
        title and the thing to be further clarified, for example, if the title was a given title, a supplied title etc.

        It allows any human-made material or immaterial thing to be given a title. It is possible to imagine a title
        being created without a specific object in mind;

    Properties:
        P102.1 has type: E55 Type
    Examples:
        - the first book of the Old Testament (E33) has title “Genesis” (E35)
        - has type translated (E55)
    In First Order Logic:
        P102(x,y) ⊃ E71(x)
        P102(x,y) ⊃ E35(y)
        P102(x,y,z) ⊃ [P102(x,y) ∧ E55(z)]
        P102(x,y) ⊃ P1(x,y)

    """

    p102_has_title: Optional[E35Title] = Field(default=None, description='P102 has title (is title of)')


# ******************************************************************************************************************* #


class P127HasBroaderTerm(PropertyMixin):
    """'P127 has broader term (has narrower term)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P127

    Domain:
        E55 Type
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E55 Type with another instance of E55 Type that has a broader meaning;

        It allows instances of E55 Types to be organised into hierarchies. This is the sense of "broader term generic
        (BTG)" as defined in ISO 25964-2:2013;

        This property is transitive;

    Properties:
        -
    Examples:
        - dime (E55) has broader term coin (E55)
    In First Order Logic:
        P127(x,y) ⊃ E55(x)
        P127(x,y) ⊃ E55(y)

    """

    p127_has_broader_term: Optional[E55Type] = Field(
        default=None,
        description='P127 has broader term (has narrower term)'
    )


# ******************************************************************************************************************* #


class P137Exemplifies(PropertyMixin):
    """'P137 exemplifies (is exemplified by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P137

    Domain:
        E1 CRM Entity
    Range:
        E55 Type
    SubProperty Of:
        E1 CRM Entity. P2 has type (is type of): E55 Type
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E1 CRM Entity with an instance of E55 Type for which it has been
        declared to be a particularly characteristic example;

        The P137.1 in the taxonomic role property of P137 exemplifies (is exemplified by) allows differentiation of
        taxonomic roles. The taxonomic role renders the specific relationship of this example to the type, such as
        "prototypical", "archetypical", "lectotype", etc. The taxonomic role "lectotype" is not associated with the
        instance of E83 Type Creation itself, but selected in a later phase;

    Properties:
        P137.1 in the taxonomic role: E55 Type
    Examples:
        - Object BM000098044 of the Clayton Herbarium (E20) exemplifies Spigelia marilandica (L.) L. (E55) in the
          taxonomic role lectotype
    In First Order Logic:
        P137(x,y) ⊃ E1(x)
        P137(x,y) ⊃ E55(y)
        P137(x,y,z) ⊃ [P137(x,y) ∧ E55(z)]
        P137(x,y) ⊃ P2(x,y)

    """

    p137_exemplifies: Optional[List[E55Type]] = Field(
        default=None,
        description='P137 exemplifies (is exemplified by)'
    )


# ******************************************************************************************************************* #


class P139HasAlternativeForm(PropertyMixin):
    """'P139 has alternative form' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P139

    Domain:
        E41 Appellation
    Range:
        E41 Appellation
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property establishes a relationship of equivalence between two instances of E41 Appellation independent
        from any item identified by them. It is a dynamic asymmetric relationship, where the range expresses the
        derivative, if such a direction can be established. Otherwise, the relationship is symmetric. The relationship
        is not transitive;

        The equivalence applies to all cases of use of an instance of E41 Appellation. Multiple names assigned to an
        object, which are not equivalent for all things identified with a specific instance of E41 Appellation, should
        be modelled as repeated values of P1 is identified by (identifies);

        P139.1 has type allows the type of derivation, such as “transliteration from Latin 1 to ASCII” be refined..

    Properties:
        P139.1 has type: E55 Type
    Examples:
        - "Martin Doerr" (E41) has alternative form "Martin Dörr" (E41) has type Alternate spelling (E55)
        - "Гончарова, Наталья Сергеевна" (E41) has alternative form "Gončarova, Natal´â Sergeevna" (E41) has type
          ISO 9:1995 transliteration (E55)
        - “Αθήνα” has alternative form “Athina” has type transcription.
    In First Order Logic:
        P139(x,y) ⊃ E41(x)
        P139 (x,y) ⊃ E41(y)
        P139(x,y,z) ⊃ [P139(x,y) ∧ E55(z)]
        P139(x,y) ⊃ P139(y,x)

    """

    p139_has_alternative_form: Optional[E41Appellation] = Field(
        default=None,
        description='P139 has alternative form'
    )


# ******************************************************************************************************************* #


class P150DefinesTypicalPartsOf(PropertyMixin):
    """'P150 defines typical parts of (defines typical wholes for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P150

    Domain:
        E55 Type
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E55 Type “A” with an instance of E55 Type “B”, when items of type “A”
        typically form part of items of type “B”, such as “car motors” and “cars”. The property is not transitive;

        It allows types to be organised into hierarchies based on one type describing a typical part of another. This
        property is equivalent to "broader term partitive (BTP)" as defined in ISO 2788 and “broaderPartitive”
        in SKOS;

    Properties:
        -
    Examples:
        - Car motors (E55) defines typical parts of cars (E55)
    In First Order Logic:
        P150(x,y) ⊃ E55(x)
        P150(x,y) ⊃ E55(y)

    """

    p150_defines_typical_parts_of: Optional[E55Type] = Field(
        default=None,
        description='P150 defines typical parts of (defines typical wholes for)'
    )


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
