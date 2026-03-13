# -*- coding: utf-8 -*-

"""Temporal CRM properties (mixin classes for entity models);

CIDOC-CRM v7.0

----------------------------------------------
Properties
----------------------------------------------
P4   has time-span                  E2  -> E52
P5   consists of                    E3  -> E3
P7   took place at                  E4  -> E53
P8   took place on or within        E4  -> E18
P9   consists of                    E4  -> E4
P10  falls within                   E4  -> E4
P11  had participant                E5  -> E39
P12  occurred in the presence of    E5  -> E77
P14  carried out by                 E7  -> E39
P15  was influenced by              E7  -> E1
P16  used specific object           E7  -> E70
P17  was motivated by               E7  -> E1
P19  was intended use of            E7  -> E71
P20  had specific purpose           E7  -> E55
P21  had general purpose            E7  -> E55
P22  transferred title to           E8  -> E39
P23  transferred title from         E8  -> E39
P24  transferred title of           E8  -> E18
P25  moved                          E9  -> E19
P26  moved to                       E9  -> E53
P27  moved from                     E9  -> E53
P28  custody surrendered by         E10 -> E39
P29  custody received by            E10 -> E39
P30  transferred custody of         E10 -> E18
P31  has modified                   E11 -> E18
P32  used general technique         E7  -> E55
P33  used specific technique        E11 -> E29
P34  concerned                      E14 -> E18
P35  has identified                 E14 -> E3
P37  assigned                       E15 -> E42
P39  measured                       E16 -> E18
P40  observed dimension             E16 -> E54
P41  classified                     E17 -> E1
P42  assigned                       E17 -> E55
P92  brought into existence         E63 -> E77
P93  took out of existence          E64 -> E77
P94  has created                    E65 -> E28
P95  has formed                     E66 -> E74
P96  by mother                      E67 -> E21
P97  from father                    E67 -> E21
P98  brought into life              E67 -> E21
P99  dissolved                      E68 -> E74
P100 was death of                   E69 -> E21
P108 has produced                   E12 -> E24
P110 augmented                      E79 -> E24
P111 added                          E79 -> E18
P112 diminished                     E80 -> E24
P113 removed                        E80 -> E18
P123 resulted in                    E81 -> E77
P124 transformed                    E81 -> E77
P125 influenced                     E7  -> E1
P126 employed                       E7  -> E55
P134 continued                      E7  -> E7
P135 created type                   E65 -> E55
P136 was based on                   E13 -> E1
P140 assigned attribute to          E13 -> E1
P141 assigned                       E13 -> E1
P142 used constituent               E15 -> E90
P143 joined                         E85 -> E39
P144 joined with                    E85 -> E74
P145 separated                      E86 -> E39
P146 separated from                 E86 -> E74
P147 curated                        E87 -> E78
P151 was formed from                E66 -> E74
P173 starts before or with end of   E2  -> E2
P174 starts before or with start    E2  -> E2
P175 starts after or with start     E2  -> E2
P176 starts after or with end       E2  -> E2
P177 assigned property type         E13 -> E55
P179 had sales price                E96 -> E97
P182 ends before or with start      E2  -> E2
P183 ends before or with end        E2  -> E2
P184 ends after or with start       E2  -> E2
P185 ends after or with end         E2  -> E2
P186 produced thing of product type E12 -> E99

"""


from __future__ import annotations

from typing import Optional

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


__all__ = ('P4HasTimeSpan', 'P5ConsistsOf', 'P7TookPlaceAt', 'P8TookPlaceOnOrWithin', 'P9ConsistsOf',
           'P10FallsWithin', 'P11HadParticipant', 'P12OccurredInPresenceOf', 'P13Destroyed', 'P14CarriedOutBy',
           'P15WasInfluencedBy', 'P16UsedSpecificObject', 'P17WasMotivatedBy', 'P19WasIntendedUseOf',
           'P20HadSpecificPurpose', 'P21HadGeneralPurpose', 'P22TransferredTitleTo', 'P23TransferredTitleFrom',
           'P24TransferredTitleOf', 'P25Moved', 'P26MovedTo', 'P27MovedFrom', 'P28CustodySurrenderedBy',
           'P29CustodyReceivedBy', 'P30TransferredCustodyOf', 'P31HasModified', 'P32UsedGeneralTechnique',
           'P33UsedSpecificTechnique', 'P34Concerned', 'P35Identified', 'P37Assigned', 'P38Deassigned',
           'P39Measured', 'P40ObservedDimension', 'P41Classified', 'P42Assigned', 'P92BroughtIntoExistence',
           'P93TookOutOfExistence', 'P94HasCreated', 'P95HasFormed', 'P96ByMother', 'P97FromFather',
           'P98BroughtIntoLife', 'P99Dissolved', 'P100WasDeathOf', 'P108HasProduced', 'P110Augmented', 'P111Added',
           'P112Diminished', 'P113Removed', 'P123ResultedIn', 'P124Transformed', 'P125UsedObjectOfType',
           'P126Employed', 'P134Continued', 'P135CreatedType', 'P136WasBasedOn', 'P140AssignedAttributeTo',
           'P141Assigned', 'P142UsedConstituent', 'P143Joined', 'P144JoinedWith', 'P145Separated',
           'P146SeparatedFrom', 'P147Curated', 'P151WasFormedFrom', 'P173StartsBeforeOrWithTheEndOf',
           'P174StartsBeforeTheEndOf', 'P175StartsBeforeOrWithTheStartOf', 'P176StartsBeforeTheStartOf',
           'P177AssignedPropertyType', 'P179HadSalesPrice', 'P182EndsBeforeOrWitheStartOf',
           'P183EndsBeforeTheStartOf', 'P184EndsBeforeOrWithTheEndOf', 'P185EndsBeforeTheEndOf',
           'P186ProducedThingOfProductType', )


class P4HasTimeSpan(PropertyMixin):
    """'P4 has time span (is time-span of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P4

    Domain:
        E2 Temporal Entity
    Range:
        E52 Time-Span
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one(0,1:0,n)

    Scope Note:
        This property associates an instance of E2 Temporal Entity with the instance of E52 Time-Span during which it
        was on-going. The associated instance of E52 Time-Span is understood as the real time-span during which the
        phenomena making up the temporal entity instance were active. More than one instance of E52 Temporal Entity
        may share a common instance of E52 Time-Span only if they come into being and end being due to an identical
        declarations or events;

    Properties:
        -
    Examples:
        - the Yalta Conference (E7) has time-span Yalta Conference time-span (E52)
    In First Order Logic:
        P4(x,y) ⊃ E2(x)
        P4(x,y) ⊃ E52(y)

    """

    p4_has_timespan: Optional[str] = Field(default=None, description='P4 has time-span (is time-span of)')


# ******************************************************************************************************************* #


class P5ConsistsOf(PropertyMixin):
    """'P5 consists of (forms part of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P5

    Domain:
        E3 Condition State
    Range:
        E3 Condition State
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property describes the decomposition of an instance of E3 Condition State into discrete, subsidiary
        states;

        It is assumed that the sub-states into which the condition state is analysed form a logical whole - although
        the entire story may not be completely known – and that the sub-states are in fact constitutive of the general
        condition state. For example, a general condition state of “in ruins” may be decomposed into the individual
        stages of decay;

        This property is transitive;

    Properties:
        -
    Examples:
        - The Condition State of the ruined Parthenon (E3) consists of the bombarded state after the explosion of
          a Venetian shell in 1687 (E3) [The Venetians in Athens and the Destruction of the Parthenon in 1687,
          ·Theodor E. Mommsen, American Journal of Archaeology, Vol. 45, No. 4 (Oct. - Dec., 1941), pp. 544-5]
    In First Order Logic:
        P5(x,y) ⊃ E3(x)
        P5(x,y) ⊃ E3(y)

    """

    p5_consists_of: Optional[str] = Field(default=None, description='P5 consists of (forms part of)')


# ******************************************************************************************************************* #


class P7TookPlaceAt(PropertyMixin):
    """'P7 took place at (witnessed)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P7

    Domain:
        E4 Period
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property describes the spatial location of an instance of E4 Period;

        The related instance of E53 Place should be seen as a wider approximation of the geometric area within which
        the phenomena that characterise the period in question occurred, see below. P7 took place at (witnessed) does
        not convey any meaning other than spatial positioning (frequently on the surface of the earth). For example,
        the period “Révolution française” can be said to have taken place in “France in 1789”; the “Victorian” period
        may be said to have taken place in “Britain from 1837-1901” and its colonies, as well as other parts of Europe
        and North America. An instance of E4 Period can take place at multiple non-contiguous, non-overlapping
        locations;

        It is a shortcut of the more fully developed path from E4 Period through P161 has spatial projection,
        E53 Place, P89 falls within to E53 Place. E4 Period is a subclass of E92 Spacetime Volume. By the definition
        of P161 has spatial projection an instance of E4 Period takes place on all its spatial projections, that is,
        instances of E53 Place. Something happening at a given place can also be considered to happen at a larger
        place containing the first. For example, the assault on the Bastille July 14th 1789 took place in the area
        covered by Paris in 1789 but also in the area covered by France in 1789;

    Properties:
        -
    Examples:
        - the period “Révolution française” (E4) took place at the area covered by France in 1789 (E53)
    In First Order Logic:
        P7(x,y) ⊃ E4(x)
        P7(x,y) ⊃ E53(y)

    """

    p7_took_place_at: Optional[str] = Field(default=None, description='P7 took place at (witnessed)')


# ******************************************************************************************************************* #


class P8TookPlaceOnOrWithin(PropertyMixin):
    """'P8 took place on or within (witnessed)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P8

    Domain:
        E4 Period
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the location of an instance of E4 Period with respect to an instance of
        E19 Physical Object;

        P8 took place on or within (witnessed) is a shortcut of the more fully developed path from ‘E4 Period’ through
        ‘P7 took place at’, ‘E53 Place’, ‘P156i is occupied by’, to ‘E18 Physical Thing’

        It describes a period that can be located with respect to the space defined by an E19 Physical Object such as
        a ship or a building. The precise geographical location of the object during the period in question may be
        unknown or unimportant;

        For example, the French and German armistice of 22 June 1940 was signed in the same railway carriage as
        the armistice of 11 November 1918;

    Properties:
        -
    Examples:
        - the coronation of Queen Elizabeth II (E7) took place on or within Westminster Abbey (E19)
    In First Order Logic:
        P8(x,y) ⊃ E4(x)
        P8(x,y) ⊃ E18(y)

    """

    p8_took_place_on_or_within: Optional[str] = Field(default=None, description='P8 took place on or within'
                                                                                ' (witnessed)')


# ******************************************************************************************************************* #


