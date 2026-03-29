# -*- coding: utf-8 -*-

"""Physical object properties: composition, custody, location, visual content;

(Mixin classes for entity models);

CIDOC-CRM v7.0

----------------------------------------------
Properties
----------------------------------------------
P43  has dimension                  E70 -> E54
P44  has condition                  E18 -> E3
P45  consists of                    E18 -> E57
P46  is composed of                 E18 -> E18
P49  has former or current keeper   E18 -> E39
P50  has current keeper             E18 -> E39
P51  has former or current owner    E18 -> E39
P52  has current owner              E18 -> E39
P53  has former or current location E18 -> E53
P54  has current permanent location E19 -> E53
P55  has current location           E19 -> E53
P56  bears feature                  E19 -> E26
P57  has number of parts            E19 -> E60
P59  has section                    E18 -> E53
P62  depicts                        E24 -> E1
P65  shows visual item              E24 -> E36
P101 had as general use             E70 -> E55
P103 was intended for               E71 -> E55
P109 has current or former curator  E78 -> E39
P128 carries                        E18 -> E90
P130 shows features of              E70 -> E70
P156 occupies                       E18 -> E53
P196 defines                        E18 -> E92
Pxxx holds or supports              E18 -> E18

"""


from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (
        CoercedNumber,
        E1CRMEntity,
        E3ConditionState,
        E18PhysicalThing,
        E26PhysicalFeature,
        E36VisualItem,
        E39Actor,
        E53Place,
        E54Dimension,
        E55Type,
        E57Material,
        E70Thing,
        E90SymbolicObject,
        E92SpaceTimeVolume,
    )


__all__ = ('P43HasDimension', 'P44HasCondition', 'P45ConsistsOf', 'P46IsComposedOf', 'P49HasFormerOrCurrentKeeper',
           'P50HasCurrentKeeper', 'P51HasCurrentOrFormerOwner', 'P52HasCurrentOwner', 'P53HasFormerOrCurrentLocation',
           'P54HasCurrentPermanentLocation', 'P55HasCurrentLocation', 'P56BearsFeature', 'P57HasNumberOfParts',
           'P59HasSection', 'P62Depicts', 'P65ShowsVisualItem', 'P101HadAGeneralUse', 'P103WasIntendedFor',
           'P109HasCurrentOrFormerCurator', 'P128Carries', 'P130ShowsFeaturesOf', 'P156Occupies', 'P196Defines',
           'PxxxHoldsOrSupports', )


class P43HasDimension(PropertyMixin):
    """'P43 has dimension (is dimension of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P43

    Domain:
        E70 Thing
    Range:
        E54 Dimension
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property records a E54 Dimension of some E70 Thing.

        It is a shortcut of the more fully developed path from ‘E70 Thing’ through ‘P39 measured’, ‘E16 Measurement’,
        ‘P40 observed dimension’, to ‘E54 Dimension’. It offers no information about how and when an E54 Dimension was
        established, nor by whom;

        An instance of E54 Dimension is specific to an instance of E70 Thing;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) has dimension height of silver cup 232 (E54) has unit (P91) mm (E58), has value (P90)
          224 (E60)
    In First Order Logic:
        P43(x,y) ⊃ E70(x)
        P43(x,y) ⊃ E54(y)

    """

    p43_has_dimension: Optional[E54Dimension] = Field(default=None, description='P43 has dimension (is dimension of)')


# ******************************************************************************************************************* #


class P44HasCondition(PropertyMixin):
    """'P44 has condition (is condition of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P44

    Domain:
        E18 Physical Thing
    Range:
        E3 Condition State
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property records an E3 Condition State for some E18 Physical Thing;

        It is a shortcut of the more fully developed path from ‘E18 Physical Thing’ through ‘P34 concerned’,
        ‘E14 Condition Assessment’, ‘P35 has identified’, to ‘E3 Condition State’. It offers no information about how
        and when the E3 Condition State was established, nor by whom;

        An instance of Condition State is specific to an instance of Physical Thing;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) has condition oxidation traces were present in 1997 (E3) has type
          oxidation traces (E55)
    In First Order Logic:
        P44(x,y) ⊃ E18(x)
        P44(x,y) ⊃ E3(y)

    """

    p44_has_condition: Optional[E3ConditionState] = Field(
        default=None,
        description='P44 has condition (is condition of)'
    )


# ******************************************************************************************************************* #


class P45ConsistsOf(PropertyMixin):
    """'P45 consists of (is incorporated in)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P45

    Domain:
        E18 Physical Thing
    Range:
        E57 Material
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instances of E57 Materials of which an instance of E18 Physical Thing
        is composed;

        All physical things consist of physical materials. P45 consists of (is incorporated in) allows the different
        Materials to be recorded. P45 consists of (is incorporated in) refers here to observed Material as opposed to
        the consumed raw material;

        A Material, such as a theoretical alloy, may not have any physical instances;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) consists of silver (E57)
    In First Order Logic:
        P45(x,y) ⊃ E18(x)
        P45(x,y) ⊃ E57(y)

    """

    p45_consists_of: List[E57Material] = Field(description='P45 consists of (is incorporated in)')


