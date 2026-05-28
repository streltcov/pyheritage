# -*- coding: utf-8 -*-

"""CRMsci entity models;

CRMsci v2.0

Entities
--------
S1 Matter Removal
S2 Sample Taking
S3 Measurement by Sampling
S4 Observation
S5 Inference Making
S6 Data Evaluation
S7 Simulation or Prediction
S8 Categorical Hypothesis Building
S9 Property Type
S10 Material Substantial
S11 Amount of Matter
S12 Amount of Fluid
S13 Sample
S14 Fluid Body
S15 Observable Entity
S17 Physical Genesis
S18 Alteration
S19 Encounter Event
S20 Rigid Physical Feature
S21 Measurement
S22 Segment of Matter
S23 Position Determination
S24 Sample Splitting

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core import entities as _core_entities_module
from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E5Event,
    E7Activity,
    E13AttributeAssignment,
    E26PhysicalFeature,
    E53Place,
    E55Type,
    E63BeginningOfExistence,
    E70Thing,
)
from pyheritage.cidoc.crmsci.properties import (
    O1Diminished,
    O2Removed,
    O3SampledFrom,
    O4SampledAt,
    O5Removed,
    O6IsFormerOrCurrentPartOf,
    O7Confines,
    O8Observed,
    O9ObservedPropertyType,
    O10AssignedDimension,
    O11Described,
    O12HasDimension,
    O15Occupied,
    O16ObservedValue,
    O17Generated,
    O18Altered,
    O19EncounteredObject,
    O20SampledFromTypeOfPart,
)


__all__ = (
    'S10MaterialSubstantial',
    'S11AmountOfMatter',
    'S12AmountOfFluid',
    'S13Sample',
    'S14FluidBody',
    'S15ObservableEntity',
    'S17PhysicalGenesis',
    'S18Alteration',
    'S19EncounterEvent',
    'S1MatterRemoval',
    'S20RigidPhysicalFeature',
    'S21Measurement',
    'S22SegmentOfMatter',
    'S23PositionDetermination',
    'S24SampleSplitting',
    'S2SampleTaking',
    'S3MeasurementBySampling',
    'S4Observation',
    'S5InferenceMaking',
    'S6DataEvaluation',
    'S7SimulationOrPrediction',
    'S8CategoricalHypothesisBuilding',
    'S9PropertyType',
)


@entity_register(label='S1 Matter Removal')
class S1MatterRemoval(O1Diminished, O2Removed, E7Activity, ABC):
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
class S4Observation(O16ObservedValue, O8Observed, O9ObservedPropertyType, E13AttributeAssignment, ABC):
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
class S15ObservableEntity(O12HasDimension, E1CRMEntity, ABC):
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
class S10MaterialSubstantial(O15Occupied, E70Thing, S15ObservableEntity):
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


@entity_register(label='S11 Amount of Matter')
class S11AmountOfMatter(S10MaterialSubstantial, ABC):
    """'S11 Amount of Matter' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S11

    SubClass Of:
        S10 Material Substantial

    SuperClass Of:
        S12 Amount of Fluid
        S13 Sample

    Scope Note:
        This class comprises fixed amounts of matter specified as some air, some water, some soil, etc.,
        defined by the total and integrity of their material content. In order to be able to identify
        and preserve an instance of S11 Amount of Matter, some sort of confinement is needed that serves
        as a constraint for the enclosed matter and the integrity of the content, such as a bottle.
        In contrast to instances of E18 Physical Thing, no stability of form is required. The content
        may be put into another bottle without losing its identity. An instance of S11 Amount of Matter
        may lose its identifying features by such processes. What matters for the identity of an instance
        of S11 Amount of Matter is the preservation of a relevant composition from the initial state of
        definition onwards.

    Examples:
        - the mass of soil that was removed from sections 1, 2, 3 and 4 of the site of Palamari at Skyros
          island, Greece, after the cleaning of the site in 2006 (S11) (Archaeological Institute of
          America, 2006)
        - the amount of natural cement (S11) that was added in a proportion of 5% in 2016 for the
          development of the sample of mortar in the laboratory of Ceramic, in Boumerdes University
          (Kelouaz et al., 2016)

    In First Order Logic:
        S11(x) ⇒ S10(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S13 Sample')
class S13Sample(S11AmountOfMatter):
    """'S13 Sample' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S13

    SubClass Of:
        S11 Amount of Matter

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of S11 Amount of Matter taken from some instance of S10 Material
        Substantial with the intention to be analyzed, studied or just to be kept as reference.

    Examples:
        - the groundwater sample (S13) taken from borehole 10/G5 of the area of Mygdonia basin
          (Lucchese et al., 2013; Kritikos et al., 2013; InGeoCloudS, 2012; InGeoCloudS, 2013)
        - the micro-sample 7, taken from the painting 'Cupid complaining to Venus' (Cranach)
          by Joyce Plesters in June, 1963 (S13) (The National Gallery, London, 1963)

    In First Order Logic:
        S13(x) ⇒ S11(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S14 Fluid Body')
class S14FluidBody(S10MaterialSubstantial, ABC):
    """'S14 Fluid Body' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S14

    SubClass Of:
        S10 Material Substantial

    SuperClass Of:
        S12 Amount of Fluid

    Scope Note:
        This class comprises a mass of matter in fluid form environmentally constraint in some
        persistent form allowing for identifying it for the management or research of material
        phenomena, such as a part of the sea, a river, the atmosphere or the milk in a bottle.
        Fluids are generally defined by the continuity criterion which is characteristic of their
        substance: their amorphous matter is continuous and tends to flow. Therefore, contiguous
        amounts of matter within a fluid body may stay contiguous or at least be locally spatially
        confined for a sufficiently long time in order to be temporarily identified and traced.
        This is a much weaker concept of stability of form than the one we would apply to what one
        would call a physical object. In general, an instance of Fluid Body may gain or lose matter
        over time through so-called sources or sinks in its surface, in contrast to physical things,
        which may lose or gain matter by exchange of pieces such as spare parts or corrosion.

    Examples:
        - the Rhine River

    In First Order Logic:
        S14(x) ⇒ S10(x)

    Properties:
        (none — inherits O15 occupied: E53 Place and O25 contains: S10 Material Substantial from
        S10 Material Substantial)

    """


# ******************************************************************************************************************* #


@entity_register(label='S12 Amount of Fluid')
class S12AmountOfFluid(O6IsFormerOrCurrentPartOf, S11AmountOfMatter, S14FluidBody):
    """'S12 Amount of Fluid' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S12

    SubClass Of:
        S11 Amount of Matter
        S14 Fluid Body

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises fixed amounts of fluid (be they gas or liquid) defined by the total
        of its material content, typically molecules. They frequently acquire identity in laboratory
        practice by the fact of being kept or handled together within some adequate containers.

    Examples:
        - J.K.'s blood sample 0019FCF5 for the measurement of the cholesterol blood level (fictitious)

    In First Order Logic:
        S12(x) ⇒ S11(x)
        S12(x) ⇒ S14(x)

    Properties:
        O6 is former or current part of (has former or current part): S14 Fluid Body

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
class S20RigidPhysicalFeature(O7Confines, E26PhysicalFeature, E53Place):
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
class S18Alteration(O18Altered, E5Event, ABC):
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
class S17PhysicalGenesis(O17Generated, E63BeginningOfExistence, S18Alteration, ABC):
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
class S2SampleTaking(O3SampledFrom, O4SampledAt, O5Removed, O20SampledFromTypeOfPart, S1MatterRemoval, ABC):
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


# ******************************************************************************************************************* #


@entity_register(label='S3 Measurement by Sampling')
class S3MeasurementBySampling(S2SampleTaking, S21Measurement):
    """'S3 Measurement by Sampling' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S3

    SubClass Of:
        S2 Sample Taking
        S21 Measurement

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of taking a sample and measuring or analyzing it as one unit
        of activity that results in the assignment of a value to a property of the sampled实物.
        S3 Measurement by Sampling inherits the properties of S2 Sample Taking (O3 sampled from:
        S10 Material Substantial and O4 sampled at: E53 Place) and the properties of S21 Measurement
        (O24 measured: S15 Observable Entity), if the sample is not documented beyond the context
        of the activity.

    Examples:
        - the chemical analysis 1 on 20/4/2004 which sampled from layer 50501 and observed the
          presence of organic matter (S3) (Lucchese et al., 2013; Kritikos et al., 2013;
          InGeoCloudS, 2012; InGeoCloudS, 2013)
        - the Sphaerosyllis levantina specimen length measurement on 12/3/1999 (S3)
          (Bekiari et al., 2014)
        - the measurement of refractive index of a glass sample from the painting 'The Virgin and
          Child before a Firescreen' (after Campin) in 2014 (S3) (Foister, S, 2015)

    In First Order Logic:
        S3(x) ⇒ S2(x)
        S3(x) ⇒ S21(x)

    Properties:
        (none — inherits all from S2 Sample Taking and S21 Measurement)

    """


# ******************************************************************************************************************* #


@entity_register(label='S19 Encounter Event')
class S19EncounterEvent(O19EncounteredObject, S4Observation):
    """'S19 Encounter Event' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S19

    SubClass Of:
        S4 Observation

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of S4 Observation (substance) where an E39 Actor encounters
        an instance of E18 Physical Thing at some location that is not further examined or observed
        within the context of this activity. The encountered object is generally part of a larger
        physical feature or collection, and is subject to being identified and described.

    Examples:
        - the encounter of the Villa of the Papyri scrolls in Herculaneum in 1752 (S19)
          (Bonn-Muller, 2010)
        - the detection of lagocephalus sceleratus was carried out with the trawler 419 in the
          Mediterranean sea, during the first week of August 2014 (S19)
          (Bekiari et al., 2014)
        - the encounter of oak planks from a ship during a dig in a mound at the farm Lille Oseberg
          in Norway in 1904 (S19) (Ferguson, 2009, p.10-11)

    In First Order Logic:
        S19(x) ⇒ S4(x)

    Properties:
        O19 encountered object (was object encountered through): E18 Physical Thing
        O21 encountered at (witnessed encounter): E53 Place

    """


# ******************************************************************************************************************* #


@entity_register(label='S5 Inference Making')
class S5InferenceMaking(E13AttributeAssignment, ABC):
    """'S5 Inference Making' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S5

    SubClass Of:
        E13 Attribute Assignment

    SuperClass Of:
        S6 Data Evaluation
        S7 Simulation or Prediction
        S8 Categorical Hypothesis Building

    Scope Note:
        This class comprises the action of making propositions and statements about particular states of
        affairs in reality or in possible realities or categorical descriptions of reality by using
        inferences from other statements based on hypotheses and any form of formal or informal logic.
        It includes evaluations, calculations, and interpretations based on mathematical formulations
        and propositions.

    Examples:
        - the inference made by Sakellarakis in 1980 about the sacrifice of a young man in the Minoan
          temple of Anemospilia based on the skeleton found (and 2 more) in the west room of the temple
          and the ritual bronze knife on it and the hypothesis that he died from loss of blood (S5)
          [the evidence was that his bones remained white in contrast to the others]
          (Sakellarakis and Sapouna-Sakellaraki, 1981)
        - the inference that the underdrawing of the painting 'Cupid complaining to Venus' was done
          with red pigment, based on the observation that red pigment lines appear under the top paint
          layers (S5) (Foister, 2015)

    In First Order Logic:
        S5(x) ⇒ E13(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S6 Data Evaluation')
class S6DataEvaluation(O10AssignedDimension, O11Described, S5InferenceMaking):
    """'S6 Data Evaluation' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S6

    SubClass Of:
        S5 Inference Making

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises the action of concluding propositions on a respective reality from
        observational data by making evaluations based on mathematical inference rules and calculations
        using established hypotheses, such as the calculation of an earthquake epicenter. S6 Data
        Evaluation is not defined as S21/E16 Measurement; Secondary derivations of dimensions of an
        object from data measured by different processes are regarded as S6 Data Evaluation and not
        determining instances of Measurement in its own right. For instance, the volume of a statue
        concluded from a 3D model is an instance of S6 Data Evaluation and not of Measurement.

    Examples:
        - the calculation of the earthquake epicenter of Lokris area in 1989 by IGME (S6)
          (Ganas et al., 2006)
        - the calculation of the intensity distance and assignment of PGA_N using the gcf2sac software
          from the EPPO shock wave recording of 2/2/1990 in Athens (S6)
          (Lucchese et al., 2013; Kritikos et al., 2013; InGeoCloudS, 2012; InGeoCloudS, 2013)
        - the calculation of the overall height of the statue of Hercules in the Temple of Hercules in
          Amman from the measurement of the size of the fragment of the fingers (S6)
          ('Temple of Hercules (Amman)', Wikipedia, 2022)

    In First Order Logic:
        S6(x) ⇒ S5(x)

    Properties:
        O10 assigned dimension (dimension was assigned by): E54 Dimension
        O11 described (was described by): S15 Observable Entity

    """


# ******************************************************************************************************************* #


@entity_register(label='S7 Simulation or Prediction')
class S7SimulationOrPrediction(S5InferenceMaking):
    """'S7 Simulation or Prediction' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S7

    SubClass Of:
        S5 Inference Making

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of executing algorithms or software for simulating the behavior
        and the properties of a system of interacting components that form part of reality or not by
        using a mathematical model of the respective interactions. In particular it implies making
        predictions about the future behaviors of a system of interacting components of reality by
        starting simulation from an actually observed state, such as weather forecasts. Simulations
        may also be used to understand the effects of a theory, to compare theoretical predictions
        with reality, or to show differences with another theory.

    Examples:
        - the forecasting of the imminent flooding of Venice in November 2012 by the Hellenic Centre
          for Marine Research using the Poseidon Sea Level Forecast System, 72 hours before its actual
          occurrence (S7) (slide 18 in Kores et al., 2013)
        - predicting the required temperature to maintain a target RH(%) of 50 based on monthly average
          temperature and RH in Birmingham, UK (S7) [using the 'Calculator for conservation heating']
          (Padfield, no date)

    In First Order Logic:
        S7(x) ⇒ S5(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S8 Categorical Hypothesis Building')
class S8CategoricalHypothesisBuilding(S5InferenceMaking):
    """'S8 Categorical Hypothesis Building' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S8

    SubClass Of:
        S5 Inference Making

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises the action of making categorical hypotheses based on inference rules and
        theories; By categorical hypotheses we mean assumptions about the kinds of interactions and
        related kinds of structures of a domain that have the character of "laws" of nature or human
        behavior, be it necessary or probabilistic. Categorical hypotheses are developed by "induction"
        from finite numbers of observation and the absence of observations of particular kinds. As such,
        categorical hypotheses are always subject to falsification by new evidence. Instances of S8
        Categorical Hypothesis Building include making and questioning categorical hypotheses.

    Examples:
        - hypothesising that 'no binding before the 9th century is made with spine supports' by
          Szirmai (S8) [documented in section 7.1 and 7.2 of 'The Archaeology of Medieval bookbinding']
          (Szirmai, J.A. 1999)

    In First Order Logic:
        S8(x) ⇒ S5(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S9 Property Type')
class S9PropertyType(E55Type):
    """'S9 Property Type' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S9

    SubClass Of:
        E55 Type

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises types of properties. Typically, instances of S9 Property Type would be
        taken from an ontology or terminological system. In particular, instances of this class can
        be used to describe in a parametric way what kind of properties the values in scientific data
        sets are about. By virtue of such descriptions, numeric data can be interpreted as sets of
        propositions in terms of a formal ontology, such as "concentration of nitrate", observed in
        the ground water from a certain borehole.

    Examples:
        - the velocity (S9) (of a station that is observed, meaning a share-wave velocity over the
          first 30 m). (Lucchese et al., 2013; Kritikos et al., 2013; InGeoCloudS, 2012;
          InGeoCloudS, 2013)
        - the retention time (S9) [in gas chromatography, meaning the time it takes for a component
          to pass through the chromatographer's column] ('Gas chromatography', Wikipedia, 2018)

    In First Order Logic:
        S9(x) ⇒ E55(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='S22 Segment of Matter')
class S22SegmentOfMatter(S20RigidPhysicalFeature):
    """'S22 Segment of Matter' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S22

    SubClass Of:
        S20 Rigid Physical Feature

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises physical features with relative stability of form and structure within a
        declared spatial volume of interest. The spatial extent of an instance of S22 Segment of Matter
        may be declared or defined by a researcher or observer usually because the arrangement and
        composition of substance is characteristic for the surrounding matter or can be interpreted as
        traces of its genesis and subsequent internal and external processes it was exposed to. The
        defining spatial extent is typically declared on a continuous matter by means of geometric
        determination without observable boundaries on all sides or any side. It may however be
        extracted at some point in time along the declared boundaries.

        An instance of S22 Segment of Matter is regarded to be existing from the time on it completely
        solidified with a structure that is still preserved in a recognizable way at the time of its
        spatial definition. Its existence is regarded to end when its respective integrity is partially
        or completely corrupted. Uncorrupted subsections of an instance of S22 Segment of Matter may
        continue to exist as segments of matter in their own right beyond the existence of the
        containing instance, and may have solidified before it.

        Typical examples are segments of archaeological or geological layers. They are regarded as
        uncorrupted even if they have undergone conformal deformations, such as compressions or shifts,
        as long as the effects of these deformations do not destroy the relevant structures of interest.

    Examples:
        - the clay floor A11 [Heterogeneous, yellow to grey silty clay; clear, wavy lower boundary]
          (illu p. 1601, Croix et al, 2019)

    In First Order Logic:
        S22(x) ⇒ S20(x)

    Properties:
        O23 is defined by (defines): E92 Spacetime Volume

    """


# ******************************************************************************************************************* #


@entity_register(label='S23 Position Determination')
class S23PositionDetermination(S4Observation):
    """'S23 Position Determination' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S23

    SubClass Of:
        S4 Observation

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of determining positions in space and time. The determined
        position is intended to approximate a part or all of the extent of the presence (instance of
        E93 Presence) of an instance of E18 Physical Thing or E4 Period of interest, such as the
        outer walls of an excavated settlement, the position of a ship sailing or the start and end
        of athlete's run in a competition. Characteristically, a theodolite or GPS device may be
        positioned on some persistent feature. Determining the position of the device will yield an
        approximation of the position of the feature of interest. Alternatively, some material item
        may be observed moving through a determined position at a given time.

        This class does not inherit properties from class S21 Measurement. A position determination
        is an evaluation of a combination of measurement of multiple associated distances and/or
        angles (instances of E54 Dimension) from a particular spot to certain reference points of
        previously known position in the same reference space. A particular role is played by the
        Earth's magnetic field and rotational axis as reference for an angle or direction. Often,
        the observed constituting dimensions are not documented, or hidden in an electronic device
        software. The determined position is given as an E94 Space Primitive corresponding to a
        declarative place. Together with the measured time-span covering the time-critical
        observations it forms a spacetime volume, which should normally overlap with the
        spatiotemporal extent of the thing or phenomenon of interest.

    Examples:
        - the determination of the position of the Titanic for the initial distress call after
          hitting an iceberg (S23) [The iceberg was hit on 14 April 1912 at 23:40 ship's time.
          The subsequent position determination was likely done by Capt. Edward Smith and was
          transmitted 15 April 1912 at 00:27.] (Halpern, 2011)
        - the determination of the position of the Titanic by officer Joseph G. Boxhall after the
          initial distress signal was sent (S23) [done between 00:27 and 00:35, when Boxhall showed
          the coordinates to Smith] (Halpern, 2011)
        - the determination of the position of the Titanic by Robert Ballard's team after the
          Titanic ship-wreck was found (S23) (Ballard et al., 1987)
        - Samuel Halpern's 2007 determination of the position of the Titanic at the time of the
          collision (S23) [based on the position of the ship-wreck] (Halpern, 2007)

    In First Order Logic:
        S23(x) ⇒ S4(x)

    Properties:
        O30 determined position (was determined by): E94 Space Primitive
        O31 has validity time-span (is time-span validity for): E52 Time-Span
        O32 determined position of (was located by): S15 Observable Entity

    """


# ******************************************************************************************************************* #


@entity_register(label='S24 Sample Splitting')
class S24SampleSplitting(S2SampleTaking):
    """'S24 Sample Splitting' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S24

    SubClass Of:
        S2 Sample Taking

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises the activity of dividing an instance of S13 Sample into new instances
        of S13 Sample. This activity describes cases of sub-sampling where the resulting instance
        maintains the characteristic qualities of the original instance. Any observations of these
        qualities made on the new instance also apply to the original one. This class should be used
        to model cases of splitting a homogenous sample into multiple ones.

    Examples:
        - the activity of removing a part from the sample, which was originally taken from the tusk
          fragment GT993 by Godfrey et al. in 2000, in order to analyse it through ICP-AES analysis
          to reveal the composition of the original sample [A sample from a section of the tusk
          fragment GT993 which was originally found in the ship-wreck of Vergulde Draeck in Western
          Australia was taken. This sample was homogenous (ground to fine powder). Part of the sample
          was then removed for elemental analysis using inductively coupled plasma atomic emission
          spectrometry (ICP-AES). Another part was removed for carbon/nitrogen analysis using a LECO
          analyser.] (Godfrey et al., 2002)

    In First Order Logic:
        S24(x) ⇒ S2(x)

    Properties:
        O27 split (was source for): S13 Sample
        O29 removed sub-sample (was sub-sample removed by): S13 Sample

    """


__crmsci_namespace__ = {
    'S9PropertyType': S9PropertyType,
    'S10MaterialSubstantial': S10MaterialSubstantial,
    'S11AmountOfMatter': S11AmountOfMatter,
    'S13Sample': S13Sample,
    'S14FluidBody': S14FluidBody,
    'S15ObservableEntity': S15ObservableEntity,
}


# ******************************************************************************************************************* #


__namespace__ = {**_core_entities_module.__namespace__, **__crmsci_namespace__}


S10MaterialSubstantial.model_rebuild(_types_namespace=__namespace__)
S1MatterRemoval.model_rebuild(_types_namespace=__namespace__)
S2SampleTaking.model_rebuild(_types_namespace=__namespace__)
S4Observation.model_rebuild(_types_namespace=__namespace__)
S6DataEvaluation.model_rebuild(_types_namespace=__namespace__)
S12AmountOfFluid.model_rebuild(_types_namespace=__namespace__)
S15ObservableEntity.model_rebuild(_types_namespace=__namespace__)
S17PhysicalGenesis.model_rebuild(_types_namespace=__namespace__)
S18Alteration.model_rebuild(_types_namespace=__namespace__)
S19EncounterEvent.model_rebuild(_types_namespace=__namespace__)
S20RigidPhysicalFeature.model_rebuild(_types_namespace=__namespace__)
