# -*- coding: utf-8 -*-

"""CRMDig entity models;

CRMDig v5.0

Entities
--------
D1 Digital Object
D2 Digitization Process
D3 Formal Derivation
D7 Digital Machine Event
D8 Digital Device
D9 Data Object
D10 Software Execution
D11 Digital Measurement Event
D12 Data Transfer Event
D13 Digital Information Carrier
D14 Software
D29 Annotation Object
D30 Annotation Event
D35 Area

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core.entities import (
    E22HumanMadeObject,
    E31Document,
    E65Creation,
    E73InformationObject,
    E89PropositionalObject,
)


__all__ = (
    'D1DigitalObject',
    'D7DigitalMachineEvent',
    'D8DigitalDevice',
    'D9DataObject',
    'D10SoftwareExecution',
    'D13DigitalInformationCarrier',
    'D14Software',
    'D29AnnotationObject',
    'D30AnnotationEvent',
    'D35Area',
)


@entity_register(label='D8 Digital Device')
class D8DigitalDevice(E22HumanMadeObject):
    """'D8 Digital Device' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D8

    SubClass Of:
        E22 Human-Made Object

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises identifiable material items such as computers, scanners, cameras,
        etc. that have the capability to process or produce instances of D1 Digital Object;

    Examples:
        -

    In First Order Logic:
        D8(x) => E22(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='D13 Digital Information Carrier')
class D13DigitalInformationCarrier(E22HumanMadeObject):
    """'D13 Digital Information Carrier' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D13

    SubClass Of:
        E22 Human-Made Object

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises all instances of E84 Information Carrier that are explicitly
        designed to be used as persistent digital physical carriers of instances of D1 Digital
        Object. An instance of D13 Digital Information Carrier may or may not contain
        information, e.g., an empty diskette;

    Examples:
        -

    In First Order Logic:
        D13(x) => E22(x)

    Properties:
        L19 stores (is stored on): D1 Digital Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D29 Annotation Object')
class D29AnnotationObject(E89PropositionalObject):
    """'D29 Annotation Object' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D29

    SubClass Of:
        E89 Propositional Object

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises objects that make propositions about other artefacts. Instances of
        this class are not the attributes themselves, by which things are annotated, but
        represent the connection between the concepts related in a proposition, and the
        activities of creation, modification and deletion;

    Examples:
        -

    In First Order Logic:
        D29(x) => E89(x)

    Properties:
        L43 annotates (is annotated by): E1 CRM Entity

    """


# ******************************************************************************************************************* #


@entity_register(label='D30 Annotation Event')
class D30AnnotationEvent(E65Creation):
    """'D30 Annotation Event' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D30

    SubClass Of:
        E65 Creation

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of creating an annotation in the form of an instance of
        D29 Annotation Object. These activities typically constitute characteristic parts in
        scholarly and scientific workflows and processes, often in a dialogue or exchange of
        opinions between experts;

    Examples:
        -

    In First Order Logic:
        D30(x) => E65(x)

    Properties:
        L48 created annotation (was annotation created by): D29 Annotation Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D1 Digital Object')
class D1DigitalObject(E73InformationObject):
    """'D1 Digital Object' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D1

    SubClass Of:
        E73 Information Object

    SuperClass Of:
        D9 Data Object
        D14 Software
        D35 Area

    Scope Note:
        This class comprises identifiable immaterial items that can be represented as sets of
        bit sequences, such as data sets, e-texts, images, audio or video items, software, etc.,
        and are documented as single units;

    Examples:
        -

    In First Order Logic:
        D1(x) => E73(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='D14 Software')
class D14Software(D1DigitalObject):
    """'D14 Software' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D14

    SubClass Of:
        D1 Digital Object

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises software codes, computer programs, procedures and functions that
        are used to operate a system of digital objects;

    Examples:
        -

    In First Order Logic:
        D14(x) => D1(x)

    Properties:
        (none)

    """


# ******************************************************************************************************************* #


@entity_register(label='D35 Area')
class D35Area(D1DigitalObject):
    """'D35 Area' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D35

    SubClass Of:
        D1 Digital Object

    SuperClass Of:
        (none)

    Scope Note:
        This class describes a part (of any shape or size) of interest in basically any media
        object stored in the Object Repository, i.e., a text, an image, a video or a 3D model.
        It points to content consisting of just a portion or area of a file;

    Examples:
        -

    In First Order Logic:
        D35(x) => D1(x)

    Properties:
        L49 is primary area of (has primary area): D1 Digital Object
        L50 is propagated area (has propagated area): D1 Digital Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D9 Data Object')
class D9DataObject(E31Document):
    """'D9 Data Object' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D9

    SubClass Of:
        D1 Digital Object
        E31 Document

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of D1 Digital Object that are the result of measurements
        or other observations and/or their algorithmic evaluation in the form of structured data,
        such as encoded formal propositions, CSV files or equivalent representations;

    Examples:
        -

    In First Order Logic:
        D9(x) => D1(x)
        D9(x) => E31(x)

    Properties:
        L61 contains value set of (has value set representation): E54 Dimension

    """


# ******************************************************************************************************************* #


@entity_register(label='D7 Digital Machine Event')
class D7DigitalMachineEvent(E65Creation, ABC):
    """'D7 Digital Machine Event' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D7

    SubClass Of:
        E11 Modification
        E65 Creation

    SuperClass Of:
        D10 Software Execution
        D11 Digital Measurement Event
        D12 Data Transfer Event

    Scope Note:
        This class comprises events that happen on physical digital devices following a human
        activity that intentionally caused its immediate or delayed initiation and results in
        the creation of a new instance of D1 Digital Object on behalf of the human actor.

    Examples:
        -

    In First Order Logic:
        D7(x) => E11(x)
        D7(x) => E65(x)

    Properties:
        L10 had input (was input of): D1 Digital Object
        L11 had output (was output of): D1 Digital Object
        L12 happened on device (was device for): D8 Digital Device
        L18 has modified (was modified by): D13 Digital Information Carrier
        L23 used software or firmware (was software or firmware used by): D14 Software

    """


# ******************************************************************************************************************* #


@entity_register(label='D10 Software Execution')
class D10SoftwareExecution(D7DigitalMachineEvent):
    """'D10 Software Execution' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D10

    SubClass Of:
        D7 Digital Machine Event

    SuperClass Of:
        D3 Formal Derivation

    Scope Note:
        This class comprises events by which a digital device runs a software program or a
        series of computing operations on a digital object as a single task, which is completely
        determined by its digital input, the software and the generic properties of the device.

    Examples:
        -

    In First Order Logic:
        D10(x) => D7(x)

    Properties:
        L2 used as source (was source for): D1 Digital Object
        L13 used parameters (parameters for): D1 Digital Object
        L24 created logfile (was logfile created by): D1 Digital Object

    """