# ******************************************************************************************************************* #


class P46IsComposedOf(PropertyMixin):
    """'P46 is composed of (forms part of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P46

    Domain:
        E18 Physical Thing
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        E19 Physical Object. P56 bears feature (is found on): E26 Physical Feature
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E18 Physical Thing with another instance of Physical Thing that forms
        part of it. The spatial extent of the composing part is included in the spatial extent of the whole;

        Component elements, since they are themselves instances of E18 Physical Thing, may be further analysed into
        sub-components, thereby creating a hierarchy of part decomposition. An instance of E18 Physical Thing may be
        shared between multiple wholes, for example two buildings may share a common wall. This property does not
        specify when and for how long a component element resided in the respective whole. If a component is not part
        of a whole from the beginning of existence or until the end of existence of the whole, the classes
        E79 Part Addition and E90 Part Removal can be used to document when a component became part of a particular
        whole and/or when it stopped being a part of it. For the time-span of being part of the respective whole, the
        component is completely contained in the place the whole occupies;

        This property is intended to describe specific components that are individually documented, rather than
        general aspects. Overall descriptions of the structure of an instance of E18 Physical Thing are captured by
        the P3 has note property;

        The instances of E57 Material of which an item of E18 Physical Thing is composed should be documented using
        P45 consists of (is incorporated in);

        This property is transitive;

    Properties:
        -
    Examples:
        - the Royal carriage (E22) forms part of the Royal train (E22)
        - the “Hog’s Back” (E24) forms part of the “Fosseway” (E24)
    In First Order Logic:
        P46(x,y) ⊃ E18(x)
        P46(x,y) ⊃ E18(y)
        P46(x,y) ⊃ P132(x,y)
        P46(x,y) ⊃ (∃uzw)[E93(u) ∧ P166 (x,u) ∧ E52(z) ∧ P164(u,z) ∧ E93(w) ∧ P166 (y,w) ∧
        P164(w,z) ∧ P10(w,u)]

    """

    p46_is_composed_of: Optional[List[E18PhysicalThing]] = Field(
        default=None,
        description='P46 is composed of (forms part of)'
    )


# ******************************************************************************************************************* #


class P49HasFormerOrCurrentKeeper(PropertyMixin):
    """'P49 has former or current keeper (is former or current keeper of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P49

    Domain:
        E18 Physical Thing
    Range:
        E39 Actor
    SubProperty Of:
        -
    SuperProperty Of:
        E18 Physical Thing. P50 has current keeper (is current keeper of): E39 Actor
        E78 Curated Holding. P109 has current or former curator (is current or former curator of): E39 Actor
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor who has or has had custody of an instance of
        E18 Physical Thing at some time. This property leaves open the question if parts of this physical thing have
        been added or removed during the time-spans it has been under the custody of this actor, but it is required
        that at least a part which can unambiguously be identified as representing the whole has been under this
        custody for its whole time. The way, in which a representative part is defined, should ensure that it is
        unambiguous who keeps a part and who the whole and should be consistent with the identity criteria of the kept
        instance of E18 Physical Thing;

        The distinction with P50 has current keeper (is current keeper of) is that P49 has former or current keeper
        (is former or current keeper of) leaves open the question as to whether the specified keepers are current;

        P49 has former or current keeper (is former or current keeper of) is a shortcut for the more detailed path
        from ‘E18 Physical Thing’ through ‘P30 transferred custody of’, ‘E10 Transfer of Custody’, ‘P28 custody
        surrendered by’ or ‘P29 custody received by’ to ‘ E39 Actor’;

    Properties:
        -
    Examples:
        - paintings from The Iveagh Bequest (E18) has former or current keeper Secure Deliveries Inc. (E74)
    In First Order Logic:
        P49(x,y) ⊃ E18(x)
        P49(x,y) ⊃ E39(y)

    """

    p49_has_former_or_current_keeper: Optional[List[E39Actor]] = Field(
        default=None,
        description='P49 has former or current keeper (is former or current keeper of)'
    )


# ******************************************************************************************************************* #


