# -*- coding: utf-8 -*-

"""CRMinf entity models;

CRMinf v1.0

Entities
--------
I1  Argumentation
I2  Belief
I3  Inference Logic
I4  Proposition Set
I5  Inference Making
I6  Belief Value
I7  Belief Adoption
I10 Provenance Statement
I11 Situation
I12 Adopted Belief
I13 Intended Meaning Belief
I14 Provenance Belief
I15 Provenance Assessment
I16 Meaning Comprehension
I17 Categorical Hypothesis Building

"""


from abc import ABC

from pydantic import Field

from pyheritage.cidoc.base import entity_register
from pyheritage.cidoc.core.entities import (
    E7Activity,
    E59PrimitiveValue,
    E73InformationObject,
    E89PropositionalObject,
)


__all__ = (
    'I1Argumentation',
    'I3InferenceLogic',
    'I4PropositionSet',
    'I6BeliefValue',
    'I11Situation',
)


@entity_register(label='I3 Inference Logic')
class I3InferenceLogic(E89PropositionalObject):
    """'I3 Inference Logic' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I3

    SubClass Of:
        E89 Propositional Object

    SuperClass Of:
        -

    Scope Note:
        This class comprises the rules used as inputs to I5 Inference Making;

        In this context, the term "logic" is used in the most general sense of the Greek term, and not in the
        mathematical sense only. Examples are the direct application of formal logic, mathematical theories and
        calculus, formal or informal default reasoning based on default values associated with categories,
        probabilistic reasoning-based mathematical models and assumed or observed frequencies for certain categories,
        application of theoretical social models and comparisons with "cultural parallels", etc. An instance of
        Inference Logic could also be a reference to the exact software release of a Bayesian reasoner, a rule such
        as "later layers are on top of earlier layers", or even a term like "social intuition", if this is scholarly
        acceptable (after Doerr, Kritsotaki and Boutsika, 2011);

        Indeed, anything that is scientifically or academically acceptable as a method for drawing conclusions may
        be included, for instance, human pattern recognition;

        A particular instance of I3 Inference Logic would be the algorithm implemented in a particular revision of
        a software package;

        Instances of I3 Inference Logic not only comprise the method of reasoning, but also the set of categorical
        laws or axioms used in the argumentation. Often, both are inextricably interwoven, for instance in a
        software implementation;

    Examples:
        - Dating using a reference typology
        - Use of parallels

    In First Order Logic:
        I3(x) ⇒ E89(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='I6 Belief Value')
class I6BeliefValue(E59PrimitiveValue):
    """'I6 Belief Value' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I6

    SubClass Of:
        E59 Primitive Value

    SuperClass Of:
        -

    Scope Note:
        This class comprises any encoding of the value of the truth of an I2 Belief. It may be expressed in terms
        of discrete logic, modal logic, probability, fuzziness, or any other adequate representational system;

        A minimum requirement of flexibility is for three values: True; False; Unknown;

    Examples:
        - True
        - False

    In First Order Logic:
        I6(x) ⇒ E59(x)

    Properties:
        -

    """

    value: str = Field(default='Unknown', description='I6 belief value')


# ******************************************************************************************************************* #


@entity_register(label='I4 Proposition Set')
class I4PropositionSet(E73InformationObject, ABC):
    """'I4 Proposition Set' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I4

    SubClass Of:
        E73 Information Object

    SuperClass Of:
        I10 Provenance Statement
        I11 Situation

    Scope Note:
        This class comprises the sets of formal, binary propositions that an I2 Belief is held about. It could
        be implemented as a named graph, a spreadsheet, or any other structured dataset. Regardless of the
        specific syntax employed, the effective propositions it contains should be made up of unambiguous
        identifiers, concepts of a formal ontology, and constructs of logic;

    Examples:
        - Francesca Bologna's belief that Publius Cornelius Tacitus meant that "Nero was at Antium when the
          Great Fire broke out and did not return to Rome until the fire approached his house" (I12)

    In First Order Logic:
        I4(x) ⇒ E73(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='I11 Situation')
class I11Situation(I4PropositionSet):
    """'I11 Situation' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I11

    SubClass Of:
        I4 Proposition Set

    SuperClass Of:
        -

    Scope Note:
        This class comprises the persistence of particular value ranges of the properties of a particular thing
        or things, over a timespan. The identity of an instance of I11 Situation is given by prescribing kinds
        of properties and a particular timespan and optionally the spatial area. This prescription of properties
        enables the possibility of observing the values of those properties prescribed, that hold in the specified
        timespan and spatial area;

        In general, there are no natural boundaries to the combination of the kinds of properties or the space
        and the timespan under consideration upon defining a situation, other than the interest and ability of
        the observer to do so. Therefore, this class is purely epistemological in nature, describing arbitrary
        units of observation of the world;

    Examples:
        - the persistence of the value of the pH for sample XIV during the period of the pH measurement, which
          took place one month after the application of Ca(OH)2 dispersion to the sample (Giori et al. 2002);

    In First Order Logic:
        I11(x) ⇒ I4(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


@entity_register(label='I1 Argumentation')
class I1Argumentation(E7Activity, ABC):
    """'I1 Argumentation' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I1

    SubClass Of:
        E7 Activity

    SuperClass Of:
        I5 Inference Making
        I7 Belief Adoption
        I15 Provenance Assessment
        I16 Meaning Comprehension
        S4 Observation

    Scope Note:
        This class comprises the activity of making honest inferences or observations. An honest inference or
        observation is one in which the E39 Actor carrying out the I1 Argumentation justifies and believes that
        the I6 Belief Value associated with the resulting I2 Belief about the I4 Proposition Set is the correct
        value at the time that the activity was undertaken and that any I3 Inference Logic or methodology was
        correctly applied;

        One instance of E39 Actor may carry out an instance of I1 Argumentation, though the E39 Actor may, of
        course, be an instance of E74 Group;

    Examples:
        - My classification and dating of this bowl (I5) (fictitious)
        - My adoption of the belief that Dragendorff type 29 bowls are from the 1st Century AD (I7) (fictitious)

    In First Order Logic:
        I1(x) ⇒ E7(x)

    Properties:
        J2 concluded that (was concluded by): I2 Belief

    """
