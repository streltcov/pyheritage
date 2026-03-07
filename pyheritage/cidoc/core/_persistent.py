# -*- coding: utf-8 -*-

"""Persistent items CRM entities;

Module implements:
    - E18 Physical Thing
    - E19 Physical Object
    - E20 Biological Object
    - E22 Human-Made Object
    - E24 Physical Human Made Object
    - E25 Human-Made Feature
    - E26 Physical Feature
    - E27 Site
    - E70 Thing
    - E71 Human-Made Thing
    - E72 Legal Object
    - E77 Persistent Item
    - E78 Curated Holding

"""


from pyheritage.cidoc.core._crm_base import E1CRMEntity
from pyheritage.cidoc.core.base import entity_register


__all__ = ('E18PhysicalThing', 'E19PhysicalObject', 'E20BiologicalObject', 'E22HumanMadeObject',
           'E24PhysicalHumanMadeObject', 'E25HumanMadeFeature', 'E26PhysicalFeature', 'E27Site', 'E70Thing',
           'E71HumanMadeThing', 'E72LegalObject', 'E77PersistentItem', 'E78CuratedHolding', )


@entity_register(label='E77 Persistent Item')
class E77PersistentItem(E1CRMEntity):
    """'E77 Persistent Item' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E77

    SubClass Of:
        E1 CRM Entity
    SuperClass Of:
        E39 Actor
        E70 Thing
    Scope Note:
        This class comprises items that have persistent characteristics of structural nature substantially related
        to their identity and their integrity, sometimes known as “endurants” in philosophy. Persistent Items may be
        physical entities, such as people, animals or things, conceptual entities such as ideas, concepts, products
        of the imagination or even names;

        Instances of E77 Persistent Item may be present or be part of interactions in different periods or events.
        They can repeatedly be recognized at disparate occasions during their existence by characteristics of
        structural nature. The respective characteristics need not be exactly the same during all the existence of
        an instance of E77 Persistent Item. Often, they undergo gradual change, still bearing some similarities with
        that of previous times, or dissappear completely and new emerge. For instance, a person, from the time of
        being born on, will gradually change all its features and acquire new ones, such as a scar. Even the DNA in
        different body cells will develop defects and mutations. Nevertheless, relevant characteristics use to be
        sufficiently similar to recognize the instance for some substantial period of time;

        The more specific criteria that determine the identity of instances of subclasses of E77 Persistent Item may
        vary considerably and are described of referred to in the respective scope notes. The decision about which
        exact criteria to use depends on whether the observable behaviour of the respective part of reality such
        confined conforms to the reasoning the user is interested in. For example, a building can be regarded as
        no longer existing if it is dismantled and the materials reused in a different configuration. On the other
        hand, human beings go through radical and profound changes during their life-span, affecting both material
        composition and form, yet preserve their identity by other criteria, such as being bodily separated from other
        persons. Similarly, inanimate objects may be subject to exchange of parts and matter. On the opposite, the
        identity of a (version of a) text of a scientific publication is given by the exact arrangement of its
        relevant symbols;

        The main classes of objects that fall outside the scope of the E77 Persistent Item class are temporal objects
        such as periods, events and acts, and descriptive properties;

        An instance of E77 Persistent Item does not require actual knowledge of the identifying features of the
        instance being currently known. There may be cases, where the actual identifying features of an instance of
        E77 Persistent Item are not decidable at a particular state of knowledge;

    Examples:
        - Leonard da Vinci (Strano, 1953)
        - Stonehenge (Richards, 2005)
        - the hole in the ozone layer (Hufford and Horwitz, 2005)
        - the First Law of Thermodynamics (Craig and Gislason, 2002)
        - the Bermuda Triangle (Dolan, 2005)
    In First Order Logic:
        E77(x) ⊃ E1(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E70 Thing')
class E70Thing(E77PersistentItem):
    """'E70 Thing' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E70

    SubClass Of:
        E77 Persistent Item
    SuperClass Of:
        E71 Human-Made Thing
        E72 Legal Object
    Scope Note:
        This general class comprises discrete, identifiable, instances of E77 Persistent Item that are documented as
        single units, that either consist of matter or depend on being carried by matter and are characterized by
        relative stability;

        They may be intellectual products or physical things. They may for instance have a solid physical form, an
        electronic encoding, or they may be a logical concept or structure;

    Examples:
        - my photograph collection (E78)
        - the bottle of milk in my refrigerator (E22)
        - the Riss A1 plan of the Straßburger Münster (French: Cathédrale Notre-Dame de Strasbourg) (E29)
          (Liess, R., 1985)
        - the thing on the top of Otto Hahn’s desk (E19)
        - the form of the no-smoking sign (E36)
        - the cave of Dirou, Mani, Greece (E27) (Psimenos. 2005)
    In First Order Logic:
        E70(x) ⊃ E77(x)
    Properties:
        P43 has dimension (is dimension of): E54 Dimension
        P101 had as general use (was use of): E55 Type
        P130 shows features of (features are also found on): E70 Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='E71 Human-Made Thing')
