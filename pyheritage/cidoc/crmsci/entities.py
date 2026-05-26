# -*- coding: utf-8 -*-

"""CRMsci entity models;

CRMsci v2.0

Entities
--------
S1 Matter Removal
S2 Sample Taking
S4 Observation
S10 Material Substantial
S15 Observable Entity
S17 Physical Genesis
S18 Alteration
S20 Rigid Physical Feature
S21 Measurement

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E5Event,
    E7Activity,
    E13AttributeAssignment,
    E26PhysicalFeature,
    E53Place,
    E63BeginningOfExistence,
    E70Thing,
)


__all__ = (
    'S10MaterialSubstantial',
    'S15ObservableEntity',
    'S17PhysicalGenesis',
    'S18Alteration',
    'S1MatterRemoval',
    'S20RigidPhysicalFeature',
    'S21Measurement',
    'S2SampleTaking',
    'S4Observation',
)


@entity_register(label='S1 Matter Removal')
class S1MatterRemoval(E7Activity, ABC):
    """'S1 Matter Removal' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S1

    SubClass Of:
        E7 Activity

    SuperClass Of:
        E80 Part Removal
        S2 Sample Taking

    Scope Note:
        This class comprises the activities that result in an instance of S10 Material Substantial being
        decreased by the removal of an amount of matter. Typical scenarios include the removal of a
        component or piece of a physical object, removal of an archaeological or geological layer, taking
        a tissue sample from a body or a sample of fluid from a body of water. The removed matter may
        acquire a persistent identity of different nature beyond the act of its removal, such as becoming
        a physical object in the narrower sense. Such cases should be modeled by using multiple
        instantiation with adequate concepts of creating the respective items.

    Examples:
        - the removal of the layer of black overpainting that covered the background of 'La Gioconda
          of the Prado' between 2011 and 2012 by the Prado Museum in Madrid (S1) (Museo del Prado, 2012)

    In First Order Logic:
        S1(x) ⇒ E7(x)

    Properties:
        O1 diminished (was diminished by): S10 Material Substantial
        O2 removed (was removed by): S11 Amount of Matter

    """


# ******************************************************************************************************************* #


@entity_register(label='S4 Observation')
class S4Observation(E13AttributeAssignment, ABC):
    """'S4 Observation' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S4

    SubClass Of:
        E13 Attribute Assignment

    SuperClass Of:
        S5 Inference Making
        S6 Data Evaluation
        S19 Encounter Event
        S21 Measurement
        S23 Position Determination

    Scope Note:
        This class comprises the activity of gaining knowledge about an instance of S15 Observable Entity
        through a methodical procedure. Observation may involve the use of instruments and recording the
        information obtained. The observation activity results in the assignment of a value to an instance
        of S9 Property Type of the observed entity, which can be recorded as an instance of E1 CRM Entity.
        The observed property type and the resultant value may be explicitly recorded as instances of
        S9 Property Type and E1 CRM Entity, respectively.

        Observations are the primary events responsible for the creation of data about instances of
        S15 Observable Entity. Inferences and data transformations that rely on results of prior observations
        are, by definition, not considered observations. Observations can be the source of additional evidence
        from which further knowledge may be inferred through reasoning. The notion of observation formalised
        here is analogous to the convention of referring to "primary data" in scientific discourse.

        Observations begin when an observer, sensor, or device starts to monitor or measure the state
        or behaviour of an observable entity and ends when the observer, sensor, or device stops.
        This includes, for example, the activity of counting the number of birds in a particular area,
        or measuring a certain physical quantity of a particular instance of S10 Material Substantial
        at a particular location.

    Examples:
        - the observation of the first case of H5N1 Avian Influenza in Guangdong, China in 1996 (S4)
        - the daily measurement of the level of the Po River at the Torino measuring station (S4)

    In First Order Logic:
        S4(x) ⇒ E13(x)

    Properties:
        O8 observed (was observed by): S15 Observable Entity
        O9 observed property type (property type was observed by): S9 Property Type
        O16 observed value (value was observed by): E1 CRM Entity

    """


# ******************************************************************************************************************* #


@entity_register(label='S15 Observable Entity')
class S15ObservableEntity(E1CRMEntity, ABC):
    """'S15 Observable Entity' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S15

    SubClass Of:
        E1 CRM Entity

    SuperClass Of:
        E5 Event
        S10 Material Substantial

    Scope Note:
        This class comprises instances of E5 Event or S10 Material Substantial (i.e. items or phenomena,
        such as physical things, their behaviour, states and interactions or events), that can be observed
        by measurement or detection devices or by human sensory impression including when enhanced by tools.

        In order to be observable, instances of E5 Event must consist of some interaction or action of
        material substance. In some cases, the spatiotemporal confinement of the event itself, such as a flash,
        a car stopping etc. marks the limits of a documented observation of an event. In other cases, such as
        the situation of a car passing by a certain object, the spatiotemporal limits of the event of observing
        itself, as well as the direction of attention or the orientation of used instruments, may constrain the
        observed detail of a larger process, e.g., noticing the sight of a car passing by; a light emission, etc.

        Conceptual objects manifest through their carriers such as books, digital media, or even human memory.
        Attributes of conceptual objects, such as number of words, can be observed on their carriers. If the
        respective properties between carriers differ, either they carry different instances of conceptual objects
        or the difference can be attributed to accidental deficiencies in one of the carriers. In that sense even
        immaterial objects are observable. By this model we address the fact that frequently, the actually
        observed carriers of conceptual objects are not explicitly identified in documentation, i.e., they are
        assumed to have existed but they are unknown as individuals.

    Examples:
        - the domestic goose from Guangdong/1/1996 (H5N1) that was identified in 1996 in farmed geese in
          southern China as circulating highly pathogenic H5N1 (E20)
        - the flight of a male Bearded Vulture observed near Loukia, Heraklion, Crete in the morning of the
          24th of October 2020 (E5)
        - the eruption of Krakatoa volcano at Indonesia in 1883 (E5)
        - the cupid head area in the X-Ray of the painting 'Cupid complaining to Venus' (E25)

    In First Order Logic:
        S15(x) ⇒ E1(x)

    Properties:
        O12 has dimension (is dimension of): E54 Dimension

    """


# ******************************************************************************************************************* #


@entity_register(label='S10 Material Substantial')
class S10MaterialSubstantial(E70Thing, S15ObservableEntity):
    """'S10 Material Substantial' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S10

    SubClass Of:
        E70 Thing
        S15 Observable Entity

    SuperClass Of:
        S14 Fluid Body
        S11 Amount of Matter
        E18 Physical Thing

    Scope Note:
        This class comprises constellations of matter with a relative stability of any form sufficient to
        associate them with a persistent identity, such as being confined to certain extent, having a relative
        stability of form or structure, or containing a fixed amount of matter. In particular, it comprises
        physical things in the narrower sense and fluid bodies. It is an abstraction of physical substance for
        solid and non-solid things of matter.

    Examples:
        - the groundwater of the 5-22 basin of Central Macedonia (S10)
        - the Mesozoic carbonate sequence with flysch extracted from the area of Nafplion that was mapped
          and studied by Tattaris in 1970 (S10)
        - Parnassos, the limestone mountain

    In First Order Logic:
        S10(x) ⇒ E70(x)

    Properties:
        O15 occupied (was occupied by): E53 Place
        O25 contains (is contained in): S10 Material Substantial

    """


# ******************************************************************************************************************* #


@entity_register(label='S21 Measurement')
class S21Measurement(S4Observation, ABC):
    """'S21 Measurement' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S21

    SubClass Of:
        S4 Observation

    SuperClass Of:
        S3 Measurement by Sampling
        E16 Measurement

    Scope Note:
        This class comprises actions measuring instances of S15 Observable Entity, properties of physical
        things, or phenomena, states and interactions or events, that can be determined by a systematic
        procedure. Primary data from measurement devices are regarded to be results of an observation process.

    Examples:
        - the magnitude measurement of the earthquake of Mexico city in 2017. (S21) [It had the magnitude
          6.2 Richter] (Mindock, 2017)
        - the sensor measurement by IGME in 1999 which measured the landslide displacement in the area of
          Parnitha, Greece. (S21) (Lucchese et al., 2013; Kritikos et al., 2013; InGeoCloudS, 2012;
          InGeoCloudS, 2013)

    In First Order Logic:
        S21(x) ⇒ S4(x)

    Properties:
        O24 measured (was measured by): S15 Observable Entity

    """


# ******************************************************************************************************************* #


@entity_register(label='S20 Rigid Physical Feature')
class S20RigidPhysicalFeature(E26PhysicalFeature, E53Place):
    """'S20 Rigid Physical Feature' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S20

    SubClass Of:
        E26 Physical Feature
        E53 Place

    SuperClass Of:
        E27 Site
        S22 Segment of Matter

    Scope Note:
        This class comprises physical features with sufficient stability of form in itself and with respect
        to the physical object bearing it in order to associate a permanent reference space within which
        its form is invariant and at rest. The maximum volume in space that an instance of S20 Rigid
        Physical Feature occupies defines uniquely a place for the feature with respect to its surrounding
        matter.

    Examples:
        - the cupid head area in the X-Ray of the painting 'Cupid complaining to Venus' (S20)
        - a fault that cross-cuts the Mesozoic carbonate sequence extracted from the area of Nafplion (S20)
        - a foraminifera shell in a thin section from the carbonate sample collected from the region of
          Mesozoic carbonate sequence (S20)

    In First Order Logic:
        S20(x) ⇒ E18(x)

    Properties:
        O7 confines (is confined by): S10 Material Substantial
        O23 is defined by (defines): E92 Spacetime Volume

    """


# ******************************************************************************************************************* #


@entity_register(label='S18 Alteration')
class S18Alteration(E5Event, ABC):
    """'S18 Alteration' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S18

    SubClass Of:
        E5 Event

    SuperClass Of:
        S17 Physical Genesis
        E11 Modification

    Scope Note:
        This class comprises natural events or man-made processes that create, alter or change physical
        things, by affecting permanently their form or consistency without changing their identity.
        Examples include alterations on depositional features-layers by natural factors or disturbance
        by roots or insects, organic alterations, petrification, etc.

    Examples:
        - the petrification process of the Lesvos forest related to the intense volcanic activity in
          Lesvos island during late Oligocene - middle Miocene period (S18) (Marinos, 1997)
        - the flattening of the Lanhydrock Pedigree parchment after humidification (E11)
          (Pickwoad, N., 2016)

    In First Order Logic:
        S18(x) ⇒ E5(x)

    Properties:
        O18 altered (was altered by): E18 Physical Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='S17 Physical Genesis')