class P50HasCurrentKeeper(PropertyMixin):
    """'P50 has current keeper (is current keeper of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P50

    Domain:
        E18 Physical Thing
    Range:
        E39 Actor
    SubProperty Of:
        E18 Physical Thing. P49 has former or current keeper (is former or current keeper of): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the an instance of E39 Actor that had custody of an instance of E18 Physical Thing at
        the time of validity of the record or database containing the statement that uses this property;

        P50 has current keeper (is current keeper of) is a shortcut for the more detailed path from
        ‘E18 Physical Thing’ through, ‘P30i custody transferred through’, ‘E10 Transfer of Custody’,
        ‘P29 custody received by’ ,to ‘E39 Actor’;

    Properties:
        -
    Examples:
        - paintings from The Iveagh Bequest (E18) has current keeper The National Gallery (E74)
    In First Order Logic:
        P50(x,y) ⊃ E18(x)
        P50(x,y) ⊃ E39(y)
        P50(x,y) ⊃ P49(x,y)

    """

    p50_has_current_keeper: Optional[List[E39Actor]] = Field(
        default=None,
        description='P50 has current keeper (is current keeper of)'
    )


# ******************************************************************************************************************* #


class P51HasCurrentOrFormerOwner(PropertyMixin):
    """'P51 has former or current owner (is former or current owner of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P51

    Domain:
        E18 Physical Thing
    Range:
        E39 Actor
    SubProperty Of:
        -
    SuperProperty Of:
        E18 Physical Thing. P52 has current owner (is current owner of): E39 Actor
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of E39 Actor that is or had been the legal owner (i.e. title holder) of
        an instance of E18 Physical Thing at some time;

        The distinction with P52 has current owner (is current owner of) is that P51 has former or current owner
        (is former or current owner of) does not indicate whether the specified owners are current. P51 has former
        or current owner (is former or current owner of) is a shortcut for the more detailed path from
        ‘E18 Physical Thing’ through ‘P24i changed ownership through’, ‘E8 Acquisition’, ‘P23 transferred title from’,
        or ‘P22 transferred title to’,to ‘E39 Actor’

    Properties:
        -
    Examples:
        - paintings from the Iveagh Bequest (E18) has former or current owner Lord Iveagh (E21)
    In First Order Logic:
        P51(x,y) ⊃ E18(x)
        P51(x,y) ⊃ E39(y)

    """

    p51_has_current_or_former_owner: Optional[List[E39Actor]] = Field(
        default=None,
        description='P51 has former or current owner (is former or current owner of)'
    )


# ******************************************************************************************************************* #


class P52HasCurrentOwner(PropertyMixin):
    """'P52 has current owner (is current owner of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P52

    Domain:
        E18 Physical Thing
    Range:
        E39 Actor
    SubProperty Of:
        E18 Physical Thing. P51 has former or current owner (is former or current owner of): E39 Actor
        E72 Legal Object. P105 right held by (has right on): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the instance of E21 Person or E74 Group that was the owner of an instance of
        E18 Physical Thing at the time of validity of the record or database containing the statement that uses this
        property;

        P52 has current owner (is current owner of) is a shortcut for the more detailed path from
        ‘E18 Physical Thing through’, ‘P24i changed ownership through, ‘E8 Acquisition’, ‘P22 transferred title to’,
        to ‘E39 Actor’, if and only if this acquisition event is the most recent;

    Properties:
        -
    Examples:
        - paintings from the Iveagh Bequest (E18) has current owner «English Heritage» (E40)
    In First Order Logic:
        P52 (x,y) ⊃ E18(x)
        P52 (x,y) ⊃ E39(y)
        P52(x,y) ⊃ P51(x,y)
        P52(x,y) ⊃ P105(x,y)

    """

    p52_has_current_owner: Optional[List[E39Actor]] = Field(
        default=None,
        description='P52 has current owner (is current owner of)'
    )


# ******************************************************************************************************************* #


class P53HasFormerOrCurrentLocation(PropertyMixin):
    """'P53 has former or current location (is former or current location of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P53

    Domain:
        E18 Physical Thing
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        E19 Physical Object. P55 has current location (currently holds): E53 Place
        E18 Physical Thing. P156 occupies (is occupied by): E53 Place
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies an instance of E53 Place as the former or current location of an instance of
        E18 Physical Thing;

        In the case of instances of E19 Physical Object, the property does not allow any indication of the Time-Span
        during which the instance of E19 Physical Object was located at this instance of E53 Place, nor if this is the
        current location;

        In the case of immobile objects, the Place would normally correspond to the Place of creation;

        P53 has former or current location (is former or current location of) is a shortcut. A more detailed
        representation can make use of the fully developed (i.e. indirect) path from ‘E19 Physical Object’, though,
        ‘P25i moved by’, ‘E9 Move’, ‘P26 moved to’ or ‘P27 moved from’, to ‘ E53 Place’;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) has former or current location Display Case 4, Room 23, Museum of Oxford (E53)
    In First Order Logic:
        P53(x,y) ⊃ E18(x)
        P53(x,y) ⊃ E53(y)

    """

    p53_has_former_or_current_location: List[E53Place] = Field(
        description='P53 has former or current location (is former or current location of)'
    )


