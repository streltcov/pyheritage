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
P134 continued                      E7  -> E7
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
P179 had sales price                E96 -> E97
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
           'P39Measured', 'P40ObservedDimension', )


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
