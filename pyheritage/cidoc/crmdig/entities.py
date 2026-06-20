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


from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core.entities import (
    E22HumanMadeObject,
    E65Creation,
    E73InformationObject,
    E89PropositionalObject,
)


__all__ = (
    'D1DigitalObject',
    'D8DigitalDevice',
    'D13DigitalInformationCarrier',
    'D29AnnotationObject',
    'D30AnnotationEvent',
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