class E71HumanMadeThing(E70Thing):
    """'E71 Human-Made Thing' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E71

    SubClass Of:
        E70 Thing
    SuperClass Of:
        E24 Physical Human-Made Thing
        E28 Conceptual Object
    Scope Note:
        This class comprises discrete, identifiable human-made items that are documented as single units;

        These items are either intellectual products or human-made physical things, and are characterized by relative
        stability. They may for instance have a solid physical form, an electronic encoding, or they may be logical
        concepts or structures;

    Examples:
        - Beethoven’s 5th Symphony (E73) (Lockwood, 2015)
        - Michelangelo’s David (Paoletti, 2015)
        - Einstein’s Theory of General Relativity (E73) (Hartle, 2003)
        - the taxon ‘Fringilla coelebs Linnaeus,1758’ (E55) (Sinkevicius and Narusevicius, 2002)
    In First Order Logic:
        E71(x) ⊃ E70(x)
    Properties:
        P102 has title (is title of): E35 Title
        P103 was intended for (was intention of): E55 Type

    """


# ******************************************************************************************************************* #


@entity_register(label='E72 Legal Object')
class E72LegalObject(E70Thing):
    """'E72 Legal Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E72

    SubClass Of:
        E70 Thing
    SuperClass Of:
        E18 Physical Thing
        E90 Symbolic Object
    Scope Note:
        This class comprises those material or immaterial items to which instances of E30 Right, such as the right of
        ownership or use, can be applied;

        This is true for all instances of E18 Physical Thing. In the case of instances of E28 Conceptual Object,
        however, the identity of an instance of E28 Conceptual Object or the method of its use may be too ambiguous to
        reliably establish instances of E30 Right, as in the case of taxa and inspirations. Ownership of corporations
        is currently regarded as out of scope of the CIDOC CRM;

    Examples:
        - the Cullinan diamond (E19) (Scarratt and Shor, 2006)
        - definition of the CIDOC Conceptual Reference Model Version 5.0.4 (E73) (ISO 21127: 2004)
    In First Order Logic:
        E72(x) ⊃ E70(x)
    Properties:
        P104 is subject to (applies to): E30 Right
        P105 right held by (has right on): E39 Actor

    """


# ******************************************************************************************************************* #


