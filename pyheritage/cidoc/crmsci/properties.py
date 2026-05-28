# -*- coding: utf-8 -*-

"""CRMsci property models;

CRMsci v2.0

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E1CRMEntity, E5Event, E18PhysicalThing, E53Place, E54Dimension, E55Type
    from pyheritage.cidoc.crmsci.entities import (
        S9PropertyType,
        S10MaterialSubstantial,
        S11AmountOfMatter,
        S13Sample,
        S14FluidBody,
        S15ObservableEntity,
    )


__all__ = (
    'O1Diminished',
    'O2Removed',
    'O3SampledFrom',
    'O4SampledAt',
    'O5Removed',
    'O6IsFormerOrCurrentPartOf',
    'O7Confines',
    'O8Observed',
    'O9ObservedPropertyType',
    'O10AssignedDimension',
    'O11Described',
    'O12HasDimension',
    'O13Triggered',
    'O15Occupied',
    'O16ObservedValue',
    'O17Generated',
    'O18Altered',
    'O19EncounteredObject',
    'O20SampledFromTypeOfPart',
)


class O1Diminished(PropertyMixin):
    """'O1 diminished (was diminished by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O1

    Domain:
        S1 Matter Removal
    Range:
        S10 Material Substantial
    SubProperty Of:
        -
    SuperProperty Of:
        E80 Part Removal. P112 diminished (was diminished by): E24 Physical Human-Made Thing
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S1 Matter Removal with the instance of
        S10 Material Substantial that this activity diminished. Although an instance of
        S1 Matter Removal activity normally concerns only one item of S10 Material
        Substantial, it is possible that it concerns more than one, e.g., when sampling
        a water body, both the water body and the riverbed are affected. Therefore the
        instantiation of a particular subproperty of O1 diminished is not necessary.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O1(x,y) ⊃ S1(x)
        O1(x,y) ⊃ S10(y)

    """

    o1_diminished: List[S10MaterialSubstantial] = Field(
        default=None,
        min_length=1,
        description='O1 diminished (was diminished by)',
    )


# ******************************************************************************************************************* #


class O2Removed(PropertyMixin):
    """'O2 removed (was removed by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O2

    Domain:
        S1 Matter Removal
    Range:
        S11 Amount of Matter
    SubProperty Of:
        -
    SuperProperty Of:
        S2 Sample Taking. O5 removed (was removed by): S13 Sample
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of S1 Matter Removal with the instance of
        S11 Amount of Matter that was removed during that activity. The removed matter
        may be a sample of some kind, but not necessarily.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O2(x,y) ⊃ S1(x)
        O2(x,y) ⊃ S11(y)

    """

    o2_removed: List[S11AmountOfMatter] = Field(
        default=None,
        description='O2 removed (was removed by)',
    )


# ******************************************************************************************************************* #


class O3SampledFrom(PropertyMixin):
    """'O3 sampled from (was sample by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O3

    Domain:
        S2 Sample Taking
    Range:
        S10 Material Substantial
    SubProperty Of:
        S1 Matter Removal. O1 diminished (was diminished by): S10 Material Substantial
    SuperProperty Of:
        S24 Sample Splitting. O27 split (was source for): S13 Sample
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S2 Sample Taking with the instance of
        S10 Material Substantial from which a sample was taken. In particular, it may be
        a feature or a fluid body from which a sample was removed.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O3(x,y) ⊃ S2(x)
        O3(x,y) ⊃ S10(y)
        O3(x,y) ⊃ O1(x,y)

    """

    o3_sampled_from: List[S10MaterialSubstantial] = Field(
        default=None,
        min_length=1,
        description='O3 sampled from (was sample by)',
    )


# ******************************************************************************************************************* #


class O4SampledAt(PropertyMixin):
    """'O4 sampled at (was sampling location of)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O4

    Domain:
        S2 Sample Taking
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        necessary one to many (1,1:0,n)

    Scope Note:
        This property associates an instance of S2 Sample Taking with the instance of
        E53 Place ("spot") at which this activity sampled. It identifies the narrowest
        relevant area on the material substantial from which the sample was taken. This
        may be known or given in absolute terms or relative to an instance of the
        material substantial from which it was taken. If samples are taken from more
        than one spot, the sample taking activity must be documented by separate
        instances for each spot. The property P7 took place at, inherited from E4 Period,
        describes the position of the area in which the sampling activity occurred; this
        latter comprises the space within which operators and instruments were contained
        during the activity, and the sample taking spot.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O4(x,y) ⊃ S2(x)
        O4(x,y) ⊃ E53(y)

    """

    o4_sampled_at: E53Place = Field(
        description='O4 sampled at (was sampling location of)',
    )


# ******************************************************************************************************************* #


class O5Removed(PropertyMixin):
    """'O5 removed (was removed by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O5

    Domain:
        S2 Sample Taking
    Range:
        S13 Sample
    SubProperty Of:
        S1 Matter Removal. O2 removed (was removed by): S11 Amount of Matter
    SuperProperty Of:
        S24 Sample Splitting. O29 removed sub-sample (was sub-sample removed by): S13 Sample
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S2 Sample Taking with the instance of
        S13 Sample that was taken during the activity.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O5(x,y) ⊃ S2(x)
        O5(x,y) ⊃ S13(y)
        O5(x,y) ⊃ O2(x,y)

    """

    o5_removed: List[S13Sample] = Field(
        default=None,
        min_length=1,
        description='O5 removed (was removed by)',
    )


# ******************************************************************************************************************* #


class O6IsFormerOrCurrentPartOf(PropertyMixin):
    """'O6 is former or current part of (has former or current part)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O6

    Domain:
        S12 Amount of Fluid
    Range:
        S14 Fluid Body
    SubProperty Of:
        S10 Material Substantial. O25 contains (is contained in): S10 Material Substantial
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of S12 Amount of Fluid with an instance of
        S14 Fluid Body which formed or forms part of it. It allows instances of S14 Fluid
        Body to be analyzed into elements of S12 Amount of Fluid.

    Properties:
        -
    Examples:
        - J.K.'s blood sample 0019FCF5 (S12) is former or current part of J.K.'s blood (S14)
          (fictitious)

    In First Order Logic:
        O6(x,y) ⊃ S12(x)
        O6(x,y) ⊃ S14(y)

    """

    o6_is_former_or_current_part_of: List[S14FluidBody] = Field(
        default=None,
        description='O6 is former or current part of (has former or current part)',
    )


# ******************************************************************************************************************* #


class O7Confines(PropertyMixin):
    """'O7 confines (is confined by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O7

    Domain:
        S20 Rigid Physical Feature
    Range:
        S10 Material Substantial
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of S20 Rigid Physical Feature with an instance
        of S10 Material Substantial that it partially or completely confines. It describes
        cases in which rigid features such as stratigraphic layers, walls, dams, riverbeds,
        etc. form the boundaries of some item such as another stratigraphic layer or the
        waters of a river.

    Properties:
        -
    Examples:
        - The Stavros -- Farsala artesian acquifer (S20) confines the overexploited
          groundwater of the area (S10) (Rozos et al., 2017)
        - The posthole (S20) confines the organic material (S10) identified in the 1997
          analysis of the post holes of the structure 2 in the Tutu archaeological village
          site (Righter, 2002)
        - Borehole No1234 confines intake No5 (Lucchese et al., 2013; InGeoCloudS, 2012;
          InGeoCloudS, 2013; Kritikos et al., 2013)

    In First Order Logic:
        O7(x,y) ⊃ S20(x)
        O7(x,y) ⊃ S10(y)

    """

    o7_confines: List[S10MaterialSubstantial] = Field(
        default=None,
        description='O7 confines (is confined by)',
    )


# ******************************************************************************************************************* #


class O8Observed(PropertyMixin):
    """'O8 observed (was observed by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O8

    Domain:
        S4 Observation
    Range:
        S15 Observable Entity
    SubProperty Of:
        E13 Attribute Assignment. P140 assigned attribute to (was attributed by): E1 CRM Entity
    SuperProperty Of:
        S21 Measurement. O24 measured (was measured by): S15 Observable Entity
        S23 Position Determination. O32 determined position of (was located by): S15 Observable Entity
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of S4 Observation with an instance of S15
        Observable Entity that was observed. Specifically it describes that a thing, a
        feature, a phenomenon or its reaction is observed by an activity of Observation.

    Properties:
        -
    Examples:
        - The engineers' observation on the slope of Panagopoula coastal site, near Patras,
          on the 25th-26th April 1971 and the 3rd May 1971 (S4) observed the rotational
          landslide at the same site (S15) (Tavoularis et al., 2017).
        - The survey (S4) of Sinai MS GREEK 418 observed a detached triple-braided clasp
          strap (S15) (Honey and Pickwoad, 2010).

    In First Order Logic:
        O8(x,y) ⊃ S4(x)
        O8(x,y) ⊃ S15(y)
        O8(x,y) ⊃ P140(x,y)

    """

    o8_observed: S15ObservableEntity = Field(
        description='O8 observed (was observed by)',
    )


# ******************************************************************************************************************* #


class O9ObservedPropertyType(PropertyMixin):
    """'O9 observed property type (property type was observed by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O9

    Domain:
        S4 Observation
    Range:
        S9 Property Type
    SubProperty Of:
        E13 Attribute Assignment. P177 assigned property of type (is type of property assigned): E55 Type
    SuperProperty Of:
        -
    Quantification:
        one to one (1,1:0,n)

    Scope Note:
        This property associates an instance of S4 Observation with the instance of S9
        Property Type for which the observation provides a value or evidence, such as
        "concentration of nitrate" observed in the water from a particular borehole.
        Encoding the observed property by type, observed entity and value (properties O9,
        O10, O16) is a method to circumscribe the reification of the observed property by
        the respective instance of S4 Observation.

    Properties:
        -
    Examples:
        - The seismic hazard analysis and recording by EPPO in 1990 (S4), in the area of
          Attiki observed property type share wave velocity (S9) and recorded it
          (Lucchese et al., 2013; Kritikos et al., 2013; InGeoCloudS, 2012; InGeoCloudS, 2013)
        - The Gas Chromatography analysis (S4) of the sample 'mid-blue paint from the sky'
          observed property type retention time (S9). (Foister, 2015)

    In First Order Logic:
        O9(x,y) ⊃ S4(x)
        O9(x,y) ⊃ S9(y)
        O9(x,y) ⊃ P177(x,y)

    """

    o9_observed_property_type: S9PropertyType = Field(
        description='O9 observed property type (property type was observed by)',
    )


# ******************************************************************************************************************* #


class O10AssignedDimension(PropertyMixin):
    """'O10 assigned dimension (dimension was assigned by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O10

    Domain:
        S6 Data Evaluation
    Range:
        E54 Dimension
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S6 Data Evaluation with an instance of
        E54 Dimension that a data evaluation activity has assigned. In that case, dimensions
        may be determined by making evaluations on observational data based on mathematical
        inference rules and calculations.

    Properties:
        -
    Examples:
        - The shock wave recording (S6) carried out by EPPO in 1999 assigned dimension
          PSA_10 (E54) [The dimension had value 0.0008.] (Lucchese et al., 2013; Kritikos
          et al., 2013; InGeoCloudS, 2012; InGeoCloudS, 2013)

    In First Order Logic:
        O10(x,y) ⊃ S6(x)
        O10(x,y) ⊃ E54(y)

    """

    o10_assigned_dimension: List[E54Dimension] = Field(
        default=None,
        min_length=1,
        description='O10 assigned dimension (dimension was assigned by)',
    )


# ******************************************************************************************************************* #


class O11Described(PropertyMixin):
    """'O11 described (was described by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O11

    Domain:
        S6 Data Evaluation
    Range:
        S15 Observable Entity
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S6 Data Evaluation with an instance of
        S15 Observable Entity for which a data evaluation activity provides a description.
        This description of any Observable Entity is based on data evaluations.

    Properties:
        -
    Examples:
        - The quantitative analysis of Munsell colour data carried out by C.T. Brown in
          1999 in Yukatan, Mexico (S6) described the slipped sherds of Mayapan period
          ceramics (S15) (Ruck and Brown, 2015).
        - The linear extrapolation of overall figure height from the size of the fingers
          (S6) described the statue of Hercules (S15) [The statue is located in Amman]
          ('Temple of Hercules (Amman)', Wikipedia, 2022).

    In First Order Logic:
        O11(x,y) ⊃ S6(x)
        O11(x,y) ⊃ S15(y)

    """

    o11_described: List[S15ObservableEntity] = Field(
        default=None,
        min_length=1,
        description='O11 described (was described by)',
    )


# ******************************************************************************************************************* #


class O12HasDimension(PropertyMixin):
    """'O12 has dimension (is dimension of)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O12

    Domain:
        S15 Observable Entity
    Range:
        E54 Dimension
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property associates an instance of S15 Observable Entity with an instance of
        E54 Dimension that the observable entity has. It offers no information about how
        and when an E54 Dimension was established. In case the instance of S15 Observable
        Entity is more specifically an instance of E18 Physical Thing, using the property
        O12 has dimension (is dimension of) is equivalent to using the property P43 has
        dimension (is dimension of). In other words, using the one implies the other.

    Properties:
        -
    Examples:
        - The earthquake of Mexico city in 2017 (E7) has dimension magnitude 6.2 Richter
          (Mindock, 2017).
        - The landslide that was activated in Parnitha in 1999 after the earthquake (E26),
          has dimension crest length > 70 (Lucchese et al., 2013; Kritikos et al., 2013;
          InGeoCloudS, 2012; InGeoCloudS, 2013).

    In First Order Logic:
        O12(x,y) ⊃ S15(x)
        O12(x,y) ⊃ E54(y)
        [O12(x,y) ∧ E18(x)] ⊃ P43(x,y)
        [P43(x,y) ∧ E18(x)] ⊃ O12(x,y)

    """

    o12_has_dimension: List[E54Dimension] = Field(
        default=None,
        description='O12 has dimension (is dimension of)',
    )


# ******************************************************************************************************************* #


class O13Triggered(PropertyMixin):
    """'O13 triggered (was triggered by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O13

    Domain:
        E5 Event
    Range:
        E5 Event
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E5 Event that triggered another instance
        of E5 Event with the latter. It identifies the interaction between events: an
        event can activate (trigger) other events in a target system that is in a
        situation of sustained tension, such as a trap or an unstable mountain slope
        giving way to a land slide after a rain or earthquake. In that sense the
        triggering event is interpreted as a cause. However, the association of the two
        events is based on their temporal proximity, with the triggering event ending
        when the triggered event starts.

    Properties:
        -
    Examples:
        - The earthquake of Parnitha in 1999 (E5) triggered the rotational landslide
          that was observed along the road on the same day (E5). (fictitious)
        - The explosion at the Montserrat massif in 2007 (E5) (near Barcelona, Spain)
          triggered the rock fall event (E5) which happened on 2007-02-14
          (Vilajosana et al., 2008).
        - The 1966 flood in Florence (E5) triggered mould growth on books (E5) stored
          in flooded library rooms (Rubinstein, N., 1966).

    In First Order Logic:
        O13(x,y) ⊃ E5(x)
        O13(x,y) ⊃ E5(y)
        O13(x,y) ⊃ P182(x,y)

    """

    o13_triggered: List[E5Event] = Field(
        default=None,
        description='O13 triggered (was triggered by)',
    )


# ******************************************************************************************************************* #


class O15Occupied(PropertyMixin):
    """'O15 occupied (was occupied by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O15

    Domain:
        S10 Material Substantial
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to one (1,1:0,n)

    Scope Note:
        This property associates an instance of S10 Material Substantial with the instance
        of E53 Place that this substance occupied. It describes the space filled (occupied)
        by a physical matter. This property is the development of the shortcut expressed
        in the proposition of classification: "S20 Physical Feature" isA "E53 Place".
        This property is equivalent to P156 occupies (is occupied by) with domain E18
        Physical Thing and range E53 Place.

    Properties:
        -
    Examples:
        - The layer of pink plaster that occupied the block 30 floor of the area X. on
          2009-02-03. [The plaster covered the floor] (fictitious)

    In First Order Logic:
        O15(x,y) ⊃ S10(x)
        O15(x,y) ⊃ E53(y)
        [O15(x,y) ∧ E18(x)] ⊃ P156(x,y)
        [P156(x,y) ∧ E18(x)] ⊃ O15(x,y)

    """

    o15_occupied: E53Place = Field(
        description='O15 occupied (was occupied by)',
    )


# ******************************************************************************************************************* #


class O16ObservedValue(PropertyMixin):
    """'O16 observed value (value was observed by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O16

    Domain:
        S4 Observation
    Range:
        E1 CRM Entity
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        S23 Position Determination. O30 determined position (was determined by): E94 Space Primitive
        E16 Measurement. P40 observed dimension (was observed in): E54 Dimension
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates a value assigned to an entity observed by S4 Observation.

    Properties:
        -
    Examples:
        - The surface survey at the bronze age site of Mitrou in east Lokris carried out
          by Cornell University in 1989 (S4) observed value 600 (of sherds) (E1)
          (Kramer-Hajos and O'Neill, 2008).

    In First Order Logic:
        O16(x,y) ⊃ S4(x)
        O16(x,y) ⊃ E1(y)
        O16(x,y) ⊃ P141(x,y)

    """

    o16_observed_value: E1CRMEntity = Field(
        description='O16 observed value (value was observed by)',
    )


# ******************************************************************************************************************* #


class O17Generated(PropertyMixin):
    """'O17 generated (was generated by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O17

    Domain:
        S17 Physical Genesis
    Range:
        E18 Physical Thing
    SubProperty Of:
        S18 Alteration. O18 altered (was altered by): E18 Physical Thing
    SuperProperty Of:
        E12 Production. P108 has produced (was produced by): E24 Physical Human-Made Thing
    Quantification:
        one to many, necessary (1,n:0,1)

    Scope Note:
        This property associates an instance of S17 Physical Genesis event with an
        instance of E18 Physical Thing that the event generated.

    Properties:
        -
    Examples:
        - The landslide of Parnitha in 1999 generated the head of the landslide feature.
          (fictitious)
        - The mud flow in the western region of Thessaly million years ago generated the
          deposits of solidified mud with irregular surface in the area. (fictitious)
        - The introduction of my copper samples in the salt-spray apparatus (S17)
          generated new corrosion layers of cuprite and malachite (E18).
          (Velios, 1998)

    In First Order Logic:
        O17(x,y) ⊃ S17(x)
        O17(x,y) ⊃ E18(y)

    """

    o17_generated: List[E18PhysicalThing] = Field(
        default=None,
        min_length=1,
        description='O17 generated (was generated by)',
    )


# ******************************************************************************************************************* #


class O18Altered(PropertyMixin):
    """'O18 altered (was altered by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O18

    Domain:
        S18 Alteration
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
        S17 Physical Genesis. O17 generated (was generated by): E18 Physical Thing
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S18 Alteration process with an instance
        of E18 Physical Thing which was altered by this activity.

    Properties:
        -
    Examples:
        - The death of the trees caused by beetle infestation in 1995 (S18), altered
          the Brazilian forest (E18) (Paine, 2008).
        - The application of tension (S18) altered the humidified parchment of the
          Lanhydrock Pedigree (E18) (Pickwoad, 2010).

    In First Order Logic:
        O18(x,y) ⊃ S18(x)
        O18(x,y) ⊃ E18(y)

    """

    o18_altered: List[E18PhysicalThing] = Field(
        default=None,
        min_length=1,
        description='O18 altered (was altered by)',
    )


# ******************************************************************************************************************* #


class O19EncounteredObject(PropertyMixin):
    """'O19 encountered object (was object encountered through)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O19

    Domain:
        S19 Encounter Event
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of S19 Encounter Event with an instance of
        E18 Physical Thing that was encountered or observed as present during the event.

    Properties:
        -
    Examples:
        - The encounter of a marble floor during the digging of a well in 1750 (S19)
          encountered object the Villa of the Papyri in Herculaneum (E18).
          (Sider, 1990, p. 536)
        - The encounter of oak planks from a ship during a dig in a mound at the farm
          Lille Oseberg in Norway, in 1904 (S19) encountered object the Oseberg Ship
          (E18). (Ferguson, 2009, p.10-11)

    In First Order Logic:
        O19(x,y) ⊃ S19(x)
        O19(x,y) ⊃ E18(y)
        O19(x,y) ⊃ (∃z)[E53(z) ∧ O21(x,z)]

    """

    o19_encountered_object: List[E18PhysicalThing] = Field(
        default=None,
        min_length=1,
        description='O19 encountered object (was object encountered through)',
    )


# ******************************************************************************************************************* #


class O20SampledFromTypeOfPart(PropertyMixin):
    """'O20 sampled from type of part (type of part was sampled by)' CRMsci property;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#O20

    Domain:
        S2 Sample Taking
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of S2 Sample Taking with the instance of
        E55 Type that describes what kind of part was sampled. It identifies features
        and material substantial as types of parts of sampling positions.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        O20(x,y) ⊃ S2(x)
        O20(x,y) ⊃ E55(y)

    """

    o20_sampled_from_type_of_part: List[E55Type] = Field(
        default=None,
        description='O20 sampled from type of part (type of part was sampled by)',
    )
