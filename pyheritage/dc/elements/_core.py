# -*- coding: utf-8 -*-

"""Dublin Core elements - title, creator;


"""


from pyheritage.dc.base import dc_element, DCEntityBase


__all__ = ('DCTitle', 'DCCreator', )


@dc_element(label="dc:title")
class DCTitle(DCEntityBase):
    """A name given to the resource;

    https://www.dublincore.org/specifications/dublin-core/dcmi-element-terms/elements/dc/title/

    Typically, Title will be a name by which the resource is formally known;

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
