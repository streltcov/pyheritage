# -*- coding: utf-8 -*-

"""Actor properties: residence, contacts, membership, parentage;

(Mixin classes for entity models);

CIDOC-CRM v7.0

------------------------------------------------
Properties
------------------------------------------------
P74  has current or former residence  E39 -> E53
P75  possesses                        E39 -> E30
P76  has contact point                E39 -> E41
P107 has current or former member     E74 -> E39
P152 has parent                       E21 -> E21

"""


from typing import Optional

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


__all__ = ('P74HasCurrentOrFormerResidence', 'P75Possesses', 'P76HasContactPoint', 'P107HasCurrentOrFormerMember',
           'P152HasParent', )


class P74HasCurrentOrFormerResidence(PropertyMixin):
    """'P74 has current or former residence (is current or former residence of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P74

    Domain:
        E39 Actor
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the current or former place of residence (an instance of E53 Place) of an instance of
        E39 Actor;

        The residence may be either the place where the actor resides, or a legally registered address of any kind;

    Properties:
        -
    Examples:
        - Queen Elizabeth II (E39) has current or former residence Buckingham Palace (E53)
    In First Order Logic:
        P74(x,y) ⊃ E39(x)
        P74(x,y) ⊃ E53(y)

    """

    p74_has_current_of_former_residence: Optional[str] = Field(
        default=None,
        description='P74 has current or former residence (is current or former residence of)'
    )


# ******************************************************************************************************************* #


class P75Possesses(PropertyMixin):
    """'P75 possesses (is possessed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P75

    Domain:
        E39 Actor
    Range:
        E30 Right
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E39 Actor to an instance of E30 Right over which the actor holds or
        has held a legal claim;

    Properties:
        -
    Examples:
        - Michael Jackson (E21) possesses Intellectual property rights on the Beatles’ back catalogue (E30)
    In First Order Logic:
        P75(x,y) ⊃ E39(x)
        P75(x,y) ⊃ E30(y)

    """

    p75_possesses: Optional[str] = Field(default=None, description='P75 possesses (is possessed by)')


# ******************************************************************************************************************* #


class P76HasContactPoint(PropertyMixin):
    """'P76 has contact point (provides access to)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P76

    Domain:
        E39 Actor
    Range:
        E41 Appellation
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E39 Actor to an instance of E41 Appellation which a communication
        service uses to direct communications to this actor, such as an e-mail address, fax number, or postal address;

    Properties:
        -
    Examples:
        - RLG (E40) has contact point “bl.ric@rlg.org” (E41)
    In First Order Logic:
        P76(x,y) ⊃ E39(x)
        P76(x,y) ⊃ E41(y)

    """

    p76_has_contact_point: Optional[str] = Field(default=None, description='P76 has contact point'
                                                                           ' (provides access to)')


# ******************************************************************************************************************* #


class P107HasCurrentOrFormerMember(PropertyMixin):
    """'P107 has current or former member (is current or former member of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P107

    Domain:
        E74 Group
    Range:
        E39 Actor
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E74 Group with an instance of E39 Actor that is or has been a member
        thereof;

        Instances of E74 Grous and E21 Person, may all be members of instances of E74 Group.An instance of E74 Group
        may be founded initially without any member;

        This property is a shortcut of the more fully developed path E74 Group , P144i gained member by, E85 Joining,
        P143 joined , E39 Actor;

        The property P107.1 kind of member can be used to specify the type of membership or the role the member has in
        the group;

    Properties:
        P107.1 kind of member: E55 Type
    Examples:
        - Moholy Nagy (E21) is current or former member of Bauhaus (E74)
        - National Museum of Science and Industry (E74) has current or former member The National Railway Museum (E74)
        - The married couple Queen Elisabeth and Prince Phillip (E74) has current or former member Prince Phillip
          (E21) with P107.1 kind of member husband (E55 Type)
    In First Order Logic:
        P107(x,y) ⊃ E74(x)
        P107(x,y) ⊃ E39(y)
        P107(x,y,z) ⊃ [P107(x,y) ∧ E55(z)]

    """

    p107_has_current_or_former_member: Optional[str] = Field(
        default=None,
        description='P107 has current or former member (is current or former member of)'
    )


# ******************************************************************************************************************* #


class P152HasParent(PropertyMixin):
    """'P152 has parent (is parent of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P152

    Domain:
        E21 Person
    Range:
        E21 Person
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (2,n:0:n)

    Scope Note:
        This property associates an instance of E21 Person with another instance of E21 Person who plays the role of
        the first instance’s parent, regardless of whether the relationship is biological parenthood, assumed or
        pretended biological parenthood or an equivalent legal status of rights and obligations obtained by a social
        or legal act. This property is, among others, a shortcut of the fully developed paths from ‘E21Person’ through
        ‘P98i was born’, ‘E67 Birth’, ‘P96 by mother’ to ‘E21 Person’, and from ‘E21Person’ through ‘P98i was born’,
        ‘E67 Birth’, ‘P97 from father’ to ‘E21 Person’;

        This property is not transitive;

    Properties:
        -
    Examples:
        - Gaius Octavius (E29) has parent Julius Caesar (E29)
        - Steve Jobs (E29) has parent Joanne Simpson (biological mother)(E29)
        - Steve Jobs (E29) has parent Clara Jobs (adoption mother) (E29)ZWSP
    In First Order Logic:
        P152(x,y) ⊃ E21(x)
        P152(x,y) ⊃ E21(y)

    """

    p152_has_parent: Optional[str] = Field(default=None, description='P152 has parent (is parent of)')
