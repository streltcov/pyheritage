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
from pyheritage.cidoc.core import entities as _core_entities
from pyheritage.cidoc.core.entities import (
    E11Modification,
    E22HumanMadeObject,
    E31Document,
    E65Creation,
    E73InformationObject,
    E89PropositionalObject,
)
from pyheritage.cidoc.crmdig.properties import (
    L1Digitized,
    L2UsedAsSource,
    L10HadInput,
    L11HadOutput,
    L12HappenedOnDevice,
    L13UsedParameters,
    L14Transferred,
    L15HasSender,
    L16HasReceiver,
    L18HasModified,
    L19Stores,
    L20HasCreated,
    L21UsedAsDerivationSource,
    L22CreatedDerivative,
    L23UsedSoftwareOrFirmware,
    L24CreatedLogfile,
    L43Annotates,
    L48CreatedAnnotation,
    L49IsPrimaryAreaOf,
    L50IsPropagatedArea,
    L61ContainsValueSetOf,
)
from pyheritage.cidoc.crmsci import entities as _crmsci_entities
from pyheritage.cidoc.crmsci.entities import S21Measurement


__all__ = (
    'D1DigitalObject',
    'D2DigitizationProcess',
    'D3FormalDerivation',
    'D7DigitalMachineEvent',
    'D8DigitalDevice',
    'D9DataObject',
    'D10SoftwareExecution',
    'D11DigitalMeasurementEvent',
    'D12DataTransferEvent',
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
class D13DigitalInformationCarrier(L19Stores, E22HumanMadeObject):
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
class D29AnnotationObject(L43Annotates, E89PropositionalObject):
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
class D30AnnotationEvent(L48CreatedAnnotation, E65Creation):
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
class D35Area(L49IsPrimaryAreaOf, L50IsPropagatedArea, D1DigitalObject):
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
class D9DataObject(L61ContainsValueSetOf, D1DigitalObject, E31Document):
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
class D7DigitalMachineEvent(
    L10HadInput,
    L11HadOutput,
    L12HappenedOnDevice,
    L18HasModified,
    L23UsedSoftwareOrFirmware,
    E11Modification,
    E65Creation,
    ABC
):
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
        the creation of a new instance of D1 Digital Object on behalf of the human actor;

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
class D10SoftwareExecution(L2UsedAsSource, L13UsedParameters, L24CreatedLogfile, D7DigitalMachineEvent):
    """'D10 Software Execution' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D10

    SubClass Of:
        D7 Digital Machine Event

    SuperClass Of:
        D3 Formal Derivation

    Scope Note:
        This class comprises events by which a digital device runs a software program or a
        series of computing operations on a digital object as a single task, which is completely
        determined by its digital input, the software and the generic properties of the device;

    Examples:
        -

    In First Order Logic:
        D10(x) => D7(x)

    Properties:
        L2 used as source (was source for): D1 Digital Object
        L13 used parameters (parameters for): D1 Digital Object
        L24 created logfile (was logfile created by): D1 Digital Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D11 Digital Measurement Event')
class D11DigitalMeasurementEvent(L20HasCreated, D7DigitalMachineEvent, S21Measurement):
    """'D11 Digital Measurement Event' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D11

    SubClass Of:
        D7 Digital Machine Event
        S21 Measurement

    SuperClass Of:
        D2 Digitization Process

    Scope Note:
        This class comprises actions measuring physical properties using a digital device, that
        are determined by a systematic procedure and creates an instance of D9 Data Object,
        which is stored on an instance of D13 Digital Information Carrier;

    Examples:
        -

    In First Order Logic:
        D11(x) => D7(x)
        D11(x) => S21(x)

    Properties:
        L20 has created (was created by): D9 Data Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D12 Data Transfer Event')
class D12DataTransferEvent(L14Transferred, L15HasSender, L16HasReceiver, D7DigitalMachineEvent):
    """'D12 Data Transfer Event' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D12

    SubClass Of:
        D7 Digital Machine Event

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises events that transfer a digital object from one digital carrier to
        another. Normally, the digital object remains the same;

    Examples:
        -

    In First Order Logic:
        D12(x) => D7(x)

    Properties:
        L14 transferred (was transferred by): D1 Digital Object
        L15 has sender (was sender for): D8 Digital Device
        L16 has receiver (was receiver of): D8 Digital Device

    """


# ******************************************************************************************************************* #


@entity_register(label='D3 Formal Derivation')
class D3FormalDerivation(L21UsedAsDerivationSource, L22CreatedDerivative, D10SoftwareExecution):
    """'D3 Formal Derivation' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D3

    SubClass Of:
        D10 Software Execution

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises events that result in the creation of a D1 Digital Object from
        another one following a deterministic algorithm, such that the resulting instance of
        digital object shares representative properties with the original object;

    Examples:
        -

    In First Order Logic:
        D3(x) => D10(x)

    Properties:
        L21 used as derivation source (was derivation source for): D1 Digital Object
        L22 created derivative (was derivative created by): D1 Digital Object

    """


# ******************************************************************************************************************* #


@entity_register(label='D2 Digitization Process')
class D2DigitizationProcess(L1Digitized, D11DigitalMeasurementEvent):
    """'D2 Digitization Process' CRMDig entity;

    https://cidoc-crm.org/extensions/crmdig/html/CRMdig_v5.0.html#D2

    SubClass Of:
        D11 Digital Measurement Event

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises events that result in the creation of instances of D9 Data Object
        that represent the appearance, form or recorded inner structure of an instance of E18
        Physical Thing such as paper documents, statues, buildings, paintings, biological
        objects etc.;

    Examples:
        -

    In First Order Logic:
        D2(x) => D11(x)

    Properties:
        L1 digitized (was digitized by): E18 Physical Thing

    """


# ******************************************************************************************************************* #


__crmdig_namespace__ = {
    'D10SoftwareExecution': D10SoftwareExecution,
    'D11DigitalMeasurementEvent': D11DigitalMeasurementEvent,
    'D12DataTransferEvent': D12DataTransferEvent,
    'D13DigitalInformationCarrier': D13DigitalInformationCarrier,
    'D14Software': D14Software,
    'D1DigitalObject': D1DigitalObject,
    'D2DigitizationProcess': D2DigitizationProcess,
    'D29AnnotationObject': D29AnnotationObject,
    'D30AnnotationEvent': D30AnnotationEvent,
    'D35Area': D35Area,
    'D3FormalDerivation': D3FormalDerivation,
    'D7DigitalMachineEvent': D7DigitalMachineEvent,
    'D8DigitalDevice': D8DigitalDevice,
    'D9DataObject': D9DataObject,
}

__namespace__ = {
    **_core_entities.__namespace__,
    **_crmsci_entities.__crmsci_namespace__,
    **__crmdig_namespace__,
}


# ******************************************************************************************************************* #


D10SoftwareExecution.model_rebuild(_types_namespace=__namespace__)
D11DigitalMeasurementEvent.model_rebuild(_types_namespace=__namespace__)
D12DataTransferEvent.model_rebuild(_types_namespace=__namespace__)
D13DigitalInformationCarrier.model_rebuild(_types_namespace=__namespace__)
D14Software.model_rebuild(_types_namespace=__namespace__)
D1DigitalObject.model_rebuild(_types_namespace=__namespace__)
D2DigitizationProcess.model_rebuild(_types_namespace=__namespace__)
D29AnnotationObject.model_rebuild(_types_namespace=__namespace__)
D30AnnotationEvent.model_rebuild(_types_namespace=__namespace__)
D35Area.model_rebuild(_types_namespace=__namespace__)
D3FormalDerivation.model_rebuild(_types_namespace=__namespace__)
D7DigitalMachineEvent.model_rebuild(_types_namespace=__namespace__)
D8DigitalDevice.model_rebuild(_types_namespace=__namespace__)
D9DataObject.model_rebuild(_types_namespace=__namespace__)
