# -*- coding: utf-8 -*-

"""Temporal phenomena entities;

-------------------------
Entities
-------------------------
E2 Temporal Entity
E3 Condition State
E4 Period
E5 Event
E6 Destruction
E7 Activity
E8 Acquisition
E9 Move
E10 Transfer of Custody
E11 Modification
E12 Production
E13 Attribute Assignment
E14 Condition Assessment
E15 Identifier Assignment
E16 Measurement
E17 Type Assignment
E63 Beginning of Existence
E64 End of Existence
E65 Creation
E66 Formation
E67 Birth
E68 Dissolution
E69 Death
E79 Part Addition
E80 Part Removal
E81 Transformation
E83 Type Creation
E85 Joining
E86 Leaving
E87 Curation Activity
E96 Purchase

"""


from pyheritage.cidoc.core.entities._crm_base import E1CRMEntity
from pyheritage.cidoc.core.entities._spacetime import E92SpaceTimeVolume
from pyheritage.cidoc.core.properties import P4HasTimeSpan, P5ConsistsOf


__all__ = ('E2TemporalEntity', 'E3ConditionState', 'E4Period', 'E5Event', 'E6Destruction', 'E7Activity',
           'E8Acquisition', 'E9Move', 'E10TransferOfCustody', 'E11Modification', 'E12Production',
           'E13AttributeAssignment', 'E14ConditionAssessment', 'E15IdentifierAssignment', 'E16Measurement',
           'E17TypeAssignment', 'E63BeginningOfExistence', 'E64EndOfExistence', )


class E2TemporalEntity(P4HasTimeSpan, E1CRMEntity):
    """'E2 Temporal Entity' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E2

    SubClass Of:
        E1 CRM Entity

    SuperClass Of:
        E3 Condition State
        E4 Period

    Scope Note:
        This class comprises all phenomena, such as the instances of E4 Periods and E5 Events, which happen over a
        limited extent in time. This extent in time must be contiguous, i.e., without gaps. In case the defining kinds
        of phenomena for an instance of E2 Temporal Entity cease to happen, and occur later again at another time, we
        regard that the former instance of E2 Temporal Entity has ended and a new instance has come into existence. In
        more intuitive terms, the same event cannot happen twice;
        In some contexts, such phenomena are also called perdurants. This class is disjoint from E77 Persistent Item
        and is an abstract class that typically has no direct instances. E2 Temporal Entity is specialized into
        E4 Period, which applies to a particular geographic area (defined with a greater or lesser degree of
        precision), and E3 Condition State, which applies to instances of E18 Physical Thing;

    """


# ******************************************************************************************************************* #


class E3ConditionState(P5ConsistsOf, E2TemporalEntity):
    """'E3 Condition State' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E3

    SubClass Of:
        E2 Temporal Entity

    SuperClass Of:
        -

    Scope Note:
        This class comprises the states of objects characterised by a certain condition over a time-span.

        An instance of this class describes the prevailing physical condition of any material object or feature during
        a specific instance of E52 Time Span. In general, the time-span for which a certain condition can be asserted
        may be shorter than the real time-span, for which this condition held;

        The nature of that condition can be described using P2 has type. For example, the instance of
        E3 Condition State “condition of the SS Great Britain between 22 September 1846 and 27 August 1847” can be
        characterized as an instance “wrecked” of E55 Type;

    Examples:
        - the "reconstructed" state of the “Amber Room” in Tsarskoje Selo from summer 2003 until now (Owen, 2009)
        - the "ruined" state of Peterhof Palace near Saint Petersburg from 1944 to 1946 (Maddox, 2015)
        - the state of my turkey in the oven at 14:30 on 25 December, 2002 (P2 has type: E55 Type “still not cooked”)
        - the topography of the leaves of Sinai Printed Book 3234.2361 on the 10th of July 2007 (described as: of
          type "cockled")

    In First Order Logic:
        E3(x) ⊃ E2(x)

    Properties:
        P5 consists of (forms part of): E3 Condition State

    """


# ******************************************************************************************************************* #


