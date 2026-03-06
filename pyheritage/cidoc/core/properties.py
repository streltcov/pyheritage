# -*- coding: utf-8 -*-

"""Properties (mixin-classes for entity models) of CIDOC-CRM v7.0;

"""


from __future__ import annotations

from typing import Any, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core._primitives import CoercedNumber, CoercedString


__all__ = ('P1IsIdentifiedBy', 'P2HasType', 'P3HasNote', 'P4HasTimeSpan', 'P5ConsistsOf', 'P7TookPlaceAt',
           'P8TookPlaceOnOrWithin', 'P9ConsistsOf', 'P10FallsWithin', 'P11HadParticipant', 'P12OccurredInPresenceOf',
           'P13Destroyed', 'P14CarriedOutBy', 'P15WasInfluencedBy', 'P16UsedSpecificObject', 'P17WasMotivatedBy',
           'P19WasIntendedUseOf', 'P20HadSpecificPurpose', 'P21HadGeneralPurpose', 'P22TransferredTitleTo',
           'P23TransferredTitleFrom', 'P24TransferredTitleOf', 'P25Moved', 'P26MovedTo', 'P72HasLanguage',
           'P82AtSomeTimeWithin', 'P86FallsWithin', 'P90HasValue', 'P91HasUnit', 'P190HasSymbolicContent',
           'P191HadDuration', )


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