@entity_register(label='E18 Physical Thing')
class E18PhysicalThing(E72LegalObject):
    """'E18 Physical Thing' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E18

    SubClass Of:
        E72 Legal Object
    SuperClass Of:
        E19 Physical Object
        E24 Physical Human-Made Thing
        E26 Physical Feature
    Scope Note:
        This class comprises all persistent physical items with a relatively stable form, human-made or natural;

        Depending on the existence of natural boundaries of such things, the CIDOC CRM distinguishes the instances of
        E19 Physical Object from instances of E26 Physical Feature, such as holes, rivers, pieces of land etc. Most
        instances of E19 Physical Object can be moved (if not too heavy), whereas features are integral to the
        surrounding matter;

        An instance of E18 Physical Thing occupies not only a particular geometric space at any instant of its
        existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies
        a real, that is phenomenal, volume in spacetime. We include in the occupied space the space filled by the
        matter of the physical thing and all its inner spaces, such as the interior of a box. For the purpose of more
        detailed descriptions of the presence of an instance of E18 Physical Thing in space and time it can be
        associated with its specific instance of E92 Spacetime Volume by the property P196 defines (is defined by);

        The CIDOC CRM is generally not concerned with amounts of matter in fluid or gaseous states, as long as they
        are not confined in an identifiable way for an identifiable minimal time-span;

    Examples:
        - the Cullinan Diamond (E19) (Scarratt and Shor, 2006)
        - the cave “Ideon Andron” in Crete (E26) (Smith, 1844-49)
        - the Mona Lisa (E22) (Mohem, 2006)
    In First Order Logic:
        E18(x) ⊃ E72(x)
    Properties:
        P44 has condition (is condition of): E3 Condition State
        P45 consists of (is incorporated in): E57 Material
        P46 is composed of (forms part of): E18 Physical Thing
        P49 has former or current keeper (is former or current keeper of): E39 Actor
        P50 has current keeper (is current keeper of): E39 Actor
        P51 has former or current owner (is former or current owner of): E39 Actor
        P52 has current owner (is current owner of): E39 Actor
        P53 has former or current location (is former or current location of): E53 Place
        P59 has section (is located on or within): E53 Place
        P128 carries (is carried by): E90 Symbolic Object
        P156 occupies (is occupied by): E53 Place
        P196 defines (is defined by): E92 Spacetime Volume
        Pxxx holds or supports: E18 Physical Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='E19 Physical Object')
class E19PhysicalObject(E18PhysicalThing):
    """'E19 Physical Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E19

    SubClass Of:
        E18 Physical Thing
    SuperClass Of:
        E20 Biological Object
        E22 Human-Made Object
    Scope Note:
        This class comprises items of a material nature that are units for documentation and have physical boundaries
        that separate them completely in an objective way from other objects;

        The class also includes all aggregates of objects made for functional purposes of whatever kind, independent
        of physical coherence, such as a set of chessmen. Typically, instances of E19 Physical Object can be moved
        (if not too heavy);

        In some contexts, such objects, except for aggregates, are also called “bona fide objects” (Smith & Varzi,
        2000, pp.401-420), i.e. naturally defined objects;

        The decision as to what is documented as a complete item, rather than by its parts or components, may be
        a purely administrative decision or may be a result of the order in which the item was acquired;

    Examples:
        - John SmithAphrodite of Milos (Kousser, 2005)
        - the Palace of Knossos (Evans, 1921-36)
        - the Cullinan Diamond (Scarratt and Shor, 2006)
        - Apollo 13 at the time of launch (Lovell and Kluger, 1994)
    In First Order Logic:
        E19(x) ⊃ E18(x)
    Properties:
        P54 has current permanent location (is current permanent location of): E53 Place
        P55 has current location (currently holds): E53 Place
        P56 bears feature (is found on): E26 Physical Feature
        P57 has number of parts: E60 Number

    """


# ******************************************************************************************************************* #


@entity_register(label='E20 Biological Object')
class E20BiologicalObject(E19PhysicalObject):
    """'E20 Biological Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E20

    SubClass Of:
        E19 Physical Object
    SuperClass Of:
        E21 Person
    Scope Note:
        This class comprises individual items of a material nature, which live, have lived or are natural products of
        or from living organisms;

        Artificial objects that incorporate biological elements, such as Victorian butterfly frames, can be documented
        as both instances of E20 Biological Object and E22 Human-Made Object;

    Examples:
        me
        Tut-Ankh-Amun (Edwards, 1979)
        Boukephalas [Horse of Alexander the Great](Lamb, 2005)
        petrified dinosaur excrement PA1906-344
    In First Order Logic:
        E20(x) ⊃ E19(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E24 Physical Human-Made Object')
class E24PhysicalHumanMadeObject(E18PhysicalThing, E71HumanMadeThing):
    """'E24 Physical Human-Made Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E24

    SubClass Of:
        E18 Physical Thing
        E71 Human-Made Thing
    SuperClass Of:
        E22 Human-Made Object
        E25 Human-Made Feature
        E78 Curated Holding
    Scope Note:
        This class comprises all persistent physical items of any size that are purposely created by human activity.
        This class comprises, besides others, Human-Made objects, such as a swords, and Human-Made features, such as
        rock art. For example, a “cup and ring” carving on bedrock is regarded as instance of
        E24 Physical Human-Made Thing;

        Instances of Human-Made thing may be the result of modifying pre-existing physical things, preserving larger
        parts or most of the original matter and structure, which poses the question if they are new or even
        Human-Made, the respective interventions of production made on such original material should be obvious and
        sufficient to regard that the product has a new, distinct identity and intended function and is human-made.
        Substantial continuity of the previous matter and structure in the new product can be documented by describing
        the production process also as instance of E81 Transformation;

        Whereas interventions of conservation and repair are not regarded to produce a new Human-Made thing, the
        results of preparation of natural history specimen that substantially change their natural or original state
        should be regarded as physical Human-Made things, including the uncovering of petrified biological features
        from a solid piece of stone. On the other side, scribbling a museum number on a natural object should not be
        regarded to make it Human-Made. This notwithstanding, parts, sections, segments, or features of a physical
        Human-Made thing may continue to be non-Human-Made and preserved during the production process, for example
        natural pearls used as a part of an eardrop;

    Examples:
        - the Forth Railway Bridge (E22) (The Forth Railway Bridge centenary 1890-1990 ICE Proceedings, 1990,
          Vol.88(6), pp.1079-1107.
        - the Channel Tunnel (E25) (Holliday, I., Marcou, G., and Vickerman, R. W., 1991)
        - the Historical Collection of the Museum Benaki in Athens (E78) (Georgoula, E., 2005)
        - the Rosetta Stone (E22)
        - my paperback copy of Crime & Punishment (E22) (fictitious)
        - the computer disk at ICS-FORTH that stores the canonical Definition of the CIDOC CRM v.3.2 (E22)
        - ▪ my empty DVD disk (E22) (fictitious)
    In First Order Logic:
        E24(x) ⊃ E18(x)
        E24(x) ⊃ E71(x)
    Properties:
        P62 depicts (is depicted by): E1 CRM Entity
        P65 shows visual item (is shown by): E36 Visual Item

    """


# ******************************************************************************************************************* #


@entity_register(label='E22 Human-Made Object')
class E22HumanMadeObject(E19PhysicalObject, E24PhysicalHumanMadeObject):
    """'E22 Human-Made Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E27

    SubClass Of:
        E19 Physical Object
        E24 Physical Human-Made Thing
    SuperClass Of:
        -
    Scope Note:
        This class comprises physical objects purposely created by human activity.

        No assumptions are made as to the extent of modification required to justify regarding an object as
        human-made. For example, an inscribed piece of rock or a preserved butterfly are both regarded as instances
        of E22 Human-Made Object;

    Examples:
        - Mallard (the World’s fastest steam engine) (Solomon, 2003)
        - the Portland Vase (Walker, 2004)
        - the Coliseum (Hopkins, 2005)
    In First Order Logic:
        E22(x) ⊃ E19(x)
        E22(x) ⊃ E24(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E26 Physical Feature')
class E26PhysicalFeature(E18PhysicalThing):
    """'E26 Physical Feature' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E26

    SubClass Of:
        E18 Physical Thing
    SuperClass Of:
        E25 Human-Made Feature
        E27 Site
    Scope Note:
        This class comprises identifiable features that are physically attached in an integral way to particular
        physical objects;

        Instances of E26 Physical Feature share many of the attributes of instances of E19 Physical Object. They may
        have a one-, two- or three-dimensional geometric extent, but there are no natural borders that separate them
        completely in an objective way from the carrier objects. For example, a doorway is a feature but the door
        itself, being attached by hinges, is not;

        Instances of E26 Physical Feature can be features in a narrower sense, such as scratches, holes, reliefs,
        surface colours, reflection zones in an opal crystal or a density change in a piece of wood. In the wider
        sense, they are portions of particular objects with partially imaginary borders, such as the core of the
        Earth, an area of property on the surface of the Earth, a landscape or the head of a contiguous marble statue.
        They can be measured and dated, and it is sometimes possible to state who or what is or was responsible for
        them. They cannot be separated from the carrier object, but a segment of the carrier object may be identified
        (or sometimes removed) carrying the complete feature;

        This definition coincides with the definition of "fiat objects" (Smith & Varzi, 2000, pp.401-420), with the
        exception of aggregates of “bona fide objects”;

    Examples:
        the temple in Abu Simbel before its removal, which was carved out of solid rock (Hawass, 2000)
        Albrecht Duerer's signature on his painting of Charles the Great (Strauss, 1974)
        the damage to the nose of the Great Sphinx in Giza (Temple, 2009)
        Michael Jackson’s nose prior to plastic surgery
    In First Order Logic:
        E26(x) ⊃ E18(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E25 Human-Made Feature')
class E25HumanMadeFeature(E24PhysicalHumanMadeObject, E26PhysicalFeature):
    """'E25 Human-Made Feature' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E25

    SubClass Of:
        E24 Physical Human-Made Thing
        E26 Physical Feature
    SuperClass Of:
        -
    Scope Note:
        This class comprises physical features that are purposely created by human activity, such as scratches,
        artificial caves, artificial water channels, etc. In particular, it includes the information encoding features
        on mechanical or digital carriers;

        No assumptions are made as to the extent of modification required to justify regarding a feature as
        human-made. For example, rock art or even “cup and ring” carvings on bedrock are regarded as types of
        E25 Human-Made Feature;

    Examples:
        - the Manchester Ship Canal (Famie, 1980)
        - Michael Jackson’s nose following plastic surgery
        - The laser-readable “pits” engraved June 2014 on Martin Doerr’s CD-R, copying songs of Edith Piaf’s.
        - The carved letters on the Rosetta Stone
    In First Order Logic:
        E25(x) ⊃ E24(x)
        E25(x) ⊃ E26(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E27 Site')
class E27Site(E26PhysicalFeature):
    """'E27 Site' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E27

    SubClass Of:
        E26 Physical Feature
    SuperClass Of:
        -
    Scope Note:
        This class comprises pieces of land or sea floor.

        In contrast to the purely geometric notion of E53 Place, this class describes constellations of matter on the
        surface of the Earth or other celestial body, which can be represented by photographs, paintings and maps;

        Instances of E27 Site are composed of relatively immobile material items and features in a particular
        configuration at a particular location;

    Examples:
        - the Amazon river basin (Hegen, 1966)
        - Knossos (Evans, 1921-36)
        - the Apollo 11 landing site (Siegler and Smrekar, 2014)
        - Heathrow Airport (Wicks, 2014)
        - the submerged harbour of the Minoan settlement of Gournia, Crete (Watrous, 2012)
        - the island of Crete
    In First Order Logic:
        E27(x)⊃ E26(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='E78 Curated Holding')
class E78CuratedHolding(E24PhysicalHumanMadeObject):
    """'E78 Curated Holding' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E78

    SubClass Of:
        E24 Physical Human-Made Thing
    SuperClass Of:
        -
    Scope Note:
        This class comprises aggregations of instances of E18 Physical Thing that are assembled and maintained
        (“curated” and “preserved,” in museological terminology) by one or more instances of E39 Actor over time for
        a specific purpose and audience, and according to a particular collection development plan. Typical instances
        of curated holdings are museum collections, archives, library holdings and digital libraries. A digital
        library is regarded as an instance of E18 Physical Thing because it requires keeping physical carriers of
        the electronic content;

        Items may be added or removed from an E78 Curated Holding in pursuit of this plan. This class should not be
        confused with the E39 Actor maintaining the E78 Curated Holding often referred to with the name of the
        E78 Curated Holding (e.g. “The Wallace Collection decided…”);

        Collective objects in the general sense, like a tomb full of gifts, a folder with stamps or a set of chessmen,
        should be documented as instances of E19 Physical Object, and not as instances of E78 Curated Holding. This is
        because they form wholes either because they are physically bound together or because they are kept together
        for their functionality;

    Examples:
        - the John Clayton Herbarium
        - the Wallace Collection (Ingamells, 1990)
        - Mikael Heggelund Foslie’s coralline red algae Herbarium at Museum of Natural History and Archaeology,
          Trondheim, Norway
        - The Digital Collections of the Munich DigitiZation Center (MDZ) accessible via
          https://www.digitale-sammlungen.de/ at least in January 2018.
    In First Order Logic:
        E78(x) ⊃ E24(x)
    Properties:
        P109 has current or former curator (is current or former curator of): E39 Actor

    """