class P9ConsistsOf(PropertyMixin):
    """'P9 consists of (forms part of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P9

    Domain:
        E4 Period
    Range:
        E4 Period
    SubProperty Of:
        E92 Spacetime Volume. P10i contains (falls within): E92 Spacetime Volume
        E92 Spacetime Volume. P132 spatiotemporally overlaps with: E92 Spacetime Volume
    SuperProperty Of:
        -
    Quantification:
        one to many, (0,n:0,1)

    Scope Note:
        This property associates an instance of E4 Period with another instance of E4 Period that is defined by
        a subset of the phenomena that define the former. Therefore the spacetime volume of the latter must
        fall within the spacetime volume of the former;

        This property is transitive.

    Properties:
        -
    Examples:
        - Cretan Bronze Age (E4) consists of Middle Minoan (E4)
    In First Order Logic:
        P9(x,y) ⊃ E4(x)
        P9(x,y) ⊃ E4(y)
        P9(x,y) ⊃ P10(y,x)

    """

    p9_consists_of: Optional[str] = Field(default=None, description='P9 consists of (forms part of)')


# ******************************************************************************************************************* #


class P10FallsWithin(PropertyMixin):
    """'P10 falls within (contains)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P10

    Domain:
        E92 Spacetime Volume
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        E92 Spacetime Volume. P132 spatiotemporally overlaps with: E92 Spacetime Volume
    SuperProperty Of:
        E93 Presence. P166 was a presence of (had presence): E92 Spacetime Volume
        E4 Period. P9i forms part of (consists of): E4 Period
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E92 Spacetime Volume with another instance of E92 Spacetime Volume
        that falls within the latter. In other words, all points in the former are also points in the latter;

        This property is transitive;

    Properties:
        -
    Examples:
        - the Great Plague (E4) falls within The Gothic period (E4)
    In First Order Logic:
        P10(x,y) ⊃ E92(x)
        P10(x,y) ⊃ E92(y)
        P10(x,y) ⊃ P132(x,y)

    """

    p10_falls_within: Optional[str] = Field(default=None, description='P10 falls within (contains)')


# ******************************************************************************************************************* #


class P11HadParticipant(PropertyMixin):
    """'P11 had participant (participated in) CRM property';

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P11

    Domain:
        E5 Event
    Range:
        E39 Actor
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        E7 Activity. P14 carried out by (performed): E39 Actor
        E67 Birth. P96 by mother (gave birth): E21 Person
        E68 Dissolution. P99 dissolved (was dissolved by): E74 Group
        E85 Joining. P143 joined (was joined by): E39 Actor
        E85 Joining. P144 joined with (gained member by): E74 Group
        E86 Leaving. P145 separated (left by): E39 Actor
        E86 Leaving. P146 separated from (lost member by): E74 Group
        E66 Formation. P151 was formed from (participated in): E74 Group
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the active or passive participation of instances of E39 Actors in an instance of
        E5 Event;

        It documents known events in which an instance of E39 Actor has participated during the course of that
        actor’s life or history. The instances of E53 Place and E52 Time-Span where and when these events happened
        provide us with constraints about the presence of the related instances of E39 Actor in the past. Collective
        actors, i.e., instances of E74 Group, may physically participate in events via their representing instances
        of E21 Persons only. The participation of multiple actors in an event is most likely an indication of their
        acquaintance and interaction;

        The property implies that the actor was involved in the event but does not imply any causal relationship. For
        instance, someone having been portrayed can be said to have participated in the creation of the portrait;

    Properties:
        -
    Examples:
        - Napoleon (E21) participated in The Battle of Waterloo (E7)
        - Maria (E21) participated in Photographing of Maria (E7)
    In First Order Logic:
        P11(x,y) ⊃ E5(x)
        P11(x,y) ⊃ E39(y)
        P11(x,y) ⊃ P12(x,y)

    """

    p11_had_participant: Optional[str] = Field(default=None, description='P11 had participant (participated in)')


# ******************************************************************************************************************* #


class P12OccurredInPresenceOf(PropertyMixin):
    """'P12 occurred in presence of (was present at)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P12

    Domain:
        E5 Event
    Range:
        E77 Persistent Item
    SubProperty Of:
        -
    SuperProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
        E7 Activity. P16 used specific object (was used for): E70 Thing
        E9 Move. P25 moved (moved by): E19 Physical Object
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
        E64 End of Existence. P93 took out of existence (was taken out of existence by): E77 Persistent Item
        E79 Part Addition. P111 added (was added by): E18 Physical Thing
        E80 Part Removal. P113 removed (was removed by): E18 Physical Thing
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property describes the active or passive presence of an E77 Persistent Item in an instance of E5 Event
        without implying any specific role;

        It documents known events in which an instance of E77 Persistent Item was present during the course of
        its life or history. For example, an object may be the desk, now in a museum on which a treaty was signed. The
        instance of E53 Place and the instance of E52 Time-Span where and when these events happened provide us with
        constraints about the presence of the related instance E77 Persistent Item in the past. Instances of
        E90 Symbolic Object, in particular information objects, are physically present in events via at least
        one of the instances of E18 Physical Thing carrying them. Note, that the human mind can be such a carrier.
        A precondition for a transfer of information to a person or another new physical carrier is the presence of
        the respective information object and this person or physical thing in one event;

    Properties:
        -
    Examples:
        - Deckchair 42 (E19) was present at The sinking of the Titanic (E5)
    In First Order Logic:
        P12(x,y) ⊃ E5(x)
        P12(x,y) ⊃ E77(y)

    """

    p12_occurred_in_presence_of: Optional[str] = Field(default=None, description='P12 occurred in presence of'
                                                                                 ' (was present at)')


# ******************************************************************************************************************* #


class P13Destroyed(PropertyMixin):
    """'P13 destroyed (was destroyed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P13

    Domain:
        E6 Destruction
    Range:
        E18 Physical Thing
    SubProperty Of:
        E64 End of Existence. P93 took out of existence (was taken out of existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary (1,n:0,1)

    Scope Note:
        This property links an instance of E6 Destruction to an instance of E18 Physical Thing that has been
        destroyed by it;

        Destruction implies the end of an item’s life as a subject of cultural documentation – the physical matter
        of which the item was composed may in fact continue to exist. An instance of E6 Destruction may be contiguous
        with an instance of E12 Production that brings into existence a derived object composed partly of matter from
        the destroyed object;

    Properties:
        -
    Examples:
        - the Tay Bridge Disaster (E6) destroyed The Tay Bridge (E22)
    In First Order Logic:
        P13 (x,y) ⊃ E6 (x)
        P13 (x,y) ⊃ E18(y)
        P13 (x,y) ⊃ P93(x,y)

    """

    p13_destroyed: Optional[str] = Field(default=None, description='P13 destroyed (was destroyed by)')


# ******************************************************************************************************************* #


class P14CarriedOutBy(PropertyMixin):
    """'P14 carried out by (performed)';

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P14

    Domain:
        E7 Activity
    Range:
        E39 Actor
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        E8 Acquisition. P22 transferred title to (acquired title through): E39 Actor
        E8 Acquisition. P23 transferred title from (surrendered title through): E39 Actor
        E10 Transfer of Custody. P28 custody surrendered by (surrendered custody through): E39 Actor
        E10 Transfer of Custody. P29 custody received by (received custody through): E39 Actor
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property describes the active participation of an instance of E39 Actor in an instance of E7 Activity;

        It implies causal or legal responsibility. The P14.1 in the role of property of the property specifies the
        nature of an Actor’s participation;

    Properties:
        P14.1 in the role of: E55 Type

    Examples:
        - the painting of the Sistine Chapel (E7) carried out by Michaelangelo Buonaroti (E21) in the role of master
          craftsman (E55)
    In First Order Logic:
        P14 (x,y) ⊃ E7(x)
        P14 (x,y)⊃ E39(y)
        P14 (x,y) ⊃ P11(x,y)
        P14(x,y,z) ⊃ [P14(x,y) ∧ E55(z)]

    """

    p14_carried_out_by: Optional[str] = Field(default=None, description='P14 carried out by (performed)')


# ******************************************************************************************************************* #


class P15WasInfluencedBy(PropertyMixin):
    """'P15 was influenced by (influenced)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P15

    Domain:
        E7 Activity
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
        E7 Activity. P17 was motivated by (motivated): E1 CRM Entity
        E7 Activity. P134 continued (was continued by): E7 Activity
        E83 Type Creation. P136 was based on (supported type creation): E1 CRM Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This is a high level property, which captures the relationship between an instance of E7 Activity and
        anything, that is, an instance of E1 CRM Entitythat may have had some bearing upon it;

        The property has more specific sub properties;

    Properties:
        -
    Examples:
        - the designing of the Sydney Harbour Bridge (E7) was influenced by the Tyne bridge (E22)
    In First Order Logic:
        P15 (x,y) ⊃ E7(x)
        P15 (x,y) ⊃ E1(y)

    """

    p15_was_influenced_by: Optional[str] = Field(default=None, description='P15 was influenced by (influenced)')


# ******************************************************************************************************************* #


class P16UsedSpecificObject(PropertyMixin):
    """'P16 used specific object (was used for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P16

    Domain:
        E7 Activity
    Range:
        E70 Thing
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
        E7 Activity. P15 was influenced by (influenced): E1 CRM Entity
    SuperProperty Of:
        E7 Activity. P33 used specific technique (was used by): E29 Design or Procedure
        E79 Part Addition. P111 added (was added by): E18 Physical Thing
        E15 Identifier Assignment. P142 used constituent (was used in): E90 Symbolic Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the use of material or immaterial things in a way essential to the performance or the
        outcome of an instance of E7 Activity;

        This property typically applies to tools, instruments, moulds, raw materials and items embedded in a product.
        It implies that the presence of the object in question was a necessary condition for the action. For example,
        the activity of writing this text required the use of a computer. An immaterial thing can be used if at least
        one of its carriers is present. For example, the software tools on a computer;

        Another example is the use of a particular name by a particular group of people over some span to identify
        a thing, such as a settlement. In this case, the physical carriers of this name are at least the people
        understanding its use;

    Properties:
        P16.1 mode of use: E55 Type

    Examples:
        - the writing of this scope note (E7) used specific object Nicholas Crofts’ computer (E22) mode of use Typing
          Tool; Storage Medium (E55)
        - the people of Iraq calling the place identified by TGN ‘7017998’ (E7) used specific object “Quyunjig”
          (E41)mode of use Current; Vernacular (E55)
    In First Order Logic:
        P16 (x,y) ⊃ E7(x)
        P16 (x,y) ⊃ E70(y)
        P16 (x,y) ⊃ P12(x,y)
        P16 (x,y) ⊃ P15(x,y)
        P16(x,y,z) ⊃ [P16(x,y) ∧ E55(z)]

    """

    p16_used_specific_object: Optional[str] = Field(default=None, description='P16 used specific object'
                                                                              ' (was used for)')


# ******************************************************************************************************************* #


class P17WasMotivatedBy(PropertyMixin):
    """'P17 was motivated by (motivated)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P17

    Domain:
        E7 Activity
    Range:
        E1 CRM Entity
    SubProperty Of:
        E7 Activity. P15 was influenced by (influenced): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes an item or items that are regarded as a reason for carrying out the instance of
        E7 Activity;

        For example, the discovery of a large hoard of treasure may call for a celebration, an order from
        head quarters can start a military manoeuvre;

    Properties:
        -
    Examples:
        - the resignation of the chief executive (E7) was motivated by the collapse of SwissAir (E68).
        - the coronation of Elizabeth II (E7) was motivated by the death of George VI (E69)
    In First Order Logic:
        P17(x,y) ⊃ E7(x)
        P17(x,y) ⊃ E1(y)
        P17 (x,y) ⊃ P15(x,y)

    """

    p17_was_motivated_by: Optional[str] = Field(default=None, description='P17 was motivated by (motivated)')


