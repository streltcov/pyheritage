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
from pyheritage.cidoc.core import entities as _core_entities
from pyheritage.cidoc.core.entities import (
    E2TemporalEntity,
    E7Activity,
    E13AttributeAssignment,
    E59PrimitiveValue,
    E73InformationObject,
    E89PropositionalObject,
)


__all__ = (
    'I1Argumentation',
    'I2Belief',
    'I3InferenceLogic',
    'I4PropositionSet',
    'I5InferenceMaking',
    'I6BeliefValue',
    'I7BeliefAdoption',
    'I10ProvenanceStatement',
    'I11Situation',
    'I12AdoptedBelief',
    'I13IntendedMeaningBelief',
    'I14ProvenanceBelief',
    'I15ProvenanceAssessment',
    'I16MeaningComprehension',
    'I17CategoricalHypothesisBuilding',
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


# ******************************************************************************************************************* #


@entity_register(label='I2 Belief')
class I2Belief(E2TemporalEntity, ABC):
    """'I2 Belief' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I2

    SubClass Of:
        E2 Temporal Entity

    SuperClass Of:
        I12 Adopted Belief
        I13 Intended Meaning Belief
        I14 Provenance Belief

    Scope Note:
        This class comprises the notion that the associated I4 Proposition Set is held to have a particular
        I6 Belief Value by a particular E39 Actor. This can be understood as the period of time that an
        individual group holds a particular set of propositions to be true, false, or somewhere in between;

    Examples:
        - Ian Hodder's belief from 1996 on, that Floor B was earlier than wall C of building 1 in the north
          area of Catalhöyük (Hodder 1999).

    In First Order Logic:
        I2(x) ⇒ E2(x)

    Properties:
        J4 that (is subject of): I4 Proposition Set
        J5 holds to be: I6 Belief Value

    """


# ******************************************************************************************************************* #


@entity_register(label='I5 Inference Making')
class I5InferenceMaking(I1Argumentation, E13AttributeAssignment):
    """'I5 Inference Making' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I5

    SubClass Of:
        I1 Argumentation
        E13 Attribute Assignment

    SuperClass Of:
        I17 Categorical Hypothesis Building
        S6 Data Evaluation
        S7 Simulation or Prediction

    Scope Note:
        This class comprises the action of making honest propositions and statements about particular states of
        affairs in reality or possible realities, or categorical descriptions of reality by using inferences from
        other statements based on hypotheses and any form of formal or informal logic. It includes evaluations,
        calculations, and interpretations, based on mathematical formulations and propositions;

        It is characterized by the use of an existing I2 Belief as the premise that, taken together with a set
        of I3 Inference Logic, draws a further I2 Belief as a conclusion;

        Documenting instances of I5 Inference making primarily enables tracing the dependency of knowledge from
        conclusion to premise through subsequent inferences possibly back to primary evidence, so that the range
        of influence of knowledge revision at any intermediate stage of complex inference chains on current
        convictions can be narrowed down by query. The explicit reference to the applied inference logic further
        allows scholars and scientists to assess if they can or would follow the documented argument. The class
        is not intended to promote the use of computationally decidable systems of logic as replacements of
        scholarly justifications of arguments, even though it allows for documenting the use of decidable logic,
        if that was deemed adequate for the problem at hand. Principles of scholarly justifications of arguments
        are also regarded as kinds of inference logic;

    Examples:
        - My classification and dating of this bowl (fictitious)

    In First Order Logic:
        I5(x) ⇒ I1(x)
        I5(x) ⇒ E13(x)

    Properties:
        J1 used as premise (was premise for): I2 Belief
        J3 applied (was applied by): I3 Inference Logic

    """


# ******************************************************************************************************************* #


@entity_register(label='I7 Belief Adoption')
class I7BeliefAdoption(I1Argumentation):
    """'I7 Belief Adoption' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I7

    SubClass Of:
        I1 Argumentation

    SuperClass Of:
        -

    Scope Note:
        This class comprises the action of an E39 Actor adopting propositions taken from an interpretation of
        the intended meaning of an instance of E73 Information Object as being true, or in some way likely to
        be true. The adopted propositions constitute the conclusion of the action in the form of a new instance
        of I12 Adopted belief of the actor adopting it;

        The basis of I7 Belief Adoption is the justification of trust in the source of the adopted propositions,
        rather than the application of rules for inferring the respective propositions from logical premises;

        Typical examples are the citation of academic papers or the reuse of datasets;

        Where an instance of I7 Belief Adoption is based on personal communication (marked as pers.comm. in the
        studied text), this should be represented by using P2 has type: "Pers.Comm.", directly from the instance
        of I7 Belief Adoption;

    Examples:
        - Francesca Bologna's adoption of Tacitus' belief where Emperor Nero was when the Great Fire started.
          (Bologna 2021);

    In First Order Logic:
        I7(x) ⇒ I1(x)

    Properties:
        J7 is based on evidence from (is evidence for): E73 Information Object
        J13 adopted interpretation (was concluded by): I12 Adopted Belief
        J15 assumed meaning (was assumed by): I13 Intended Meaning Belief
        J18 assumed provenance (was assumed by): I14 Provenance Belief

    """


# ******************************************************************************************************************* #


@entity_register(label='I10 Provenance Statement')
class I10ProvenanceStatement(I4PropositionSet):
    """'I10 Provenance Statement' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I10

    SubClass Of:
        I4 Proposition Set

    SuperClass Of:
        -

    Scope Note:
        This class comprises statements about the provenance of instances of E70 Thing existing at the time of
        making the provenance statements. An instance of I10 Provenance Statement must contain propositions about
        the presence of the respective instances of E70 Thing in an event or spatiotemporal context of reference.
        Characteristically, it may pertain to the writing by a known author at a known or unknown date or place,
        or to the existence of the text known to some public, regardless of the truth of authorship.

        In case that only information objects exist describing the proper thing of interest, such as a photo, or
        photo of a photo, of a lost archaeological object, an instance of I10 Provenance Statement should contain
        the relevant chain of intermediate events transferring the information from the proper thing of interest
        up to the extant information objects taken into account, or refer to it.

        The property J20 is about the provenance of can be used to link the instance of I10 Provenance Statement
        as a whole, with the proper thing of interest. It constitutes a constraint to the provenance statement
        that it must contain the description of the relevant context of reference, and, if applicable, to the
        relevant chain of intermediate events transferring the information.

    Examples:
        - The statement: "The copy of Tacitus, Publius Cornelius. The Annals. Book 15 [15.6] at the hands of
          Francesca Bologna from the British Museum in 2021 represents a text written by the ancient Roman
          historian, Publius Cornelius Tacitus."

    In First Order Logic:
        I10(x) ⇒ I4(x)

    Properties:
        J20 is about the provenance of (has provenance claim): E70 Thing

    """


# ******************************************************************************************************************* #


@entity_register(label='I12 Adopted Belief')
class I12AdoptedBelief(I2Belief):
    """'I12 Adopted Belief' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I12

    SubClass Of:
        I2 Belief

    SuperClass Of:
        -

    Scope Note:
        This class comprises the notion that an instance of E39 Actor adopted the meaning of an associated
        instance of I4 Proposition Set by arguments of trust from a source created by another instance of E39
        Actor, and holds it as being true or in some way likely to be true. This source can be documented via
        the property J14 adopted interpretation of (has adopted interpretation). The used interpretation of the
        meaning of the source may be a belief of the adopting Actor or another one and can be documented as an
        instance of I13 Intended Meaning Belief, if this detail is relevant;

    Examples:
        - Francesca Bologna's belief that Nero was at Antium, when the Great Fire broke out and did not return
          to Rome until the fire approached his house (Bologna 2021);

    In First Order Logic:
        I12(x) ⇒ I2(x)

    Properties:
        J14 adopted interpretation of (has adopted interpretation): E73 Information Object

    """


# ******************************************************************************************************************* #


@entity_register(label='I13 Intended Meaning Belief')
class I13IntendedMeaningBelief(I2Belief):
    """'I13 Intended Meaning Belief' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I13

    SubClass Of:
        I2 Belief

    SuperClass Of:
        -

    Scope Note:
        This class comprises beliefs on the part of an instance of E39 Actor that a particular I4 Proposition
        Set formally represents (in part or in its entirety) the intended meaning that was created by another
        instance of E39 Actor, without considering an opinion yet about its truth or trustworthiness;

        The belief constitutes an interpretation of the source. The respective proposition set can be documented
        using the property J16 assumed meaning (is supposed meaning in), whereas the respective source can be
        documented via the property J17 about (has interpretation) and holds as being true or in some way likely
        to be true;

    Examples:
        - Francesca Bologna's belief that Publius Cornelius Tacitus meant that "Nero was at Antium when the
          Great Fire broke out and did not return to Rome until the fire approached his house". (Bologna 2021)
        - Francesca Bologna's belief that Gaius Suetonius Tranquillus meant that "Nero was singing in Rome
          while it burned from July 19 in 64 AD". (Bologna 2021)

    In First Order Logic:
        I13(x) ⇒ I2(x)

    Properties:
        J16 assumed meaning (is supposed meaning in): I4 Proposition Set
        J17 about (has interpretation): E73 Information Object

    """


# ******************************************************************************************************************* #


@entity_register(label='I14 Provenance Belief')
class I14ProvenanceBelief(I2Belief):
    """'I14 Provenance Belief' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I14

    SubClass Of:
        I2 Belief

    SuperClass Of:
        -

    Scope Note:
        This class comprises beliefs of an Actor that a particular instance of E70 Thing, in general available
        to this Actor, is identical to one present in a relevant event or context of reference in the past, such
        as a text in a book being sufficiently identical to the one in the claimed author's original manuscript
        or edition in order to be used by the Actor for citation. Other examples are the provenance of
        archaeological objects in collections, which may pertain to the claimed excavation spot or to the
        inferred context of their creation;

        The term "in general available" means that the thing is either physically in the hands of the actor or
        that the actor or an actor of their trust has the principled ability to get access to the thing. In case
        that only information objects exist describing the proper thing of interest, such as a photo of a lost
        archaeological object, an instance of I14 Provenance Belief should be based on arguments including
        references to provenance beliefs about descriptions, representations and the described things;

        A formal description about the assumed provenance can be documented via the property J19 that. Note
        that, depending on the intended argumentation about the respective instance of E70 Thing, different
        aspects of provenance may be described about the same instance of E70 Thing;

    Examples:
        - Francesca Bologna's belief about the authenticity of Tacitus, Publius Cornelius. The Annals. Book 15;

    In First Order Logic:
        I14(x) ⇒ I2(x)

    Properties:
        J19 that (is subject of): I10 Provenance Statement

    """


# ******************************************************************************************************************* #


@entity_register(label='I15 Provenance Assessment')
class I15ProvenanceAssessment(I1Argumentation):
    """'I15 Provenance Assessment' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I15

    SubClass Of:
        I1 Argumentation

    SuperClass Of:
        -

    Scope Note:
        This class comprises activities of making arguments and concluding about the likely provenance of
        instances of E70 Thing existing at the time of this assessment. These activities may further be about
        the provenance of things referred to or represented by existing information objects, and subsequent
        references;

    Examples:
        - the assessment by Ernst Pernicka et al. about the provenance of the Nebra Sky Disc
          (Pernicka et al. 2020)

    In First Order Logic:
        I15(x) ⇒ I1(x)

    Properties:
        J21 concluded provenance (was assessed by): I14 Provenance Belief

    """


@entity_register(label='I16 Meaning Comprehension')
class I16MeaningComprehension(I1Argumentation):
    """'I16 Meaning Comprehension' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I16

    SubClass Of:
        I1 Argumentation

    SuperClass Of:
        -

    Scope Note:
        This class comprises processes of interpreting the intended meaning of parts or the whole of the content
        of an instance of E73 Information Object as propositions. Such interpretations may include the
        disambiguation of the meaning of words and expressions, expanding abbreviations, resolving named entities,
        references and co-references, and complementing missing text parts, without however arguing about the
        actual truth of the information;

        In principle, any use of an information object pertaining to its meaning implies an instance of I16
        Meaning Comprehension. However, in practical applications, texts in natural language are often clear
        enough so that no explicit explanation of the interpretation is needed for the user. In such cases, there
        is no need to create explicit instances of I16 Meaning Comprehension, but the adopted belief may directly
        be linked via J14 adopted interpretation of (has adopted interpretation), or the instance of I16 Meaning
        Comprehension may be made implicit to an instance of I7 Belief Adoption by multiple instantiation;

        Explicit documentation of instances of I16 Meaning Comprehension are useful, if the interpretations are
        not obvious and if competing arguments about them exist;

    Examples:
        - My understanding of the statements about Emperor Nero's whereabouts in Rome while it was burning from
          July 19 in 64 AD in the extant book De Vita Caesarum attributed to Gaius Suetonius Tranquillus
          (Wikipedia, 2023);

    In First Order Logic:
        I16(x) ⇒ I1(x)

    Properties:
        J22 interpreted meaning of (was interpreted by): E73 Information Object
        J23 interpreted meaning as (was interpretation by): I13 Intended Meaning Belief

    """


# ******************************************************************************************************************* #


@entity_register(label='I17 Categorical Hypothesis Building')
class I17CategoricalHypothesisBuilding(I5InferenceMaking):
    """'I17 Categorical Hypothesis Building' CRMinf entity model;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#I17

    SubClass Of:
        I5 Inference Making

    SuperClass Of:
        -

    Scope Note:
        This class comprises the action of making categorical hypotheses based on inference rules and theories.
        By categorical hypotheses we mean assumptions about the kinds of interactions and related kinds of
        structures of a domain that have the character of "laws" of nature or human behavior, be it necessary
        or probabilistic. Categorical hypotheses are developed by "induction" from finite numbers of observation
        and the absence of observations of particular kinds. As such, categorical hypotheses are always subject
        to falsification by new evidence. Instances of I17 Categorical Hypothesis Building include making and
        questioning categorical hypotheses;

    Examples:
        - hypothesising that "no binding before the 9th century is made with spine supports" by Szirmai (I17)
          [documented in section 7.1 and 7.2 of "The Archaeology of Medieval bookbinding"]
          (Szirmai, J.A. 1999)

    In First Order Logic:
        I17(x) ⇒ I5(x)

    Properties:
        -

    """


# ******************************************************************************************************************* #


__crminf_namespace__: dict[str, type] = {
    'I10ProvenanceStatement': I10ProvenanceStatement,
    'I11Situation': I11Situation,
    'I12AdoptedBelief': I12AdoptedBelief,
    'I13IntendedMeaningBelief': I13IntendedMeaningBelief,
    'I14ProvenanceBelief': I14ProvenanceBelief,
    'I15ProvenanceAssessment': I15ProvenanceAssessment,
    'I16MeaningComprehension': I16MeaningComprehension,
    'I17CategoricalHypothesisBuilding': I17CategoricalHypothesisBuilding,
    'I1Argumentation': I1Argumentation,
    'I2Belief': I2Belief,
    'I3InferenceLogic': I3InferenceLogic,
    'I4PropositionSet': I4PropositionSet,
    'I5InferenceMaking': I5InferenceMaking,
    'I6BeliefValue': I6BeliefValue,
    'I7BeliefAdoption': I7BeliefAdoption,
}

__namespace__: dict[str, type] = {
    **_core_entities.__namespace__,
    **__crminf_namespace__,
}

I1Argumentation.model_rebuild(_types_namespace=__namespace__)
I2Belief.model_rebuild(_types_namespace=__namespace__)
I3InferenceLogic.model_rebuild(_types_namespace=__namespace__)
I4PropositionSet.model_rebuild(_types_namespace=__namespace__)
I5InferenceMaking.model_rebuild(_types_namespace=__namespace__)
I6BeliefValue.model_rebuild(_types_namespace=__namespace__)
I7BeliefAdoption.model_rebuild(_types_namespace=__namespace__)
I10ProvenanceStatement.model_rebuild(_types_namespace=__namespace__)
I11Situation.model_rebuild(_types_namespace=__namespace__)
I12AdoptedBelief.model_rebuild(_types_namespace=__namespace__)
I13IntendedMeaningBelief.model_rebuild(_types_namespace=__namespace__)
I14ProvenanceBelief.model_rebuild(_types_namespace=__namespace__)
I15ProvenanceAssessment.model_rebuild(_types_namespace=__namespace__)
I16MeaningComprehension.model_rebuild(_types_namespace=__namespace__)
I17CategoricalHypothesisBuilding.model_rebuild(_types_namespace=__namespace__)
