# -*- coding: utf-8 -*-

"""Conceptual object properties: content, language, rights, structure;

(Mixin classes for entity models);

CIDOC-CRM v7.0

---------------------------------------------
Properties
---------------------------------------------
P67  refers to                     E89 -> E1
P68  foresees use of               E29 -> E57
P69  has association with          E29 -> E29
P70  documents                     E31 -> E1
P71  lists                         E32 -> E55
P72  has language                  E33 -> E56
P73  has translation               E33 -> E33
P104 is subject to                 E72 -> E30
P105 right held by                 E72 -> E39
P106 is composed of                E90 -> E90
P129 is about                      E89 -> E1
P138 represents                    E36 -> E1
P148 has component                 E89 -> E89
P165 incorporates                  E73 -> E90
P187 has production plan           E99 -> E29
P188 requires production tool      E99 -> E19

"""


from typing import Any, Optional

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


__all__ = ('P67RefersTo', 'P68ForeseesUseOf', 'P69HasAssociationWith', 'P70Documents', 'P71Lists', 'P72HasLanguage',
           'P73HasTranslation', 'P104IsSubjectTo', 'P105RightHeldBy', 'P106IsComposedOf', 'P129IsAbout',
           'P138Represents', 'P148HasComponent', 'P165Incorporates', 'P187HasProductionPlan',
           'P188RequiresProductionTool', )


class P67RefersTo(PropertyMixin):
    """'P67 refers to (is referred to by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P67

    Domain:
        E89 Propositional Object
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        E29 Design or Procedure. P68 foresees use of (use foreseen by): E57 Material
        E31 Document. P70 documents (is documented in): E1 CRM Entity
        E32 Authority Document. P71 lists (is listed in): E1 CRM Entity
        E89 Propositional Object. P129 is about (is subject of): E1 CRM Entity
        E36 Visual Item. P138 represents (has representation): E1 CRM Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property documents that an instance of E89 Propositional Object makes a statement about an instance of
        E1 CRM Entity. P67 refers to (is referred to by) has the P67.1 has type link to an instance of E55 Type. This
        is intended to allow a more detailed description of the type of reference. This differs from P129 is about
        (is subject of), which describes the primary subject or subjects of the instance of E89 Propositional Object;

    Properties:
        P67.1 has type: E55 Type
    Examples:
        - the eBay auction listing of 4 July 2002 (E73) refers to silver cup 232 (E22) has type item for sale (E55)
    In First Order Logic:
        P67(x,y) ⊃ E89(x)
        P67(x,y) ⊃ E1(y)
        P67(x,y,z) ⊃ [P67(x,y) ∧ E55(z)]

    """

    p67_refers_to: Optional[str] = Field(default=None, description='P67 refers to (is referred to by)')


# ******************************************************************************************************************* #


class P68ForeseesUseOf(PropertyMixin):
    """'P68 foresees use of (use foreseen by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P68

    Domain:
        E29 Design or Procedure
    Range:
        E57 Material
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of E57 Material foreseen to be used by an instance of E29 Design or
        Procedure;

        E29 Designs and procedures commonly foresee the use of particular instances of E57 Material. The fabrication
        of adobe bricks, for example, requires straw, clay and water. This property enables this to be documented;

        This property is not intended for the documentation of instances of E57 Materials that were used on
        a particular occasion when an instance of E29 Design or Procedure was executed;

    Properties:
        -
    Examples:
        - procedure for soda glass manufacture (E29) foresees use of soda (E57)
    In First Order Logic:
        P68(x,y) ⊃ E29(x)
        P68(x,y) ⊃ E57(y)
        P68(x,y) ⊃ P67(x,y)

    """

    p68_foresees_use_of: Optional[str] = Field(default=None, description='P68 foresees use of (use foreseen by)')


# ******************************************************************************************************************* #