# ******************************************************************************************************************* #


class P19WasIntendedUseOf(PropertyMixin):
    """'P19 was intended of (was made for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P19

    Domain:
        E7 Activity
    Range:
        E71 Human-Made Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property relates an instance of E7 Activity with instances of E71 Human-Made Thing, created specifically
        for use in the activity;

        This is distinct from the intended use of an item in some general type of activity such as the book of
        common prayer which was intended for use in Church of England services (see P101 had as general use
        (was use of));

    Properties:
        P19.1 mode of use: E55 Type

    Examples:
        - Lady Diana Spencer’s wedding dress (E71) was made for Wedding of Prince Charles and Lady Diana Spencer (E7)
          mode of use To Be Worn (E55)
    In First Order Logic:
        P19(x,y) ⊃ E7(x)
        P19(x,y) ⊃ E71(y)
        P19(x,y,z) ⊃ [P19(x,y) ∧ E55(z)]

    """

    p19_was_intended_use_of: Optional[str] = Field(default=None, description='P19 was intended of (was made for)')


# ******************************************************************************************************************* #


class P20HadSpecificPurpose(PropertyMixin):
    """'P20 had specific purpose (was purpose of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P20

    Domain:
        E7 Activity
    Range:
        E5 Event
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the relationship between a preparatory activity, an instance of E7 Activity and
        the instance of E7 Event it is intended to be preparation for;

        This includes activities, orders and other organisational actions, taken in preparation for other activities
        or events;

        P20 had specific purpose (was purpose of) implies that an activity succeeded in achieving its aim. If it does
        not succeed, such as the setting of a trap that did not catch anything, one may document the unrealized
        intention using P21 had general purpose (was purpose of):E55 Type and/or P33 used specific technique
        (was used by): E29 Design or Procedure;

    Properties:
        -
    Examples:
        - Van Eyck’s pigment grinding in 1432 (E7) had specific purpose the painting of the Ghent altar piece (E12)
    In First Order Logic:
        P20(x,y) ⊃ E7(x)
        P20(x,y) ⊃ E5(y)

    """

    p20_had_specific_purpose: Optional[str] = Field(default=None, description='P20 had specific purpose'
                                                                              ' (was purpose of)')


# ******************************************************************************************************************* #


class P21HadGeneralPurpose(PropertyMixin):
    """'P21 had general purpose (was purpose of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P21

    Domain:
        E7 Activity
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes an intentional relationship between an instance of E7 Activity and some general goal
        or purpose, described as an instance of E55 Type;

        This may involve activities intended as preparation for some type of activity or event. P21had general
        purpose (was purpose of) differs from P20 had specific purpose (was purpose of) in that no occurrence of
        an event is implied as the purpose;

    Properties:
        -
    Examples:
        - Van Eyck’s pigment grinding (E7) had general purpose painting (E55)
        - The setting of trap 2742 on May 17th 1874 (E7) had general purpose Catching Moose (E55) (Activity type
    In First Order Logic:
        P21(x,y) ⊃ E7(x)
        P21(x,y) ⊃ E55(y)

    """

    p21_had_general_purpose: Optional[str] = Field(default=None, description='P21 had general purpose'
                                                                             ' (was purpose of)')


# ******************************************************************************************************************* #


class P22TransferredTitleTo(PropertyMixin):
    """'P22 transferred title to (acquired title through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P22

    Domain:
        E8 Acquisition
    Range:
        E39 Actor
    SubProperty Of:
        E7 Activity. P14 carried out by (performed): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor that acquires the legal ownership of an object as a result
        of an instance of E8 Acquisition;

        The property will typically describe an Actor purchasing or otherwise acquiring an object from another Actor.
        However, title may also be acquired, without any corresponding loss of title by another Actor, through legal
        fieldwork such as hunting, shooting or fishing;

        In reality the title is either transferred to or from someone, or both;

    Properties:
        -
    Examples:
        - acquisition of the Amoudrouz collection by the Geneva Ethnography Museum (E8) transferred title to
          Geneva Ethnography Museum (E74)
    In First Order Logic:
        P22(x,y) ⊃ E8(x)
        P22(x,y) ⊃ E39(y)
        P22 (x,y) ⊃ P14(x,y)

    """

    p22_transferred_title_to: Optional[str] = Field(default=None, description='P22 transferred title to'
                                                                              ' (acquired title through)')


# ******************************************************************************************************************* #


class P23TransferredTitleFrom(PropertyMixin):
    """'P23 transferred title from (surrendered title through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P23

    Domain:
        E8 Acquisition
    Range:
        E39 Actor
    SubProperty Of:
        E7 Activity. P14 carried out by (performed): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance(s) of E39 Actor who relinquish legal ownership as the result of an
        instance of E8 Acquisition;

        The property will typically be used to describe a person donating or selling an object to a museum. In reality
        title is either transferred to or from someone, or both;

    Properties:
        -
    Examples:
        - acquisition of the Amoudrouz collection by the Geneva Ethnography Museum (E8) transferred title from
          Heirs of Amoudrouz (E74)
    In First Order Logic:
        P23(x,y) ⊃ E8(x)
        P23(x,y) ⊃ E39(y)
        P23 (x,y) ⊃ P14(x,y)

    """

    p23_transferred_title_from: Optional[str] = Field(default=None, description='P23 transferred title from'
                                                                                ' (surrendered title through)')


# ******************************************************************************************************************* #


class P24TransferredTitleOf(PropertyMixin):
    """'P24 transferred title of (changed ownership through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P24

    Domain:
        E8 Acquisition
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance(s) of E18 Physical Thing involved in an instance of E8 Acquisition;

        In reality, an acquisition must refer to at least one transferred item;

    Properties:
        -
    Examples:
        - acquisition of the Amoudrouz collection by the Geneva Ethnography Museum (E8) transferred title of
          Amoudrouz Collection (E78)
    In First Order Logic:
        P24(x,y) ⊃ E8(x)
        P24(x,y) ⊃ E18(y)

    """

    p24_transferred_title_of: Optional[str] = Field(default=None, description='P24 transferred title of'
                                                                              ' (changed ownership through)')


# ******************************************************************************************************************* #


class P25Moved(PropertyMixin):
    """'P25 moved (moved by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P25

    Domain:
        E9 Move
    Range:
        E19 Physical Object
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies an instance of E19 Physical Object that was moved by an instance of E9Move. A move
        must concern at least one object;

        The property implies the object’s passive participation. For example, Monet’s painting “Impression sunrise”
        was moved for the first Impressionist exhibition in 1874;

    Properties:
        -
    Examples:
        - Monet´s “Impression sunrise” (E22) moved by preparations for the First Impressionist Exhibition (E9)
    In First Order Logic:
        P25(x,y) ⊃ E9(x)
        P25(x,y) ⊃ E19(y)
        P25(x,y) ⊃ P12(x,y)

    """

    p25_moved: Optional[str] = Field(default=None, description='P25 moved (moved by)')


# ******************************************************************************************************************* #


class P26MovedTo(PropertyMixin):
    """'P26 moved to (was destination of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P26

    Domain:
        E9 Move
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies a destination, an instance of E53 place, of an instance of E9 Move;

        A move will be linked to a destination, such as the move of an artifact from storage to display. A move may be
        linked to many terminal instances of E53 Place by multiple instances of this property. In this case the move
        describes a distribution of a set of objects. The area of the move includes the origin(s), route and
        destination(s);

        Therefore the described destination is an instance of E53 Place which P89 falls within (contains) the instance
        of E53 Place the move P7 took place at;

    Properties:
        -
    Examples:
        - the movement of the Tut-Ankh-Amun Exhibition (E9) moved to The British Museum (E53)
    In First Order Logic:
        P26(x,y) ⊃ E9(x)
        P26(x,y) ⊃ E53(y)
        P26(x,y) ⊃ (∃z)[ E53(z) ∧ P7(x,z) ∧ P89(y,z)]

    """

    p26_moved_to: Optional[str] = Field(derfault=None, description='P26 moved to (was destination of)')


# ******************************************************************************************************************* #


class P27MovedFrom(PropertyMixin):
    """'P27 moved from (was origin of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P27

    Domain:
        E9 Move
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies an origin, an instance of E53 Place, of an instance of E9 Move;

        A move will be linked to an origin, such as the move of an artifact from storage to display. A move may be
        linked to many starting instances of E53 Place by multiple instances of this property. In this case the move
        describes the picking up of a set of objects. The area of the move includes the origin(s), route and
        destination(s);

        Therefore the described origin is an instance of E53 Place which P89 falls within (contains) the instance of
        E53 Place the move P7 took place at;

    Properties:
        -
    Examples:
        - the movement of the Tut-Ankh-Amun Exhibition (E9) moved from The Egyptian Museum in Cairo (E53)
    In First Order Logic:
        P27(x,y) ⊃ E9(x)
        P27(x,y) ⊃ E53(y)
        P27(x,y) ⊃ (∃z)[ E53(z) ∧ P7(x,z) ∧ P89(y,z)]

    """

    P27_moved_from: Optional[str] = Field(default=None, description='P27 moved from (was origin of)')


# ******************************************************************************************************************* #


class P28CustodySurrenderedBy(PropertyMixin):
    """'P28 custody surrendered by (surrendered custody through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P28

    Domain:
        E10 Transfer of Custody
    Range:
        E39 Actor
    SubProperty Of:
        E7 Activity. P14 carried out by (performed): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance(s) of E39 Actor who surrender custody of an instance of
        E18 Physical Thing in an instance of E10 Transfer of Custody;

        The property will typically describe an Actor surrendering custody of an object when it is handed over to
        someone else’s care. On occasion, physical custody may be surrendered involuntarily – through accident, loss
        or theft;

        In reality, custody is either transferred to someone or from someone, or both;

    Properties:
        -
    Examples:
        - the Secure Deliveries Inc. crew (E74) surrendered custody through The delivery of the paintings by Secure
          Deliveries Inc. to the National Gallery (E10);
    In First Order Logic:
        P28(x,y) ⊃ E10(x)
        P28(x,y) ⊃ E39(y)
        P28(x,y) ⊃ P14(x,y)

    """

    p28_custody_surrendered_by: Optional[str] = Field(default=None, description='P28 custody surrendered by'
                                                                                ' (surrendered custody through)')


# ******************************************************************************************************************* #


class P29CustodyReceivedBy(PropertyMixin):
    """'P29 custody received by (received custody through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P29

    Domain:
        E10 Transfer of Custody
    Range:
        E39 Actor
    SubProperty Of:
        E7 Activity. P14 carried out by (performed): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance(s) E39 Actor who receive custody of an instance of E18 Physical Thing
        in an instance of E10 Transfer of Custody;

        The property will typically describe Actors receiving custody of an object when it is handed over from another
        Actor’s care. On occasion, physical custody may be received involuntarily or illegally – through accident,
        unsolicited donation, or theft;

        In reality, custody is either transferred to someone or from someone, or both;

    Properties:
        -
    Examples:
        - representatives of The National Gallery (E74) received custody through. The delivery of the paintings by
          Secure Deliveries Inc. to the National Gallery (E10)
    In First Order Logic:
        P29 (x,y) ⊃ E10(x)
        P29 (x,y) ⊃ E39(y)
        P29(x,y) ⊃ P14(x,y)

    """

    p29_custody_received_by: Optional[str] = Field(default=None, description='P29 custody received by'
                                                                             ' (received custody through)')