class E4Period(E2TemporalEntity, E92SpaceTimeVolume):
    """'E4 Period' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E4

    SubClass Of:
        E2 Temporal Entity
        E92 Spacetime Volume
    SuperClass Of:
        E5 Event
    Scope Note:
        This class comprises sets of coherent phenomena or cultural manifestations occurring in time and space;

        It is the social or physical coherence of these phenomena that identify an instance of E4 Period and not the
        associated spatiotemporal extent. This extent is only the “ground” or space in an abstract physical sense that
        the actual process of growth, spread and retreat has covered. Consequently, different periods can overlap and
        coexist in time and space, such as when a nomadic culture exists in the same area and time as a sedentary
        culture. This also means that overlapping land use rights, common among first nations, amounts to overlapping
        periods;

        Often, this class is used to describe prehistoric or historic periods such as the “Neolithic Period”, the
        “Ming Dynasty” or the “McCarthy Era”, but also geopolitical units and activities of settlements are regarded
        as special cases of E4 Period. However, there are no assumptions about the scale of the associated phenomena.
        In particular all events are seen as synthetic processes consisting of coherent phenomena. Therefore
        E4 Period is a superclass of E5 Event. For example, a modern clinical birth, an instance of E67 Birth, can be
        seen as both a single event, i.e., an instance of E5 Event, and as an extended period, i.e., an instance of
        E4 Period, that consists of multiple physical processes and complementary activities performed by multiple
        instances of E39 Actor;

        As the actual extent of an instance of E4 Period in spacetime we regard the trajectories of the participating
        physical things during their participation in an instance of E4 Period. This includes the open spaces via
        which these things have interacted and the spaces by which they had the potential to interact during that
        period or event in the way defined by the type of the respective period or event. Examples include the air
        in a meeting room transferring the voices of the participants. Since these phenomena are fuzzy, we assume
        the spatiotemporal extent to be contiguous, except for cases of phenomena spreading out over islands or other
        separated areas, including geopolitical units distributed over disconnected areas such as islands or colonies;

        Whether the trajectories necessary for participants to travel between these areas are regarded as part of the
        spatiotemporal extent or not has to be decided in each case based on a concrete analysis, taking use of the
        sea for other purposes than travel, such as fishing, into consideration. One may also argue that the
        activities to govern disconnected areas imply travelling through spaces connecting them and that these areas
        hence are spatially connected in a way, but it appears counterintuitive to consider for instance travel routes
        in international waters as extensions of geopolitical units;

        We model E4 Period as a subclass of E2 Temporal Entity and of E92 Spacetime Volume. The latter is intended as
        a phenomenal spacetime volume as defined in CIDOC CRMgeo (Doerr and Hiebel, 2013). By virtue of this multiple
        inheritance we can discuss the physical extent of an instance of E4 Period without representing each instance
        of it together with an instance of its associated spacetime volume. This model combines two quite different
        kinds of substance: an instance of E4 Period is a phenomenon while an instance of E92 Spacetime Volume is an
        aggregation of points in spacetime. However, the real spatiotemporal extent of an instance of E4 Period is
        regarded to be unique to it due to all its details and fuzziness; its identity and existence depends uniquely
        on the identity of the instance of E4 Period. Therefore this multiple inheritance is unambiguous and effective
        and furthermore corresponds to the intuitions of natural language;

        Typical use of this class in cultural heritage documentation is for documenting cultural and artistic periods.
        There are two different conceptualisations of ‘artistic style’, defined either by physical features or by
        historical context. For example, “Impressionism” can be viewed as a period in the European sphere of influence
        lasting from approximately 1870 to 1905 during which paintings with particular characteristics were produced
        by a group of artists that included (among others) Monet, Renoir, Pissarro, Sisley and Degas. Alternatively,
        it can be regarded as a style applicable to all paintings sharing the characteristics of the works produced by
        the Impressionist painters, regardless of historical context. The first interpretation is an instance of
        E4 Period, and the second defines morphological object types that fall under E55 Type;

        A geopolitical unit as a specific case of an instance of E4 Period is the set of activities and phenomena
        related to the claim of power, the consequences of belonging to a jurisdictional area and an administrative
        system that establishes a geopolitical unit. Examples from the modern period are countries or administrative
        areas of countries such as districts whose actions and structures define activities and phenomena in the area
        that they intend to govern. The borders of geopolitical units are often defined in contracts or treaties
        although they may deviate from the actual practice. The spatiotemporal properties of Geopolitical units can be
        modelled through the properties inherited from E92 Spacetime Volume;

        Another specific case of an instance of E4 Period is the actual extent of the set of activities and phenomena
        as evidenced by their physical traces that define a settlement, such as the populated period of Nineveh;

    Examples:
        - Jurassic (Hallam, 1975)
        - Populated Period of Nineveh
        - Imperial Rome under Marcus Aurelius
        - European Bronze Age (Harrison, c2004)
        - Italian Renaissance (Macdonald, 1992)
        - Thirty Years War (Lee, 1991)
        - Sturm und Drang (Berkoff, 2013)
        - Cubism (Cox, 2000)
    In First Order Logic:
        E4(x) ⊃ E2(x)
        E4(x) ⊃ E92(x)
    Properties:
        P7 took place at (witnessed): E53 Place
        P8 took place on or within (witnessed): E18 Physical Thing
        P9 consists of (forms part of): E4 Period

    """


