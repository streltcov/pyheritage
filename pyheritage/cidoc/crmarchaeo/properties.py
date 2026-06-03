# -*- coding: utf-8 -*-

"""CRMArchaeo property models;

(Mixin classes for entity models);

CRMArchaeo v2.0

------------------------------------------------
Properties
------------------------------------------------
AP1  produced                          A1  -> S11
AP2  discarded                         A1  -> S11
AP3  investigated                      A9  -> E27
AP4  produced surface                  A1  -> A10
AP5  removed part or all of            A1  -> A8
AP6  intended to approximate           A1  -> A3
AP7  produced                          A4  -> A8
AP8  disturbed                         A5  -> A8
AP9  took matter from                  A4  -> S10
AP10 destroyed                         A1  -> S22
AP11 has physical relation to          A8  -> A8
AP12 confines                          A3  -> A2
AP13 has stratigraphic relation to     A5  -> A5
AP15 is or contains remains of         A2  -> S10
AP16 assigned attribute to             A6  -> E18
AP17 is found by                       A7  -> S19
AP18 is embedding of                   A7  -> E18
AP19 is embedding in                   A7  -> A2
AP21 contains                          A2  -> E18
AP22 is equal in time to               E2  -> E2
AP23 finishes                          E2  -> E2
AP24 starts                            E2  -> E2
AP25 occurs during                     E2  -> E2
AP26 overlaps in time with             E2  -> E2
AP27 meets in time with                E2  -> E2
AP28 occurs before                     E2  -> E2
AP29 appears in                        E55 -> E4
AP30 restricted to                     E55 -> E4
AP31 typical for                       E55 -> E4
AP32 discarded into                    A1  -> S11

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E27Site
    from pyheritage.cidoc.crmarchaeo.entities import (
        A8StratigraphicUnit,
        A10ExcavationInterface,
    )
    from pyheritage.cidoc.crmsci.entities import S11AmountOfMatter


__all__ = (
    'AP1Produced',
    'AP2Discarded',
    'AP3Investigated',
    'AP4ProducedSurface',
    'AP5RemovedPartOrAll',
)


class AP1Produced(PropertyMixin):
    """'AP1 produced (was produced by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP1

    Domain:
        A1 Excavation Processing Unit
    Range:
        S11 Amount of Matter
    SubProperty Of:
        S1 Matter Removal. O2 removed (was removed by): S11 Amount of Matter
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with an
        instance of S11 Amount of Matter that was produced and documented during this
        excavation activity. The produced matter comprises finds, samples, and other
        material that the excavator separates for further analysis or curation.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP1(x,y) ⊃ A1(x)
        AP1(x,y) ⊃ S11(y)

    """

    ap1_produced: List[S11AmountOfMatter] = Field(
        default=None,
        description='AP1 produced (was produced by)',
    )


# ******************************************************************************************************************* #


class AP2Discarded(PropertyMixin):
    """'AP2 discarded (was discarded by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP2

    Domain:
        A1 Excavation Processing Unit
    Range:
        S11 Amount of Matter
    SubProperty Of:
        S1 Matter Removal. O2 removed (was removed by): S11 Amount of Matter
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with the
        instance of S11 Amount of Matter that was discarded during this activity.
        Discarded matter is removed but not kept for further analysis.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP2(x,y) ⊃ A1(x)
        AP2(x,y) ⊃ S11(y)

    """

    ap2_discarded: List[S11AmountOfMatter] = Field(
        default=None,
        description='AP2 discarded (was discarded by)',
    )


# ******************************************************************************************************************* #


class AP3Investigated(PropertyMixin):
    """'AP3 investigated (was investigated by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP3

    Domain:
        A9 Archaeological Excavation
    Range:
        E27 Site
    SubProperty Of:
        E7 Activity. P7 took place at (witnessed): E53 Place
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A9 Archaeological Excavation with the
        instance of E27 Site that is being investigated by this excavation.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP3(x,y) ⊃ A9(x)
        AP3(x,y) ⊃ E27(y)

    """

    ap3_investigated: List[E27Site] = Field(
        default=None,
        description='AP3 investigated (was investigated by)',
    )


# ******************************************************************************************************************* #


class AP4ProducedSurface(PropertyMixin):
    """'AP4 produced surface (was surface produced by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP4

    Domain:
        A1 Excavation Processing Unit
    Range:
        A10 Excavation Interface
    SubProperty Of:
        E12 Production. P108 has produced (was produced by): E24 Physical Human-Made Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with an
        instance of A10 Excavation Interface that was produced by the excavation activity.
        The excavation interface is the surface (planum, profile, etc.) resulting from
        the removal of matter.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP4(x,y) ⊃ A1(x)
        AP4(x,y) ⊃ A10(y)

    """

    ap4_produced_surface: List[A10ExcavationInterface] = Field(
        default=None,
        description='AP4 produced surface (was surface produced by)',
    )


# ******************************************************************************************************************* #


class AP5RemovedPartOrAll(PropertyMixin):
    """'AP5 removed part or all of (was partially or totally removed by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP5

    Domain:
        A1 Excavation Processing Unit
    Range:
        A8 Stratigraphic Unit
    SubProperty Of:
        S1 Matter Removal. O1 diminished (was diminished by): S10 Material Substantial
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with the
        instance of A8 Stratigraphic Unit that was entirely or partially removed during
        this excavation activity.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP5(x,y) ⊃ A1(x)
        AP5(x,y) ⊃ A8(y)

    """

    ap5_removed_part_or_all: List[A8StratigraphicUnit] = Field(
        default=None,
        min_length=1,
        description='AP5 removed part or all of (was partially or totally removed by)',
    )