# ******************************************************************************************************************* #


class P54HasCurrentPermanentLocation(PropertyMixin):
    """'P54 has current permanent location (is current permanent location of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P54

    Domain:
        E19 Physical Object
    Range:
        E53 Place
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property records the foreseen permanent location of an instance of E19 Physical Object at the time of
        validity of the record or database containing the statement that uses this property;

        P54 has current permanent location (is current permanent location of) is similar to P55 has current location
        (currently holds). However, it indicates the E53 Place currently reserved for an object, such as the permanent
        storage location or a permanent exhibit location. The object may be temporarily removed from the permanent
        location, for example when used in temporary exhibitions or loaned to another institution. The object may
        never actually be located at its permanent location;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) has current permanent location Shelf 3.1, Store 2, Museum of Oxford (E53)
    In First Order Logic:
        P54(x,y) ⊃ E19(x)
        P54(x,y) ⊃ E53(y)

    """

    p54_has_current_permanent_location: Optional[E53Place] = Field(
        default=None,
        description='P54 has current permanent location (is current permanent location of)'
    )


# ******************************************************************************************************************* #


class P55HasCurrentLocation(PropertyMixin):
    """'P55 has current location (currently holds)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P55

    Domain:
        E19 Physical Object
    Range:
        E53 Place
    SubProperty Of:
        E18 Physical Thing. P53 has former or current location (is former or current location of): E53 Place
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property records the location of an instance of E19 Physical Object at the time of validity of the record
        or database containing the statement that uses this property;

        This property is a specialisation of P53 has former or current location (is former or current location of). It
        indicates that the instance of E53 Place associated with the instance of E19 Physical Object is the current
        location of the object. The property does not allow any indication of how long the object has been at the
        current location;

        P55 has current location (currently holds) is a shortcut. A more detailed representation can make use of the
        fully developed (i.e. indirect) path from ‘E19 Physical Object’,through, ‘P25i moved by’, ‘E9 Move’,
        ‘P26 moved to’, to, ‘E53 Place’if and only if this Move is the most recent;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) has current location Display cabinet 23, Room 4, British Museum (E53)
    In First Order Logic:
        P55(x,y) ⊃ E19(x)
        P55(x,y) ⊃ E53(y)
        P55(x,y) ⊃ P53(x,y)

    """

    p55_has_current_location: Optional[E53Place] = Field(
        default=None,
        description='P55 has current location (currently holds)'
    )


# ******************************************************************************************************************* #


class P56BearsFeature(PropertyMixin):
    """'P56 bears feature (is found on)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P56

    Domain:
        E19 Physical Object
    Range:
        E26 Physical Feature
    SubProperty Of:
        E18 Physical Thing. P46 is composed of (forms part of): E18 Physical Thing
        E18 Physical Thing. Pxxx holds or supports: E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        one to many, dependent (0,n:1,1)

    Scope Note:
        This property links an instance of E19 Physical Object to an instance of E26 Physical Feature that it bears;

        An instance of E26 Physical Feature can only exist on one object. One object may bear more than one
        E26 Physical Feature. An instance of E27 Site should be considered as an instance of E26 Physical Feature on
        the surface of the Earth;

        An instance B of E26 Physical Feature being a detail of the structure of another instance A of
        E26 Physical Feature can be linked to B by use of the property P46 is composed of (forms part of). This
        implies that the subfeature B is P56i found on the same E19 Physical Object as A;

        P56 bears feature (is found on) is a shortcut. A more detailed representation can make use of the fully
        developed (i.e. indirect) path ‘E19 Physical Object’,through, ‘P59 has section’, ‘E53 Place’,
        ‘P53i is former or current location of’, to, ‘E26 Physical Feature’;

    Properties:
        -
    Examples:
        - silver cup 232 (E22) bears feature 32 mm scratch on silver cup 232 (E26)
    In First Order Logic:
        P56(x,y) ⊃E19(x)
        P56(x,y) ⊃ E26(y)
        P56(x,y) ⊃ P46(x,y)

    """

    p56_bears_feature: Optional[E26PhysicalFeature] = Field(
        default=None,
        description='P56 bears feature (is found on)'
    )


# ******************************************************************************************************************* #


class P57HasNumberOfParts(PropertyMixin):
    """'P57 has number of parts' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P57

    Domain:
        E19 Physical Object
    Range:
        E60 Number
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one (0,1:0,n)

    Scope Note:
        This property documents the number of parts, an instance of E60 Number, of which an instance of
        E19 Physical Object is composed;

        This may be used as a method of checking inventory counts with regard to aggregate or collective objects. What
        constitutes a part or component depends on the context and requirements of the documentation. Normally, the
        parts documented in this way would not be considered as worthy of individual attention;

        For a more complete description, objects may be decomposed into their components and constituents using
        P46 is composed of (forms parts of) and P45 consists of (is incorporated in). This allows each element to be
        described individually;

    Properties:
        -
    Examples:
        - chess set 233 (E22) has number of parts 33 (E60)
    In First Order Logic:
        P57(x,y) ⊃ E19(x)
        P57(x,y) ⊃ E60(y)

    """

    p57_has_number_of_parts: Optional[CoercedNumber] = Field(default=None, description='P57 has number of parts')