# ******************************************************************************************************************* #


class E5Event(E4Period):
    """'E5 Event' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E5

    SubClass Of:
        E4 Period
    SuperClass Of:
        E7 Activity
        E63 Beginning of Existence
        E64 End of Existence
    Scope Note:
        This class comprises distinct, delimited and coherent processes and interactions of a material nature, in
        cultural, social or physical systems, involving and affecting instances of E77 Persistent Item in a way
        characteristic of the kind of process. Typical examples are meetings, births, deaths, actions of decision
        taking, making or inventing things, but also more complex and extended ones such as conferences, elections,
        building of a castle, or battles;

        While the continuous growth of a tree lacks the limits characteristic of an event, its germination from a seed
        does qualify as an event. Similarly the blowing of the wind lacks the distinctness and limits of an event, but
        a hurricane, flood or earthquake would qualify as an event. Mental processes are considered as events, in
        cases where they are connected with the material externalization of their results; for example the creation of
        a poem, a performance or a change of intention that becomes obvious from subsequent actions or declarations;

        The effects of an instance of E5 Event may not lead to relevant permanent changes of properties or relations
        of the items involved in it, for example an unrecorded performances. Of course, in order to be documented,
        some kind of evidence for an event must exist, be it witnesses, traces or products of the event;

        While instances of E4 Period always require some form of coherence between its constituent phenomena, in
        addition, the essential constituents of instances of E5 Event should contribute to an overall effect; for
        example the statements made during a meeting and the listening of the audience;

        Viewed at a coarse level of detail, an instance of E5 Event may appear as if it had an ‘instantaneous’ overall
        effect, but any process or interaction of material nature in reality have an extent in time and space. At a
        fine level, instances of E5 Event may be analyzed into component phenomena and phases within a space and
        timeframe, and as such can be seen as a period, regardless of the size of the phenomena. The reverse is not
        necessarily the case: not all instances of E4 Period give rise to a noteworthy overall effect and are thus not
        instances of E5 Event;

    Examples:
        - the birth of Cleopatra (E67) (Pomeroy, 1984)
        - the destruction of Herculaneum by volcanic eruption in 79 AD (E6) (Camardo, 2013)
        - World War II (E7) (Barber, 1994)
        - the Battle of Stalingrad (E7) (Hoyt, 1993)
        - the Yalta Conference (E7) (Harbutt, 2010)
        - my birthday celebration 28-6-1995 (E7)
        - the falling of a tile from my roof last Sunday
        - the CIDOC Conference 2003 (E7)
    In First Order Logic:
        E5(x) ⊃ E4(x)
    Properties:
        P11 had participant (participated in): E39 Actor
        P12 occurred in the presence of (was present at): E77 Persistent Item

    """


# ******************************************************************************************************************* #


class E63BeginningOfExistence(E5Event):
    """'E63 Beginning of Existence' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E63

    SubClass Of:
        E5 Event
    SuperClass Of:
        E12 Production
        E65 Creation
        E66 Formation
        E67 Birth
        E81 Transformation
    Scope Note:
        This class comprises events that bring into existence any instance of E77 Persistent Item;

        It may be used for temporal reasoning about things (intellectual products, physical items, groups of people,
        living beings) beginning to exist; it serves as a hook for determination of a “terminus post quem” or
        “terminus ante quem”;

    Examples:
        - the birth of my child
        - the birth of Snoopy, my dog
        - the calving of the iceberg that sank the Titanic
        - the construction of the Eiffel Tower (Tissandier, 1889)
    In First Order Logic:
        E63(x) ⊃ E5(x)
    Properties:
        P92 brought into existence (was brought into existence by): E77 Persistent Item

    """


# ******************************************************************************************************************* #


