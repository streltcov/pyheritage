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
           'P73HasTranslation', )


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