# ******************************************************************************************************************* #


class P30TransferredCustodyOf(PropertyMixin):
    """'P30 transferred custody of (custody transferred through)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P30

    Domain:
        E10 Transfer of Custody
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance(s) of E18 Physical Thing concerned in an instance of
        E10 Transfer of Custody;

        The property will typically describe the object that is handed over by an instance of E39 Actor to to the
        custody of another instance of E39 Actor. On occasion, physical custody may be transferred involuntarily or
        illegally – through accident, unsolicited donation, or theft;

    Properties:
        -
    Examples:
        - the delivery of the paintings by Secure Deliveries Inc. to the National Gallery (E10) transferred custody of
          paintings from The Iveagh Bequest (E19)
    In First Order Logic:
        P30 (x,y) ⊃ E10(x)
        P30 (x,y) ⊃ E18(y)

    """

    p30_transferred_custody_of: Optional[str] = Field(default=None, description='P30 transferred custody of'
                                                                                ' (custody transferred through)')


# ******************************************************************************************************************* #


class P31HasModified(PropertyMixin):
    """'P31 has modified (was modified by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P31

    Domain:
        E11 Modification
    Range:
        E18 Physical Thing
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        E12 Production. P108 has produced (was produced by): E24 Physical Human-Made Thing
        E79 Part Addition. P110 augmented (was augmented by): E24 Physical Human-Made Thing
        E80 Part Removal. P112 diminished (was diminished by): E24 Physical Human-Made Thing
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E24 Physical Human-Made Thing modified in an instance of
        E11 Modification;

    Properties:
        -
    Examples:
        - rebuilding of the Reichstag (E11) has modified the Reichstag in Berlin (E24)
    In First Order Logic:
        P31(x,y) ⊃ E11(x)
        P31(x,y) ⊃ E18(y)
        P31(x,y) ⊃ P12(x,y)

    """

    p31_has_modified: Optional[str] = Field(default=None, description='P31 has modified (was modified by)')


# ******************************************************************************************************************* #


class P32UsedGeneralTechnique(PropertyMixin):
    """'P32 used general technique (was technique of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P32

    Domain:
        E7 Activity
    Range:
        E55 Type
    SubProperty Of:
        E7 Activity. P125 used object of type (was type of object used in): E55 Type
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the technique or method, modelled as an instance of E55 Type, that was employed in
        an instance of E7 Activity;

        These techniques should be drawn from an external E55 Type hierarchy of consistent terminology of general
        techniques or methods such as embroidery, oil-painting, carbon dating, etc. Specific documented techniques
        should be described as instances of E29 Design or Procedure. This property identifies the technique that was
        employed in an act of modification;

    Properties:
        -
    Examples:
        - ornamentation of silver cup 113 (E11) used general technique gold-plating (E55) (Design or Procedure Type)
    In First Order Logic:
        P32(x,y) ⊃ E7(x)
        P32(x,y) ⊃ E55(y)
        P32(x,y) ⊃ P125(x,y)

    """

    p32_used_general_technique: Optional[str] = Field(default=None, description='P32 used general technique'
                                                                                ' (was technique of)')


# ******************************************************************************************************************* #


class P33UsedSpecificTechnique(PropertyMixin):
    """'P33 used specific technique (was used by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P33

    Domain:
        E7 Activity
    Range:
        E29 Design or Procedure
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies a specific instance of E29 Design or Procedure in order to carry out an instance of
        E7 Activity or parts of it;

        The property differs from P32 used general technique (was technique of) in that P33 refers to an instance of
        E29 Design or Procedure, which is a concrete information object in its own right rather than simply being
        a term or a method known by tradition;

        Typical examples would include intervention plans for conservation or the construction plans of a building;

    Properties:
        -
    Examples:
        - Ornamentation of silver cup 232 (E11) used specific technique ‘Instructions for golden chase work by
          A N Other’ (E29)
        - Rebuilding of Reichstag (E11) used specific technique Architectural plans by Foster and Partners (E29)
    In First Order Logic:
        P33(x,y) ⊃ E7(x)
        P33(x,y) ⊃ E29(y)
        P33(x,y) ⊃ P16(x,y)

    """

    p33_used_specific_technique: Optional[str] = Field(default=None, description='P33 used specific technique'
                                                                                 ' (was used by)')


# ******************************************************************************************************************* #


class P34Concerned(PropertyMixin):
    """'P34 concerned (was assessed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P34

    Domain:
        E14 Condition Assessment
    Range:
        E18 Physical Thing
    SubProperty Of:
        E13 Attribute Assignment. P140 assigned attribute to (was attributed by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E18 Physical Thing that was assessed during an instance of
        E14 Condition Assessment activity;

        Conditions may be assessed either by direct observation or using recorded evidence. In the latter case the
        instance of E18 Physical Thing does not need to be present or extant at the time of assessment;

    Properties:
        -
    Examples:
        - 1997 condition assessment of the silver collection (E14) concerned silver cup 232 (E22)
    In First Order Logic:
        P34(x,y) ⊃ E14(x)
        P34(x,y) ⊃ E18(y)
        P34(x,y) ⊃ P140(x,y)

    """

    p34_concerned: Optional[str] = Field(default=None, description='P34 concerned (was assessed by)')


# ******************************************************************************************************************* #


class P35Identified(PropertyMixin):
    """'P35 has identified (was identified by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P35

    Domain:
        E14 Condition Assessment
    Range:
        E3 Condition State
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E3 Condition State that was observed in an instance of
        E14 Condition Assessment activity;

    Properties:
        -
    Examples:
        - 1997 condition assessment of silver cup 232 (E14) has identified oxidation traces were present in 1997 (E3)
          has type oxidation traces (E55)
    In First Order Logic:
        P35(x,y) ⊃E14(x)
        P35(x,y) ⊃ E3(y)
        P35(x,y) ⊃ P141(x,y)

    """

    p35_identified: Optional[str] = Field(default=None, description='P35 has identified (was identified by)')


# ******************************************************************************************************************* #


class P37Assigned(PropertyMixin):
    """'P37 assigned (was assigned by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P37

    Domain:
        E15 Identifier Assignment
    Range:
        E42 Identifier
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property records the identifier that was assigned to an item in an instance of P37 Identifier Assignment;

        The same identifier may be assigned on more than one occasion;

        An Identifier might be created prior to an assignment;

    Properties:
        -
    Examples:
        - 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned “232” (E42)
    In First Order Logic:
        P37(x,y) ⊃ E15(x)
        P37(x,y) ⊃ E42(y)
        P37(x,y) ⊃ P141(x,y)

    """

    p37_assigned: Optional[str] = Field(default=None, description='P37 assigned (was assigned by)')


# ******************************************************************************************************************* #


class P38Deassigned(PropertyMixin):
    """'P38 deassigned (was deassigned by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P38

    Domain:
        E15 Identifier Assignment
    Range:
        E42 Identifier
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property records the identifier that was deassigned from an instance of E1 CRM Entity;

        Deassignment of an identifier may be necessary when an item is taken out of an inventory, a new numbering
        system is introduced or items are merged or split up;

        The same identifier may be deassigned on more than one occasion;

    Properties:
        -
    Examples:
        - 31 July 2001 Identifier Assignment of the silver cup OXCMS:2001.1.32 (E15) deassigned “232” (E42)
    In First Order Logic:
        P38(x,y) ⊃ E15(x)
        P38(x,y) ⊃ E42(y)
        P38(x,y) ⊃ P141(x,y)

    """

    p38_deassigned: Optional[str] = Field(default=None, description='P38 deassigned (was deassigned by)')


# ******************************************************************************************************************* #


class P39Measured(PropertyMixin):
    """'P39 measured (was measured by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P39

    Domain:
        E16 Measurement
    Range:
        E1 CRM Entity
    SubProperty Of:
        E13 Attribute Assignment. P140 assigned attribute to (was attributed by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of E16 Measurement with the instance of E1 CRM Entity to which it
        applied. An instance of E1 CRM Entity may be measured more than once. Material and immaterial things and
        processes may be measured, e.g. the number of words in a text, or the duration of an event;

    Properties:
        -
    Examples:
        31 August 1997 measurement of height of silver cup 232 (E16) measured silver cup 232 (E22)
    In First Order Logic:
        P39(x,y) ⊃ E16(x)
        P39(x,y) ⊃ E1(y)
        P39(x,y) ⊃ P140(x,y)

    """

    p39_measured: Optional[str] = Field(default=None, description='P39 measured (was measured by)')


# ******************************************************************************************************************* #


class P40ObservedDimension(PropertyMixin):
    """'P40 observed dimension (was observed in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P40

    Domain:
        E16 Measurement
    Range:
        E54 Dimension
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property records the dimension that was observed in an E16 Measurement Event;

        E54 Dimension can be any quantifiable aspect of E70 Thing. Weight, image colour depth and monetary value are
        dimensions in this sense. One measurement activity may determine more than one dimension of one object;

        Dimensions may be determined either by direct observation or using recorded evidence. In the latter case the
        measured Thing does not need to be present or extant;

        Even though knowledge of the value of a dimension requires measurement, the dimension may be an object of
        discourse prior to, or even without, any measurement being made;

    Properties:
        -
    Examples:
        - 31 August 1997 measurement of height of silver cup 232 (E16) observed dimension silver cup 232 height
          (E54) has unit mm (E58), has value 224 (E60)
    In First Order Logic:
        P40(x,y) ⊃ E16(x)
        P40(x,y)⊃ E54(y)
        P40(x,y) ⊃ P141(x,y)

    """

    p40_observed_dimension: Optional[str] = Field(default=None, description='P40 observed dimension'
                                                                            ' (was observed in)')


# ******************************************************************************************************************* #


class P41Classified(PropertyMixin):
    """'P41 classified (was classified by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P41

    Domain:
        E17 Type Assignment
    Range:
        E1 CRM Entity
    SubProperty Of:
        E13 Attribute Assignment. P140 assigned attribute to (was attributed by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property records the item to which a type was assigned in an E17 Type Assignment activity;

        Any instance of a CIDOC CRM entity may be assigned a type through type assignment. Type assignment events
        allow a more detailed path from ‘E1 CRM Entity’ through ‘P41i was classified by’, ‘E17 Type Assignment’,
        ‘P42 assigned’, to ‘E55 Type’ for assigning types to objects compared to the shortcut offered
        by P2 has type (is type of);

    Properties:
        -
    Examples:
        - 31 August 1997 classification of silver cup 232 (E17) classified silver cup 232 (E22)
    In First Order Logic:
        P41(x,y) ⊃ E17(x)
        P41(x,y) ⊃ E1(y)
        P41(x,y) ⊃ P140(x,y)

    """

    P41_classified: Optional[str] = Field(default=None, description='P41 classified (was classified by)')