class P69HasAssociationWith(PropertyMixin):
    """'P69 has association with (is associated with)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P69

    Domain:
        E29 Design or Procedure
    Range:
        E29 Design or Procedure
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property generalises relationships like whole-part, sequence, prerequisite or inspired by between
        instances of E29 Design or Procedure. Any instance of E29 Design or Procedure may be associated with other
        designs or procedures. The property is considered to be symmetrical unless otherwise indicated by
        P69.1 has type;

        The P69.1 has type property of P69 has association with allows the nature of the association to be specified
        reading from domain to range; examples of types of association between instances of E29 Design or Procedure
        include: has part, follows, requires, etc.

        The property can typically be used to model the decomposition of the description of a complete workflow into
        a series of separate procedures;

        This property is not transitive;

    Properties:
        P69.1 has type: E55 Type
    Examples:
        - Procedure for glass blowing (E29) has association with procedure for glass heating (E29)
        - The set of instructions for performing Macbeth in Max Reinhardt's production in 1916 in Berlin at Deutsches
          Theater (E29) has association with the scene design drawing by Ernst Stern reproduced at
          http://www.glopad.org/pi/fr/record/digdoc/1003814 (E29) has type has part (E55)
        - Preparation of parchment (E29) has association with soaking and unhairing of skin (E29) has type ‘has part’
          (E55). Preparation of parchment (E29) has association with stretching of skin (E29) has type ‘has part’
          (E55). Stretching of skin (E29) has association with soaking and unhairing of skin (E29) has type
          ‘follows’ (E55).
        - The plan for reassembling the temples at Abu Simbel (E29) has association with the plan for storing and
          transporting the blocks (E29) has type 'follows' (E55)'.
    In First Order Logic:
        P69 (x,y) ⊃ E29(x)
        P69 (x,y) ⊃ E29(y)
        P69(x,y,z) ⊃ [P69(x,y) ∧ E55(z)]
        P69(x,y) ⊃P69(y,x)

    """

    p69_has_association_with: Optional[str] = Field(
        default=None,
        description='P69 has association with (is associated with)',
    )


# ******************************************************************************************************************* #


class P70Documents(PropertyMixin):
    """'P70 documents (is documented in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P70

    Domain:
        E31 Document
    Range:
        E1 CRM Entity
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property describes the CRM Entities documented as instances of E31 Document;

        Documents may describe any conceivable entity, hence the link to the highest-level entity in the CIDOC CRM
        class hierarchy. This property is intended for cases where a reference is regarded as making a proposition
        about reality. This may be of a documentary character, in the scholarly or scientific sense, or a more general
        statement;

    Properties:
        -
    Examples:
        - the British Museum catalogue (E31) documents the British Museum’s Collection (E78)
    In First Order Logic:
        P70 (x,y) ⊃ E31(x)
        P70 (x,y) ⊃ E1(y)
        P70(x,y) ⊃ P67(x,y)

    """

    p70_documents: Optional[str] = Field(default=None, description='P70 documents (is documented in)')


# ******************************************************************************************************************* #


class P71Lists(PropertyMixin):
    """'P71 lists (is listed in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P71

    Domain:
        E32 Authority Document
    Range:
        E1 CRM Entity
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E32 Authority Document, with an instance of E1 CRM Entity which it
        lists for reference purposes;

    Properties:
        -
    Examples:
        - the Art & Architecture Thesaurus (E32) lists alcazars (E55)
    In First Order Logic:
        P71(x,y) ⊃ E32(x)
        P71(x,y) ⊃ E1(y)
        P71(x,y) ⊃ P67(x,y)

    """

    p71_lists: Optional[str] = Field(default=None, description='P71 lists (is listed in)')


# ******************************************************************************************************************* #


class P72HasLanguage(PropertyMixin):
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


