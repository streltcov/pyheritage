# -*- coding: utf-8 -*-

"""CRMsci property models;

CRMsci v2.0

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E53Place, E54Dimension, E55Type
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