# ******************************************************************************************************************* #


class P42Assigned(PropertyMixin):
    """'P42 assigned (was assigned by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P42

    Domain:
        E17 Type Assignment
    Range:
        E55 Type
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property records the type that was assigned to an entity by an E17 Type Assignment activity;

        Type assignment events allow a more detailed path from ‘E1 CRM Entity’ through ‘P41i was classified by’,
        ‘E17 Type Assignment’, ‘P42 assigned’, to ‘E55 Type’ for assigning types to objects compared to the shortcut
        offered by P2 has type (is type of);

        For example, a fragment of an antique vessel could be assigned the type “attic red figured belly handled
        amphora” by expert A. The same fragment could be assigned the type “shoulder handled amphora” by expert B;

        A Type may be intellectually constructed independent from assigning an instance of it;

    Properties:
        -
    Examples:
        - 31 August 1997 classification of silver cup 232 (E17) assigned goblet (E55)
    In First Order Logic:
        P42(x,y) ⊃ E17(x)
        P42(x,y)⊃ E55(y)
        P42(x,y) ⊃ P141(x,y)

    """

    p42_assigned: Optional[str] = Field(default=None, description='P42 assigned (was assigned by)')


# ******************************************************************************************************************* #


class P92BroughtIntoExistence(PropertyMixin):
    """'P92 brought into existence (was brought into existence by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P92

    Domain:
        E63 Beginning of Existence
    Range:
        E77 Persistent Item
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        E65 Creation. P94 has created (was created by): E28 Conceptual Object
        E66 Formation. P95 has formed (was formed by): E74 Group
        E67 Birth. P98 brought into life (was born): E21 Person
        E12 Production. P108 has produced (was produced by): E24 Physical Human-Made Thing
        E81 Transformation. P123 resulted in (resulted from): E18 Physical Thing
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property links an instance of E63 Beginning of Existence to the instance of E77 Persistent Item brought
        into existence by it;

        It allows a “start” to be attached to any instance of E77 Persistent Item being documented, i.e. as instances
        of E70 Thing, E72 Legal Object, E39 Actor, E41 Appellation and E55 Type;

    Properties:
        -
    Examples:
        - the birth of Mozart (E67) brought into existence Mozart (E21)
    In First Order Logic:
        P92(x,y) ⊃ E63(x)
        P92(x,y) ⊃ E77(y)
        P92(x,y) ⊃ P12(x,y)

    """

    p92_brought_into_existence: Optional[str] = Field(
        default=None,
        description='P92 brought into existence (was brought into existence by)'
    )


# ******************************************************************************************************************* #


class P93TookOutOfExistence(PropertyMixin):
    """'P93 took out of existence (was taken out of existence by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P93

    Domain:
        E64 End of Existence
    Range:
        E77 Persistent Item
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        E6 Destruction. P13 destroyed (was destroyed by): E18 Physical Thing
        E68 Dissolution. P99 dissolved (was dissolved by): E74 Group
        E69 Death. P100 was death of (died in): E21 Person
        E81 Transformation. P124 transformed (was transformed by): E18 Physical Thing
    Quantification:
        one to many, necessary (1,n:0,1)

    Scope Note:
        This property links an instance of E64 End of Existence to the instance E77 Persistent Item taken out of
        existence by it;

        In the case of immaterial things, the instance of E64 End of Existence is considered to take place with
        the destruction of the last physical carrier;

        This allows an “end” to be attached to any instance of E77 Persistent Item being documented i.e. instances
        of E70 Thing, E72 Legal Object, E39 Actor, E41 Appellation and E55 Type. For many instances
        of E77 Persistent Item we know the maximum life-span and can infer, that they must have ended to exist. We
        assume in that case an instance of E64 End of Existence, which may be as unnoticeable as forgetting the secret
        knowledge by the last representative of some indigenous nation;

    Properties:
        -
    Examples:
        - the death of Mozart (E69) took out of existence Mozart (E21)
    In First Order Logic:
        P93 (x,y) ⊃ E64(x)
        P93 (x,y) ⊃ E77(y)
        P93(x,y) ⊃ P12(x,y)

    """

    p93_took_out_of_existence: Optional[str] = Field(
        default=None,
        description='P93 took out of existence (was taken out of existence by)'
    )


# ******************************************************************************************************************* #


class P94HasCreated(PropertyMixin):
    """'P94 has created (was created by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P94

    Domain:
        E65 Creation
    Range:
        E28 Conceptual Object
    SubProperty Of:
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
    SuperProperty Of:
        E83 Type Creation. P135 created type (was created by): E55 Type
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property links an instance of E65 Creation to the instance of E28 Conceptual Object created by it;

        It represents the act of conceiving the intellectual content of the instance of E28 Conceptual Object. It does
        not represent the act of creating the first physical carrier of the instanced of E28 Conceptual Object. As
        an example, this is the composition of a poem, not its commitment to paper;

    Properties:
        -
    Examples:
        - the composition of “The Four Friends” by A. A. Milne (E65) has created “The Four Friends”
          by A. A. Milne (E28)
    In First Order Logic:
        P94(x,y) ⊃ E65(x)
        P94(x,y) ⊃ E28(y)
        P94(x,y) ⊃ P92(x,y)

    """

    p94_has_created: Optional[str] = Field(default=None, description='P94 has created (was created by)')


# ******************************************************************************************************************* #


class P95HasFormed(PropertyMixin):
    """'P95 has formed (was formed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P95

    Domain:
        E66 Formation
    Range:
        E74 Group
    SubProperty Of:
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property associates the instance of E66 Formation with the instance of E74 Group that it founded;

    Properties:
        -
    Examples:
        - the formation of the CIDOC CRM SIG at the August 2000 CIDOC Board meeting (E66) has formed the CIDOC CRM
          Special Interest Group (E74)
    In First Order Logic:
        P95(x,y) ⊃ E66(x)
        P95(x,y) ⊃ E74(y)
        P95(x,y) ⊃ P92(x,y)

    """

    p95_has_formed: Optional[str] = Field(default=None, description='P95 has formed (was formed by)')


# ******************************************************************************************************************* #


class P96ByMother(PropertyMixin):
    """'P96 by mother (gave birth)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P96

    Domain:
        E67 Birth
    Range:
        E21 Person
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property links an instance ofE67 Birth to an instance of E21 Person in the role of birth-giving mother;

        Note that biological fathers are not necessarily participants in the Birth (see P97 from father
        (was father for)). The instance of P21 Person being born is linked to the instance of E67 Birth with the
        property P98 brought into life (was born). This is not intended for use with general natural history material,
        only people. There is no explicit method for modelling conception and gestation except by using extensions.
        This is a sub-property of P11 had participant (participated in);

    Properties:
        -
    Examples:
        - the birth of Queen Elizabeth II (E67) by mother Queen Mother (E21)
    In First Order Logic:
        P96(x,y) ⊃ E67(x)
        P96(x,y) ⊃ E21(y)
        P96(x,y) ⊃ P11(x,y)

    """

    p96_by_mother: Optional[str] = Field(default=None, description='P96 by mother (gave birth)')


# ******************************************************************************************************************* #


class P97FromFather(PropertyMixin):
    """'P97 from father (was father for)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P97

    Domain:
        E67 Birth
    Range:
        E21 Person
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property links an instance of E67 Birth to an instance of E21 Person in the role of biological father;

        Note that biological fathers are not seen as necessary participants in the birth, whereas birth-giving mothers
        are (see P96 by mother (gave birth)). The Person being born is linked to the Birth with the property
        P98 brought into life (was born);

        This is not intended for use with general natural history material, only people. There is no explicit method
        for modelling conception and gestation except by using extensions;

        An instance of E67 Birth is normally (but not always) associated with one biological father;

    Properties:
        -
    Examples:
        - King George VI (E21) was father for the birth of Queen Elizabeth II (E67)
    In First Order Logic:
        P97(x,y) ⊃ E67(x)
        P97(x,y) ⊃ E21(y)

    """

    p97_from_father: Optional[str] = Field(default=None, description='P97 from father (was father for)')


# ******************************************************************************************************************* #


class P98BroughtIntoLife(PropertyMixin):
    """'P98 brought into life (was born)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P98

    Domain:
        E67 Birth
    Range:
        E21 Person
    SubProperty Of:
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property links an instance of E67 Birth event to an instance of E21 Person in the role of offspring;

        Twins, triplets etc. are brought into life by the same instance of E67 Birth. This is not intended for use
        with general Natural History material, only people. There is no explicit method for modelling conception and
        gestation except by using extensions;

    Properties:
        -
    Examples:
        - the Birth of Queen Elizabeth II (E67) brought into life Queen Elizabeth II (E21)
    In First Order Logic:
        P98(x,y) ⊃ E67(x)
        P98(x,y) ⊃ E21(y)
        P98(x,y) ⊃ P92(x,y)

    """

    p98_brought_into_life: Optional[str] = Field(default=None, description='P98 brought into life (was born)')


# ******************************************************************************************************************* #


class P99Dissolved(PropertyMixin):
    """'P99 dissolved (was dissolved by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P99

    Domain:
        E68 Dissolution
    Range:
        E74 Group
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
        E64 End of Existence. P93 took out of existence (was taken out of existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary (1,n:0,n)

    Scope Note:
        This property associates the instance of E68 Dissolution with the instance of E74 Group that it disbanded;

    Properties:
        -
    Examples:
        - the end of The Hole in the Wall Gang (E68) dissolved The Hole in the Wall Gang (E74)
    In First Order Logic:
        P99(x,y) ⊃ E68(x)
        P99(x,y) ⊃ E74(y)
        P99(x,y) ⊃ P11(x,y)
        P99(x,y) ⊃ P93(x,y)

    """

    p99_dissolved: Optional[str] = Field(default=None, description='P99 dissolved (was dissolved by)')


# ******************************************************************************************************************* #


class P100WasDeathOf(PropertyMixin):
    """'P100 was death of (died in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P100

    Domain:
        E69 Death
    Range:
        E21 Person
    SubProperty Of:
        E64 End of Existence. P93 took out of existence (was taken out of existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary (1,n:0,n)

    Scope Note:
        This property links an E69 instance of E69Death event to the instance of E21 Person that died;

        An instance of E69Death may involve multiple people, for example in the case of a battle or disaster;

        This is not intended for use with general Natural History material, only people;

    Properties:
        -
    Examples:
        - Mozart’s death (E69) was death of Mozart (E21)
    In First Order Logic:
        P100(x,y) ⊃ E69(x)
        P100(x,y) ⊃ E21(y)
        P100(x,y) ⊃ P93(x,y)

    """

    p100_was_death_of: Optional[str] = Field(default=None, description='P100 was death of (died in)')


# ******************************************************************************************************************* #