class P73HasTranslation(PropertyMixin):
    """'P73 has translation (is translation of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P73

    Domain:
        E33 Linguistic Object
    Range:
        E33 Linguistic Object
    SubProperty Of:
        E70 Thing. P130i features are also found on (shows features of): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property links an instance of E33 Linguistic Object (A), to another instance of E33 Linguistic Object (B)
        which is the translation of A;

        When an instance of E33 Linguistic Object is translated into a new language a new instance of
        E33 Linguistic Object is created, despite the translation being conceptually similar to the source;

        This property is transitive;

    Properties:
        -
    Examples:
        - “Les Baigneurs” (E33) has translation “The Bathers” (E33)
    In First Order Logic:
        P73(x,y) ⊃ E33(x)
        P73(x,y) ⊃ E33(y)
        P73(x,y) ⊃ P130(y,x)

    """

    p73_has_translation: Optional[str] = Field(default=None, description='P73 has translation (is translation of)')


# ******************************************************************************************************************* #


class P104IsSubjectTo(PropertyMixin):
    """'P104 is subject to (applies to)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P104

    Domain:
        E72 Legal Object
    Range:
        E30 Right
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property links a particular instance of E72 Legal Object to the instances of E30 Right to which it is
        subject;

        The Right is held by an E39 Actor as described by P75 possesses (is possessed by);

    Properties:
        -
    Examples:
        - Beatles back catalogue (E72) is subject to reproduction right on Beatles back catalogue (E30)
    In First Order Logic:
        P104(x,y) ⊃ E72(x)
        P104(x,y) ⊃ E30(y)

    """

    p104_is_subject_to: Optional[str] = Field(default=None, description='P104 is subject to (applies to)')


# ******************************************************************************************************************* #


class P105RightHeldBy(PropertyMixin):
    """'P105 right held by (has right on)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P105

    Domain:
        E72 Legal Object
    Range:
        E39 Actor
    SubProperty Of:
        -
    SuperProperty Of:
        E18 Physical Thing. P52 has current owner (is current owner of): E39 Actor
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor who holds the instances of E30 Right to an instance of
        E72 Legal Object;

        It is a superproperty of P52 has current owner (is current owner of) because ownership is a right that is held
        on the owned object;

        P105 right held by (has right on) is a shortcut of the fully developed path E72 Legal Object,P104 is subject
        to, E30 Right, P75i is possessed by, E39 Actor;

    Properties:
        -
    Examples:
        - Beatles back catalogue (E73) right held by Michael Jackson (E21)
    In First Order Logic:
        P105(x,y) ⊃ E72(x)
        P105(x,y) ⊃ E39(y)

    """

    p105_right_held_by: Optional[str] = Field(default=None, description='P105 right held by (has right on)')


# ******************************************************************************************************************* #


class P106IsComposedOf(PropertyMixin):
    """'P106 is composed of (forms part of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P106

    Domain:
        E90 Symbolic Object
    Range:
        E90 Symbolic Object
    SubProperty Of:
        -
    SuperProperty Of:
        E73 Information Object. P165 incorporates (is incorporated in): E90 Symbolic Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E90 Symbolic Object with a part of it that is by itself an instance of
        E90 Symbolic Object, such as fragments of texts or clippings from an image;

        This property is transitive;

    Properties:
        -
    Examples:
        - This Scope note P106 (E33) is composed of fragments of texts (E33)
        - ‘recognizable’ P106 (E90) is composed of ‘ecognizabl’ (E90)
    In First Order Logic:
        P106(x,y) ⊃ E90(x)
        P106(x,y) ⊃ E90(y)

    """

    p106_is_composed_of: Optional[str] = Field(default=None, description='P106 is composed of (forms part of)')


# ******************************************************************************************************************* #


class P129IsAbout(PropertyMixin):
    """'P129 is about (is subject of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P129

    Domain:
        E89 Propositional Object
    Range:
        E1 CRM Entity
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property documents that an instance of E89 Propositional Object has as subject an instance of
        E1 CRM Entity;

        This differs from P67 refers to (is referred to by), which refers to an instance of E1 CRM Entity, in that it
        describes the primary subject or subjects of an instance of E89 Propositional Object;

    Properties:
        -
    Examples:
        - The text entitled ‘Reach for the sky’ (E33) is about Douglas Bader (E21)
    In First Order Logic:
        P129(x,y) ⊃ E89(x)
        P129(x,y) ⊃ E1(y)
        P129(x,y) ⊃ P67(x,y)

    """

    p129_is_about: Optional[str] = Field(default=None, description='P129 is about (is subject of)')