# ******************************************************************************************************************* #


class P59HasSection(PropertyMixin):
    """'P59 has section (is located on or within)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P59

    Domain:
        E18 Physical Thing
    Range:
        E53 Place
    SubProperty Of:
        E18 Physical Thing. P157i provides reference space for (is at rest relative to): E53 Place
    SuperProperty Of:
        -
    Quantification:
        one to many (0,n:0,1)

    Scope Note:
        This property links an area, i.e., an instance of E53 Place to the instance of E18 Physical Thing upon which
        it is found. This area may either be identified by a name, or by a geometry in terms of a coordinate system
        adapted to the shape of the respective instance of E18 Physical Thing. Typically, names identifying sections
        of physical objects are composed of the name of a kind of part and the name of the object itself, such as
        "The poop deck of H.M.S. Victory", which is composed of "poop deck" and "H.M.S. Victory";

    Properties:
        -
    Examples:
        - HMS Victory (E22) has section HMS Victory section B347.6 (E53)
    In First Order Logic:
        P59(x,y) ⊃ E18(x)
        P59(x,y) ⊃ E53(y)

    """

    p59_has_section: Optional[E53Place] = Field(default=None, description='P59 has section (is located on or within)')


# ******************************************************************************************************************* #


class P62Depicts(PropertyMixin):
    """'P62 depicts (is depicted by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P62

    Domain:
        E24 Physical Human-Made Thing
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies something that is depicted by an instance of E24 Physical Human-Made Thing. Depicting
        is meant in the sense that an instance of E24 Physical Human-Made Thing intentionally shows, through its
        optical qualities or form, a representation of the entity depicted. Photographs are by default regarded as
        being intentional in this sense. Anything that is designed to change the properties of the depiction, such as
        an e-book reader, is specifically excluded. The property does not pertain to inscriptions or any other
        information encoding;

        This property is a shortcut of the more fully developed path from E24 Physical Human-Made Thing through P65
        shows visual item, E36 Visual Item, P138 represents, E1CRM Entity. P138.1 mode of representation “depiction”
        allows the nature of the depiction to be refined;

    Properties:
        P62.1 mode of depiction: E55 Type
    Examples:
        - The painting “La Liberté guidant le peuple” by Eugène Delacroix (E84) depicts the French “July Revolution”
          of 1830 (E7)
        - the 20 pence coin held by the Department of Coins and Medals of the British Museum under registration number
          2006,1101.126 (E24) depicts Queen Elizabeth II (E21) mode of depiction Profile (E55)
    In First Order Logic:
        P62(x,y) ⊃ E24(x)
        P62(x,y) ⊃ E1(y)
        P62(x,y,z) ⊃ [P62(x,y) ∧ E55(z)]

    """

    p62_depicts: Optional[E1CRMEntity] = Field(default=None, description='P62 depicts (is depicted by)')


# ******************************************************************************************************************* #


class P65ShowsVisualItem(PropertyMixin):
    """'P65 shows visual item (is shown by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P65

    Domain:
        E24 Physical Human-Made Thing
    Range:
        E36 Visual Item
    SubProperty Of:
        E18 Physical Thing. P128 carries (is carried by): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property documents an instance of E36 Visual Item shown by an instance of E24 Physical Human-Made Thing;

        This property is similar to P62 depicts (is depicted by) in that it associates an instance of
        E24 Physical Human-Made Thing with a visual representation. However, P65 shows visual item (is shown by)
        differs from the P62 depicts (is depicted by) property in that it makes no claims about what the instance of
        E36 Visual Item is deemed to represent. An instance of E36 Visual Item identifies a recognisable image or
        visual symbol, regardless of what this image may or may not represent;

        For example, all recent British coins bear a portrait of Queen Elizabeth II, a fact that is correctly
        documented using P62 depicts (is depicted by). Different portraits have been used at different periods,
         however. P65 shows visual item (is shown by) can be used to refer to a particular portrait;

        P65 shows visual item (is shown by) may also be used for Visual Items such as signs, marks and symbols, for
        example the 'Maltese Cross' or the 'copyright symbol’ that have no particular representational content;

        This property is part of the fully developed path E24 Physical Human-Made Thing , P65 shows visual item,
        E36 Visual Item, P138 represents,E1 CRM Entity which is shortcut by, P62 depicts (is depicted by);

    Properties:
        -
    Examples:
        - My T-Shirt (E22) shows visual item Mona Lisa (E36)
    In First Order Logic: P65(x,y) ⊃ E24(x)
        P65(x,y) ⊃ E36(y)
        P65(x,y) ⊃ P128(x,y)
    In First Order Logic:
        -

    """

    p65_shows_visual_item: Optional[List[E36VisualItem]] = Field(
        default=None,
        description='P65 shows visual item (is shown by)'
    )


