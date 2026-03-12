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
P128 carries                        E18 -> E90
P130 shows features of              E70 -> E70
P156 occupies                       E18 -> E53
P196 defines                        E18 -> E92
P198 holds or supports              E18 -> E18

"""


from typing import Optional

from pydantic import Field

from pyheritage.cidoc.core.base import PropertyMixin


__all__ = ('P43HasDimension', 'P44HasCondition', 'P45ConsistsOf', 'P46IsComposedOf', 'P49HasFormerOrCurrentKeeper',
           'P50HasCurrentKeeper', 'P51HasCurrentOrFormerOwner', 'P52HasCurrentOwner', 'P53HasFormerOrCurrentLocation',
           'P54HasCurrentPermanentLocation', 'P55HasCurrentLocation', 'P56BearsFeature', 'P57HasNumberOfParts',
           'P59HasSection',)


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

    p43_has_dimension: Optional[str] = Field(default=None, description='P43 has dimension (is dimension of)')


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

    p44_has_condition: Optional[str] = Field(default=None, description='P44 has condition (is condition of)')


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

    p45_consists_of: Optional[str] = Field(default=None, description='P45 consists of (is incorporated in)')


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

    p46_is_composed_of: Optional[str] = Field(default=None, description='P46 is composed of (forms part of)')


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

    p49_has_former_or_current_keeper: Optional[str] = Field(
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

    p50_has_current_keeper: Optional[str] = Field(
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

    p51_has_current_or_former_owner: Optional[str] = Field(
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

    p52_has_current_owner: Optional[str] = Field(
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

    p53_has_former_or_current_location: Optional[str] = Field(
        default=None,
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

    p54_has_current_permanent_location: Optional[str] = Field(
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

    p55_has_current_location: Optional[str] = Field(
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

    p56_bears_feature: Optional[str] = Field(default=None, description='P56 bears feature (is found on)')


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

    p57_has_number_of_parts: Optional[str] = Field(default=None, description='P57 has number of parts')


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

    p59_has_section: Optional[str] = Field(default=None, description='P59 has section (is located on or within)')