class E64EndOfExistence(E5Event):
    """'E64 End of Existence' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E64

    SubClass Of:
        E5 Event
    SuperClass Of:
        E6 Destruction
        E68 Dissolution
        E69 Death
        E81 Transformation
    Scope Note:
        This class comprises events that end the existence of any instance of E77 Persistent Item;

        It may be used for temporal reasoning about things (physical items, groups of people, living beings) ceasing
        to exist; it serves as a hook for determination of a “terminus post quem” or “terminus ante quem”. In cases
        where substance from an instance of E64 Persistent Item continues to exist in a new form, the process would be
        documented as instances of E81 Transformation;

    Examples:
        - the death of Snoopy, my dog
        - the melting of the snowmanthe burning of the Temple of Artemis in Ephesos by Herostratos in 356BC
          (Trell, 1945)
    In First Order Logic:
        E64(x) ⊃ E5(x)
    Properties:
        P93 took out of existence (was taken out of existence by): E77 Persistent Item

    """


# ******************************************************************************************************************* #


class E6Destruction(E64EndOfExistence):
    """'E6 Destruction' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E6

    SubClass Of:
        E64 End of Existence
    SuperClass Of:
        -
    Scope Note:
        This class comprises events that destroy one or more instances of E18 Physical Thing such that they lose their
        identity as the subjects of documentation;

        Some destruction events are intentional, while others are independent of human activity. Intentional
        destruction may be documented by classifying the event as both an instance of E6 Destruction and of
        E7 Activity;

        The decision to document an object as destroyed, transformed or modified is context sensitive:

        1. If the matter remaining from the destruction is not documented, the event is modelled solely as an instance
           of E6 Destruction;
        2. An event should also be documented as an instance of E81 Transformation if it results in the destruction of
           one or more objects and the simultaneous production of others using parts or material from the original. In
           this case, the new items have separate identities. Matter is preserved, but identity is not;
        3. When the initial identity of the changed instance of E18 Physical Thing is preserved, the event should be
           documented as an instance of E11 Modification;

    Examples:
        - the destruction of Herculaneum by volcanic eruption in 79 AD (Camardo, 2013)
        - the destruction of Nineveh (E6, E7) (George, 2000)
        - the breaking of a champagne glass yesterday by my dog
    In First Order Logic:
        E6(x) ⊃ E64(x)
    Properties:
        P13 destroyed (was destroyed by): E18 Physical Thing

    """


# ******************************************************************************************************************* #


class E7Activity(E5Event):
    """'E7 Activity' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E7

    SubClass Of:
        E5 Event
    SuperClass Of:
        E8 Acquisition
        E9 Move
        E10 Transfer of Custody
        E11 Modification
        E13 Attribute Assignment
        E65 Creation
        E66 Formation
        E85 Joining
        E86 Leaving
        E87 Curation Activity
    Scope Note:
        This class comprises actions intentionally carried out by instances of E39 Actor that result in changes of
        state in the cultural, social, or physical systems documented;

        This notion includes complex, composite and long-lasting actions such as the building of a settlement or a
        war, as well as simple, short-lived actions such as the opening of a door;

    Examples:
        - the Battle of Stalingrad (Hoyt, 1993)
        - the Yalta Conference (Harbutt, 2010)
        - my birthday celebration 28-6-1995
        - the writing of “Faust” by Goethe (E65) (Williams, 1987)
        - the formation of the Bauhaus 1919 (E66) (Droste, 2006)
        - calling the place identified by TGN ‘7017998’ ‘Quyunjig’ by the people of Iraq
        - Kira Weber working in glass art from 1984 to 1993
        - Kira Weber working in oil and pastel painting from 1993
    In First Order Logic:
        E7(x) ⊃ E5(x)
    Properties:
        P14 carried out by (performed): E39 Actor
        P15 was influenced by (influenced): E1 CRM Entity
        P16 used specific object (was used for): E70 Thing
        P17 was motivated by (motivated): E1 CRM Entity
        P19 was intended use of (was made for): E71 Human-Made Thing
        P20 had specific purpose (was purpose of): E5 Event
        P21 had general purpose (was purpose of): E55 Type
        P32 used general technique (was technique of): E55 Type
        P33 used specific technique (was used by): E29 Design or Procedure
        P125 used object of type (was type of object used in): E55 Type
        P134 continued (was continued by): E7 Activity

    """


# ******************************************************************************************************************* #