# ******************************************************************************************************************* #


class P101HadAGeneralUse(PropertyMixin):
    """'P101 had as general use (was use of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P101

    Domain:
        E70 Thing
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of E70 Thing with an instance of E55 Type describing its general usage;

        It allows the relationship between particular things, both physical and immaterial, and general methods and
        techniques of use to be documented. Thus it can be asserted that a baseball bat had a general use for sport
        and a specific use for threatening people during the Great Train Robbery;

    Properties:
        -
    Examples:
        - Tony Gill’s Ford Mustang (E22) had as general use transportation (E55)
    In First Order Logic:
        P101(x,y) ⊃ E70(x)
        P101(x,y) ⊃ E55(y)
        P101(x,y) ⊃ (∃z)[E7(z) ∧ P16(z,x) ∧ P2(z,y)]

    """

    p101_had_a_general_use: Optional[List[E55Type]] = Field(
        default=None,
        description='P101 had as general use (was use of)'
    )


# ******************************************************************************************************************* #


class P109HasCurrentOrFormerCurator(PropertyMixin):
    """'P109 has current or former curator (is current or former curator of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P109

    Domain:
        E78 Curated Holding
    Range:
        E39 Actor
    SubProperty Of:
        E18 Physical Thing. P49 has former or current keeper (is former or current keeper of): E39 Actor
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property identifies the instance of E39 Actor who assumed or have assumed overall curatorial
        responsibility for an instance of E78 Curated Holding;

        It does not allow a history of curation to be recorded. This would require use of an event initiating
        a curator being responsible for a collection;

    Properties:
        -
    Examples:
        - the Robert Opie Collection (E78) has current or former curator Robert Opie (E39)
        - the Mikael Heggelund Foslie’s coralline red algae Herbarium (E78) has current or former curator
          Mikael Heggelund Foslie
    In First Order Logic:
        P109(x,y) ⊃ E78(x)
        P109(x,y) ⊃ E39(y)
        P109(x,y) ⊃ P49(x,y)

    """

    p109_has_current_or_former_curator: List[E39Actor] = Field(
        default=None,
        description='P109 has current or former curator (is current or former curator of)'
    )


# ******************************************************************************************************************* #


class P103WasIntendedFor(PropertyMixin):
    """'P103 was intended for (was intention of)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P103

    Domain:
        E71 Human-Made Thing
    Range:
        E55 Type
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property links an instance of E71 Human-Made Thing to an instance of E55 Type describing its intended
        usage;

        It creates a relation between specific human-made things, both physical and immaterial, to types of intended
        methods and techniques of use. Note: A link between specific human-made things and a specific use activity
        should be expressed using P19 was intended use of (was made for);

    Properties:
        -
    Examples:
        - this plate (E22) was intended for being destroyed at wedding reception (E55)
    In First Order Logic:
        P103(x,y) ⊃ E71(x)
        P103(x,y) ⊃ E55(y)

    """

    p103_was_intended_for: Optional[List[E55Type]] = Field(
        default=None,
        description='P103 was intended for (was intention of)'
    )


# ******************************************************************************************************************* #


class P128Carries(PropertyMixin):
    """'P128 carries (is carried by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P128

    Domain:
        E18 Physical Thing
    Range:
        E90 Symbolic Object
    SubProperty Of:
        E70 Thing. P130 shows features of (features are also found on): E70 Thing
    SuperProperty Of:
        E24 Physical Human-Made Thing. P65 shows visual item (is shown by): E36 Visual Item
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance E90 Symbolic Object carried by an instance of E18 Physical Thing. Since
        an instance of E90 Symbolic Object is defined as an immaterial idealization over potentially multiple
        carriers, any individual realization on a particular physical carrier may be defective, due to deterioration
        or shortcomings in the process of creating the realization compared to the intended ideal. As long as such
        defects do not substantially affect the complete recognition of the respective symbolic object, it is still
        regarded as carrying an instance of this E90 Symbolic Object. If these defects are of scholarly interest, the
        particular realization can be modelled as an instance of E25 Human-Made Feature. Note, that any instance of
        E90 Symbolic Object incorporated (P165) in the carried symbolic object is also carried by the same instance
        of E18 Physical Thing;

    Properties:
        -
    Examples:
        - Matthew’s paperback copy of Reach for the Sky (E18) carries the text of Reach for the Sky (E73)
    In First Order Logic:
        P128(x,y) ⊃ E18(x)
        P128(x,y) ⊃ E90(y)
        P128(x,y) ⊃ P130(x,y)

    """

    p128_carries: Optional[List[E90SymbolicObject]] = Field(default=None, description='P128 carries (is carried by)')


