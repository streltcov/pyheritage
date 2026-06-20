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
    from pyheritage.cidoc.core.entities import E18PhysicalThing
    from pyheritage.cidoc.crmdig.entities import (
        D1DigitalObject,
        D8DigitalDevice,
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