class S17PhysicalGenesis(E63BeginningOfExistence, S18Alteration, ABC):
    """'S17 Physical Genesis' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S17

    SubClass Of:
        E63 Beginning of Existence
        S18 Alteration

    SuperClass Of:
        E12 Production

    Scope Note:
        This class comprises events or processes that result in (generate) physical things, man-made or
        natural, coming into being in the form by which they are later identified. The creation of a new
        physical item, at the same time, can be a result of an alteration (modification) -- it can become
        a new thing due to an alteration activity.

    Examples:
        - the desertification process that resulted in the spatial distribution of 'tiger bush' pattern
          on the gradually sloped terrain in Western Africa, as it was studied in 1994 (S17)
          (Thiery et al., 1995)
        - the corrosion process affecting my copper samples in the artificial aging salt-spray apparatus
          after 10 cycles which produced layers of cuprite and malachite (E12)

    In First Order Logic:
        S17(x) ⇒ E63(x)
        S17(x) ⇒ S18(x)

    Properties:
        O17 generated (was generated by): E18 Physical Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='S2 Sample Taking')
class S2SampleTaking(S1MatterRemoval, ABC):
    """'S2 Sample Taking' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S2

    SubClass Of:
        S1 Matter Removal

    SuperClass Of:
        S3 Measurement by Sampling
        S24 Sample Splitting

    Scope Note:
        This class comprises the activity that results in taking an amount of matter as sample for
        further analysis from a material substantial such as a body of water, a geological formation
        or an archaeological object. The removed matter may acquire a persistent identity of different
        nature beyond the act of its removal, such as becoming a physical object in the narrower sense.
        The sample is typically removed from a physical feature which is used as a frame of reference,
        the place of sampling. In case of non-rigid Material Substantials, the source of sampling may
        regarded not to be modified by the activity of sample taking.

    Examples:
        - the water sampling carried out by IGME, sampled from borehole 10/G5 at 419058.03, 4506565,
          95.7 Mygdonia basin on 28/6/2005 (S2) (Lucchese et al., 2013; Kritikos et al., 2013;
          InGeoCloudS, 2012; InGeoCloudS, 2013)
        - the collection of specimen 'FHO - Benth. - 1055' from a plant of the species 'spiciformis'
          in Zambia by Bullock, A.A. in 1939 (S2)
        - the collection of micro-sample 7, from the paint layer on the area of the apple shown on the
          painting 'Cupid complaining to Venus' (Cranach) by Joyce Plesters in June 1963 (S2)
          (The National Gallery, London, 1963)

    In First Order Logic:
        S2(x) ⇒ S1(x)

    Properties:
        O3 sampled from (was sample by): S10 Material Substantial
        O4 sampled at (was sampling location of): E53 Place
        O5 removed (was removed by): S13 Sample
        O20 sampled from type of part (type of part was sampled by): E55 Type

    """