# ******************************************************************************************************************* #


class P138Represents(PropertyMixin):
    """'P138 represents (has representation)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P138

    Domain:
        E36 Visual Item
    Range:
        E1 CRM Entity
    SubProperty Of:
        E89 Propositional Object. P67 refers to (is referred to by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property establishes the relationship between an instance of E36 Visual Item and the instance of
        E1 CRM Entity that it visually represents;

        Any entity may be represented visually. This property is part of the fully developed path from
        E24 Physical Human-Made Thing through P65 shows visual item (is shown by), E36 Visual Item,
        P138 represents (has representation) to E1 CRM Entity, which is shortcut by P62depicts (is depicted by);
        P138.1 mode of representation allows the nature of the representation to be refined;

        This property is also used for the relationship between an original and a digitisation of the original by the
        use of techniques such as digital photography, flatbed or infrared scanning. Digitisation is here seen as
        a process with a mechanical, causal component rendering the spatial distribution of structural and optical
        properties of the original and does not necessarily include any visual similarity identifiable by
        human observation."

    Properties:
        P138.1 mode of representation: E55 Type
    Examples:
        - the digital file found at http://www.emunch.no/N/full/No-MM_N0001-01.jpg (E36) represents page 1 of
          Edward Munch's manuscript MM N 1, Munch-museet (E22) mode of representation Digitisation(E55)
        - The 3D model VAM_A.200-1946_trace_1M.ply (E73) represents Victoria & Albert Museum’s Madonna and child
          sculpture (visual work) A.200-1946 (E22) mode of representation 3D surface (E55)
    In First Order Logic:
        P138(x,y) ⊃ E36(x)
        P138(x,y) ⊃ E1(y)
        P138(x,y,z) ⊃ [P138(x,y) ∧ E55(z)]
        P138(x,y) ⊃ P67(x,y)

    """

    p138_represents: Optional[str] = Field(default=None, description='P138 represents (has representation)')


# ******************************************************************************************************************* #


class P148HasComponent(PropertyMixin):
    """'P148 has component (is component of)' CRM  property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P148

    Domain:
        E89 Propositional Object
    Range:
        E89 Propositional Object
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (0:n,0:n)

    Scope Note:
        This property associates an instance of E89 Propositional Object with a structural part of it that is by
        itself an instance of E89 Propositional Object;

        This property is transitive

    Properties:
        -
    Examples:
        - Dante’s “Divine Comedy” (E89) has component Dante’s “Hell” (E89)
    In First Order Logic:
        P148(x,y) ⊃ E89(x)
        P148(x,y) ⊃ E89(y)

    """

    p148_has_component: Optional[str] = Field(default=None, description='P148 has component (is component of)')


# ******************************************************************************************************************* #


