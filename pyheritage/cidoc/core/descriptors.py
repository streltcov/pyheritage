# -*- coding: utf-8 -*-

"""'Bridge entities' carry a literal value, but are fully-fledged CRM nodes;

Each is defined with its own properties, because these properties are not required by other entity models;

Module defines:
    - P72 has language
    - P190 has symbolic content
    - E41 Appellation
    - E90 Symbolic Object

"""


from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from pyheritage.cidoc.core.base import CRMEntityBase, entity_register
from pyheritage.cidoc.core.primitives import CoercedString


__all__ = ('P72HasLanguage', 'P190HasSymbolicContent', 'E90SymbolicObject', 'E42Identifier', 'E41Appellation',)


class P72HasLanguage:
    """'P72 has language' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P72

    Domain:
        - E33 Linguistic Object
    Range:
        - E56 Language
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance(s) of E33 Linguistic Object with an instance of E56 Language in which it
        is, at least partially, expressed;

        Linguistic Objects are composed in one or more human Languages. This property allows these languages to be
        documented;

    Properties:
        -
    Examples:
        - the American Declaration of Independence (E33) has language 18th Century English (E56)
    In First Order Logic:
        - P72(x,y) ⊃ E33(x)
        - P72(x,y) ⊃ E56(y)

    """
    p72_has_language: Optional[Any] = None


# ******************************************************************************************************************* #


class P190HasSymbolicContent:
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


# ******************************************************************************************************************* #


@entity_register(label="E90 Symbolic Object")
class E90SymbolicObject(P190HasSymbolicContent, CRMEntityBase):
    """E90 Symbolic Object entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E90

    SubClass Of:
        - E28 Conceptual Object
        - E72 Legal Object
    SuperClass Of:
        - E41 Appellation
        - E73 Information Object

    Scope Note:
        This class comprises identifiable symbols and any aggregation of symbols, such as characters, identifiers,
        traffic signs, emblems, texts, data sets, images, musical scores, multimedia objects, computer program code
        or mathematical formulae that have an objectively recognizable structure and that are documented as single
        units;

        It includes sets of signs of any nature, which may serve to designate something, or to communicate some
        propositional content. An instance of E90 Symbolic Object may or may not have a specific meaning, for
        example an arbitrary character string;

        In some cases, the content of an instance of E90 Symbolic Object may completely be represented by
        a serialized digital content model, such as a sequence of ASCII-encoded characters, an XML or HTML document,
        or a TIFF image. The property P3 has note and its subproperty P190 has symbolic content allow for the
        description of this content model. In order to disambiguate which symbolic level is the carrier of the
        meaning, the property P3.1 has type can be used to specify the encoding (e.g. "bit", "Latin character",
        RGB pixel);

    Examples:
        - ‘ecognizabl’
        - The “no-smoking” sign (E36)
        - “BM000038850.JPG” (E41)
        - image BM000038850.JPG from the Clayton Herbarium in London (E36)
        - The distribution of form, tone and colour found on Leonardo da Vinci’s painting named “Mona Lisa”
          in daylight (E36)
        - The Italian text of Dante’s “Divina Commedia” as found in the authoritative critical edition La Commedia
          secondo l’antica vulgata a cura di Giorgio Petrocchi, Milano: Mondadori, 1966-67 (= Le Opere di Dante
          Alighieri, Edizione Nazionale a cura della Società Dantesca Italiana, VII, 1-4) (E33)
    In First Order Logic:
        - E90(x) ⊃ E28(x)
        - E90(x) ⊃ E72(x)
    Properties:
        = P106 is composed of (forms part of): E90 Symbolic Object
        - P190 has symbolic content: E62 String

    """


# ******************************************************************************************************************* #


