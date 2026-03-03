# -*- coding: utf-8 -*-

"""'Bridge entities' carry a literal value, but are fully-fledged CRM nodes;

Each is defined with its own properties, because these properties are not required by other entity models;

Module defines:
    - P2 has type (is type of)
    - P72 has language
    - P90 has value
    - P91 has unit (is unit of)
    - P190 has symbolic content
    - E41 Appellation
    - E52 Time Span
    - E54 Dimension
    - E90 Symbolic Object

"""


from __future__ import annotations

from typing import Any, Optional

from pydantic import Field

from pyheritage.cidoc.core.base import CRMEntityBase, entity_register
from pyheritage.cidoc.core.primitives import CoercedNumber, CoercedString


__all__ = ('P72HasLanguage', 'P190HasSymbolicContent', 'E90SymbolicObject', 'E42Identifier', 'E41Appellation',)


class P2HasType:
    """'P2 has type (is type of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P2

    Domain:
        - E1 CRM Entity
    Range:
        - E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        - E1 CRM Entity. P137 exemplifies (is exemplified by): E55 Type
        - E13 Attribute Assignment. P177 assigned property type: E55 Type
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
        - P2(x,y) ⊃ E1(x)
        - P2(x,y) ⊃ E55(y)

    """

    p2_has_type: list[Any] = Field(default_factory=list)


# ******************************************************************************************************************* #


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

    p72_has_language: Optional[Any] = Field(default=None)


# ******************************************************************************************************************* #


class P82AtSomeTimeWithin:
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


class P86FallsWithin:
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


class P90HasValue:
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


class P91HasUnit:
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


class P191HadDuration:
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


# ******************************************************************************************************************* #


@entity_register(label="E54 Dimension")
class E54Dimension(P90HasValue, P91HasUnit, P2HasType, CRMEntityBase):
    """'E54 Dimension' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E54

    SubClass Of:
        - E1 CRM Entity
    SuperClass Of:
        - E97 Monetary Amount
    Scope Note:
        This class comprises quantifiable properties that can be measured by some calibrated means and can be
        approximated by values, i.e. points or regions in a mathematical or conceptual space, such as natural or real
        numbers, RGB values etc;

        An instance of E54 Dimension represents the true quantity, independent from its numerical approximation,
        e.g. in inches or in cm. The properties of the class E54 Dimension allow for expressing the numerical
        approximation of the values of instances of E54 Dimension. If the true values belong to a non-discrete
        space, such as spatial distances, it is recommended to record them as approximations by intervals or regions
        of indeterminacy enclosing the assumed true values. For instance, a length of 5 cm may be recorded as
        4.5-5.5 cm, according to the precision of the respective observation. Note, that interoperability of values
        described in different units depends critically on the representation as value regions;

        Numerical approximations in archaic instances of E58 Measurement Unit used in historical records should be
        preserved. Equivalents corresponding to current knowledge should be recorded as additional instances of
        E54 Dimension as appropriate;

    Examples:
        - The 250 metric ton weight of the Luxor Obelisk
        - The 5.17 m height of the statue of David by Michaelangelo
        - The 530.2 carats of the Great Star of Africa diamond
        - The AD1262-1312, 1303-1384 calibrated C14 date for the Shroud of Turin
        - The 33 m diameter of the Stonehenge Sarcen Circle
        - The 755.9 foot length of the sides of the Great Pyramid at Giza
        - Christies’ hammer price for “Vase with Fifteen Sunflowers” (E97) has currency British Pounds (E98)
        - The time span of the Battle of Issos 333 B.C.E. (E52) had duration Battle of Issos duration (E54)
    In First Order Logic:
        - E54(x) ⊃ E1(x)
    Properties:
        - P90 has value: E60 Number
        - P91 has unit (is unit of): E58 Measurement Unit

    """


# ******************************************************************************************************************* #


@entity_register(label="E97 Monetary Amount")
class E97MonetaryAmount(E54Dimension):
    """'E97 Monetary Amount' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E97

    SubClass Of:
        - E54 Dimension
    SuperClass Of:
        -
    Scope Note:
        This class comprises quantities of monetary possessions or obligations in terms of their nominal value with
        respect to a particular currency. These quantities may be abstract accounting units, the nominal value of
        a heap of coins or bank notes at the time of validity of the respective currency, the nominal value of a bill
        of exchange or other documents expressing monetary claims or obligations. It specifically excludes amounts
        expressed in terms of weights of valuable items, like gold and diamonds, and quantities of other non-currency
        items, like goats or stocks and bonds;

    Examples:
        - Christies’ hammer price for “Vase with Fifteen Sunflowers” (E97) has currency British Pounds (E98)
    In First Order Logic:
        - E97(x) ⊃ E54(x)
    Properties:
        - P180 has currency (was currency of): E98 Currency
        - P181 has amount: E60 Number

    """


# ******************************************************************************************************************* #


@entity_register(label="E52 Time-Span")
class E52TimeSpan(P82AtSomeTimeWithin, P86FallsWithin, P191HadDuration, CRMEntityBase):
    """'E52 Time Span' CRM entity model;

    SubClass Of:
        - E1 CRM Entity
    SuperClass Of:1
        -
    Scope Note:
        This class comprises abstract temporal extents, in the sense of Galilean physics, having a beginning, an end
         and a duration;

        Instances of E52 Time-Span have no semantic connotations about phenomena happening within the temporal extent
        they represent. They do not convey any meaning other than a positioning on the “time-line” of chronology. The
        actual extent of an instance of E52 Time-Span can be approximated by properties of E52 Time-Span giving inner
        and outer bounds in the form of dates (instances of E61 Time Primitive). Comparing knowledge about time-spans
        is fundamental for chronological reasoning;

        Some instances of E52 Time-Span may be defined as the actual, in principle observable, temporal extent of
        instances of E2 Temporal Entity via the property P4 has time-span (is time-span of): E52 Time-Span. They
        constitute phenomenal time-spans as defined in CRMgeo (Doerr and Hiebel 2013). Since our knowledge of history
        is imperfect and physical phenomena are fuzzy in nature, the extent of phenomenal time-spans can only be
        described in approximation. An extreme case of approximation, might, for example, define an instance of
        E52 Time-Span having unknown beginning, end and duration. It may, nevertheless, be associated with other
        descriptions by which we can infer knowledge about it, such as in relative chronologies;

        Some instances of E52 may be defined precisely as representing a declaration of a temporal extent, as, for
        instance, done in a business contract. They constitute declarative time-spans as defined in CRMgeo (Doerr and
        Hiebel 2013) and can be described via the property E61 Time Primitive P170 defines time
        (time is defined by): E52 Time-Span;

        When used as a common E52 Time-Span for two events, it will nevertheless describe them as being simultaneous,
        even if nothing else is known;

    Examples:
        - 1961
        - From 12-17-1993 to 12-8-1996
        - 14h30 – 16h22 4th July 1945
        - 9.30 am 1.1.1999 to 2.00 pm 1.1.1999
        - duration of the Ming Dynasty (Chan, 2011)
    In First Order Logic:
        - E52(x) ⊃ E1(x)
    Properties:
        - P79 beginning is qualified by: E62 String
        - P80 end is qualified by: E62 String
        - P81 ongoing throughout: E61 Time Primitive
        - P82 at some time within: E61 Time Primitive
        - P86 falls within (contains): E52 Time-Span
        - P191 had duration (was duration of): E54 Dimension

    """