class P108HasProduced(PropertyMixin):
    """'P108 has produced (was produced by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P108

    Domain:
        E12 Production
    Range:
        E24 Physical Human-Made Thing
    SubProperty Of:
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property identifies the instance of E24 Physical Human-Made Thing that came into existence as a result
        of the instance of E12 Production;

        The identity of an instance of E24 Physical Human-Made Thing is not defined by its matter, but by its
        existence as a subject of documentation. An E12 Production can result in the creation of multiple instances
        of E24 Physical Human-Made Thing;

    Properties:
        -
    Examples:
        - The building of Rome (E12) has produced Τhe Colosseum (E22)
    In First Order Logic:
        P108(x,y) ⊃ E12(x)
        P108(x,y) ⊃ E24(y)
        P108(x,y) ⊃ P31(x,y)
        P108(x,y) ⊃ P92(x,y)

    """

    p108_has_produced: Optional[str] = Field(default=None, description='P108 has produced (was produced by)')


# ******************************************************************************************************************* #


class P110Augmented(PropertyMixin):
    """'P110 augmented (was augmented by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P110

    Domain:
        E79 Part Addition
    Range:
        E24 Physical Human-Made Thing
    SubProperty Of:
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E24 Physical Human-Made Thing that is added to (augmented) in
        an instance of E79 Part Addition;

        Although an instance of E79 Part Addition event normally concerns only one instance of
        E24 Physical Human-Made Thing, it is possible to imagine circumstances under which more than one item might
        be added to (augmented). For example, the artist Jackson Pollock trailing paint onto multiple canvasses;

    Properties:
        -
    Examples:
        - the final nail-insertion Event (E79) augmented Coffin of George VI (E24)
    In First Order Logic:
        P110(x,y) ⊃ E79(x)
        P110(x,y) ⊃ E24(y)
        P110(x,y) ⊃ P31(x,y)

    """

    p110_augmented: Optional[str] = Field(default=None, description='P110 augmented (was augmented by)')


# ******************************************************************************************************************* #


class P111Added(PropertyMixin):
    """'P111 added (was added by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P111

    Domain:
        E79 Part Addition
    Range:
        E18 Physical Thing
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E18 Physical Thing that is added during an instance of
        E79 Part Addition activity;

    Properties:
        -
    Examples:
        - the insertion of the final nail (E79) added the last nail in George VI’s coffin (E18)
    In First Order Logic:
        P111(x,y) ⊃ E79(x)
        P111(x,y) ⊃ E18(y)
        P111(x,y) ⊃ P12(x,y)
        P111(x,y) ⊃ P16(x,y)

    """

    p111_added: Optional[str] = Field(default=None, description='P111 added (was added by)')


# ******************************************************************************************************************* #


class P112Diminished(PropertyMixin):
    """'P112 diminished (was diminished by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P112

    Domain:
        E80 Part Removal
    Range:
        E24 Physical Human-Made Thing
    SubProperty Of:
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance E24 Physical Human-Made Thing that was diminished by an instance of
        E80 Part Removal;

        Although an instance of E80 Part removal activity normally concerns only one instance of
        E24 Physical Human-Made Thing, it is possible to imagine circumstances under which more than one item might be
        diminished by a single instance of E80 Part Removal activity;

    Properties:
        -
    Examples:
        - the coffin of Tut-Ankh-Amun (E22) was diminished by The opening of the coffin of Tut-Ankh-Amun (E80)
    In First Order Logic:
        P112(x,y) ⊃ E80(x)
        P112(x,y) ⊃ E24(y)
        P112(x,y) ⊃ P31(x,y)

    """

    p112_diminished: Optional[str] = Field(default=None, description='P112 diminished (was diminished by)')


# ******************************************************************************************************************* #


class P113Removed(PropertyMixin):
    """'P113 removed (was removed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P113

    Domain:
        E80 Part Removal
    Range:
        E18 Physical Thing
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E18 Physical Thing that is removed during an instance of
        E80 Part Removal activity;

    Properties:
        -
    Examples:
        - the opening of the coffin of Tut-Ankh-Amun (E80) removed The mummy of Tut-Ankh-Amun (E20,E22)
    In First Order Logic:
        P113(x,y) ⊃ E80(x)
        P113(x,y) ⊃ E18(y)
        P113(x,y) ⊃ P12(x,y)

    """

    p113_removed: Optional[str] = Field(default=None, description='P113 removed (was removed by)')


# ******************************************************************************************************************* #


class P123ResultedIn(PropertyMixin):
    """'P123 resulted in (resulted from)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P123

    Domain:
        E81 Transformation
    Range:
        E18 Physical Thing
    SubProperty Of:
        E63 Beginning of Existence. P92 brought into existence (was brought into existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance or instances of E18 Physical Thing that are the result of an instance
        of E81 Transformation. New items replace the transformed item or items, which cease to exist as units of
        documentation. The physical continuity between the old and the new is expressed by the links to the common
        instance of E81 Transformation

    Properties:
        -
    Examples:
        - the transformation of the Venetian Loggia in Heraklion into a city hall (E81) resulted in the City Hall
          of Heraklion (E22)
        - the death and mummification of Tut-Ankh-Amun (E81) resulted in the Mummy of Tut-Ankh-Amun (E22 and E20)
    In First Order Logic:
        P123(x,y) ⊃ E81(x)
        P123(x,y) ⊃ E18(y)
        P123(x,y) ⊃ P92(x,y)

    """

    p123_resulted_in: Optional[str] = Field(default=None, description='P123 resulted in (resulted from)')


# ******************************************************************************************************************* #


class P124Transformed(PropertyMixin):
    """'P124 transformed (was transformed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P124

    Domain:
        E81 Transformation
    Range:
        E18 Physical Thing
    SubProperty Of:
        E64 End of Existence. P93 took out of existence (was taken out of existence by): E77 Persistent Item
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary (1,n:0,1)

    Scope Note:
        This property identifies the instance or instances E18 Physical Thing that have ceased to exist due to
        an instance of E81 Transformation;

        The item that has ceased to exist and was replaced by the result of the Transformation. The continuity
        between both items, the new and the old, is expressed by the links to the common instance of
        E81 Transformation;

    Properties:
        -
    Examples:
        - the transformation of the Venetian Loggia in Heraklion into a city hall (E81) transformed
          the Venetian Loggia in Heraklion (E22)
        - the death and mummification of Tut-Ankh-Amun (E81) transformed the ruling Pharao Tut-Ankh-Amun (E21)
    In First Order Logic:
        P124(x,y) ⊃ E81(x)
        P124(x,y) ⊃ E18(y)
        P124(x,y) ⊃ P93(x,y)

    """

    p124_transformed: Optional[str] = Field(default=None, description='P124 transformed (was transformed by)')


# ******************************************************************************************************************* #


class P125UsedObjectOfType(PropertyMixin):
    """'P125 used object of type (was type of object used in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P125

    Domain:
        E7 Activity
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        E7 Activity. P32 used general technique (was technique of): E55 Type
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E7 Activity to an instance of E55 Type,which defines used in
        an instance of E7 Activity, when the specific instance is either unknown or not of interest, such as
        use of "a hammer";

    Properties:
        -
    Examples:
        - at the Battle of Agincourt (E7), the English archers used object of type long bow (E55)
    In First Order Logic:
        P125(x,y) ⊃ E7(x)
        P125(x,y) ⊃ E55(y)
        P125(x,y) iff (∃z)[E70(z) ∧ P16(x,z) ∧ P2(z,y)]

    """

    p125_used_object_of_type: Optional[str] = Field(
        default=None,
        description='P125 used object of type (was type of object used in)'
    )


# ******************************************************************************************************************* #


class P126Employed(PropertyMixin):
    """'P126 employed (was employed in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P126

    Domain:
        E11 Modification
    Range:
        E57 Material
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance of E57 Material employed in aninstanc of E11 Modification;

        The instance of E57 Material used during the instance of E11 Modification does not necessarily become
        incorporated into the instance of E24 Physical Human-Made Thing that forms the subject of the instance
        of E11 Modification;

    Properties:
        -
    Examples:
        - the repairing of the Queen Mary (E11) employed Steel (E57)
        - distilled water (E57) was employed in the restoration of the Sistine Chapel (E11)
    In First Order Logic:
        P126(x,y) ⊃ E11(x)
        P126(x,y) ⊃ E57(y)

    """

    p126_employed: Optional[str] = Field(default=None, description='P126 employed (was employed in)')


# ******************************************************************************************************************* #


class P134Continued(PropertyMixin):
    """'P134 continued (was continued by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P134

    Domain:
        E7 Activity
    Range:
        E7 Activity
    SubProperty Of:
        E7 Activity. P15 was influenced by (influenced): E1 CRM Entity
        E2 Temporal Entity. P174 starts before the end of (ends after the start of): E2 Temporal Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates two instances of E7 Activity, where the domain is considered as an intentional
        continuation of the range. A continuation of an activity may happen when the continued activity is still
        ongoing or after the continued activity has completely ended. The continuing activity may have started
        already before it decided to continue the other one. Continuation implies a coherence of intentions and
        outcomes of the involved activities;

        This property is not transitive;

    Properties:
        -
    Examples:
        - the construction of the Kölner Dom (Cologne Cathedral) (E7), abandoned in the 15th century, was continued by
          construction in the 19th century adapting the initial plans so as to preserve the intended appearance (E7)
    In First Order Logic:
        P134(x,y) ⊃ E7(x)
        P134(x,y)⊃ E7(y)
        P134(x,y) ⊃ P15(x,y)
        P134(x,y) ⊃ P174(x,y)

    """

    p134_continued: Optional[str] = Field(default=None, description='P134 continued (was continued by)')


# ******************************************************************************************************************* #


class P135CreatedType(PropertyMixin):
    """'P135 created type (was created by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P134

    Domain:
        E83 Type Creation
    Range:
        E55 Type
    SubProperty Of:
        E65 Creation. P94 has created (was created by): E28 Conceptual Object
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary (1,n:0,1)

    Scope Note:
        This property identifies the instance of E55 Type, which is created in an instance of E83Type Creation
        activity;

    Properties:
        -
    Examples:
        - The description of a new ribbon worm species by Bürger (E83) created type
          ‘Lineus coxinus (Bürger, 1892)’ (E55)
    In First Order Logic:
        P135(x,y) ⊃ E83(x)
        P135(x,y) ⊃ E55(y)
        P135(x,y) ⊃ P94(x,y)

    """

    p135_created_type: Optional[str] = Field(default=None, description='P135 created type (was created by)')


# ******************************************************************************************************************* #


class P136WasBasedOn(PropertyMixin):
    """'P136 was based on (supported type creation)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P136

    Domain:
        E83 Type Creation
    Range:
        E1 CRM Entity
    SubProperty Of:
        E7 Activity. P15 was influenced by (influenced): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies one or more instances of E1 CRM Entity that were used as evidence to declare a new
        instance of E55 Type;

        The examination of these items is often the only objective way to understand the precise characteristics of
        a new type. Such items should be deposited in a museum or similar institution for that reason. The taxonomic
        role renders the specific relationship of each item to the type, such as "holotype" or "original element";

    Properties:
        P136.1 in the taxonomic role: E55 Type
    Examples:
        - the taxon creation of the plant species ‘Serratula glauca Linné, 1753.’ (E83) was based on Object
          BM000576251 of the Clayton Herbarium (E20) in the taxonomic role original element (E55)
    In First Order Logic:
        P136(x,y) ⊃ E83(x)
        P136(x,y) ⊃ E1(y)
        P136(x,y,z) ⊃ [P136(x,y) ∧ E55(z)]
        P136(x,y) ⊃ P15(x,y)

    """

    p136_was_based_on: Optional[str] = Field(default=None, description='P136 was based on (supported type creation)')