class E8Acquisition(E7Activity):
    """'E8 Acquisition' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E8

    SubClass Of:
        E7 Activity
    SuperClass Of:
        E96 Purchase
    Scope Note:
        This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more other
        instances of E39 Actor;

        The class also applies to the establishment or loss of ownership of instances of E18 Physical Thing. It does
        not, however, imply changes of any other kinds of right. The recording of the donor and/or recipient is
        optional. It is possible that in an instance of E8 Acquisition there is either no donor or no recipient.
        Depending on the circumstances, it may describe:
        - the beginning of ownership
        - the end of ownership
        - the transfer of ownership
        - the acquisition from an unknown source
        - the loss of title due to destruction of the item

        It may also describe events where a collector appropriates legal title, for example by annexation or field
        collection. The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM
        therefore models legal ownership (E8 Acquisition) and physical custody (E10 Transfer of Custody) separately.
        Institutions will then model their specific notions of accession and deaccession as combinations of these;

    Examples:
        - the collection of a hammer-head shark of the genus Sphyrna (Carchariniformes) XXXtbc by John Steinbeck and
          Edward Ricketts at Puerto Escondido in the Gulf of Mexico on March 25th, 1940. (Steinbeck, 2000)
        - the acquisition of El Greco’s painting entitled ‘The Apostles Peter and Paul’ by the State Hermitage in
          Saint Petersburg
        - the loss of my stuffed chaffinch ‘Fringilla coelebs Linnaeus, 1758’ due to insect damage last year
    In First Order Logic:
        E8(x) ⊃ E7(x)
    Properties:
        P22 transferred title to (acquired title through): E39 Actor
        P23 transferred title from (surrendered title through): E39 Actor
        P24 transferred title of (changed ownership through): E18 Physical Thing

    """


# ******************************************************************************************************************* #


class E9Move(E7Activity):
    """'E9 Move' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E9

    SubClass Of:
        E7 Activity
    SuperClass Of:
        -
    Scope Note:
        This class comprises changes of the physical location of the instances of E19 Physical Object;

        Note, that the class E9 Move inherits the property P7 took place at (witnessed): E53 Place. This property
        should be used to describe the trajectory or a larger area within which a move takes place, whereas the
        properties P26 moved to (was destination of), P27 moved from (was origin of) describe the start and end points
        only. Moves may also be documented to consist of other moves (via P9 consists of (forms part of)), in order to
        describe intermediate stages on a trajectory. In that case, start and end points of the partial moves should
        match appropriately between each other and with the overall event;

    Examples:
        - the relocation of London Bridge from the UK to the USA. (Clarke, 1992)
        - the movement of the exhibition “Treasures of Tut-Ankh-Amun” 1976-1979 (Treasures of Tutankhamun, exhibition
          catalogue, 1972)
    In First Order Logic:
        E9(x) ⊃ E7(x)
    Properties:
        P25 moved (moved by): E19 Physical Object
        P26 moved to (was destination of): E53 Place
        P27 moved from (was origin of): E53 Place

    """


# ******************************************************************************************************************* #


class E10TransferOfCustody(E7Activity):
    """'E10 Transfer of Custody' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E10

    SubClass Of:
        E7 Activity
    SuperClass Of:
        -
    Scope Note:
        This class comprises transfers of physical custody of objects between instances of E39 Actor;

        The recording of the donor and/or recipient is optional. It is possible that in an instance of
        E10 Transfer of Custody there is either no donor or no recipient. Depending on the circumstances
        it may describe:
        - the beginning of custody
        - the end of custody
        - the transfer of custody
        - the receipt of custody from an unknown source
        - the declared loss of an object

        The distinction between the legal responsibility for custody and the actual physical possession of the object
        should be expressed using the property P2 has type (is type of). A specific case of transfer of custody is
        theft. The sense of physical possession requires that the object of custody is in the hands of the keeper
        at least with a part representative for the whole. The way, in which a representative part is defined, should
        ensure that it is unambiguous who keeps a part and who the whole and should be consistent with the identity
        criteria of the kept instance of E18 Physical Thing. For instance, in the case of a set of cutlery we may
        require the majority of pieces having been in the hands of the actor regardless which individual pieces are
        kept over time;

        The interpretation of the museum notion of "accession" differs between institutions. The CIDOC CRM therefore
        models legal ownership and physical custody separately. Institutions will then model their specific notions of
        accession and deaccession as combinations of these;

    Examples:
        - the delivery of the paintings by Secure Deliveries Inc. to the National Gallery
        - the return of Picasso’s “Guernica” to Madrid’s Prado in 1981 (Chipp, 1988)
    In First Order Logic:
        E10(x) ⊃ E7(x)
    Properties:
        P28 custody surrendered by (surrendered custody through): E39 Actor
        P29 custody received by (received custody through): E39 Actor
        P30 transferred custody of (custody transferred through): E18 Physical Thing

    """


