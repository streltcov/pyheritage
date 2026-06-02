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
from pyheritage.cidoc.core.entities import E12Production, E13AttributeAssignment, E25HumanMadeFeature, E64EndOfExistence
from pyheritage.cidoc.crmsci.entities import (
    S1MatterRemoval,
    S4Observation,
    S17PhysicalGenesis,
    S18Alteration,
    S20RigidPhysicalFeature,
)


__all__ = (
    'A1ExcavationProcessingUnit',
    'A10ExcavationInterface',
    'A2StratigraphicVolumeUnit',
    'A3StratigraphicInterface',
    'A4StratigraphicGenesis',
    'A5StratigraphicModification',
    'A6GroupDeclarationEvent',
    'A7Embedding',
    'A8StratigraphicUnit',
    'A9ArchaeologicalExcavation',
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


@entity_register(label='A5 Stratigraphic Modification')
class A5StratigraphicModification(S18Alteration, ABC):
    """'A5 Stratigraphic Modification' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A5

    SubClass Of:
        S18 Alteration

    SuperClass Of:
        A4 Stratigraphic Genesis

    Scope Note:
        This class comprises activities or processes resulting in the modification of Stratigraphic
        Units after their genesis through instances of A4 Stratigraphic Genesis Event.

    Examples:
        - The event that eroded the number (1) Stratigraphic Volume Unit in Figure 4 and diminished
          it to its actual size.
        - During the excavation at Eagle Cave, Texas, archaeologists found many burrows, about 7 cm
          in diameter on average, deriving from rodents, lizards, and insects, which have disturbed
          (A5) the intact layers (A8). [Larsen, M. 2015].
        - At the Dutton Paleo-Indian site, Colorado, involutions (flame-structures) due to
          aquaturbations, caused deformation (A5) of the saturated soil (A8).
          [Wood & Johnson 1978, pp. 315-380].

    In First Order Logic:
        A5(x) ⇒ S18(x)

    Properties:
        AP8 disturbed (was disturbed by): A8 Stratigraphic Unit
        AP13 has stratigraphic relation to (is stratigraphic relation of): A5 Stratigraphic Modification

    """


# ******************************************************************************************************************* #


@entity_register(label='A4 Stratigraphic Genesis')
class A4StratigraphicGenesis(S17PhysicalGenesis, A5StratigraphicModification, ABC):
    """'A4 Stratigraphic Genesis' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A4

    SubClass Of:
        S17 Physical Genesis
        A5 Stratigraphic Modification

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises activities or processes that have produced homogeneous, distinguishable
        units of stratification that are in a relatively stable form from the time of their genesis
        until they are observed. Such processes may be the aggregation of cycles of
        erosion/destruction, deposit/accumulation, or transformation/modification occurring on a
        particular site throughout a particular period of time. These processes are usually not only
        due to natural forces (i.e., climate, the impact of flora and fauna, other natural events),
        but also to human activities, in particular excavation and construction. An event of
        stratification genesis typically produces two main forms of stratification units, both a
        deposit and an interface.

    Examples:
        - The cut in the pre-existing strata of the posthole in Figure 8 produced the stratigraphic
          interface number [3]; the filling of the posthole with detritus or some other matter
          produced stratigraphic unit number (18).
        - In the excavation of Akrotiri, Thera, five distinct layers (A2) of pumice create a level
          (A8), about one metre thick, which covers the ruins caused by the earthquake (A4). Above
          the pumice, the deposition of successive layers (A2) of volcanic ash created an 8-10 m
          thick level (A8) (Fig. 5, 9). [Doumas 2015].
        - At the northern section of trenches 6 and 21 from the Paliambela Kolindros site at least
          seven (7) distinct fill episodes (A4) of a neolithic ditch produced the deposits (A8)
          L14-L18 and L22-L24 (Fig. 10).

    In First Order Logic:
        A4(x) ⇒ S17(x)
        A4(x) ⇒ A5(x)

    Properties:
        AP7 produced (was produced by): A8 Stratigraphic Unit
        AP9 took matter from (provided matter to): S10 Material Substantial

    """


# ******************************************************************************************************************* #


@entity_register(label='A6 Group Declaration Event')
class A6GroupDeclarationEvent(E13AttributeAssignment):
    """'A6 Group Declaration Event' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A6

    SubClass Of:
        E13 Attribute Assignment

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises interpretive activities that lead to the recognition two or more
        instances of Stratigraphic Units (A8) or other Physical Thing (E18) that simultaneously
        exist at the time of this activity or at the time of an archaeological observation this
        activity refers to as source and that are attributed to be the remains of one complete
        instance of Physical Thing (E18) that had existed at a time of reference in the past.
        Instances of this class could be, for example: two stratigraphic units (with no evident
        contact) cut through by a ditch having been segments of the same original stratigraphic
        unit, two or more surviving parts of a structure having been segments of the same wall,
        a number of postholes being the indication of a past wooden house or a number of potsherds
        being segments of the same original artefact.

    Examples:
        - The excavator declared the post holes [7] and [8] in Figure 4 to be part of one building.
        - Individual deposits (A8) forming the fill of a neolithic ditch (L14-18 and L22-24) in
          Trenches 6 and 21 at the archaeological site of Paliambela Kolindros have been grouped
          by the excavating team into larger stratigraphic entities or fill episodes (A8)
          [Figure 10].

    In First Order Logic:
        A6(x) ⇒ E13(x)

    Properties:
        AP16 assigned attribute to (was attributed by): E18 Physical Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='A7 Embedding')
class A7Embedding(A8StratigraphicUnit):
    """'A7 Embedding' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A7

    SubClass Of:
        A8 Stratigraphic Unit

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of A8 Stratigraphic Unit partially or completely embedding
        one or more instances of E20 Physical Thing and at a particular position with relative
        stability in one or more instances of A2 Stratigraphic Volume Units. Normally, an embedding
        is expected to have been stable from the time of generation of the first instance of A2
        Stratigraphic Volume Unit that surrounds it. However, it may also be due to later intrusion.
        As an empirical fact, the expert may only be able to decide that a particular embedding is
        not recent, i.e. has been persisting for longer than the activity that encountered it. This
        class can be used to document the fact of embedding generally with respect to the surrounding
        matter or, more specifically, with respect to a more precise position within this matter.

    Examples:
        - Several pottery vessels (E19) that were discovered (S19) during the excavation process of
          Room 6 (A1) of the West House at Akrotiri, Thera, were embedded (A7) within the deposit
          (A8) on the ground floor (E53) (Fig.8) (Michailidou 2001, Fig.55, Fig.59).
        - San Galgano's sword embedded at the Hermitage of Monte Siepi, as a symbol of peace he
          embedded his sword in a stone, which can still be seen today.

    In First Order Logic:
        A7(x) ⇒ A8(x)

    Properties:
        AP17 is found by (found): S19 Encounter Event
        AP18 is embedding of (is embedded): E18 Physical Thing
        AP19 is embedding in (contains embedding): A2 Stratigraphic Volume Unit

    """


# ******************************************************************************************************************* #


@entity_register(label='A9 Archaeological Excavation')
class A9ArchaeologicalExcavation(S4Observation):
    """'A9 Archaeological Excavation' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A9

    SubClass Of:
        S4 Observation

    SuperClass Of:
        (none)

    Scope Note:
        This class describes the general concept of archaeological excavation intended as a
        coordinated set of activities performed on an area considered as part of a broader
        topographical, rural, urban, or monumental context. An archaeological excavation is
        usually under the responsibility of a coordinator, officially designated, which is legally
        and scientifically responsible for all the activities carried out within each instance of
        A1 Excavation Processing Unit and is also responsible for the documentation of the whole
        process.

    Examples:
        - The archaeological excavation (A9) of the West House (E24) that took place at the
          archaeological site of Akrotiri, Thera (E53) during the years (1967-1973) (E52) by the
          archaeologist Sp. Marinatos (E39). [Μιχαηλίδου 2001, p. 41] [Palyvou 200].

    In First Order Logic:
        A9(x) ⇒ S4(x)

    Properties:
        AP3 investigated (was investigated by): E27 Site

    """


# ******************************************************************************************************************* #


@entity_register(label='A10 Excavation Interface')
class A10ExcavationInterface(S20RigidPhysicalFeature, E25HumanMadeFeature):
    """'A10 Excavation Interface' CRMArchaeo entity;

    https://cidoc-crm.org/extensions/crmarchaeo/html/CRMarchaeo_v2.0.html#A10

    SubClass Of:
        S20 Rigid Physical Feature
        E25 Human-Made Feature

    SuperClass Of:
        (none)

    Scope Note:
        This class comprises instances of S20 Rigid Physical Feature that constitutes a surface
        produced through one or several instances of A1 Excavation Processing Unit. Instances are
        often documented through drawing and/or measured by technical means such as photography,
        tachymetry or laser scanning. Using a planar excavation methodology this is typically the
        surface of a planum or the surface of a profile. Using a stratigraphic excavation
        methodology, the instance of A10 Excavation Interface would have the intention to
        approximate an instance of A3 Stratigraphic Interface. The drawing and measurement of
        profiles is also common practice when a stratigraphic excavation methodology is used.

    Examples:
        - The Excavation Interface Planum 6 of square I22 in Area F-I is documented in the field
          drawing "Planum 6 F-I i22" created in Fall 1982.
        - The Excavation Interface Eastern profile of square I22 in Area F-I is documented in field
          drawing "Ostprofil F-I i22" and confines the excavation square I22 to the east.

    In First Order Logic:
        A10(x) ⇒ S20(x)
        A10(x) ⇒ E25(x)

    Properties:
        (none)

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
    'A10ExcavationInterface': A10ExcavationInterface,
    'A1ExcavationProcessingUnit': A1ExcavationProcessingUnit,
    'A2StratigraphicVolumeUnit': A2StratigraphicVolumeUnit,
    'A3StratigraphicInterface': A3StratigraphicInterface,
    'A4StratigraphicGenesis': A4StratigraphicGenesis,
    'A5StratigraphicModification': A5StratigraphicModification,
    'A6GroupDeclarationEvent': A6GroupDeclarationEvent,
    'A7Embedding': A7Embedding,
    'A8StratigraphicUnit': A8StratigraphicUnit,
    'A9ArchaeologicalExcavation': A9ArchaeologicalExcavation,
}


# ******************************************************************************************************************* #


from pyheritage.cidoc.crmsci import entities as _crmsci_entities_module  # noqa: E402


__namespace__ = {
    **_core_entities_module.__namespace__,
    **_crmsci_entities_module.__crmsci_namespace__,
    **__crmarchaeo_namespace__,
}


A10ExcavationInterface.model_rebuild(_types_namespace=__namespace__)
A1ExcavationProcessingUnit.model_rebuild(_types_namespace=__namespace__)
A2StratigraphicVolumeUnit.model_rebuild(_types_namespace=__namespace__)
A3StratigraphicInterface.model_rebuild(_types_namespace=__namespace__)
A4StratigraphicGenesis.model_rebuild(_types_namespace=__namespace__)
A5StratigraphicModification.model_rebuild(_types_namespace=__namespace__)
A6GroupDeclarationEvent.model_rebuild(_types_namespace=__namespace__)
A7Embedding.model_rebuild(_types_namespace=__namespace__)
A8StratigraphicUnit.model_rebuild(_types_namespace=__namespace__)
A9ArchaeologicalExcavation.model_rebuild(_types_namespace=__namespace__)
