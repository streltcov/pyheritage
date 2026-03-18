# -*- coding: utf-8 -*-

"""Persistent items CRM entities;

-------------------------
Entities
-------------------------
E18 Physical Thing
E19 Physical Object
E20 Biological Object
E21 Person
E22 Human-Made Object
E24 Physical Human Made Object
E25 Human-Made Feature
E26 Physical Feature
E27 Site
E28 Conceptual Object
E29 Design or Procedure
E30 Right
E31 Document
E32 Authority Document
E33 Linguistic Object
E34 Inscription
E35 Title
E36 Visual Item
E37 Mark
E39 Actor
E41 Appellation
E42 Identifier
E55 Type
E56 Language
E57 Material
E58 Measurement Unit
E70 Thing
E71 Human-Made Thing
E72 Legal Object
E73 Information Object
E74 Group
E77 Persistent Item
E78 Curated Holding
E89 Propositional Object
E90 Symbolic Object
E97 Monetary Amount
E98 Currency
E99 Product Type

"""


from pyheritage.cidoc.core.base import entity_register
from pyheritage.cidoc.core.entities._crm_base import E1CRMEntity
from pyheritage.cidoc.core.entities._spacetime import E54Dimension
from pyheritage.cidoc.core.properties import (
    P43HasDimension,
    P44HasCondition,
    P45ConsistsOf,
    P46IsComposedOf,
    P49HasFormerOrCurrentKeeper,
    P50HasCurrentKeeper,
    P51HasCurrentOrFormerOwner,
    P52HasCurrentOwner,
    P53HasFormerOrCurrentLocation,
    P54HasCurrentPermanentLocation,
    P55HasCurrentLocation,
    P56BearsFeature,
    P57HasNumberOfParts,
    P59HasSection,
    P62Depicts,
    P65ShowsVisualItem,
    P67RefersTo,
    P68ForeseesUseOf,
    P69HasAssociationWith,
    P70Documents,
    P71Lists,
    P72HasLanguage,
    P73HasTranslation,
    P74HasCurrentOrFormerResidence,
    P75Possesses,
    P76HasContactPoint,
    P101HadAGeneralUse,
    P102HasTitle,
    P103WasIntendedFor,
    P104IsSubjectTo,
    P105RightHeldBy,
    P106IsComposedOf,
    P107HasCurrentOrFormerMember,
    P109HasCurrentOrFormerCurator,
    P127HasBroaderTerm,
    P128Carries,
    P129IsAbout,
    P130ShowsFeaturesOf,
    P138Represents,
    P139HasAlternativeForm,
    P148HasComponent,
    P150DefinesTypicalPartsOf,
    P152HasParent,
    P156Occupies,
    P165Incorporates,
    P180HasCurrency,
    P181HasAmount,
    P187HasProductionPlan,
    P188RequiresProductionTool,
    P190HasSymbolicContent,
    P196Defines,
    PxxxHoldsOrSupports,
)


__all__ = ('E18PhysicalThing', 'E19PhysicalObject', 'E20BiologicalObject', 'E21Person', 'E22HumanMadeObject',
           'E24PhysicalHumanMadeObject', 'E25HumanMadeFeature', 'E26PhysicalFeature', 'E27Site',
           'E28ConceptualObject', 'E29DesignOrProcedure', 'E30Right', 'E31Document', 'E32AuthorityDocument',
           'E33LinguisticObject', 'E34Inscription', 'E35Title', 'E36VisualItem', 'E37Mark', 'E39Actor',
           'E41Appellation', 'E42Identifier', 'E55Type', 'E56Language', 'E57Material', 'E58MeasurementUnit',
           'E70Thing', 'E71HumanMadeThing', 'E72LegalObject', 'E73InformationObject', 'E74Group', 'E77PersistentItem',
           'E78CuratedHolding', 'E89PropositionalObject', 'E90SymbolicObject', 'E97MonetaryAmount', 'E98Currency',
           'E99ProductType', )


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
class E70Thing(P43HasDimension, P101HadAGeneralUse, P130ShowsFeaturesOf, E77PersistentItem):
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
class E71HumanMadeThing(P102HasTitle, P103WasIntendedFor, E70Thing):
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
class E72LegalObject(P104IsSubjectTo, P105RightHeldBy, E70Thing):
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
class E18PhysicalThing(P44HasCondition, P45ConsistsOf, P46IsComposedOf, P49HasFormerOrCurrentKeeper,
                       P50HasCurrentKeeper, P51HasCurrentOrFormerOwner, P52HasCurrentOwner,
                       P53HasFormerOrCurrentLocation, P59HasSection, P128Carries, P156Occupies, P196Defines,
                       PxxxHoldsOrSupports, E72LegalObject):
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
class E19PhysicalObject(P54HasCurrentPermanentLocation, P55HasCurrentLocation, P56BearsFeature, P57HasNumberOfParts,
                        E18PhysicalThing):
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
class E24PhysicalHumanMadeObject(P62Depicts, P65ShowsVisualItem, E18PhysicalThing, E71HumanMadeThing):
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