# ******************************************************************************************************************* #


class P140AssignedAttributeTo(PropertyMixin):
    """'P140 assigned attribute to (was attributed by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P140

    Domain:
        E13 Attribute Assignment
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        E14 Condition Assessment. P34 concerned (was assessed by): E18 Physical Thing
        E16 Measurement. P39 measured (was measured by): E1 CRM Entity
        E17 Type Assignment. P41 classified (was classified by): E1 CRM Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity about
        which it made an attribution. The instance of E1 CRM Entity plays the role of the domain of the attribution;

        The kind of attribution made should be documented using P177 assigned property type;

    Properties:
        -
    Examples:
        - February 1997 Current Ownership Assessment of Martin Doerr’s silver cup (E13) assigned attribute to Martin
          Doerr’s silver cup (E19)
        - 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned attribute to
          silver cup 232 (E19)
    In First Order Logic:
        P140(x,y) ⊃ E13(x)
        P140(x,y) ⊃ E1(y)

    """

    p140_assigned_attribute_to: Optional[str] = Field(
        default=None,
        description='P140 assigned attribute to (was attributed by)'
    )


# ******************************************************************************************************************* #


class P141Assigned(PropertyMixin):
    """'P141 assigned (was assigned by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P141

    Domain:
        E13 Attribute Assignment
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        E14 Condition Assessment. P35 has identified (was identified by): E3 Condition State
        E15 Identifier Assignment. P37 assigned (was assigned by): E42 Identifier
        E15 Identifier Assignment. P38 deassigned (was deassigned by): E42 Identifier
        E16 Measurement. P40 observed dimension (was observed in): E54 Dimension
        E17 Type Assignment. P42 assigned (was assigned by): E55 Type
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E13 Attribute Assignment with the instance of E1 CRM Entity used
        in the attribution. The instance of E1 CRM Entity here plays the role of the range of the attribution;

        The kind of attribution made should be documented using p177 assigned property type;

    Properties:
        -
    Examples:
        - February 1997 Current Ownership Assessment of Martin Doerr’s silver cup (E13) assigned Martin Doerr (E21)
        - 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned object
          identifier 232
    In First Order Logic:
        P141(x,y) ⊃ E13(x)
        P141(x,y) ⊃ E1(y)

    """

    p141_assigned: Optional[str] = Field(default=None, description='P141 assigned (was assigned by)')


# ******************************************************************************************************************* #


class P142UsedConstituent(PropertyMixin):
    """'P142 used constituent (was used in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P142

    Domain:
        E15 Identifier Assignment
    Range:
        E90 Symbolic Object
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        (0:n,0:n)

    Scope Note:
        This property associates an instance of E15 Identifier Assignment with the instance of E90 Symbolic Object
        used as constituent of an instance of E42 Identifier in this act of assignment;

    Properties:
        -
    Examples:
        - On June 1, 2001 assigning the personal name identifier “Guillaume, de Machaut, ca. 1300-1377” (E15) used
          constituent “ca. 1300-1377” (E41)
        - Assigning a uniform title to the anonymous textual work known as ‘The Adoration of the Shepherds’(E15) used
          constituent ‘Coventry’ (E41)
        - Assigning a uniform title to Pina Bausch’s choreographic work entitled ‘Rite of spring’ (E15) used
          constituent ‘(Choreographic Work: Bausch)’(E90)
        - Assigning a uniform title to the motion picture directed in 1933 by Merian C. Cooper and
          Ernest B. Schoedsack and entitled ‘King Kong’ (E15) used constituent ‘1933’ (E41)
        - Assigning the corporate name identifier ‘Univerza v Ljubljani. Oddelek za bibliotekarstvo’
          to The Department for library science of the University of Ljubljana (E15) used constituent
          ‘Univerza v Ljubljani’ (E42)
    In First Order Logic:
        P142(x,y) ⊃ E15(x)
        P142(x,y) ⊃ E90(y)
        P142(x,y) ⊃ P16(x,y)

    """

    p142_used_constituent: Optional[str] = Field(default=None, description='P142 used constituent (was used in)')


# ******************************************************************************************************************* #


class P143Joined(PropertyMixin):
    """'P143 joined (was joined by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P143

    Domain:
        E85 Joining
    Range:
        E39 Actor
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor that becomes member of an instance of E74 Group in an
        instance of E85 Joining;

        Joining events allow for describing people becoming members of a group with the more detailed path E74 Group,
        P144i gained member by, E85 Joining, P143 joined , E39 Actor, compared to the shortcut offered by P107 has
        current or former member (is current or former member of);

    Properties:
        -
    Examples:
        - The election of Sir Isaac Newton as Member of Parliament to the Convention Parliament of 1689 (E85) joined
          Sir Isaac Newton (E21)
        - The inauguration of Mikhail Sergeyevich Gorbachev as leader of the Union of Soviet Socialist Republics
          (USSR) in 1985 (E85) joined Mikhail Sergeyevich Gorbachev (E21)
        - The implementation of the membership treaty January 1. 1973 between EU and Denmark (E85) joined
          Denmark (E74)
    In First Order Logic:
        P143(x,y) ⊃ E85(x)
        P143(x,y) ⊃ E39(y)
        P143(x,y) ⊃ P11(x,y)

    """

    p143_joined: Optional[str] = Field(default=None, description='P143 joined (was joined by)')


# ******************************************************************************************************************* #


class P144JoinedWith(PropertyMixin):
    """'P144 joined with (gained member by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P144

    Domain:
        E85 Joining
    Range:
        E74 Group
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E74 Group of which an instance of E39 Actor becomes a member through
        an instance of E85 Joining;

        Although a Joining activity normally concerns only one instance of E74 Group, it is possible to imagine
        circumstances under which becoming member of one Group implies becoming member of another Group as well;

        Joining events allow for describing people becoming members of a group with a more detailed path from
        E74 Group through, P144i gained member by, E85 Joining, P143 joined , E39 Actor, compared to the shortcut
        offered by P107 has current or former member (is current or former member of);

        The property P144.1 kind of member can be used to specify the type of membership or the role the member has
        in the group;

    Properties:
        P144.1 kind of member: E55 Type
    Examples:
        - The election of Sir Isaac Newton as Member of Parliament to the Convention Parliament of 1689 (E85) joined
          with the Convention Parliament (E74)
        - The inauguration of Mikhail Sergeyevich Gorbachev as Leader of the Union of Soviet Socialist Republics
          (USSR) in 1985 (E85) joined with the office of Leader of the Union of Soviet Socialist Republics (USSR)
          (E74) with P144.1 kind of member President (E55)
        - The implementation of the membership treaty January 1. 1973 between EU and Denmark (E85) joined with
          EU (E74)
    In First Order Logic:
        P144(x,y) ⊃ E85(x)
        P144(x,y)⊃ E74(y)
        P144(x,y,z) ⊃ [P144(x,y) ∧ E55(z)]
        P144(x,y) ⊃ P11(x,y)

    """

    p144_joined_with: Optional[str] = Field(default=None, description='P144 joined with (gained member by)')


# ******************************************************************************************************************* #


class P145Separated(PropertyMixin):
    """'P145 separated (left by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P145

    Domain:
        E86 Leaving
    Range:
        E39 Actor
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor that leaves an instance of E74 Group through an instance
        of E86 Leaving;

    Properties:
        -
    Examples:
        - The end of Sir Isaac Newton’s duty as Member of Parliament for the University of Cambridge to the Convention
          Parliament in 1702 separated Sir Isaac Newton
        - George Washington’s leaving office in 1797 separated George Washington
        - The implementation of the treaty regulating the termination of Greenland membership in EU between EU,
          Denmark and Greenland February 1. 1985 (E86) separated Greenland (E74)
    In First Order Logic:
        P145(x,y) ⊃ E86(x)
        P145(x,y) ⊃ E39(y)
        P145(x,y) ⊃ P11(x,y)

    """

    p145_separated: Optional[str] = Field(default=None, description='P145 separated (left by)')


# ******************************************************************************************************************* #


class P146SeparatedFrom(PropertyMixin):
    """'P146 separated from (lost member by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P146

    Domain:
        E86 Leaving
    Range:
        E74 Group
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E74 Group an instance of E39 Actor leaves through an instance of
        E86 Leaving;

        Although a Leaving activity normally concerns only one instance of E74 Group, it is possible to imagine
        circumstances under which leaving one E74 Group implies leaving another E74 Group as well;

    Properties:
        -
    Examples:
        - The end of Sir Isaac Newton’s duty as Member of Parliament for the University of Cambridge to the Convention
          Parliament in 1702 separated from the Convention Parliament
        - George Washington’s leaving office in 1797 separated from the office of President of the United States
        - The implementation of the treaty regulating the termination of Greenland membership in EU between EU,
          Denmark and Greenland February 1. 1985 separated from EU (E74)
    In First Order Logic:
        P146(x,y) ⊃ E86(x)
        P146(x,y) ⊃ E74(y)
        P146(x,y) ⊃ P11(x,y)

    """

    p146_separated_from: Optional[str] = Field(default=None, description='P146 separated from (lost member by)')


# ******************************************************************************************************************* #


class P147Curated(PropertyMixin):
    """'P147 curated (was curated by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P147

    Domain:
        E87 Curation Activity
    Range:
        E78 Curated Holding
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of E87 Curation Activity with the instance of E78 Curated Holdingwith
        that is subject of that curation activity following some implicit or explicit curation plan;

    Properties:
        -
    Examples:
        - The activities (E87) by the Benaki Museum curated the acquisition of dolls and games of urban and folk
          manufacture dating from the 17th to the 20th century, from England, France and Germany for the “Toys, Games
          and Childhood Collection (E78) of the Museum
        - The activities (E87) of the Historical Museum of Crete, Heraklion, Crete, curated the development of the
          permanent Numismatic Collection (E78)
        - The activities (E87) by Mikael Heggelund Foslie curated the Mikael Heggelund Foslie’s coralline red algae
          Herbarium
    In First Order Logic:
        P147(x,y) ⊃ E87(x)
        P147(x,y) ⊃ E78(y)

    """

    p147_curated: Optional[str] = Field(default=None, description='P147 curated (was curated by)')


# ******************************************************************************************************************* #


class P151WasFormedFrom(PropertyMixin):
    """'P151 was formed from (participated in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P151

    Domain:
        E66 Formation
    Range:
        E74 Group
    SubProperty Of:
        E5 Event. P11 had participant (participated in): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        (0,n:0:n)

    Scope Note:
        This property associates an instance of E66 Formation with an instance of E74 Group from which the new group
        was formed preserving a sense of continuity such as in mission, membership or tradition;

    Properties:
        -
    Examples:
        - The formation of the House of Bourbon-Conti in 1581 (E66) was formed from House of Condé (E74)
    In First Order Logic:
        P151(x,y) ⊃ E66(x)
        P151(x,y) ⊃ E74(y)
        P151(x,y) ⊃ P11(x,y)

    """

    p151_was_formed_from: Optional[str] = Field(default=None, description='P151 was formed from (participated in)')


