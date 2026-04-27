# -*- coding: utf-8 -*-

"""Dublin Core elements - all 15 DC elements;

"""


from pyheritage.dc.base import dc_element, DCEntityBase


__all__ = (
    'DCCoverage', 'DCCreator', 'DContributor', 'DDescription', 'DCFormat',
    'DCIdentifier', 'DCLanguage', 'DCRelation', 'DCRights', 'DCSource',
    'DCTitle', 'DCTType', 'DCDate', 'DPublisher', 'DSubject',
)


@dc_element(label="dc:title")
class DCTitle(DCEntityBase):
    """A name given to the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/title/

    Typically, Title will be a name by which the resource is formally known;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:subject")
class DSubject(DCEntityBase):
    """A topic of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/subject/

    Typically, Subject will be expressed as keywords, key phrases, or classification codes
    that describe the topic of the resource;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:description")
class DDescription(DCEntityBase):
    """An account of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/description/

    Description may include but is not limited to: an abstract, table of contents, reference description,
    or free-text account of the resource;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:publisher")
class DPublisher(DCEntityBase):
    """An entity responsible for making the resource available;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/publisher/

    Examples of Publisher include a person, an organization, or a service;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:creator")
class DCCreator(DCEntityBase):
    """An entity primarily responsible for making the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/creator/

    Examples of Creator include a person, an organization, or a service;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:contributor")
class DContributor(DCEntityBase):
    """An entity responsible for making contributions to the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/contributor/

    Examples of Contributor include a person, an organization, or a service;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:date")
class DCDate(DCEntityBase):
    """A date of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/date/

    Date may be used to express dates, date-time, or other temporal data;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:type")
class DCTType(DCEntityBase):
    """The nature or genre of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/type/

    Recommended practice is to use a controlled vocabulary. For example, values from the DCMI Type Vocabulary;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:format")
class DCFormat(DCEntityBase):
    """The file format, physical medium, or dimensions of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/format/

    Examples of Format include the file extension (e.g., "pdf"), or mime type (e.g., "application/pdf");

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:identifier")
class DCIdentifier(DCEntityBase):
    """An unambiguous reference to the resource within a given context;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/identifier/

    Recommended practice is to identify the resource by means of a string conforming to a formal
    identification system;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:source")
class DCSource(DCEntityBase):
    """A related resource from which the described resource is derived;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/source/

    The described resource may be derived from the related resource in whole or in part;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:language")
class DCLanguage(DCEntityBase):
    """A language of the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/language/

    Recommended practice is to use a controlled vocabulary such as RFC 4646;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:relation")
class DCRelation(DCEntityBase):
    """A related resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/relation/

    Recommended practice is to identify the related resource by means of a string conforming
    to a formal identification system;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:coverage")
class DCCoverage(DCEntityBase):
    """The spatial or temporal topic of the resource, the spatial applicability of the resource,
    or the jurisdiction under which the resource is relevant;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/coverage/

    Spatial topic, spatial applicability, or temporal may be a named place, a location, or other
    geographic feature;

    """

    value: str


# ******************************************************************************************************************* #


@dc_element(label="dc:rights")
class DCRights(DCEntityBase):
    """Information about rights held in and over the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/rights/

    Typically, Rights contains intellectual property rights statements;

    """

    value: str