class E28ConceptualObject(E71HumanMadeThing):
    """'E28 Conceptual Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E28

    SubClass Of:
        E71 Human-Made Thing
    SuperClass Of:
        E55 Type
        E89 Propositional Object
        E90 Symbolic Object
    Scope Note:
        This class comprises non-material products of our minds and other human produced data that have become objects
        of a discourse about their identity, circumstances of creation or historical implication. The production of
        such information may have been supported by the use of technical devices such as cameras or computers;

        Characteristically, instances of this class are created, invented or thought by someone, and then may be
        documented or communicated between persons. Instances of E28 Conceptual Object have the ability to exist
        on more than one particular carrier at the same time, such as paper, electronic signals, marks, audio media,
        paintings, photos, human memories, etc.;

        They cannot be destroyed. They exist as long as they can be found on at least one carrier or in at least one
        human memory. Their existence ends when the last carrier and the last memory are lost;

    Examples:
        - Beethoven’s “Ode an die Freude” (Ode to Joy) (E73) (Kershaw, 1999)
        - the definition of “ontology” in the Oxford English Dictionary (E73)
        - the knowledge about the victory at Marathon carried by the famous runner (E89)
        - [explanation note: In the following examples we illustrate the distinction between a propositional object,
          its names and its encoded forms. The Maxwell equations are a good example, because they belong to the
          fundamental laws of physics and their mathematical content yields identical, unambiguous results regardless
          formulation and encoding]
        - ‘Maxwell equations’ [preferred subject access point from LCSH] (E41)
        - http://lccn.loc.gov/sh85082387 [5], as of 19 November 2012]
        - **explanation: This is only the name for the Maxwell equations as standardized by the Library of Congress
          and NOT the equations themselves.
        - ‘Equations, Maxwell’ [variant subject access point, from the same source] (E41)
        - **explanation: This is another name for the equation standardized by the Library of Congress and not the
          equations themselves
        - Maxwell's equations (E89)
        - ** explanation: This is the propositional content of the equations proper, independent of any particular
          notation or mathematical formalism.
        - The encoding of Maxwells equations as in https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Maxwell
          [6]'s Equations.svg/500px-Maxwell'sEquations.svg.png (E73)
        - ** explanation: This is one possible symbolic encoding of the propositional content of the equations.
    In First Order Logic:
        E28(x) ⊃ E71(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E39Actor(P74HasCurrentOrFormerResidence, P75Possesses, P76HasContactPoint, E77PersistentItem):
    """'E39 Actor' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E39

    SubClass Of:
        E77 Persistent Item
    SuperClass Of:
        E21 Person
        E74 Group
    Scope Note:
        This class comprises people, either individually or in groups, who have the potential to perform intentional
        actions of kinds for which someone may be held responsible;

    Examples:
        - London and Continental Railways (E40)
        - the Governor of the Bank of England in 1975 (E21)
        - Sir Ian McKellan (E21) (Gibson, 1986)
    In First Order Logic:
        E39(x) ⊃ E77(x)
    Properties:
        P74 has current or former residence (is current or former residence of): E53 Place
        P75 possesses (is possessed by): E30 Right
        P76 has contact point (provides access to): E41 Appellation

    """


# ******************************************************************************************************************* #


class E21Person(P152HasParent, E20BiologicalObject, E39Actor):
    """'E21 Person' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E21

    SubClass Of:
        E20 Biological Object
        E39 Actor
    SuperClass Of:
        -
    Scope Note:
        This class comprises real persons who live or are assumed to have lived;

        Legendary figures that may have existed, such as Ulysses and King Arthur, fall into this class if the
        documentation refers to them as historical figures. In cases where doubt exists as to whether several persons
        are in fact identical, multiple instances can be created and linked to indicate their relationship. The CIDOC
        CRM does not propose a specific form to support reasoning about possible identity;

        In a bibliographic context, a name presented following the conventions usually employed for personal names
        will be assumed to correspond to an actual real person (an instance of E21 Person), unless evidence is
        available to indicate that this is not the case. The fact that a persona may erroneously be classified as
        an instance of E21 Person does not imply that the concept comprises personae;

    Examples:
        - Tut-Ankh-Amun (Edwards, 1979)
        - Nelson Mandela (Brown, 2006)
    In First Order Logic:
        E21(x) ⊃ E20(x)
        E21(x) ⊃ E39(x)
    Properties:
        P152 has parent (is parent of): E21 Person

    """


# ******************************************************************************************************************* #


@entity_register(label='E78 Curated Holding')
class E78CuratedHolding(P109HasCurrentOrFormerCurator, E24PhysicalHumanMadeObject):
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

# ******************************************************************************************************************* #


@entity_register(label="E90 Symbolic Object")
class E90SymbolicObject(P106IsComposedOf, P190HasSymbolicContent, E1CRMEntity):
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
class E41Appellation(P139HasAlternativeForm, E90SymbolicObject):
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


class E55Type(P127HasBroaderTerm, P150DefinesTypicalPartsOf, E28ConceptualObject):
    """'E55 Type' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E55

    SubClass Of:
        E28 Conceptual Object
    SuperClass Of:
        E56 Language
        E57 Material
        E58 Measurement Unit
        E98 Currency
        E99 Product Type
    Scope Note:
        This class comprises concepts denoted by terms from thesauri and controlled vocabularies used to characterize
        and classify instances of CIDOC CRM classes. Instances of E55 Type represent concepts in contrast to instances
        of E41 Appellation which are used to name instances of CIDOC CRM classes;

        E55 Type is the CIDOC CRM’s interface to domain specific ontologies and thesauri. These can be represented
        in the CIDOC CRM as subclasses of E55 Type, forming hierarchies of terms, i.e. instances of E55 Type linked
        via P127 has broader term (has narrower term): E55Type. Such hierarchies may be extended with additional
        properties;

    Examples:
        - weight, length, depth [types of E54]
        - portrait, sketch, animation [types of E36]
        - French, English, German [E56]
        - excellent, good, poor [types of E3]
        - Ford Model T, chop stick [types of E22]
        - cave, doline, scratch [types of E26]
        - poem, short story [types of E33]
        - wedding, earthquake, skirmish [types of E5]
    In First Order Logic:
        E55(x) ⊃ E28(x)
    Properties:
        P127 has broader term (has narrower term): E55 Type
        P150 defines typical parts of (defines typical wholes for): E55 Type

    """


# ******************************************************************************************************************* #


class E56Language(E55Type):
    """'E56 Language' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E56

    SubClass Of:
        E55 Type
    SuperClass Of:
        -
    Scope Note:
        This class is a specialization of E55 Type and comprises the natural languages in the sense of concepts;

        This type is used categorically in the model without reference to instances of it, i.e. the Model does not
        foresee the description of instances of instances of E56 Language, e.g.: “instances of Mandarin Chinese”;

        It is recommended that internationally or nationally agreed codes and terminology are used to denote instances
        of E56 Language, such as those defined in ISO 639-1:2002 and later versions;

    Examples:
        - el [Greek] (Palmer, 1980)
        - en [English] (Wilson, 1983)
        - eo [Esperanto] (Nuessel, 2000)
        - es [Spanish] (Pineda, 1993)
        - fr [French] (Rickard, 1974)
    In First Order Logic:
        E56(x) ⊃ E55(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E57Material(E55Type):
    """'E57 Material' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E57

    SubClass Of:
        E55 Type
    SuperClass Of:
        -
    Scope Note:
        This class is a specialization of E55 Type and comprises the concepts of materials;

        Instances of E57 Material may denote properties of matter before its use, during its use, and as incorporated
        in an object, such as ultramarine powder, tempera paste, reinforced concrete. Discrete pieces of raw-materials
        kept in museums, such as bricks, sheets of fabric, pieces of metal, should be modelled individually in the
        same way as other objects. Discrete used or processed pieces, such as the stones from Nefer Titi's temple,
        should be modelled as parts (cf. P46 is composed of (forms part of): E18 Physical Thing);

        This type is used categorically in the model without reference to instances of it, i.e. the Model does not
        foresee the description of instances of instances of E57 Material, e.g.: “instances of gold”;

        It is recommended that internationally or nationally agreed codes and terminology are used;

    Examples:
        - Brick (Gurcke, 1987)
        - Gold (Watson, 1990)
        - Aluminium (Norman, 1986)
        - Polycarbonate (Mhaske, 2011)
        - Resin (Barton, 1992)
    In First Order Logic:
        E57(x) ⊃ E55(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E58MeasurementUnit(E55Type):
    """'E58 Measurement Unit' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E58

    SubClass Of:
        E55 Type
    SuperClass Of:
        E98 Currency
    Scope Note:
        This class is a specialization of E55 Type and comprises the types of measurement units: feet, inches,
        centimetres, litres, lumens, etc.;

        This type is used categorically in the model without reference to instances of it, i.e. the Model does not
        foresee the description of instances of instances of E58 Measurement Unit, e.g.: “instances of cm”;

        Système International (SI) units or internationally recognized non-SI terms should be used whenever possible,
        such as those defined by ISO80000:2009. Archaic Measurement Units used in historical records should
        be preserved;

    Examples:
        - cm [centimetre]
        - km [kilometre]
        - m [meter]
        - m/s [meters per second] (Hau, 1999)
        - A [Ampere]
        - GRD [Greek Drachme] (Daniel, 2014) (E98)
        - C [degrees centigrade] (Beckman, 1998)
    In First Order Logic:
        E58(x) ⊃ E55(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E89PropositionalObject(P67RefersTo, P129IsAbout, P148HasComponent, E28ConceptualObject):
    """'E89 Propositional Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E89

    SubClass Of:
        E28 Conceptual Object
    SuperClass Of:
        E30 Right
        E73 Information Object
    Scope Note:
        This class comprises immaterial items, including but not limited to stories, plots, procedural prescriptions,
        algorithms, laws of physics or images that are, or represent in some sense, sets of propositions about real or
        imaginary things and that are documented as single units or serve as topic of discourse;

        This class also comprises items that are “about” something in the sense of a subject. In the wider sense, this
        class includes expressions of psychological value such as non-figural art and musical themes. However,
        conceptual items such as types and classes are not instances of E89 Propositional Object. This should not
        be confused with the definition of a type, which is indeed an instance of E89 Propositional Object;

    Examples:
        - Maxwell’s Equations (Huray, 2010)
        - The ideational contents of Aristotle’s book entitled ‘Metaphysics’ as rendered in the Greek texts
          translated in … Oxford edition…
        - The underlying prototype of any “no-smoking” sign (E36)
        - The common ideas of the plots of the movie "The Seven Samurai" by Akira Kurosawa and the movie
          “The Magnificent Seven” by John Sturges
        - The image content of the photo of the Allied Leaders at Yalta published by UPI, 1945 (E36)
        - The character "Little Red Riding Hood" variants of which appear amongst others in Grimm brothers’
          ‘Rotkäppchen’, other oral fairy tales and the film 'Hoodwinked'
        - The place "Havnor" as invented by Ursula K. Le Guin for her ‘Earthsea’ book series, the related maps and
          appearing in derivative works based on these novels
    In First Order Logic:
        E89(x) ⊃ E28(x)
    Properties:
        P67 refers to (is referred to by): E1 CRM Entity
        P129 is about (is subject of): E1 CRM Entity
        P148 has component (is component of): E89 Propositional Object

    """


# ******************************************************************************************************************* #


class E73InformationObject(P165Incorporates, E89PropositionalObject, E90SymbolicObject):
    """'E73 Information Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E73

    SubClass Of:
        E89 Propositional Object
        E90 Symbolic Object
    SuperClass Of:
        E29 Design or Procedure
        E31 Document
        E33 Linguistic Object
        E36 Visual Item
    Scope Note:
        This class comprises identifiable immaterial items, such as a poems, jokes, data sets, images, texts,
        multimedia objects, procedural prescriptions, computer program code, algorithm or mathematical formulae,
        that have an objectively recognizable structure and are documented as single units. The encoding structure
        known as a "named graph" also falls under this class, so that each "named graph" is an instance of
        E73 Information Object;

        An instance of E73 Information Object does not depend on a specific physical carrier, which can include human
        memory, and it can exist on one or more carriers simultaneously;

        Instances of E73 Information Object of a linguistic nature should be declared as instances of the
        E33 Linguistic Object subclass. Instances of E73 Information Object of a documentary nature should be declared
        as instances of the E31 Document subclass. Conceptual items such as types and classes are not instances of
        E73 Information Object, nor are ideas without a reproducible expression;

    Examples:
        - image BM000038850.JPG from the Clayton Herbarium in London (E31)
        - E. A. Poe's "The Raven" (Poe, 1869)
        - the movie "The Seven Samurai" by Akira Kurosawa (Mellen, 2002)
        - the Maxwell Equations (Huray, 2010)
        - The Getty AAT as published as Linked Open Data, accessed 1/10/2014
    In First Order Logic:
        E73(x) ⊃ E89(x)
        E73(x) ⊃ E90(x)
    Properties:
        P165 incorporates (is incorporated in): E90 Symbolic Object

    """


# ******************************************************************************************************************* #


class E74Group(P107HasCurrentOrFormerMember, E39Actor):
    """'E74 Group' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E73

    SubClass Of:
        E39 Actor
    SuperClass Of:
        -
    Scope Note:
        This class comprises any gatherings or organizations of human individuals or groups that act collectively or
        in a similar way due to any form of unifying relationship. In the wider sense this class also comprises
        official positions which used to be regarded in certain contexts as one actor, independent of the current
        holder of the office, such as the president of a country. In such cases, it may happen that the group never
        had more than one member. A joint pseudonym (i.e., a name that seems indicative of an individual but that is
        actually used as a persona by two or more people) is a particular case of E74 Group;

        A gathering of people becomes an instance of E74 Group when it exhibits organizational characteristics
        usually typified by a set of ideas or beliefs held in common, or actions performed together. These might be
        communication, creating some common artifact, a common purpose such as study, worship, business, sports,
        etc. Nationality can be modelled as membership in an instance of E74 Group (cf. HumanML markup). Married
        couples and other concepts of family are regarded as particular examples of E74 Group;

    Examples:
        - the impressionists (Wilson, 1983)
        - the Navajo (Correll, 1972)
        - the Greeks (Williams, 1993)
        - the peace protestors in New York City on February 15 2003
        - Exxon-Mobil (‘Exxon Mobil Corp’, Mergent's dividend achievers, vol. 3, no. 3, 2006, pp. 97-97)
        - King Solomon and his wives (Thieberger, 1947)
        - The President of the Swiss Confederation
        - Nicolas Bourbaki (Aczel, 2007)
        - Betty Crocker (Crocker, 2012)
        - Ellery Queen (Wheat, 2005)
        - Greenpeace
        - Paveprime Ltd
        - the National Museum of Denmark
    In First Order Logic:
        E74(x) ⊃ E39(x)
    Properties:
        P107 has current or former member (is current or former member of): E39 Actor

    """


# ******************************************************************************************************************* #


class E29DesignOrProcedure(P68ForeseesUseOf, P69HasAssociationWith, E73InformationObject):
    """'E29 Design or Procedure' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E29

    SubClass Of:
        E73 Information Object
    SuperClass Of:
        -
    Scope Note:
        This class comprises documented plans for the execution of actions in order to achieve a result of a specific
        quality, form or contents. In particular, it comprises plans for deliberate human activities that may result
        in new instances of E71 Human-Made Thing or for shaping or guiding the execution of an instance of
        E7 Activity;

        Instances of E29 Design or Procedure can be structured in parts and sequences or depend on others;
        This is modelled using P69 has association with (is associated with): E29 Design or Procedure

        Designs or procedures can be seen as one of the following:
        A schema for the activities it describes
        A schema of the products that result from their application;
        An independent intellectual product that may have never been applied, such as Leonardo da Vinci’s famous plans
        for flying machines;
        Because designs or procedures may never be applied or only partially executed, the CIDOC CRM models a loose
        relationship between the plan and the respective product;

    Examples:
        - the ISO standardisation procedure
        - the musical notation for Beethoven’s “Ode to Joy”
        - the architectural drawings for the Kölner Dom in Cologne, Germany
        - The drawing on the folio 860 of the Codex Atlanticus from Leonardo da Vinci, 1486-1490, kept in the
          Biblioteca Ambrosiana in Milan
    In First Order Logic:
        E29(x) ⊃ E73(x)
    Properties:
        P68 foresees use of (use foreseen by): E57 Material
        P69 has association with (is associated with): E29 Design or Procedure

    """


# ******************************************************************************************************************* #


class E30Right(E89PropositionalObject):
    """'E30 Right' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E30

    SubClass Of:
        E89 Propositional Object
    SuperClass Of:
        -
    Scope Note:
        This class comprises legal privileges concerning material and immaterial things or their derivatives;
        These include reproduction and property rights;

    Examples:
        - copyright held by ISO on ISO/CD 21127
        - ownership of the “Mona Lisa” by the Louvre
    In First Order Logic:
        E30(x) ⊃ E89(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E31Document(P70Documents, E73InformationObject):
    """'E31 Document' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E31

    SubClass Of:
        E73 Information Object
    SuperClass Of:
        E32 Authority Document
    Scope Note:
        This class comprises identifiable immaterial items that make propositions about reality;

        These propositions may be expressed in text, graphics, images, audiograms, videograms or by other similar
        means. Documentation databases are regarded as instances of E31 Document. This class should not be confused
        with the concept “document” in Information Technology, which is compatible with E73 Information Object;

    Examples:
        - the Encyclopaedia Britannica (E32) (Kogan, 1958)
        - The image content of the photo of the Allied Leaders at Yalta published by UPI, 1945 (E36 )
        - the Doomsday Book
    In First Order Logic:
        E31(x) ⊃ E73(x)
    Properties:
        P70 documents (is documented in): E1 CRM Entity

    """


# ******************************************************************************************************************* #


class E32AuthorityDocument(P71Lists, E31Document):
    """'E32 Authority Document' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E32

    SubClass Of:
        E31 Document
    SuperClass Of:
        -
    Scope Note:
        This class comprises encyclopaedia, thesauri, authority lists and other documents that define terminology or
        conceptual systems for consistent use;

    Examples:
        - Webster's Dictionary
        - Getty Art and Architecture Thesaurus (Getty Trust, 1990)
        - the CIDOC Conceptual Reference Model (Gergatsoulis, M. et al., 2010)
    In First Order Logic:
        E32(x) ⊃ E31(x)
    Properties:
        P71 lists (is listed in): E1 CRM Entity

    """


# ******************************************************************************************************************* #


class E33LinguisticObject(P72HasLanguage, P73HasTranslation, E73InformationObject):
    """'E33 Linguistic Object' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E33

    SubClass Of:
        E73 Information Object
    SuperClass Of:
        E34 Inscription
        E35 Title
    Scope Note:
        This class comprises identifiable expressions in natural language or languages.

        Instances of E33 Linguistic Object can be expressed in many ways: e.g. as written texts, recorded speech or
        sign language. However, the CIDOC CRM treats instances of E33 Linguistic Object independently from the medium
        or method by which they are expressed. Expressions in formal languages, such as computer code or mathematical
        formulae, are not treated as instances of E33 Linguistic Object by the CIDOC CRM. These should be modelled as
        instances of E73 Information Object;

        The text (in a wider sense) of an instance of E33 Linguistic Object can be documented in a note by
        P3 has note: E62 String

    Examples:
        - the text of the Ellesmere Chaucer manuscript (Hilmo, 2004)
        - the lyrics of the song "Blue Suede Shoes" (Cooper, 2008)
        - the text of the Jabberwocky by Lewis Carroll (Carroll, 1981)
        - the text of "Doktoro Jekyll kaj Sinjoro Hyde" (an Esperanto translation of Dr Jekyll and Mr Hyde)
          (Stevenson, 1909)
    In First Order Logic:
        E33(x) ⊃ E73(x)
    Properties:
        P72 has language (is language of): E56 Language
        P73 has translation (is translation of): E33 Linguistic Object

    """


# ******************************************************************************************************************* #


class E35Title(E33LinguisticObject, E41Appellation):
    """'E35 Title' CRM entity;

    SubClass Of:
        E33 Linguistic Object
        E41 Appellation
    SuperClass Of:
        -
    Scope Note:
        This class comprises textual strings that within a cultural context can be clearly identified as titles due to
        their form. Being a subclass of E41 Appellation, E35 Title can only be used when such a string is actually
        used as a title of a work, such as a text, an artwork, or a piece of music;

        Titles are proper noun phrases or verbal phrases, and should not be confused with generic object names such as
        “chair”, “painting” or “book” (the latter are common nouns that stand for instances of E55 Type). Titles may
         be assigned by the creator of the work itself, or by a social group;

        This class also comprises the translations of titles that are used as surrogates for the original titles in
        different social contexts;

    Examples:
        - “The Merchant of Venice” (McCullough, 2005)
        - “Mona Lisa” (Mohen, 2006)
        - “La Pie or The Magpie” (Bortolatto, 1981)
        - “Lucy in the Sky with Diamonds” (Lennon, 1967)
    In First Order Logic:
        E35(x) ⊃ E33(x)
        E35(x) ⊃ E41(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E36VisualItem(P138Represents, E73InformationObject):
    """'E36 Visual Item' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E36

    SubClass Of:
        E73 Information Object
    SuperClass Of:
        E37 Mark
    Scope Note:
        This class comprises the intellectual or conceptual aspects of recognisable marks and images;

        This class does not intend to describe the idiosyncratic characteristics of an individual physical embodiment
        of a visual item, but the underlying prototype. For example, a mark such as the ICOM logo is generally
        considered to be the same logo when used on any number of publications. The size, orientation and colour may
        change, but the logo remains uniquely identifiable. The same is true of images that are reproduced many times;
        This means that visual items are independent of their physical support;

        The class E36 Visual Item provides a means of identifying and linking together instances of
        E24 Physical Human-Made Thing that carry the same visual symbols, marks or images etc. The property
        P62 depicts (is depicted by) between E24 Physical Human-Made Thing and depicted subjects (E1 CRM Entity) is
        a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65 shows visual item
        (is shown by), E36 Visual Item, P138 represents (has representation) to E1CRM Entity, which in addition
        captures the optical features of the depiction;

    Examples:
        - the visual appearance of Monet’s “La Pie”
        - the Coca-Cola logo (E34)
        - the Chi-Rho (E37)
        - the communist red star (E37)
    In First Order Logic:
        E36(x) ⊃ E73(x)
    Properties:
        P138 represents (has representation): E1 CRM Entity

    """


# ******************************************************************************************************************* #


class E37Mark(E36VisualItem):
    """'E37 Mark' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E37

    SubClass Of:
        E36 Visual Item
    SuperClass Of:
        E34 Inscription
    Scope Note:
        This class comprises symbols, signs, signatures or short texts applied to instances of
        E24 Physical Human-Made Thing by arbitrary techniques in order to indicate the creator, owner, dedications,
        purpose, etc.;

        This class specifically excludes features that have no semantic significance, such as scratches or tool marks;
        These should be documented as instances of E25 Human-Made Feature;

        New proposal by MD –issue 463

        This class comprises symbols, signs, signatures or texts applied to instances of E24 Physical Human-Made Thing
        by arbitrary techniques in order to indicate the creator, owner, dedications, purpose, etc. Instances of
        E37 Mark do not represent the actual image of a mark, but the abstract ideal, as they use to be codified in
        reference documents that are used in cultural documentation;

    Examples:
        - Minoan double axe mark (Lowe Fri, 2011)
        - ©
        - ☺
    In First Order Logic:
        E37(x) ⊃ E36(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E34Inscription(E33LinguisticObject, E37Mark):
    """'E34 Inscription' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E34

    SubClass Of:
        E33 Linguistic Object
        E37 Mark
    SuperClass Of:
        -
    Scope Note:
        This class comprises recognisable, texts attached to instances of E24 Physical Human-Made Thing;

        The transcription of the text can be documented in a note by P3 has note: E62 String. The alphabet used can be
        documented by P2 has type: E55 Type. This class does not intend to describe the idiosyncratic characteristics
        of an individual physical embodiment of an inscription, but the underlying prototype. The physical embodiment
        is modelled in the CIDOC CRM as instances of E24 Physical Human-Made Thing;

        The relationship of a physical copy of a book to the text it contains is modelled using E18 Physical Thing;
        P128 carries (is carried by): E33 Linguistic Object;

    Examples:
        - “keep off the grass” on a sign stuck in the lawn of the quad of Balliol College
        - The text published in Corpus Inscriptionum Latinarum V 895
        - Kilroy was here
    In First Order Logic:
        E34(x) ⊃ E33(x)
        E34(x) ⊃ E37(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label="E97 Monetary Amount")
class E97MonetaryAmount(P180HasCurrency, P181HasAmount, E54Dimension):
    """'E97 Monetary Amount' CRM entity model;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E97

    SubClass Of:
        - E54 Dimension
    SuperClass Of:
        -
    Scope Note:
        This class comprises quantities of monetary possessions or obligations in terms of their nominal value with
        respect to a particular currency. These quantities may be abstract accounting units, the nominal value of
        a heap of coins or banknotes at the time of validity of the respective currency, the nominal value of a bill
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


class E98Currency(E58MeasurementUnit, E55Type):
    """'E98 Currency' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E98

    SubClass Of:
        E55 Type
        E58 Measurement Unit
    SuperClass Of:
        -
    Scope Note:
        This class comprises the units in which a monetary system, supported by an administrative authority or other
        community, quantifies and arithmetically compares all monetary amounts declared in the unit. The unit of
        a monetary system must describe a nominal value which is kept constant by its administrative authority and
        an associated banking system if it exists, and not by market value. For instance, one may pay with grams of
        gold, but the respective monetary amount would have been agreed as the gold price in US dollars on the day of
        the payment. Under this definition, British Pounds, U.S. Dollars, and European Euros are examples of currency,
        but “grams of gold” is not. One monetary system has one and only one currency. Instances of this class must
        not be confused with coin denominations, such as “Dime” or “Sestertius”. Non-monetary exchange of value in
        terms of quantities of a particular type of goods, such as cows, do not constitute a currency;

    Examples:
        - “As” (Roman mid republic)
        - “Euro”, (Temperton, 1997)
        - “US Dollar” (Rose, 1978)
    In First Order Logic:
        E98(x) ⊃ E55(x)
        E98(x) ⊃ E58(x)
    Properties:
        -

    """


# ******************************************************************************************************************* #


class E99ProductType(P187HasProductionPlan, P188RequiresProductionTool, E55Type):
    """'E99 Product Type' CRM entity;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#E99

    SubClass Of:
        E55 Type
    SuperClass Of:
        -
    Scope Note:
        Scope note: This classes comprises types that stand as the models for instances of E22 Human-Made Object that
        are produced as the result of production activities using plans exact enough to result in one or more series
        of uniform, functionally and aesthetically identical and interchangeable items. The product type is the
        intended ideal form of the manufacture process. It is typical of instances of E22 that conform to an
        instance of E99 Product Type that its component parts are interchangeable with component parts of other
        instances of E22 made after the model of the same instance of E99. Frequently, the uniform production
        according to a given instance of E99 Product Type is achieved by creating individual tools, such as moulds
        or print plates that are themselves carriers of the design of the product type. Modern tools may use the
        flexibility of electronically controlled devices to achieve such uniformity. The product type itself, i.e.,
        the potentially unlimited series of aesthetically equivalent items, may be the target of artistic design,
        rather than the individual object. In extreme cases, only one instance of a product type may have been
        produced, such as in a "print on demand" process which was only triggered once. However, this should not be
        confused with industrial prototypes, such as car prototypes, which are produced prior to the production line
        being set up, or test the production line itself;

    Examples:
        - : Volkswagen Type 11 (Beetle)
        - Dragendorff 54 samian vessel
        - 1937 Edward VIII brass threepenny bit
        - Qin Crossbow trigger un-notched Part B (Bg2u)
        - Nokia Cityman 1320 (The first Nokia mobile phone)
    In First Order Logic:
        E99(x) ⊃ E55(x)
    Properties:
        P187 has production plan (is production plan for): E29 Design or Procedure
        P188 requires production tool (is production tool for): E19 Physical Object

    """
