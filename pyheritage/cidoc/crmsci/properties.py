# -*- coding: utf-8 -*-

"""CRMsci property models;

CRMsci v2.0

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E53Place, E55Type
    from pyheritage.cidoc.crmsci.entities import S10MaterialSubstantial, S11AmountOfMatter, S13Sample


__all__ = (
    'O1Diminished',
    'O2Removed',
    'O3SampledFrom',
    'O4SampledAt',
    'O5Removed',
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
