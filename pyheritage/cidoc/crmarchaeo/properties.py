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
    from pyheritage.cidoc.core.entities import (
        E18PhysicalThing,
        E27Site,
        E55Type,
    )
    from pyheritage.cidoc.crmarchaeo.entities import (
        A2StratigraphicVolumeUnit,
        A3StratigraphicInterface,
        A5StratigraphicModification,
        A8StratigraphicUnit,
        A10ExcavationInterface,
    )
    from pyheritage.cidoc.crmsci.entities import (
        S10MaterialSubstantial,
        S11AmountOfMatter,
        S19EncounterEvent,
        S22SegmentOfMatter,
    )


__all__ = (
    'AP1Produced',
    'AP2Discarded',
    'AP3Investigated',
    'AP4ProducedSurface',
    'AP5RemovedPartOrAll',
    'AP6IntendedToApproximate',
    'AP7Produced',
    'AP8Disturbed',
    'AP9TookMatterFrom',
    'AP10Destroyed',
    'AP11HasPhysicalRelationTo',
    'AP12Confines',
    'AP13HasStratigraphicRelationTo',
    'AP15IsOrContainsRemainsOf',
    'AP16AssignedAttributeTo',
    'AP17IsFoundBy',
    'AP18IsEmbeddingOf',
    'AP19IsEmbeddingIn',
    'AP21Contains',
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


# ******************************************************************************************************************* #


class AP6IntendedToApproximate(PropertyMixin):
    """'AP6 intended to approximate (was approximated by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP6

    Domain:
        A1 Excavation Processing Unit
    Range:
        A3 Stratigraphic Interface
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with the
        instance of A3 Stratigraphic Interface that this excavation activity intended to
        approximate. It records the intention of the excavator to follow a particular
        stratigraphic interface when creating an excavation interface.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP6(x,y) ⊃ A1(x)
        AP6(x,y) ⊃ A3(y)

    """

    ap6_intended_to_approximate: List[A3StratigraphicInterface] = Field(
        default=None,
        description='AP6 intended to approximate (was approximated by)',
    )


# ******************************************************************************************************************* #


class AP7Produced(PropertyMixin):
    """'AP7 produced (was produced by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP7

    Domain:
        A4 Stratigraphic Genesis
    Range:
        A8 Stratigraphic Unit
    SubProperty Of:
        S17 Physical Genesis. O17 generated (was generated by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of A4 Stratigraphic Genesis with the
        instance of A8 Stratigraphic Unit that was produced by this genesis event or
        process.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP7(x,y) ⊃ A4(x)
        AP7(x,y) ⊃ A8(y)

    """

    ap7_produced: List[A8StratigraphicUnit] = Field(
        default=None,
        min_length=1,
        description='AP7 produced (was produced by)',
    )


# ******************************************************************************************************************* #


class AP8Disturbed(PropertyMixin):
    """'AP8 disturbed (was disturbed by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP8

    Domain:
        A5 Stratigraphic Modification
    Range:
        A8 Stratigraphic Unit
    SubProperty Of:
        S18 Alteration. O18 altered (was altered by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A5 Stratigraphic Modification with the
        instance of A8 Stratigraphic Unit that was disturbed by this modification event.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP8(x,y) ⊃ A5(x)
        AP8(x,y) ⊃ A8(y)

    """

    ap8_disturbed: List[A8StratigraphicUnit] = Field(
        default=None,
        description='AP8 disturbed (was disturbed by)',
    )


# ******************************************************************************************************************* #


class AP9TookMatterFrom(PropertyMixin):
    """'AP9 took matter from (provided matter to)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP9

    Domain:
        A4 Stratigraphic Genesis
    Range:
        S10 Material Substantial
    SubProperty Of:
        S17 Physical Genesis. O17 generated (was generated by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of A4 Stratigraphic Genesis with the
        instance of S10 Material Substantial from which it took matter to form the
        stratigraphic unit.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP9(x,y) ⊃ A4(x)
        AP9(x,y) ⊃ S10(y)

    """

    ap9_took_matter_from: List[S10MaterialSubstantial] = Field(
        default=None,
        min_length=1,
        description='AP9 took matter from (provided matter to)',
    )


# ******************************************************************************************************************* #


class AP10Destroyed(PropertyMixin):
    """'AP10 destroyed (was destroyed by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP10

    Domain:
        A1 Excavation Processing Unit
    Range:
        S22 Segment of Matter
    SubProperty Of:
        S1 Matter Removal. O1 diminished (was diminished by): S10 Material Substantial
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of A1 Excavation Processing Unit with the
        instance of S22 Segment of Matter that was destroyed by this excavation activity.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP10(x,y) ⊃ A1(x)
        AP10(x,y) ⊃ S22(y)

    """

    ap10_destroyed: List[S22SegmentOfMatter] = Field(
        default=None,
        min_length=1,
        description='AP10 destroyed (was destroyed by)',
    )


# ******************************************************************************************************************* #


class AP11HasPhysicalRelationTo(PropertyMixin):
    """'AP11 has physical relation to (is physical relation from)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP11

    Domain:
        A8 Stratigraphic Unit
    Range:
        A8 Stratigraphic Unit
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A8 Stratigraphic Unit with another
        instance of A8 Stratigraphic Unit to which it has a physical relation.
        The qualifier AP11.1 allows specifying the type of relation.

    Properties:
        AP11.1 has type: E55 Type
    Examples:
        -
    In First Order Logic:
        AP11(x,y) ⊃ A8(x)
        AP11(x,y) ⊃ A8(y)

    """

    ap11_has_physical_relation_to: List[A8StratigraphicUnit] = Field(
        default=None,
        description='AP11 has physical relation to (is physical relation from)',
    )

    ap11_1_has_type: List[E55Type] = Field(
        default=None,
        description='AP11.1 has type (type of physical relation)',
    )


# ******************************************************************************************************************* #


class AP12Confines(PropertyMixin):
    """'AP12 confines (is confined by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP12

    Domain:
        A3 Stratigraphic Interface
    Range:
        A2 Stratigraphic Volume Unit
    SubProperty Of:
        S20 Rigid Physical Feature. O7 confines (is confined by): S10 Material Substantial
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A3 Stratigraphic Interface with the instance of
        A2 Stratigraphic Volume Unit that it bounds. The interface is the boundary surface that
        confines the volume of the stratigraphic unit.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP12(x,y) ⊃ A3(x)
        AP12(x,y) ⊃ A2(y)

    """

    ap12_confines: List[A2StratigraphicVolumeUnit] = Field(
        default=None,
        description='AP12 confines (is confined by)',
    )


# ******************************************************************************************************************* #


class AP13HasStratigraphicRelationTo(PropertyMixin):
    """'AP13 has stratigraphic relation to (is stratigraphic relation of)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP13

    Domain:
        A5 Stratigraphic Modification
    Range:
        A5 Stratigraphic Modification
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A5 Stratigraphic Modification with another
        instance of A5 Stratigraphic Modification with which it has a stratigraphic relation.
        The qualifiers AP13.1 and AP13.2 allow specifying the type and justification of the
        relation.

    Properties:
        AP13.1 has type: E55 Type
        AP13.2 justified by (is justification of): AP11 has physical relation to
    Examples:
        -
    In First Order Logic:
        AP13(x,y) ⊃ A5(x)
        AP13(x,y) ⊃ A5(y)

    """

    ap13_has_stratigraphic_relation_to: List[A5StratigraphicModification] = Field(
        default=None,
        description='AP13 has stratigraphic relation to (is stratigraphic relation of)',
    )

    ap13_1_has_type: List[E55Type] = Field(
        default=None,
        description='AP13.1 has type (type of stratigraphic relation)',
    )


# ******************************************************************************************************************* #


class AP15IsOrContainsRemainsOf(PropertyMixin):
    """'AP15 is or contains remains of (is or has remains contained in)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP15

    Domain:
        A2 Stratigraphic Volume Unit
    Range:
        S10 Material Substantial
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A2 Stratigraphic Volume Unit with an instance
        of S10 Material Substantial that it is or contains remains of. This allows linking
        stratigraphic deposits to the original material that they represent.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP15(x,y) ⊃ A2(x)
        AP15(x,y) ⊃ S10(y)

    """

    ap15_is_or_contains_remains_of: List[S10MaterialSubstantial] = Field(
        default=None,
        description='AP15 is or contains remains of (is or has remains contained in)',
    )


# ******************************************************************************************************************* #


class AP16AssignedAttributeTo(PropertyMixin):
    """'AP16 assigned attribute to (was attributed by)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP16

    Domain:
        A6 Group Declaration Event
    Range:
        E18 Physical Thing
    SubProperty Of:
        E13 Attribute Assignment. P141 assigned (was assigned by): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A6 Group Declaration Event with the instance of
        E18 Physical Thing to which an attribute was assigned by this declaration event.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP16(x,y) ⊃ A6(x)
        AP16(x,y) ⊃ E18(y)

    """

    ap16_assigned_attribute_to: List[E18PhysicalThing] = Field(
        default=None,
        description='AP16 assigned attribute to (was attributed by)',
    )


# ******************************************************************************************************************* #


class AP17IsFoundBy(PropertyMixin):
    """'AP17 is found by (found)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP17

    Domain:
        A7 Embedding
    Range:
        S19 Encounter Event
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A7 Embedding with the instance of S19 Encounter
        Event through which the embedded object was found.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP17(x,y) ⊃ A7(x)
        AP17(x,y) ⊃ S19(y)

    """

    ap17_is_found_by: List[S19EncounterEvent] = Field(
        default=None,
        description='AP17 is found by (found)',
    )


# ******************************************************************************************************************* #


class AP18IsEmbeddingOf(PropertyMixin):
    """'AP18 is embedding of (is embedded)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP18

    Domain:
        A7 Embedding
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A7 Embedding with the instance of E18 Physical
        Thing that is embedded within this embedding.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP18(x,y) ⊃ A7(x)
        AP18(x,y) ⊃ E18(y)

    """

    ap18_is_embedding_of: List[E18PhysicalThing] = Field(
        default=None,
        description='AP18 is embedding of (is embedded)',
    )


# ******************************************************************************************************************* #


class AP19IsEmbeddingIn(PropertyMixin):
    """'AP19 is embedding in (contains embedding)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP19

    Domain:
        A7 Embedding
    Range:
        A2 Stratigraphic Volume Unit
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of A7 Embedding with the instance of A2
        Stratigraphic Volume Unit that contains this embedding.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP19(x,y) ⊃ A7(x)
        AP19(x,y) ⊃ A2(y)

    """

    ap19_is_embedding_in: List[A2StratigraphicVolumeUnit] = Field(
        default=None,
        min_length=1,
        description='AP19 is embedding in (contains embedding)',
    )


# ******************************************************************************************************************* #


class AP21Contains(PropertyMixin):
    """'AP21 contains (is contained in)' CRMArchaeo property;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#AP21

    Domain:
        A2 Stratigraphic Volume Unit
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of A2 Stratigraphic Volume Unit with an instance of
        E18 Physical Thing that it contains.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        AP21(x,y) ⊃ A2(x)
        AP21(x,y) ⊃ E18(y)

    """

    ap21_contains: List[E18PhysicalThing] = Field(
        default=None,
        description='AP21 contains (is contained in)',
    )
