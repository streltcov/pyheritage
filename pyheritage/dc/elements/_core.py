# -*- coding: utf-8 -*-

"""Dublin Core elements - title, creator, subject, description, publisher,
contributor, date, type, format, identifier;


"""


from pyheritage.dc.base import dc_element, DCEntityBase


__all__ = (
    'DCCreator', 'DContributor', 'DDescription', 'DCFormat', 'DCIdentifier',
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