# ******************************************************************************************************************* #


class P130ShowsFeaturesOf(PropertyMixin):
    """'P130 shows features of (features are also found on)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P130

    Domain:
        E70 Thing
    Range:
        E70 Thing
    SubProperty Of:
        -
    SuperProperty Of:
        E18 Physical Thing. P128 carries (is carried by): E90 Symbolic Object
        E33 Linguistic Object. P73i is translation of (has translation): E33 Linguistic Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property generalises the notions of "copy of" and "similar to" into a directed relationship, where the
        domain expresses the derivative or influenced item and the range the source or influencing item, if such
        a direction can be established. The property can also be used to express similarity in cases that can be
        stated between two objects only, without historical knowledge about its reasons. The property expresses
        a symmetric relationship in case no direction of influence can be established either from evidence on the
        item itself or from historical knowledge. This holds in particular for siblings of a derivation process from
        a common source or non-causal cultural parallels, such as some weaving patterns;

        The P130.1 kind of similarity property of the P130 shows features of (features are also found on) property
        enables the relationship between the domain and the range to be further clarified, in the sense from domain
        to range, if applicable. For example, it may be expressed if both items are product “of the same mould”, or
        if two texts “contain identical paragraphs”;

        If the reason for similarity is a sort of derivation process, i.e., that the creator has used or had in mind
        the form of a particular thing during the creation or production, this process should be explicitly
        modelled. In these cases, P130 shows features of can be regarded as a shortcut of such a process. However,
        the current model does not contain any path specific enough to infer this property. Specializations of
        the CIDOC CRM may however be more explicit, for instance describing the use of moulds etc.;

        This property is not transitive;

    Properties:
        P130.1 kind of similarity: E55 Type
    Examples:
        - Mary Lamb’s Cymbeline [from Charles and Mary Lamb’s Tales from Shakespeare] shows features of William
          Shakespeare’s Cymbeline
        - The audio recording of Dante Alighieri's La divina commedia read by Enrico de Negri shows features of the
          text of Dante Alighieri's La divina commedia
    In First Order Logic:
        P130 (x,y) ⊃ E70(x)
        P130 (x,y) ⊃ E70(y)
        P130(x,y,z) ⊃ [P130(x,y) ∧ E55(z)]

    """

    p130_shows_features_of: Optional[List[E70Thing]] = Field(
        default=None,
        description='P130 shows features of (features are also found on)'
    )


# ******************************************************************************************************************* #


class P156Occupies(PropertyMixin):
    """'P156 occupies (is occupied by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P156

    Domain:
        E18 Physical Thing
    Range:
        E53 Place
    SubProperty Of:
        E18 Physical Thing. P53 has former or current location (is former or current location of): E53 Place
        E18 Physical Thing. P157i provides reference space for (is at rest relative to): E53 Place
    SuperProperty Of:
        -
    Quantification:
        one to one (0,1:1,1)

    Scope Note:
        This property describes the largest volume in space, an instance of E53 Place, that an instance of
        E18 Physical Thing has occupied at any time during its existence, with respect to the reference space relative
        to the physical thing itself. This allows for describing the thing itself as a place that may contain other
        things, such as a box that may contain coins. In other words, it is the volume that contains all the points
        which the thing has covered at some time during its existence. The reference space for the associated place
        must be the one that is permanently at rest (P157 is at rest relative to) relative to the physical thing. For
        instances of E19 Physical Objects it is the one which is at rest relative to the object itself, i.e. which
        moves together with the object. For instances of E26 Physical Feature it is one which is at rest relative to
        the physical feature itself and the surrounding matter immediately connected to it. Therefore there is
        a 1:1 relation between the instance E18 Physical Thing and the instance of E53 Place it occupies. We include
        in the occupied space the space filled by the matter of the physical thing and all its inner spaces;

        This property implies the fully developed path from E18 Physical Thing through P196 defines,
        E92 Spacetime Volume, P161 has spatial projection, E53 Place. However, in contrast to P156 occupies, the
        property P161 has spatial projection does not constrain the reference space of the referred instance
        of E53 Place;

        In contrast to P156 occupies, for the property P53 has former or current location the following holds:

        It does not constrain the reference space of the referred instance of E53 Place;

        It identifies a possibly wider instance of E53 Place at which a thing is or has been for some unspecified
        time span;

        If the reference space of the referred instance of E53 Place is not at rest with respect to the physical thing
        found there, the physical thing may move away after some time to another place and/or may have been at some
        other place before. The same holds for the fully developed path from E18 Physical Thing through P196 defines,
        E92 Spacetime Volume, P161 has spatial projection, E53 Place;

    Properties:
        -
    Examples:
        - The Saint Titus reliquary occupies the space of the Saint Titus reliquary [the reliquary is currently kept
          in the Saint Titus Church in Heraklion, Crete since 1966 and contains the skull of Saint Titus]
    In First Order Logic:
        P156(x,y) ⊃ E53(y)
        P156(x,y) ⊃ E18(x)
        P156 (x,y) = [E18(x) ∧ E53(y) ∧ P196(x,z) ∧ P161(z,y) ∧ P157(y,x)]

    """

    p156_occupies: Optional[E53Place] = Field(default=None, description='P156 occupies (is occupied by)')