# ******************************************************************************************************************* #


class E11Modification(E7Activity):
    """'E11 Modification' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E11

    SubClass Of:
        E7 Activity
    SuperClass Of:
        E12 Production
        E79 Part Addition
        E80 Part Removal
    Scope Note:
        This class comprises instances of E7 Activity that create, alter or change instances of
        E24 Physical Human-Made Thing;

        This class includes the production of an item from raw materials, and other so far undocumented objects, and
        the preventive treatment or restoration of an object for conservation;

        Since the distinction between modification and production is not always clear, modification is regarded as
        the more generally applicable concept. This implies that some items may be consumed or destroyed in an
        instance of E11 Modification, and that others may be produced as a result of it. An event should also be
        documented using an instance of E81 Transformation if it results in the destruction of one or more objects
        and the simultaneous production of others using parts or material from the originals. In this case, the new
        items have separate identities;

        If the instance of E29 Design or Procedure utilized for the modification prescribes the use of specific
        materials, they should be documented using property P68 foresees use of (use foreseen by): E57 Material of
        E29 Design or Procedure, rather than via P126 employed (was employed in): E57 Material;

    Examples:
        - the construction of the SS Great Britain (E12)(Gregor, 1971)
        - the impregnation of the Vasa warship in Stockholm for preservation after 1956(Håfors, 2010)
        - the transformation of the Enola Gay into a museum exhibit by the National Air and Space Museum in
          Washington DC between 1993 and 1995 (E12, E81) (Yakel, 2000)
        - the last renewal of the gold coating of the Toshogu shrine in Nikko, Japan(Cali and Dougil, 2012)
    In First Order Logic:
        E11(x) ⊃ E7(x)
    Properties:
        P31 has modified (was modified by): E18 Physical Thing
        P126 employed (was employed in): E57 Material

    """


# ******************************************************************************************************************* #


class E12Production(E11Modification, E63BeginningOfExistence):
    """'E12 Production' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E12

    SubClass Of:
        E11 Modification
        E63 Beginning of Existence
    SuperClass Of:
        -
    Scope Note:
        This class comprises activities that are designed to, and succeed in, creating one or more new items;

        It specializes the notion of modification into production. The decision as to whether or not an object is
        regarded as new is context sensitive. Normally, items are considered “new” if there is no obvious overall
        similarity between them and the consumed items and material used in their production. In other cases, an item
        is considered “new” because it becomes relevant to documentation by a modification. For example, the
        scribbling of a name on a potsherd may make it a voting token. The original potsherd may not be worth
        documenting, in contrast to the inscribed one;

        This entity can be collective: the printing of a thousand books, for example, would normally be considered
        a single event;

        An event should also be documented using an instance of E81 Transformation if it results in the destruction
        of one or more objects and the simultaneous production of others using parts or material from the originals.
        In this case, the new items have separate identities and matter is preserved, but identity is not;

    Examples:
        - the construction of the SS Great Britain (Gregor, 1971)
        - the first casting of the Little Mermaid from the harbour of Copenhagen (Dewey, 2003)
        - Rembrandt’s creating of the seventh state of his etching “Woman sitting half dressed beside a stove”, 1658,
          identified by Bartsch Number 197 (E12,E65,E81) (Hind, 1923)
    In First Order Logic:
        E12(x) ⊃ E11(x)
        E12(x) ⊃ E63(x)
    Properties:
        P108 has produced (was produced by): E24 Physical Human-Made Thing
        P186 produced thing of product type (is produced by): E99 Product Type

    """


# ******************************************************************************************************************* #


