# -*- coding: utf-8 -*-

"""CRMArchaeo entity models;

CRMArchaeo v2.0

Entities
--------
A1 Excavation Processing Unit
A2 Stratigraphic Volume Unit
A3 Stratigraphic Interface
A4 Stratigraphic Genesis
A5 Stratigraphic Modification
A6 Group Declaration Event
A7 Embedding
A8 Stratigraphic Unit
A9 Archaeological Excavation
A10 Excavation Interface

"""


from abc import ABC

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core import entities as _core_entities_module
from pyheritage.cidoc.core.entities import E12Production, E64EndOfExistence
from pyheritage.cidoc.crmsci.entities import S1MatterRemoval, S4Observation, S20RigidPhysicalFeature


__all__ = (
    'A1ExcavationProcessingUnit',
    'A2StratigraphicVolumeUnit',
    'A3StratigraphicInterface',
    'A8StratigraphicUnit',
)


@entity_register(label='A8 Stratigraphic Unit')
class A8StratigraphicUnit(S20RigidPhysicalFeature, ABC):
    """'A8 Stratigraphic Unit' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A8

    SubClass Of:
        S20 Rigid Physical Feature

    SuperClass Of:
        A2 Stratigraphic Volume Unit
        A3 Stratigraphic Interface

    Scope Note:
        This class comprises instances of S20 Rigid Physical Features which appear as the result of a
        stratigraphic genesis event or process. The form of an instance of A8 Stratigraphic Unit should be
        of a kind that can be attributed to a single genesis event or process and has the potential to be
        observed. One genesis event may have created more than one SU. An instance of A8 Stratigraphic Unit
        is regarded to exist as long as a part of its matter is still in place with respect to a surrounding
        reference space, such that its spatial features can be associated with effects of the genesis process
        of interest.

        This also implies that a certain degree of coherent ("conformal") deformation is tolerable within
        its time-span of existence. Therefore, the place an instance of A8 Stratigraphic Unit occupies can
        be uniquely identified with respect to the surrounding reference space of archaeological interest.

    Examples:
        - The excavator declared the post holes [7] and [8] in Figure 4 to be part of one building.
        - In the excavation of Akrotiri, Thera, five distinct layers (A2) of pumice create a level (A8)
          about one metre thick which covers the ruins caused by the earthquake (A4) (Fig. 9) [Doumas 2015].

    In First Order Logic:
        A8(x) ⇒ S20(x)

    Properties:
        AP11 has physical relation to (is physical relation from): A8 Stratigraphic Unit

    """


# ******************************************************************************************************************* #