# ******************************************************************************************************************* #


class P196Defines(PropertyMixin):
    """'P196 defines (is defined by)' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#P196

    Domain:
        E18 Physical Thing
    Range:
        E92 Spacetime Volume
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        one to one, necessary (1,1:0,1)

    Scope Note:
        This property associates an instance of E18 Physical Thing with the instance of E92 Spacetime Volume that
        constitutes the complete trajectory of its geometric extent through spacetime for the whole time of the
        existence of the instance of E18 Physical Thing;

        An instance of E18 Physical Thing not only occupies a particular geometric space at each instant of its
        existence, but in the course of its existence it also forms a trajectory through spacetime, which occupies
        a real, that is phenomenal, volume in spacetime, i.e., the instance of E92 Spacetime Volume this property
        associates it with. This real spatiotemporal extent of the instance of E18 Physical Thing is regarded as being
        unique, in all its details and fuzziness; the identity and existence of the E92 Spacetime Volume depends
        uniquely on the identity of the instance of E18 Physical Thing, whose existence defines it. It constitutes
        a phenomenal spacetime volume as defined in CRMgeo (Doerr and Hiebel 2013);

        Included in this spacetime volume are both the spaces filled by the matter of the physical thing and any inner
        space that may exist, for instance the interior of a box. Physical things consisting of aggregations of
        physically unconnected objects, such as a set of chessmen, occupy a finite number of individually contiguous
        subsets of this spacetime volume equal to the number of objects that constitute the set and that are never
        connected during its existence;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        P196(x,y) ⊃ E18(x)
        P196(x,y) ⊃ E92(y)

    """

    p196_defines: E92SpaceTimeVolume = Field(default=None, description='P196 defines (is defined by)')


# ******************************************************************************************************************* #


class PxxxHoldsOrSupports(PropertyMixin):
    """'Pxxx holds or supports' CRM property;

    https://cidoc-crm.org/html/cidoc_crm_v7.0.html#Pxxx

    Domain:
        E18 Physical Thing
    Range:
        E18 Physical Thing
    SubProperty Of:
        -
    SuperProperty Of:
        E19 Physical Object. P56 bears feature (is found on): E26 Physical Feature
    Quantification:
        many to many

    Scope Note:
        This property relates one instance of E18 Physical Thing which acts as a container or support, such as
        a shelf, for another instance of E18 Physical Thing. Pxxx holds or supports is a shortcut of the more fully
        developed path from the domain E18 Physical Thing through P59 has section, E53 Place, P53i is former or
        current location of, to the range E18 Physical Thing. It is not a sub-property of P46 is composed of, as
        the held or supported object is not a component of the container or support;

        This property can be used to avoid explicitly instantiating the E53 Place which is defined by an instance of
        E18 Physical Thing, especially when the only intended use of that instance of E18 Physical Thing is to act
        as a container or surface for the storage of other instances of E18 Physical Thing. The place’s existence is
        defined by the existence of the container or surface, and will go out of existence at the same time as the
        Destruction of the container or surface. As such, there are very few situations in which the identity of
        the place needs to be distinguished from the defining physical thing;

    Properties:
        -
    Examples:
        - The archival folder (E22) “6” _holds or supports_ the piece of paper (E22) carrying the text of a letter
          from Alloway to Sleigh
        - The artist’s materials box (E22) labeled “VG6” _holds or supports_ Van Gogh’s paintbrush 23 (E22)
        - The storage box “VG” (E22) _holds or supports_ the artist’s materials box (E22) labeled “VG6”
        - The bronze coin bank “72.AC.99” (E22) _holds or supports_ silver coin “72.AC.99-1” (E22)
        - The bookshelf “GRI-708.1” (E22) _holds or supports_ the book (E22) “Catalog of Paintings in
          the J. Paul Getty Museum”
    In First Order Logic:
        -

    """

    p198_holds_or_supports: Optional[List[E18PhysicalThing]] = Field(
        default=None,
        description='Pxxx holds or supports'
    )
