# -*- coding: utf-8 -*-

"""CRMDig property models;

(Mixin classes for entity models);

CRMDig v5.0

------------------------------------------------
Properties
------------------------------------------------
L1  digitized                          D2  -> E18
L2  used as source                     D10 -> D1
L10 had input                          D7  -> D1
L11 had output                         D7  -> D1
L12 happened on device                 D7  -> D8
L13 used parameters                    D10 -> D1
L14 transferred                        D12 -> D1
L15 has sender                         D12 -> D8
L16 has receiver                       D12 -> D8
L18 has modified                       D7  -> D13
L19 stores                             D13 -> D1
L20 has created                        D11 -> D9
L21 used as derivation source          D3  -> D1
L22 created derivative                 D3  -> D1
L23 used software or firmware          D7  -> D14
L24 created logfile                    D10 -> D1
L43 annotates                          D29 -> E1
L48 created annotation                 D30 -> D29
L49 is primary area of                 D35 -> D1
L50 is propagated area                 D35 -> D1
L54 is same as                         E1  -> E1
L61 contains value set of              D9  -> E54

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import (
        E1CRMEntity,
        E18PhysicalThing,
        E54Dimension,
    )
    from pyheritage.cidoc.crmdig.entities import (
        D1DigitalObject,
        D8DigitalDevice,
        D9DataObject,
        D13DigitalInformationCarrier,
        D14Software,
        D29AnnotationObject,
    )


__all__ = (
    'L1Digitized',
    'L2UsedAsSource',
    'L10HadInput',
    'L11HadOutput',
    'L12HappenedOnDevice',
    'L13UsedParameters',
    'L14Transferred',
    'L15HasSender',
    'L16HasReceiver',
    'L18HasModified',
    'L19Stores',
    'L20HasCreated',
    'L21UsedAsDerivationSource',
    'L22CreatedDerivative',
    'L23UsedSoftwareOrFirmware',
    'L24CreatedLogfile',
    'L43Annotates',
    'L48CreatedAnnotation',
    'L49IsPrimaryAreaOf',
    'L50IsPropagatedArea',
    'L54IsSameAs',
    'L61ContainsValueSetOf',
)


class L1Digitized(PropertyMixin):
    """'L1 digitized (was digitized by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L1

    Domain:
        D2 Digitization Process
    Range:
        E18 Physical Thing
    SubProperty Of:
        S21 Measurement. O24 measured (was measured by): S15 Observable Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D2 Digitization Process with an instance
        of E18 Physical Thing which is a material thing;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L1(x,y) => D2(x)
        L1(x,y) => E18(y)
        L1(x,y) => O24(x,y)

    """

    l1_digitized: List[E18PhysicalThing] = Field(
        default=None,
        description='L1 digitized (was digitized by)',
    )


# ******************************************************************************************************************* #


class L2UsedAsSource(PropertyMixin):
    """'L2 used as source (was source for)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L2

    Domain:
        D10 Software Execution
    Range:
        D1 Digital Object
    SubProperty Of:
        D7 Digital Machine Event. L10 had input (was input of): D1 Digital Object
    SuperProperty Of:
        D3 Formal Derivation. L21 used as derivation source (was derivation source for):
        D1 Digital Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D10 Software Execution with an instance
        of D1 Digital Object which is used as a source, software essential for the
        performance;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L2(x,y) => D10(x)
        L2(x,y) => D1(y)
        L2(x,y) => L10(x,y)

    """

    l2_used_as_source: List[D1DigitalObject] = Field(
        default=None,
        description='L2 used as source (was source for)',
    )


# ******************************************************************************************************************* #


class L10HadInput(PropertyMixin):
    """'L10 had input (was input of)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L10

    Domain:
        D7 Digital Machine Event
    Range:
        D1 Digital Object
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        D10 Software Execution. L2 used as source (was source for): D1 Digital Object
        D10 Software Execution. L13 used parameters (parameters for): D1 Digital Object
        D12 Data Transfer Event. L14 transferred (was transferred by): D1 Digital Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D7 Digital Machine Event with an instance
        of D1 Digital Object which is the input used to specify the machine action;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L10(x,y) => D7(x)
        L10(x,y) => D1(y)
        L10(x,y) => P16(x,y)

    """

    l10_had_input: List[D1DigitalObject] = Field(
        default=None,
        description='L10 had input (was input of)',
    )


# ******************************************************************************************************************* #


class L11HadOutput(PropertyMixin):
    """'L11 had output (was output of)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L11

    Domain:
        D7 Digital Machine Event
    Range:
        D1 Digital Object
    SubProperty Of:
        E65 Creation. P94 has created (was created by): E28 Conceptual Object
    SuperProperty Of:
        D11 Digital Measurement Event. L20 has created (was created by): D9 Data Object
        D3 Formal Derivation. L22 created derivative (was derivative created by):
        D1 Digital Object
        D10 Software Execution. L24 created logfile (was logfile created by):
        D1 Digital Object
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D7 Digital Machine Event with an instance
        of D1 Digital Object which is the output of the activity.

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L11(x,y) => D7(x)
        L11(x,y) => D1(y)
        L11(x,y) => P94(x,y)

    """

    l11_had_output: List[D1DigitalObject] = Field(
        default=None,
        description='L11 had output (was output of)',
    )


# ******************************************************************************************************************* #


class L12HappenedOnDevice(PropertyMixin):
    """'L12 happened on device (was device for)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L12

    Domain:
        D7 Digital Machine Event
    Range:
        D8 Digital Device
    SubProperty Of:
        E5 Event. P12 occurred in the presence of (was present at): E77 Persistent Item
    SuperProperty Of:
        D12 Data Transfer Event. L15 has sender (was sender for): D8 Digital Device
        D12 Data Transfer Event. L16 has receiver (was receiver of): D8 Digital Device
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D7 Digital Machine Event with a D8 Digital
        Device which happened with, e.g. a capturing event that happened on/with a digital
        camera, etc.;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L12(x,y) => D7(x)
        L12(x,y) => D8(y)
        L12(x,y) => P12(x,y)

    """

    l12_happened_on_device: List[D8DigitalDevice] = Field(
        default=None,
        description='L12 happened on device (was device for)',
    )


# ******************************************************************************************************************* #


class L13UsedParameters(PropertyMixin):
    """'L13 used parameters (parameters for)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L13

    Domain:
        D10 Software Execution
    Range:
        D1 Digital Object
    SubProperty Of:
        D7 Digital Machine Event. L10 had input (was input of): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D10 Software Execution with an instance
        of D1 Digital Object used as a parameter during the process;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L13(x,y) => D10(x)
        L13(x,y) => D1(y)
        L13(x,y) => L10(x,y)

    """

    l13_used_parameters: List[D1DigitalObject] = Field(
        default=None,
        description='L13 used parameters (parameters for)',
    )


# ******************************************************************************************************************* #


class L14Transferred(PropertyMixin):
    """'L14 transferred (was transferred by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L14

    Domain:
        D12 Data Transfer Event
    Range:
        D1 Digital Object
    SubProperty Of:
        D7 Digital Machine Event. L10 had input (was input of): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of D1 Digital Object transferred by a D12
        Data Transfer Event;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L14(x,y) => D12(x)
        L14(x,y) => D1(y)
        L14(x,y) => L10(x,y)

    """

    l14_transferred: List[D1DigitalObject] = Field(
        default=None,
        description='L14 transferred (was transferred by)',
    )


# ******************************************************************************************************************* #


class L15HasSender(PropertyMixin):
    """'L15 has sender (was sender for)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L15

    Domain:
        D12 Data Transfer Event
    Range:
        D8 Digital Device
    SubProperty Of:
        D7 Digital Machine Event. L12 happened on device (was device for): D8 Digital Device
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of D8 Digital Device used as a medium on which
        data are transferred through a D12 Data Transfer Event;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L15(x,y) => D12(x)
        L15(x,y) => D8(y)
        L15(x,y) => L12(x,y)

    """

    l15_has_sender: List[D8DigitalDevice] = Field(
        default=None,
        description='L15 has sender (was sender for)',
    )


# ******************************************************************************************************************* #


class L16HasReceiver(PropertyMixin):
    """'L16 has receiver (was receiver of)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L16

    Domain:
        D12 Data Transfer Event
    Range:
        D8 Digital Device
    SubProperty Of:
        D7 Digital Machine Event. L12 happened on device (was device for): D8 Digital Device
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies an instance of D8 Digital Device used as a medium to receive
        data through a D12 Data Transfer Event;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L16(x,y) => D12(x)
        L16(x,y) => D8(y)
        L16(x,y) => L12(x,y)

    """

    l16_has_receiver: List[D8DigitalDevice] = Field(
        default=None,
        description='L16 has receiver (was receiver of)',
    )


# ******************************************************************************************************************* #


class L18HasModified(PropertyMixin):
    """'L18 has modified (was modified by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L18

    Domain:
        D7 Digital Machine Event
    Range:
        D13 Digital Information Carrier
    SubProperty Of:
        E11 Modification. P31 has modified (was modified by): E18 Physical Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies a D13 Digital Information Carrier modified in a D7 Digital
        Machine Event for storing its results;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L18(x,y) => D7(x)
        L18(x,y) => D13(y)
        L18(x,y) => P31(x,y)

    """

    l18_has_modified: List[D13DigitalInformationCarrier] = Field(
        default=None,
        description='L18 has modified (was modified by)',
    )


# ******************************************************************************************************************* #


class L19Stores(PropertyMixin):
    """'L19 stores (is stored on)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L19

    Domain:
        D13 Digital Information Carrier
    Range:
        D1 Digital Object
    SubProperty Of:
        E18 Physical Thing. P128 carries (is carried by): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of a D13 Digital Information Carrier with the
        instance of Digital Object that is stored on it;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L19(x,y) => D13(x)
        L19(x,y) => D1(y)
        L19(x,y) => P128(x,y)

    """

    l19_stores: List[D1DigitalObject] = Field(
        default=None,
        description='L19 stores (is stored on)',
    )


# ******************************************************************************************************************* #


class L20HasCreated(PropertyMixin):
    """'L20 has created (was created by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L20

    Domain:
        D11 Digital Measurement Event
    Range:
        D9 Data Object
    SubProperty Of:
        D7 Digital Machine Event. L11 had output (was output of): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D11 Digital Measurement Event with an
        instance of D9 Data Object that was created for storing the results, i.e.,
        observed values, of the measurement;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L20(x,y) => D11(x)
        L20(x,y) => D9(y)
        L20(x,y) => L11(x,y)

    """

    l20_has_created: List[D9DataObject] = Field(
        default=None,
        description='L20 has created (was created by)',
    )


# ******************************************************************************************************************* #


class L21UsedAsDerivationSource(PropertyMixin):
    """'L21 used as derivation source (was derivation source for)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L21

    Domain:
        D3 Formal Derivation
    Range:
        D1 Digital Object
    SubProperty Of:
        D10 Software Execution. L2 used as source (was source for): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of a D3 Formal Derivation with the instance
        of D1 Digital Object that is used as a derivation source;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L21(x,y) => D3(x)
        L21(x,y) => D1(y)
        L21(x,y) => L2(x,y)

    """

    l21_used_as_derivation_source: List[D1DigitalObject] = Field(
        default=None,
        description='L21 used as derivation source (was derivation source for)',
    )


# ******************************************************************************************************************* #


class L22CreatedDerivative(PropertyMixin):
    """'L22 created derivative (was derivative created by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L22

    Domain:
        D3 Formal Derivation
    Range:
        D1 Digital Object
    SubProperty Of:
        D7 Digital Machine Event. L11 had output (was output of): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of a D3 Formal Derivation with the instance
        of D1 Digital Object that is used to create a version of;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L22(x,y) => D3(x)
        L22(x,y) => D1(y)
        L22(x,y) => L11(x,y)

    """

    l22_created_derivative: List[D1DigitalObject] = Field(
        default=None,
        description='L22 created derivative (was derivative created by)',
    )


# ******************************************************************************************************************* #


class L23UsedSoftwareOrFirmware(PropertyMixin):
    """'L23 used software or firmware (was software or firmware used by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L23

    Domain:
        D7 Digital Machine Event
    Range:
        D14 Software
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D7 Digital Machine Event with the instance
        of D14 Software that it used;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L23(x,y) => D7(x)
        L23(x,y) => D14(y)
        L23(x,y) => P16(x,y)

    """

    l23_used_software_or_firmware: List[D14Software] = Field(
        default=None,
        description='L23 used software or firmware (was software or firmware used by)',
    )


# ******************************************************************************************************************* #


class L24CreatedLogfile(PropertyMixin):
    """'L24 created logfile (was logfile created by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L24

    Domain:
        D10 Software Execution
    Range:
        D1 Digital Object
    SubProperty Of:
        D7 Digital Machine Event. L11 had output (was output of): D1 Digital Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the logfile that was created by an instance of D10
        Software Execution in order to record all the activities in the system;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L24(x,y) => D10(x)
        L24(x,y) => D1(y)
        L24(x,y) => L11(x,y)

    """

    l24_created_logfile: List[D1DigitalObject] = Field(
        default=None,
        description='L24 created logfile (was logfile created by)',
    )


# ******************************************************************************************************************* #


class L43Annotates(PropertyMixin):
    """'L43 annotates (is annotated by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L43

    Domain:
        D29 Annotation Object
    Range:
        E1 CRM Entity
    SubProperty Of:
        E89 Propositional Object. P129 is about (is subject of): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D29 Annotation Object with a relevant
        instance of E1 CRM Entity explicitly referred to in the annotation object;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L43(x,y) => D29(x)
        L43(x,y) => E1(y)
        L43(x,y) => P129(x,y)

    """

    l43_annotates: List[E1CRMEntity] = Field(
        default=None,
        description='L43 annotates (is annotated by)',
    )


# ******************************************************************************************************************* #


class L48CreatedAnnotation(PropertyMixin):
    """'L48 created annotation (was annotation created by)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L48

    Domain:
        D30 Annotation Event
    Range:
        D29 Annotation Object
    SubProperty Of:
        E65 Creation. P94 has created (was created by): E28 Conceptual Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property identifies the D29 Annotation Object (associations) that came into
        existence as a result of a D30 Annotation Event;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L48(x,y) => D30(x)
        L48(x,y) => D29(y)
        L48(x,y) => P94(x,y)

    """

    l48_created_annotation: List[D29AnnotationObject] = Field(
        default=None,
        description='L48 created annotation (was annotation created by)',
    )


# ******************************************************************************************************************* #


class L49IsPrimaryAreaOf(PropertyMixin):
    """'L49 is primary area of (has primary area)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L49

    Domain:
        D35 Area
    Range:
        D1 Digital Object
    SubProperty Of:
        E90 Symbolic Object. P106 is composed of (forms part of): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the association between an instance of a particular D35
        Area declared in an original instance of D1 Digital Object;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L49(x,y) => D35(x)
        L49(x,y) => D1(y)
        L49(x,y) => P106(x,y)

    """

    l49_is_primary_area_of: List[D1DigitalObject] = Field(
        default=None,
        description='L49 is primary area of (has primary area)',
    )


# ******************************************************************************************************************* #


class L50IsPropagatedArea(PropertyMixin):
    """'L50 is propagated area (has propagated area)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L50

    Domain:
        D35 Area
    Range:
        D1 Digital Object
    SubProperty Of:
        E90 Symbolic Object. P106 is composed of (forms part of): E90 Symbolic Object
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes the association between an instance of D35 Area and the
        instance of D1 Digital Object to which it is propagated;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L50(x,y) => D35(x)
        L50(x,y) => D1(y)
        L50(x,y) => P106(x,y)

    """

    l50_is_propagated_area: List[D1DigitalObject] = Field(
        default=None,
        description='L50 is propagated area (has propagated area)',
    )


# ******************************************************************************************************************* #


class L54IsSameAs(PropertyMixin):
    """'L54 is same as' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L54

    Domain:
        E1 CRM Entity
    Range:
        E1 CRM Entity
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property describes a non-unique identification applied to E1 CRM Entity;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L54(x,y) => E1(x)
        L54(x,y) => E1(y)

    """

    l54_is_same_as: List[E1CRMEntity] = Field(
        default=None,
        description='L54 is same as',
    )


# ******************************************************************************************************************* #


class L61ContainsValueSetOf(PropertyMixin):
    """'L61 contains value set of (has value set representation)' CRMDig property;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#L61

    Domain:
        D9 Data Object
    Range:
        E54 Dimension
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of D9 Data Object with an instance of E54
        Dimension, in the case that the former contains the set of values of the respective
        dimension in a digital format;

    Properties:
        -
    Examples:
        -
    In First Order Logic:
        L61(x,y) => D9(x)
        L61(x,y) => E54(y)

    """

    l61_contains_value_set_of: List[E54Dimension] = Field(
        default=None,
        description='L61 contains value set of (has value set representation)',
    )