class E13AttributeAssignment(E7Activity):
    """'E13 Attribute Assignment' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E13

    SubClass Of:
        E7 Activity
    SuperClass Of:
        E14 Condition Assessment
        E15 Identifier Assignment
        E16 Measurement
        E17 Type Assignment
    Scope Note:
        This class comprises the actions of making assertions about one property of an object or any single relation
        between two items or concepts. The type of the property asserted to hold between two items or concepts can be
        described by the property P177 assigned property type: E55 Type;

        For example, the class describes the actions of people making propositions and statements during certain
        scientific/scholarly procedures, e.g. the person and date when a condition statement was made, an identifier
        was assigned, the museum object was measured, etc. Which kinds of such assignments and statements need to be
        documented explicitly in structures of a schema rather than free text, depends on whether this information
        should be accessible by structured queries;

        This class allows for the documentation of how the respective assignment came about, and whose opinion it was.
        Note that all instances of properties described in a knowledge base are the opinion of someone. Per default,
        they are the opinion of the team maintaining the knowledge base. This fact must not individually be registered
        for all instances of properties provided by the maintaining team, because it would result in an endless
        recursion of whose opinion was the description of an opinion. Therefore, the use of instances of
        E13 Attribute Assignment marks the fact, that the maintaining team is in general neutral to the validity of
        the respective assertion, but registers someone else’s opinion and how it came about;

        All properties assigned in such an action can also be seen as directly relating the respective pair of items
        or concepts. Multiple use of instances of E13 Attribute Assignment may possibly lead to a collection of
        contradictory values;

        All cases of properties in this model that are also described indirectly through a subclass of
        E13 Attribute Assignment are characterised as "short cuts" of a path via this subclass. This redundant
        modelling of two alternative views is preferred because many implementations may have good reasons to model
        either the action of assertion or the short cut, and the relation between both alternatives can be captured
        by simple rules;

    Examples:
        - the assessment of the current ownership of Martin Doerr’s silver cup in February 1997
    In First Order Logic:
        E13(x) ⊃ E7(x)
    Properties:
        P140 assigned attribute to (was attributed by): E1 CRM Entity
        P141 assigned (was assigned by): E1 CRM Entity
        P177 assigned property type: E55 Type

    """


# ******************************************************************************************************************* #


class E14ConditionAssessment(E13AttributeAssignment):
    """'E14 Condition Assessment' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E14

    SubClass Of:
        E13 Attribute Assignment
    SuperClass Of:
        -
    Scope Note:
        This class describes the act of assessing the state of preservation of an object during a particular period;

        The condition assessment may be carried out by inspection, measurement or through historical research. This
        class is used to document circumstances of the respective assessment that may be relevant to interpret its
        quality at a later stage, or to continue research on related documents;

    Examples:
        - last year’s inspection of humidity damage to the frescos in the St. George chapel in our village
    In First Order Logic:
        E14(x) ⊃ E13(x)
    Properties:
        P34 concerned (was assessed by): E18 Physical Thing
        P35 has identified (was identified by): E3 Condition State

    """


# ******************************************************************************************************************* #


class E15IdentifierAssignment(E13AttributeAssignment):
    """'E15 Identifier Assignment' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E15

    SubClass Of:
        E13 Attribute Assignment
    SuperClass Of:
        -
    Scope Note:
        This class comprises activities that result in the allocation of an identifier to an instance of
        E1 CRM Entity. Instances of E15 Identifier Assignment may include the creation of the identifier from
        multiple constituents, which themselves may be instances of E41 Appellation. The syntax and kinds of
        constituents to be used may be declared in a rule constituting an instance of E29 Design or Procedure;

    Examples:
        - of such identifiers include Find Numbers, Inventory Numbers, uniform titles in the sense of librarianship
          and Digital Object Identifiers (DOI). Documenting the act of identifier assignment and deassignment is
          especially useful when objects change custody or the identification system of an organization is changed. In
          order to keep track of the identity of things in such cases, it is important to document by whom, when and
          for what purpose an identifier is assigned to an item;
        - The fact that an identifier is a preferred one for an organisation can be expressed by using the property
          E1 CRM Entity. P48 has preferred identifier (is preferred identifier of): E42 Identifier. It can better
          be expressed in a context independent form by assigning a suitable E55 Type, such as “preferred identifier
          assignment”, to the respective instance of E15 Identifier Assignment via the P2 has type property;
        - Replacement of the inventory number TA959a by GE34604 for a 17th century lament cloth at the
          Museum Benaki, Athens
        - Assigning the author-uniform title heading “Goethe, Johann Wolfgang von, 1749-1832. Faust. 1. Theil.” for
          the respective work
        - On June 1, 2001 assigning the personal name heading “Guillaume, de Machaut, ca. 1300-1377”
          to Guillaume de Machaut
    In First Order Logic:
        E15(x) ⊃ E13(x)
    Properties:
        P37 assigned (was assigned by): E42 Identifier
        P38 deassigned (was deassigned by): E42 Identifier
        P142 used constituent (was used in): E90 Symbolic Object

    """