@entity_register(label="E41 Appellation")
class E41Appellation(P72HasLanguage, E90SymbolicObject):
    """E41 Appellation entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E41

    SubClass Of:
        - E90 Symbolic Object
    SuperClass Of:
        - E35 Title
        - E42 Identifier
        - E61 Time Primitive
        - E94 Space Primitive
        - E95 Spacetime Primitive
    Scope Note:
        This class comprises signs, either meaningful or not, or arrangements of signs following a specific syntax,
        that are used or can be used to refer to and identify a specific instance of some class or category within
        a certain context;

        Instances of E41 Appellation do not identify things by their meaning, even if they happen to have one, but
        instead by convention, tradition, or agreement. Instances of E41 Appellation are cultural constructs; as such,
        they have a context, a history, and a use in time and space by some group of users. A given instance of
        E41 Appellation can have alternative forms, i.e., other instances of E41 Appellation that are always regarded
        as equivalent independent from the thing it denotes;

        Different languages may use different appellations for the same thing, such as the names of major cities. Some
        appellations may be formulated using a valid noun phrase of a particular language. In these cases, the
        respective instances of E41 Appellation should also be declared as instances of E33 Linguistic Object. Then
        the language using the appellation can be declared with the property P72 has language: E56 Language;

        Instances of E41 Appellation may be used to identify any instance of E1 CRM Entity and sometimes are
        characteristic for instances of more specific subclasses E1 CRM Entity, such as for instances of
        E52 Time-Span (for instance “dates”), E39 Actor, E53 Place or E28 Conceptual Object. Postal addresses and
        E-mail addresses are characteristic examples of identifiers used by services transporting things between
        clients;

        Even numerically expressed identifiers for extents in space or time are also regarded as instances of
        E41 Appellation, such as Gregorian dates or spatial coordinates, even though they allow for determining some
        time or location by a known procedure starting from a reference point and by virtue of that fact play a double
        role as instances of E59 Primitive Value;

        E41 Appellation should not be confused with the act of naming something. Cf. E15 Identifier Assignment

    Examples:
        - "Martin"
        - “Aquae Sulis Minerva”
        - "the Merchant of Venice" (E35) (McCullough, 2005)
        - "Spigelia marilandica (L.) L." [not the species, just the name] (Hershberger, Jenkins and Robacker, 2015)
        - "information science" [not the science itself, but the name through which we refer to it in an
           English-speaking context]
        - “安” [Chinese “an”, meaning “peace”]
        - “6°5’29”N 45°12’13”W” (example of spatial coordinate)
        - “Black queen’s bishop 4” [chess coordinate] (example of spatial coordinate)
        - “19-MAR-1922” (example of date)
        - “+41 22 418 5571” (example of contact point)
        - "weasel@paveprime.com" (example of contact point)
        - “CH-1211, Genève” (example of place appellation)
        - “1-29-3 Otsuka, Bunkyo-ku, Tokyo, 121, Japan” (example of address)
        - “the poop deck of H.M.S Victory” (example of section definition)
        - “the Venus de Milo’s left buttock” (example of section definition)
    In First Order Logic:
        - E41(x) ⊃ E90(x)
    Properties:
        - P139 has alternative form: E41 Appellation

    """


# ******************************************************************************************************************* #


@entity_register(label="E42 Identifier")
class E42Identifier(E41Appellation):
    """E42 Identifier entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E42

    SubClass Of:
        - E41 Appellation
    SuperClass Of:
        -
    Scope Note:
        This class comprises strings or codes assigned to instances of E1 CRM Entity in order to identify them
        uniquely and permanently within the context of one or more organisations. Such codes are often known as
        inventory numbers, registration codes, etc. and are typically composed of alphanumeric sequences. Postal
        addresses, telephone numbers, urls and e-mail addresses are characteristic examples of identifiers used by
        services transporting things between clients;

        The class E42 Identifier is not normally used for machine-generated identifiers used for automated processing
        unless these are also used by human agents;

    Examples:
        - “MM.GE.195”
        - “13.45.1976”
        - “OXCMS: 1997.4.1”
        - ISSN “0041-5278”
        - ISRC “FIFIN8900116”
        - Shelf mark “Res 8 P 10”
        - “Guillaume de Machaut (1300?-1377)” [a controlled personal name heading that follows the French rules]
          (Reaney, 1974)
        - “+41 22 418 5571”
        - weasel@paveprime.com
        - “1-29-3 Otsuka, Bunkyo-ku, Tokyo, 121, Japan”
        - “Rue David Dufour 5, CH-1211, Genève”
    In First Order Logic:
        - E42(x) ⊃ E41(x)
    Properties:
        -

    """