class P165Incorporates(PropertyMixin):
    """'P165 incorporates (is incorporated in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P165

    Domain:
        E73 Information Object
    Range:
        E90 Symbolic Object
    SubProperty Of:
        E90 Symbolic Object. P106 is composed of (forms part of): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        (0,n :0,n)

    Scope Note:
        This property associates an instance of E73 Information Object with an instance of E90 Symbolic Object (or any
        of its subclasses) that was included in it;

        This property makes it possible to recognise the autonomous status of the incorporated signs, which were
        created in a distinct context, and can be incorporated in many distinct self-contained expressions, and to
        highlight the difference between structural and accidental whole-part relationships between conceptual
        entities;

        It accounts for many cultural facts that are quite frequent and significant: the inclusion of a poem in
        an anthology, the re-use of an operatic aria in a new opera, the use of a reproduction of a painting for
        a book cover or a CD booklet, the integration of textual quotations, the presence of lyrics in a song that
        sets those lyrics to music, the presence of the text of a play in a movie based on that play, etc.;

        In particular, this property allows for modelling relationships of different levels of symbolic specificity,
        such as the natural language words making up a particular text, the characters making up the words and
        punctuation, the choice of fonts and page layout for the characters;

        When restricted to information objects, that is, seen as a property with E73 Information Object as domain and
        range the property is transitive;

        A digital photograph of a manuscript page incorporates the text of a manuscript page, if the respective text
        is defined as a sequence of symbols of a particular type, such as Latin characters, and the resolution and
        quality of the digital image is sufficient to resolve these symbols so they are readable on the digital image;

    Properties:
        -
    Examples:
        - The content of Charles-Moïse Briquet’s ‘Les Filigranes: dictionnaire historique des marques du papier’ (E32)
          P165 incorporates the visual aspect of the watermark used around 1358-61 by some Spanish papermaker(s) and
          identified as ‘Briquet 4019’ (E37)
        - The visual content of Jacopo Amigoni’s painting known as ‘The Singer Farinelli and friends’ (E36)
          P165 incorporates the musical notation of Farinelli’s musical work entitled ‘La Partenza’ (E73)
        - The visual content of Nicolas Poussin’s painting entitled ‘Les Bergers d’Arcadie’ (E36) P165 incorporates
          the Latin phrase ‘Et in Arcadia ego’ (E33)
    In First Order Logic:
        P165(x,y) ⊃ E73(x)
        P165(x,y) ⊃ E90(y)
        P165(x,y) ⊃ P106(x,y)

    """

    p165_incorporates: Optional[str] = Field(default=None, description='P165 incorporates (is incorporated in)')


# ******************************************************************************************************************* #


class P187HasProductionPlan(PropertyMixin):
    """'P187 has production plan (is production plan for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P187

    Domain:
        E99 Product Type
    Range:
        E29 Design or Procedure
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many (1,n:1,1)

    Scope Note:
        This property associates an instance of E99 Product Type with an instance of E29 Design or Procedure that
        completely determines the production of instances of E18 Physical Thing. The resulting instances of
        E18 Physical Thing are considered exemplars of this instance of E99 Product Type when the process specified
        is correctly executed. Note that the respective instance of E29 Design or Procedure may not necessarily be
        fixed in a written/graphical form, and may require the use of tools or models unique to the product type. The
        same instance of E99 Product Type may be associated with several variant plans;

    Properties:
        -
    Examples:
        - the production plans (E29) for Volkswagen Type 11 (Beetle) (E99)
    In First Order Logic:
        P187(x,y) ⊃ E99(x)
        P187(x,y) ⊃ E29(y)

    """

    p187_has_production_plan: Optional[str] = Field(
        default=None,
        description='P187 has production plan (is production plan for)'
    )


# ******************************************************************************************************************* #


class P188RequiresProductionTool(PropertyMixin):
    """'P188 requires production tool (is production tool for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P188

    Domain:
        E99 Product Type
    Range:
        E19 Physical Object
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many (1,n:1,1)

    Scope Note:
        This property associates an instance of E99 Product Type with an instance of E19 Physical Object that is
        needed for the production of an instance of E18 Physical Thing. When the process of production is correctly
        executed in accordance with the plan and using the specified instance of E19 Physical Object, the resulting
        instance of E18 Physical Thing is considered an exemplar of this instance of E99 Product Type. The instance of
        E19 Physical Object may bear distinct features that are transformed into characteristic features of the
        resulting instance of E18 Physical Thing. Examples include models and mouldsl

    Properties:
        -
    Examples:
        - the luggage compartment lid mould (E19) for the Volkswagen Type 11 (Beetle) (E99)
          (https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Volkswagen_Type_1_
          (Auto_classique_St._Lazare_%2710).jpg/220px-Volkswagen_Type_1_(Auto_classique_St._Lazare_%2710).jpg)
    In First Order Logic:
        P188(x,y) ⊃ E99(x)
        P188(x,y) ⊃ E19(y)

    """

    p188_requires_production_tool: Optional[str] = Field(
        default=None,
        description='P188 requires production tool (is production tool for)'
    )
