# -*- coding: utf-8 -*-

"""CRMsci entity models;

CRMsci v2.0

Entities
--------
S10 Material Substantial
S15 Observable Entity

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core.entities import E1CRMEntity, E70Thing


__all__ = ('S10MaterialSubstantial', 'S15ObservableEntity', )


@entity_register(label='S15 Observable Entity')
class S15ObservableEntity(E1CRMEntity, ABC):
    """'S15 Observable Entity' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S15

    SubClass Of:
        E1 CRM Entity

    SuperClass Of:
        E5 Event
        S10 Material Substantial

    Scope Note:
        This class comprises instances of E5 Event or S10 Material Substantial (i.e. items or phenomena,
        such as physical things, their behaviour, states and interactions or events), that can be observed
        by measurement or detection devices or by human sensory impression including when enhanced by tools.

        In order to be observable, instances of E5 Event must consist of some interaction or action of
        material substance. In some cases, the spatiotemporal confinement of the event itself, such as a flash,
        a car stopping etc. marks the limits of a documented observation of an event. In other cases, such as
        the situation of a car passing by a certain object, the spatiotemporal limits of the event of observing
        itself, as well as the direction of attention or the orientation of used instruments, may constrain the
        observed detail of a larger process, e.g., noticing the sight of a car passing by; a light emission, etc.

        Conceptual objects manifest through their carriers such as books, digital media, or even human memory.
        Attributes of conceptual objects, such as number of words, can be observed on their carriers. If the
        respective properties between carriers differ, either they carry different instances of conceptual objects
        or the difference can be attributed to accidental deficiencies in one of the carriers. In that sense even
        immaterial objects are observable. By this model we address the fact that frequently, the actually
        observed carriers of conceptual objects are not explicitly identified in documentation, i.e., they are
        assumed to have existed but they are unknown as individuals.

    Examples:
        - the domestic goose from Guangdong/1/1996 (H5N1) that was identified in 1996 in farmed geese in
          southern China as circulating highly pathogenic H5N1 (E20)
        - the flight of a male Bearded Vulture observed near Loukia, Heraklion, Crete in the morning of the
          24th of October 2020 (E5)
        - the eruption of Krakatoa volcano at Indonesia in 1883 (E5)
        - the cupid head area in the X-Ray of the painting 'Cupid complaining to Venus' (E25)

    In First Order Logic:
        S15(x) ⇒ E1(x)

    Properties:
        O12 has dimension (is dimension of): E54 Dimension

    """


# ******************************************************************************************************************* #


@entity_register(label='S10 Material Substantial')
class S10MaterialSubstantial(E70Thing, S15ObservableEntity):
    """'S10 Material Substantial' CRMsci entity;

    https://cidoc-crm.org/extensions/crmsci/html/CRMsci_v2.0.html#S10

    SubClass Of:
        E70 Thing
        S15 Observable Entity

    SuperClass Of:
        S14 Fluid Body
        S11 Amount of Matter
        E18 Physical Thing

    Scope Note:
        This class comprises constellations of matter with a relative stability of any form sufficient to
        associate them with a persistent identity, such as being confined to certain extent, having a relative
        stability of form or structure, or containing a fixed amount of matter. In particular, it comprises
        physical things in the narrower sense and fluid bodies. It is an abstraction of physical substance for
        solid and non-solid things of matter.

    Examples:
        - the groundwater of the 5-22 basin of Central Macedonia (S10)
        - the Mesozoic carbonate sequence with flysch extracted from the area of Nafplion that was mapped
          and studied by Tattaris in 1970 (S10)
        - Parnassos, the limestone mountain

    In First Order Logic:
        S10(x) ⇒ E70(x)

    Properties:
        O15 occupied (was occupied by): E53 Place
        O25 contains (is contained in): S10 Material Substantial

    """