# ******************************************************************************************************************* #


class E16Measurement(E13AttributeAssignment):
    """'E16 Measurement' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E16

    SubClass Of:
        E13 Attribute Assignment
    SuperClass Of:
        -
    Scope Note:
        This class comprises actions measuring quantitative physical properties and other values that can be
        determined by a systematic, objective procedure of direct observation of particular states of physical
        reality. Properties of instances of E90 Symbolic Object may be measured by observing some of their
        representative carriers which may or may not be named explicitly. In the case that the carrier can be named,
        the property P16 used specific object (was used for): should be used to indicate the instance(s) of
        E18 Physical Thing that was used as the empirical basis for the measurement activity;

    Examples:
        - include measuring the nominal monetary value of a collection of coins or the running time of a movie on a
          specific video cassette.
        - The E16 Measurement may use simple counting or tools, such as yardsticks or radiation detection devices. The
          interest is in the method and care applied, so that the reliability of the result may be judged at a later
          stage, or research continued on the associated documents. The date of the event is important for dimensions,
          which may change value over time, such as the length of an object subject to shrinkage. Methods and devices
          employed should be associated with instances of E16 Measurement by properties such as P33 used specific
          technique: E29 Design or Procedure, P125 used object of type: E55 Type, P16 used specific object (was used
          for): E70 Thing, whereas basic techniques such as "carbon 14 dating" should be encoded using
          P2 has type (is type of): E55 Type. Details of methods and devices reused or reusable in other instances of
          E16 Measurement should be documented for these entities rather than the measurements themselves, whereas
          details of particular execution may be documented by free text or by instantiating adequate sub-activities,
          if the detail may be of interest for an overarching query.
        - Regardless whether a measurement is made by an instrument or by human senses, it represents the initial
          transition from physical reality to information without any other documented information object in between
          within the reasoning chain that would represent the result of the interaction of the observer or device with
          reality. Therefore, inferring properties of depicted items using image material, such as satellite images,
          is not regarded as an instance of E16 Measurement, but as a subsequent instance of E13 Attribute Assignment.
          Rather, only the production of the images, understood as arrays of radiation intensities, is regarded as
          an instance of E16 Measurement. The same reasoning holds for other sensor data;
        - measurement of height of silver cup 232 on the 31st August 1997
        - the carbon 14 dating of the “Schoeninger Speer II” in 1996 [an about 400.000 years old Palaeolithic complete
          wooden spear found in Schoeningen, Niedersachsen, Germany in 1995] (Kouwenhoven, 1997)
        - The pixel size of the jpeg version of Titian’s painting Bacchus and Ariadne from 1520–3, as freely
          downloadable from the National Gallery in London’s web page
          <https://www.nationalgallery.org.uk/paintings/titian-bacchus-and-ariadne> is 581600 pixels.
        - The scope note of E21 Person in the Definition of the CIDOC Conceptual Reference Model Version 5.0.4 as
          downloaded from <http://www.cidoc-crm.org/sites/default/files/cidoc_crm_version_5.0.4.pdf> consists
          of 77 wordsl
    In First Order Logic:
        E16(x) ⊃ E13(x)
    Properties:
        P39 measured (was measured by): E1 CRM Entity
        P40 observed dimension (was observed in): E54 Dimension

    """


# ******************************************************************************************************************* #


class E17TypeAssignment(E13AttributeAssignment):
    """'E17 Type Assignment' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E17

    SubClass Of:
        E13 Attribute Assignment
    SuperClass Of:
        -
    Scope Note:
        This class comprises the actions of classifying items of whatever kind. Such items include objects, specimens,
        people, actions and concepts;

        This class allows for the documentation of the context of classification acts in cases where the value of the
        classification depends on the personal opinion of the classifier, and the date that the classification was
        made. This class also encompasses the notion of "determination," i.e. the systematic and molecular
        identification of a specimen in biology;

    Examples:
        - the first classification of object GE34604 as Lament Cloth, October 2nd
        - the determination of a cactus in Martin Doerr’s garden as ‘Cereus hildmannianus K.Schumann’, July 2003
    In First Order Logic:
        E17(x) ⊃ E13(x)
    Properties:
        P41 classified (was classified by): E1 CRM Entity
        P42 assigned (was assigned by): E55 Type

    """