@entity_register(label='A2 Stratigraphic Volume Unit')
class A2StratigraphicVolumeUnit(A8StratigraphicUnit):
    """'A2 Stratigraphic Volume Unit' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A2

    SubClass Of:
        A8 Stratigraphic Unit

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of A8 Stratigraphic Unit which are connected portions of terrain
        or other solid structures on, in, or under the surface of earth or seafloor exhibiting some
        homogeneity of structure or substance and which are completely bounded by surfaces or
        discontinuities in substance or structure with respect to other portions of the terrain or
        surfaces of objects or finds.

        Normally at least one of the surfaces, i.e. instances of A3 Stratigraphic Interface (such as
        the lower one), from the genesis event of the A2 Stratigraphic Volume Unit will remain during
        its existence.

        An instance of A2 Stratigraphic Volume Unit may contain physical objects.

    Examples:
        - The stratigraphic deposit unit number (2) of Figure 5 representing the filling of a post hole.
        - A collapsed part of the roof of the West House was found in a horizontal position on the first
          floor during the excavation of Room 3. It is made up of a number of successive layers, the
          principal ones being the thick layer "A" (A2), consisting of grey soil and small tuff stones,
          and the thinner layer "B" (A2) consisting of brownish red soil and marine pebbles (Fig. 7).
          [Μιχαηλίδου 2001, pp.64-65].

    In First Order Logic:
        A2(x) ⇒ A8(x)

    Properties:
        AP15 is or contains remains of (is or has remains contained in): S10 Material Substantial
        AP21 contains (is contained in): E18 Physical Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='A3 Stratigraphic Interface')
class A3StratigraphicInterface(A8StratigraphicUnit):
    """'A3 Stratigraphic Interface' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A3

    SubClass Of:
        A8 Stratigraphic Unit

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of A8 Stratigraphic Unit, which are coherent parts of a boundary
        surface that appear as the result of a stratigraphic genesis event or process. The interface
        marks the limit of the geometric extent of the effect of a genesis or modification event, and
        indicates in particular where the effect of this event ended. Each event of creation or
        destruction of a deposition layer implies the creation of new interfaces. Thus, there are two
        main types of interface: those that are surfaces of strata (that can be directly related to the
        corresponding stratum via the AP12 confines property), and those that are only surfaces, formed
        by the removal or destruction of existing stratifications.

    Examples:
        - The Stratigraphic Interface number [19] confines the number (2) Stratigraphic Volume Unit,
          in Figure 6.
        - The two layers A and B (A2) are separated by a stratigraphic interface (A3) (Fig.6)
          [Μιχαηλίδου 2001, pp. 64-65].

    In First Order Logic:
        A3(x) ⇒ A8(x)

    Properties:
        AP12 confines (is confined by): A2 Stratigraphic Volume Unit

    """


# ******************************************************************************************************************* #


@entity_register(label='A1 Excavation Processing Unit')
class A1ExcavationProcessingUnit(S1MatterRemoval, S4Observation, E12Production, E64EndOfExistence, ABC):
    """'A1 Excavation Processing Unit' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A1

    SubClass Of:
        S1 Matter Removal
        S4 Observation
        E12 Production
        E64 End of Existence

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities of excavating in the sense of archaeology, which are documented
        as a coherent set of actions of progressively recording and removing matter from a pre-specified
        location under specific rules. Typically, an instance of A1 Excavation Processing Unit would be
        terminated if significant discontinuities of substance or finds come to light, or if the activity
        is interrupted due to external factors, such as end of a working day. In other cases, the
        termination would be based on predefined physical specifications, such as the boundaries of a
        maximal volume of matter to be excavated in one unit of excavation.

        Depending on the methodology, an instance of A1 Excavation Processing Unit may intend to remove
        matter only within the boundaries of a particular stratigraphic unit, or it may follow a
        pre-declared spatial extent such as a trench. It may only uncover, clean or expose a structure
        or parts of it.

        The process of excavation results in the production of a set of recorded (documentation) data
        that should be sufficient to provide researchers enough information regarding the consistency
        and spatial distribution of the excavated Segment of Matter and things and features embedded
        in it. Some parts or all of the removed physical material (instances of S11 Amount of Matter)
        may be dispersed, whereas others may be kept in custody in the form of finds or samples, while
        others (such as parts of walls) may be left at the place of their discovery. The data produced
        by an instance of A1 Excavation Processing Unit should pertain to the material state of matter
        at excavation time only and should be clearly distinguished from subsequent interpretation about
        the causes for this state of matter.

    Examples:
        - The activity taking place on 21.9.2007 between 12:00 and 13:00 that excavated the
          Stratigraphic Volume Unit (2) of Figure 4 and created the surface S1 (A10).
        - The activity that excavated the first 20 cm of a spit excavation on 21.7.2007 created the
          surface S2 in Figure 4.

    In First Order Logic:
        A1(x) ⇒ S1(x)
        A1(x) ⇒ S4(x)
        A1(x) ⇒ E12(x)
        A1(x) ⇒ E64(x)

    Properties:
        AP1 produced (was produced by): S11 Amount of Matter
        AP2 discarded (was discarded by): S11 Amount of Matter
        AP4 produced surface (was surface produced by): A10 Excavation Interface
        AP5 removed part or all of (was partially or totally removed by): A8 Stratigraphic Unit
        AP6 intended to approximate (was approximated by): A3 Stratigraphic Interface
        AP10 destroyed (was destroyed by): S22 Segment of Matter
        AP32 discarded into (was discarded by): S11 Amount of Matter

    """


# ******************************************************************************************************************* #


__crmarchaeo_namespace__ = {
    'A1ExcavationProcessingUnit': A1ExcavationProcessingUnit,
    'A2StratigraphicVolumeUnit': A2StratigraphicVolumeUnit,
    'A3StratigraphicInterface': A3StratigraphicInterface,
    'A8StratigraphicUnit': A8StratigraphicUnit,
}


# ******************************************************************************************************************* #


from pyheritage.cidoc.crmsci import entities as _crmsci_entities_module  # noqa: E402


__namespace__ = {
    **_core_entities_module.__namespace__,
    **_crmsci_entities_module.__crmsci_namespace__,
    **__crmarchaeo_namespace__,
}


A1ExcavationProcessingUnit.model_rebuild(_types_namespace=__namespace__)
A2StratigraphicVolumeUnit.model_rebuild(_types_namespace=__namespace__)
A3StratigraphicInterface.model_rebuild(_types_namespace=__namespace__)
A8StratigraphicUnit.model_rebuild(_types_namespace=__namespace__)