# ******************************************************************************************************************* #


class P173StartsBeforeOrWithTheEndOf(PropertyMixin):
    """'P173 starts before or with the end of (ends after or with the start of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P173

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        -
    SuperProperty Of:
        E2 Temporal Entity. P174 starts before the end of (ends after the start of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts before
        or simultaneously with the end of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart ≤ Bend is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to the disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets, met-by, overlaps, starts, started-by, contains, finishes, finished-by, equals,
        during, overlapped by}

    Properties:
        -
    Examples:
        - The legendary run from Marathon to Athens 490BC (E7) starts before or with the end of The Battle of
          Marathon 490BC (E7)
    In First Order Logic:
        P173(x,y) ⊃ E2(x)
        P173(x,y) ⊃ E2(y)

    """

    p173_starts_before_or_with_the_end_of: Optional[str] = Field(
        default=None,
        description='P173 starts before or with the end of (ends after or with the start of)'
    )


# ******************************************************************************************************************* #


class P174StartsBeforeTheEndOf(PropertyMixin):
    """'P174 starts before the end of (ends after the start of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P174

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P173 starts before or with the end of (ends after or with
        the start of): E2 Temporal Entity
    SuperProperty Of:
        E7 Activity. P134 continued (was continued by): E7 Activity
        E2 Temporal Entity. P175 starts before or with the start of (starts after or with
        the start of): E2 Temporal Entity
        E2 Temporal Entity. P184 ends before or with the end of (ends with or after the end of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts
        definitely before the end of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart < Bend is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185.

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983] :{before, meets, overlaps, starts, started-by, contains, finishes, finished-by, equals, during,
        overlapped by}

        Typically, this property is a consequence of a known influence of some event on another event or activity,
        such as a novel written by someone being continued by someone else, or the knowledge of a defeat on a distant
        battlefield causing people to end their ongoing activities. This property is not transitive;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P174(x,y) ⊃ E2(x)
        P174(x,y) ⊃ E2(y)
        P174(x,y) ⊃ P173(x,y)

    """

    p174_starts_before_the_end_of: Optional[str] = Field(
        default=None,
        description='P174 starts before the end of (ends after the start of)'
    )


# ******************************************************************************************************************* #


class P175StartsBeforeOrWithTheStartOf(PropertyMixin):
    """'P175 starts before or with the start of (starts after or with the start of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P175

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P174 starts before the end of (ends after the start of): E2 Temporal Entity
    SuperProperty Of:
        E2 Temporal Entity. P176 starts before the start of (starts after the start of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts before
        or simultaneously with the start of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart ≤ Bstart is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets, overlaps, starts, started-by, contains, finished-by, equals}

        In a model with fuzzy borders, this property will not be transitive;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P175(x,y) ⊃ E2(x)
        P175(x,y) ⊃ E2(y)
        P175(x,y) ⊃ P174(x,y)

    """

    p175_starts_before_or_with_the_start_of: Optional[str] = Field(
        default=None,
        description='P175 starts before or with the start of (starts after or with the start of)'
    )


# ******************************************************************************************************************* #


class P176StartsBeforeTheStartOf(PropertyMixin):
    """'P176 starts before the start of (starts after the start of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P176

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P175 starts before or with the start of (starts after or with the start
        of): E2 Temporal Entity
    SuperProperty Of:
        E2 Temporal Entity. P182 ends before or with the start of (starts after or with
        the end of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity starts
        definitely before the start of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Astart < Bstart is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets, overlaps, contains, finished-by}. This property is transitive;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P176(x,y) ⊃ E2(x)
        P176(x,y) ⊃ E2(y)
        P176(x,y) ⊃ P175(x,y)

    """

    p176_starts_before_the_start_of: Optional[str] = Field(
        default=None,
        description='P176 starts before the start of (starts after the start of)'
    )


# ******************************************************************************************************************* #


class P177AssignedPropertyType(PropertyMixin):
    """'P177 assigned property type' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P177

    Domain:
        E13 Attribute Assignment
    Range:
        E55 Type
    SubProperty Of:
        E1 CRM Entity. P2 has type (is type of): E55 Type
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of E13 Attribute Assignment with the type of property or relation that
        this assignment maintains to hold between the item to which it assigns an attribute and the attribute itself.
        Note that the properties defined by the CIDOC CRM also constitute instances of E55 Type themselves. The
        direction of the assigned property type is understood to be from the attributed item (the range of property
        P140 assigned attribute to) to the attribute item (the range of the property P141 assigned). More than one
        property type may be assigned to hold between two items;

        A comprehensive explanation about refining CIDOC CRM concepts by E55 Type is given in the section “About
        Types” in the section on “Specific Modelling Constructs” of this document;

    Properties:
        -
    Examples:
        - February 1997 Current Ownership Assessment of Martin Doerr’s silver cup (E13) assigned property type
          P52 has former or current owner (is former or current keeper of) (E55)
        - 01 June 1997 Identifier Assignment of the silver cup donated by Martin Doerr (E15) assigned property type
          P48 has preferred identifier (is preferred identifier of) (E55)
    In First Order Logic:
        P177(x,y) ⊃ E13(x)
        P177(x,y) ⊃ E55(y)

    """

    p177_assigned_property_type: Optional[str] = Field(default=None, description='P177 assigned property type')


# ******************************************************************************************************************* #


class P179HadSalesPrice(PropertyMixin):
    """'P179 had sales price (was sales price of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P179

    Domain:
        E96 Purchase
    Range:
        E97 Monetary Amount
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        (1,n; 0,n)

    Scope Note:
        This property establishes the relationship between an instance of E96 Purchase and the instance of
        E97 Monetary Amount that forms the compensation for the transaction. The monetary amount agreed upon may
        change in the course of the purchase activity;

    Properties:
        -
    Examples:
        - the sale of Vincent van Gogh’s “Vase with Fifteen Sunflowers” on 1987/03/30 (E96) had sales price Christies’
          hammer price for “Vase with Fifteen Sunflowers” (E97).
        - the purchase of 10 okka of nails by the captain A. Syrmas on 18/9/1895 (E96) had sales price 20 piastre
          (grosi) (E97)
    In First Order Logic:
        P179(x,y) ⊃ E96(x)
        P179(x,y) ⊃ E97(y)

    """

    p179_had_sales_price: Optional[str] = Field(default=None, description='P179 had sales price (was sales price of)')


# ******************************************************************************************************************* #


class P182EndsBeforeOrWitheStartOf(PropertyMixin):
    """'P182 ends before or with the start of (starts after or with the end of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P182

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P176 starts before the start of (starts after the start of): E2 Temporal Entity
        E2 Temporal Entity. P185 ends before the end of (ends after the end of): E2 Temporal Entity
    SuperProperty Of:
        E2 Temporal Entity. P183 ends before the start of (starts after the end of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends before
        or simultaneously with the start of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend ≤ Bstart is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets}

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P182(x,y) ⊃ E2(x)
        P182(x,y) ⊃ E2(y)
        P182(x,y) ⊃ P176(x,y)
        P182(x,y) ⊃ P185(x,y)

    """

    p182_ends_before_or_with_start_of: Optional[str] = Field(
        default=None,
        description='P182 ends before or with the start of (starts after or with the end of)'
    )


# ******************************************************************************************************************* #


class P183EndsBeforeTheStartOf(PropertyMixin):
    """'P183 ends before the start of (starts after the end of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P183

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P182 ends before or with the start of (starts after or with
        the end of): E2 Temporal Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends
        definitely before the start of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend < Bstart is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before}

        This property is transitive;

    Properties:
        -
    Examples:
        - Gisle taking office as Bishop of Linköping 1139 AD (E7) ends before the start of The Guta saga
          composition (E65)
    In First Order Logic:
        P183(x,y) ⊃ E2(x)
        P183(x,y) ⊃ E2(y)
        P183(x,y) ⊃ P182(x,y)

    """

    p183_ends_before_the_start_of: Optional[str] = Field(
        default=None,
        description='P183 ends before the start of (starts after the end of)'
    )


# ******************************************************************************************************************* #


class P184EndsBeforeOrWithTheEndOf(PropertyMixin):
    """'P184 ends before or with the end of (ends with or after the end of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P184

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P174 starts before the end of (ends after the start of): E2 Temporal Entity
    SuperProperty Of:
        E2 Temporal Entity. P185 ends before the end of (ends after the end of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends before
        or simultaneously with the end of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend ≤ Bend is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets, overlaps, finished by, start, equals, during, finishes}

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P184(x,y) ⊃ E2(x)
        P184(x,y) ⊃ E2(y)
        P184(x,y) ⊃ P174(x,y)

    """

    p184_ends_before_or_with_the_end_of: Optional[str] = Field(
        default=None,
        description='P184 ends before or with the end of (ends with or after the end of)'
    )


# ******************************************************************************************************************* #


class P185EndsBeforeTheEndOf(PropertyMixin):
    """'P185 ends before the end of (ends after the end of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P185

    Domain:
        E2 Temporal Entity
    Range:
        E2 Temporal Entity
    SubProperty Of:
        E2 Temporal Entity. P184 ends before or with the end of (ends with or after the end of): E2 Temporal Entity
    SuperProperty Of:
        E2 Temporal Entity. P182 ends before or with the start of (starts after or with
        the end of): E2 Temporal Entity
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property specifies that the temporal extent of the domain instance A of E2 Temporal Entity ends
        definitely before the end of the temporal extent of the range instance B of E2 Temporal Entity;

        In other words, if A = [Astart, Aend] and B = [Bstart, Bend], we mean Aend < Bend is true;

        This property is part of the set of temporal primitives P173 – P176, P182 – P185;

        This property corresponds to a disjunction (logical OR) of the following Allen temporal relations
        [Allen, 1983]: {before, meets, overlaps, starts, during}

        This property is transitive;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P185(x,y) ⊃ E2(x)
        P185(x,y) ⊃ E2(y)
        P185(x,y) ⊃ P184(x,y)

    """

    p185_ends_before_the_end_of: Optional[str] = Field(
        default=None,
        description='P185 ends before the end of (ends after the end of)'
    )


# ******************************************************************************************************************* #


class P186ProducedThingOfProductType(PropertyMixin):
    """'P186 produced thing of product type (is produced by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P186

    Domain:
        E12 Production
    Range:
        E99 Product Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E12 Production with the instance of E99 Production Type, that is, the
        type of the things it produces;

    Properties:
        -
    Examples:
        - The production activity of the Volkswagen factory during 1949-1953 (E12) produced thing of product type
          Volkswagen Type 11 (Beetle) (E99);
    In First Order Logic:
        P186(x,y) ⊃ E12(x)
        P186(x,y) ⊃ E99(y)
        P186(x,y) ⊃ (∃z)[E24(z) ∧ P108(x,z) ∧ P2(z,y)]

    """

    p186_produced_thing_of_product_type: Optional[str] = Field(
        default=None,
        description='P186 produced thing of product type (is produced by)'
    )
