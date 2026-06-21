# -*- coding: utf-8 -*-

"""CRMinf property models;

(Mixin classes for entity models);

CRMinf v1.0

-------------------------------------------------
Properties
-------------------------------------------------
J1  used as premise                    I5  -> I2
J2  concluded that                     I1  -> I2
J3  applied                            I5  -> I3
J4  that (is subject of)               I2  -> I4
J5  holds to be                        I2  -> I6
J7  is based on evidence from          I7  -> E73
J13 adopted interpretation             I7  -> I12
J14 adopted interpretation of          I12 -> E73
J15 assumed meaning                    I7  -> I13
J16 assumed meaning                    I13 -> I4
J17 about (has interpretation)         I13 -> E73
J18 assumed provenance                 I7  -> I14
J19 that (is subject of)               I14 -> I10
J20 is about the provenance of         I10 -> E70
J21 concluded provenance               I15 -> I14
J22 interpreted meaning of             I16 -> E73
J23 interpreted meaning as             I16 -> I13

"""


from __future__ import annotations

from typing import List, TYPE_CHECKING

from pydantic import Field

from pyheritage.cidoc.base import PropertyMixin


if TYPE_CHECKING:
    from pyheritage.cidoc.core.entities import E70Thing, E73InformationObject
    from pyheritage.cidoc.crminf.entities import (
        I2Belief,
        I3InferenceLogic,
        I4PropositionSet,
        I6BeliefValue,
        I10ProvenanceStatement,
        I12AdoptedBelief,
        I13IntendedMeaningBelief,
        I14ProvenanceBelief,
    )


__all__ = (
    'J1UsedAsPremise',
    'J2ConcludedThat',
    'J3Applied',
    'J4That',
    'J5HoldsToBe',
    'J7IsBasedOnEvidenceFrom',
    'J13AdoptedInterpretation',
    'J14AdoptedInterpretationOf',
    'J15AssumedMeaning',
    'J16AssumedMeaning',
    'J17About',
    'J18AssumedProvenance',
    'J19That',
    'J20IsAboutTheProvenanceOf',
    'J21ConcludedProvenance',
    'J22InterpretedMeaningOf',
    'J23InterpretedMeaningAs',
)


# ******************************************************************************************************************* #


class J1UsedAsPremise(PropertyMixin):
    """'J1 used as premise (was premise for)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J1

    Domain:
        I5 Inference Making
    Range:
        I2 Belief
    SubProperty Of:
        E7 Activity. P17 was motivated by (motivated): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of I2 Belief with the instance of I5 Inference Making that used it
        as a premise.

    Properties:
        -
    Examples:
        - My classification and dating of this bowl (I5) *used as premise* my belief that Dragendorff type 29
          bowls are from the 1st century AD (I2).
        - My classification and dating of this bowl (I5) *used as premise* my belief in the observations of this
          bowl (I2).

    In First Order Logic:
        J1(x,y) ⇒ I5(x)
        J1(x,y) ⇒ I2(y)
        J1(x,y) ⇒ P17(x,y)

    """

    j1_used_as_premise: List[I2Belief] = Field(
        default=None,
        description='J1 used as premise (was premise for)',
    )


# ******************************************************************************************************************* #


class J2ConcludedThat(PropertyMixin):
    """'J2 concluded that (was concluded by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J2

    Domain:
        I1 Argumentation
    Range:
        I2 Belief
    SubProperty Of:
        E2 Temporal Entity. AP24 starts (is started by): E2 Temporal Entity
        E2 Temporal Entity. P175 starts before or with the start of \
            (starts after or with the start of): E2 Temporal Entity
        E2 Temporal Entity. P175i starts after or with the start of \
            (starts before or with the start of): E2 Temporal Entity
        E2 Temporal Entity. P185 ends before the end of (ends after the end of): E2 Temporal Entity
    SuperProperty Of:
        J13 adopted interpretation (was concluded by)
        J21 concluded provenance (was assessed by)
        J23 interpreted meaning as (was interpretation by)
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property associates an instance of I2 Belief with the instance of I1 Argumentation that concluded it.

    Properties:
        -
    Examples:
        - Ian Hodder's re-examination, in 1996, of the physical relation of wall C and floor B of building 1
          in the north area of Catalhöyük (I1) *concluded that* Ian Hodder believed from 1996 on, that Floor B
          was earlier than wall C of building 1 in the north area of Catalhöyük (I2) (Hodder 1999).

    In First Order Logic:
        J2(x,y) ⇒ I1(x)
        J2(x,y) ⇒ I2(y)
        J2(x,y) ⇒ AP24(x,y)
        J2(x,y) ⇒ P175(x,y)
        J2(x,y) ⇒ P175i(x,y)
        J2(x,y) ⇒ P185(x,y)

    """

    j2_concluded_that: List[I2Belief] = Field(
        default=None,
        min_length=1,
        description='J2 concluded that (was concluded by)',
    )


# ******************************************************************************************************************* #


class J3Applied(PropertyMixin):
    """'J3 applied (was applied by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J3

    Domain:
        I5 Inference Making
    Range:
        I3 Inference Logic
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,1)

    Scope Note:
        This property associates an instance of I3 Inference Logic with the instance of I5 Inference Making that
        used it to draw its conclusion.

    Properties:
        -
    Examples:
        - My classification and dating of this bowl (I5) *applied* use of a typology (I3).

    In First Order Logic:
        J3(x,y) ⇒ I5(x)
        J3(x,y) ⇒ I3(y)
        J3(x,y) ⇒ P16(x,y)

    """

    j3_applied: List[I3InferenceLogic] = Field(
        default=None,
        min_length=1,
        description='J3 applied (was applied by)',
    )


# ******************************************************************************************************************* #


class J4That(PropertyMixin):
    """'J4 that (is subject of)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J4

    Domain:
        I2 Belief
    Range:
        I4 Proposition Set
    SubProperty Of:
        -
    SuperProperty Of:
        J19 that (is subject of)
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I4 Proposition Set with the instance of I2 Belief that holds an
        opinion about it.

    Properties:
        -
    Examples:
        - Dragendorff's belief concerning type 29 Bowls (I2) *that* type 29 Bowls are from the 1st century AD (I4).

    In First Order Logic:
        J4(x,y) ⇒ I2(x)
        J4(x,y) ⇒ I4(y)

    """

    j4_that: List[I4PropositionSet] = Field(
        default=None,
        min_length=1,
        description='J4 that (is subject of)',
    )


# ******************************************************************************************************************* #


class J5HoldsToBe(PropertyMixin):
    """'J5 holds to be' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J5

    Domain:
        I2 Belief
    Range:
        I6 Belief Value
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to one, necessary (1,1:0,n)

    Scope Note:
        This property associates an instance of I2 Belief with the I6 Belief Value that reflects the opinion of
        the instance of I2 Belief about the I4 Proposition Set associated with it.

    Properties:
        -
    Examples:
        - Dragendorff's belief that type 29 bowls are from the 1st century AD (I2) *holds to be* True (I6)

    In First Order Logic:
        J5(x,y) ⇒ I2(x)
        J5(x,y) ⇒ I6(y)

    """

    j5_holds_to_be: I6BeliefValue = Field(
        description='J5 holds to be',
    )


# ******************************************************************************************************************* #


class J7IsBasedOnEvidenceFrom(PropertyMixin):
    """'J7 is based on evidence from (is evidence for)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J7

    Domain:
        I7 Belief Adoption
    Range:
        E73 Information Object
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        J18 assumed provenance (was assumed by)
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I7 Belief Adoption with the instance of E73 Information Object
        that was a source of or evidence for the I4 Proposition Set that was adopted.

    Properties:
        -
    Examples:
        - That Francesca Bologna adopted the belief of Tacitus concerning Emperor Nero's whereabouts at the
          beginning of the Great Fire (I7) *is based on evidence from* Tacitus, Publius Cornelius. The Annals.
          Book 15 [15.6]. (Bologna, 2021)

    In First Order Logic:
        J7(x,y) ⇒ I7(x)
        J7(x,y) ⇒ E73(y)
        J7(x,y) ⇒ P16(x,y)

    """

    j7_is_based_on_evidence_from: List[E73InformationObject] = Field(
        default=None,
        min_length=1,
        description='J7 is based on evidence from (is evidence for)',
    )


# ******************************************************************************************************************* #


class J13AdoptedInterpretation(PropertyMixin):
    """'J13 adopted interpretation (was concluded by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J13

    Domain:
        I7 Belief Adoption
    Range:
        I12 Adopted Belief
    SubProperty Of:
        I1 Argumentation. J2 concluded that (was concluded by): I2 Belief
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary, dependent (1,n:1,n)

    Scope Note:
        This property associates an instance of I7 Belief Adoption with the instance of I12 Adopted Belief that
        was established and possibly selected from the interpretation of the source or sources referred to by the
        property J14 adopted interpretation of. This property implies a relation of trust in the reliability of
        the sources. The actual believed content, i.e., propositions about some past reality that have been
        adopted from the source, should be documented using the property J4 that.

    Properties:
        -
    Examples:
        - Francesca Bologna adopting the belief of Tacitus concerning Emperor Nero's whereabouts at the beginning
          of the Great Fire (I7) *adopted interpretation* the belief of Francesca Bologna according to which Nero
          was at Antium when the Great Fire broke out and did not return to Rome until the fire had approached
          his house (I12) (Bologna, 2021)

    In First Order Logic:
        J13(x,y) ⇒ I7(x)
        J13(x,y) ⇒ I12(y)
        J13(x,y) ⇒ J2(x,y)

    """

    j13_adopted_interpretation: List[I12AdoptedBelief] = Field(
        default=None,
        min_length=1,
        description='J13 adopted interpretation (was concluded by)',
    )


# ******************************************************************************************************************* #


class J14AdoptedInterpretationOf(PropertyMixin):
    """'J14 adopted interpretation of (has adopted interpretation)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J14

    Domain:
        I12 Adopted Belief
    Range:
        E73 Information Object
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I12 Adopted Belief with a source or sources of interpretation
        from which the belief was established and possibly selected. In some cases of scholarly arguments,
        multiple source referring to a common topic may have been interpreted in order to form a particular
        belief about the topic referred to.

    Properties:
        -
    Examples:
        - Francesca Bologna's belief that "Nero was at Antium when the Great Fire broke out and did not return
          to Rome until the fire approached his house" (I12) *adopted interpretation of* Tacitus, Publius
          Cornelius. The Annals. Book 15 [15.6] (E73). (Bologna 2021)

    In First Order Logic:
        J14(x,y) ⇒ I12(x)
        J14(x,y) ⇒ E73(y)

    """

    j14_adopted_interpretation_of: List[E73InformationObject] = Field(
        default=None,
        min_length=1,
        description='J14 adopted interpretation of (has adopted interpretation)',
    )


# ******************************************************************************************************************* #


class J15AssumedMeaning(PropertyMixin):
    """'J15 assumed meaning (was assumed by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J15

    Domain:
        I7 Belief Adoption
    Range:
        I13 Intended Meaning Belief
    SubProperty Of:
        I5 Inference Making. J1 used as premise (was premise for): I2 Belief
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I7 Belief Adoption with an instance of I13 Intended Meaning
        Belief about a meaning believed to be expressed in the source or sources referred to by the property
        J14 adopted interpretation of.

    Properties:
        -
    Examples:
        - Francesca Bologna adopting the belief of Tacitus concerning Emperor Nero's whereabouts at the
          beginning of the Great Fire (I7) *assumed meaning* the belief of Francesca Bologna that what Publius
          Cornelius Tacitus meant was "Nero was at Antium when the Great Fire broke out and did not return to
          Rome until the fire approached his house" (I13) (Bologna 2021).

    In First Order Logic:
        J15(x,y) ⇒ I7(x)
        J15(x,y) ⇒ I13(y)
        J15(x,y) ⇒ J1(x,y)

    """

    j15_assumed_meaning: List[I13IntendedMeaningBelief] = Field(
        default=None,
        min_length=1,
        description='J15 assumed meaning (was assumed by)',
    )


# ******************************************************************************************************************* #


class J16AssumedMeaning(PropertyMixin):
    """'J16 assumed meaning (is supposed meaning in)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J16

    Domain:
        I13 Intended Meaning Belief
    Range:
        I4 Proposition Set
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I13 Intended Meaning Belief with the instance of I4 Proposition
        Set that represents the meaning assumed by the holder of the belief to have been intended by the
        respective source. The latter source can be documented with the property J17 about (has interpretation).

    Properties:
        -
    Examples:
        - Francesca Bologna's belief that Publius Cornelius Tacitus meant that "Nero was at Antium when the
          Great Fire broke out and did not return to Rome until the fire approached his house" (I13) *assumed
          meaning* {Nero in July 19, 64 AD ...} I4 (Bologna, 2021).

    In First Order Logic:
        J16(x,y) ⇒ I13(x)
        J16(x,y) ⇒ I4(y)

    """

    j16_assumed_meaning: List[I4PropositionSet] = Field(
        default=None,
        min_length=1,
        description='J16 assumed meaning (is supposed meaning in)',
    )


# ******************************************************************************************************************* #


class J17About(PropertyMixin):
    """'J17 about (has interpretation)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J17

    Domain:
        I13 Intended Meaning Belief
    Range:
        E73 Information Object
    SubProperty Of:
        -
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I13 Intended Meaning Belief with the instance of E73 Information
        Object that was a source of or evidence for the interpretation of its intended meaning. If sources are
        fragmentary about or complementary to a specific topic, more than one source may have been used.

    Properties:
        -
    Examples:
        - Francesca Bologna's belief that Gaius Suetonius Tranquillus meant that Nero was singing in Rome while
          it was burning from July 19 in 64 AD *about* the extant book De Vita Caesarum, attributed to Gaius
          Suetonius Tranquillus.

    In First Order Logic:
        J17(x,y) ⇒ I13(x)
        J17(x,y) ⇒ E73(y)

    """

    j17_about: List[E73InformationObject] = Field(
        default=None,
        min_length=1,
        description='J17 about (has interpretation)',
    )


# ******************************************************************************************************************* #


class J18AssumedProvenance(PropertyMixin):
    """'J18 assumed provenance (was assumed by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J18

    Domain:
        I7 Belief Adoption
    Range:
        I14 Provenance Belief
    SubProperty Of:
        I7 Belief Adoption. J7 is based on evidence from (is evidence for): E73 Information Object
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I7 Belief Adoption with an instance of I14 Provenance Belief
        about the source or sources referred to by the property J14 adopted interpretation of, which justifies
        the conviction that the trusted and adopted content of the source, or its copy at hand, is actually
        identical, or sufficiently close to the assumed original and its context of creation.

    Properties:
        -
    Examples:
        - Francesca Bologna adopting the belief of Tacitus concerning Emperor Nero's whereabouts at the
          beginning of the Great Fire (I7) *assumed provenance* her belief about the authenticity of Tacitus,
          Publius Cornelius. The Annals. Book 15 (I14).

    In First Order Logic:
        J18(x,y) ⇒ I7(x)
        J18(x,y) ⇒ I14(y)
        J18(x,y) ⇒ J7(x,y)

    """

    j18_assumed_provenance: List[I14ProvenanceBelief] = Field(
        default=None,
        min_length=1,
        description='J18 assumed provenance (was assumed by)',
    )


# ******************************************************************************************************************* #


class J19That(PropertyMixin):
    """'J19 that (is subject of)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J19

    Domain:
        I14 Provenance Belief
    Range:
        I10 Provenance Statement
    SubProperty Of:
        I2 Belief. J4 that (is subject of): I4 Proposition Set
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I14 Provenance Belief with the instance of I10 Provenance
        Statement that holds an opinion about it.

    Properties:
        -
    Examples:
        - Francesca Bologna's belief about the authenticity of Tacitus, Publius Cornelius. The Annals. Book 15
          *that* the copy of Tacitus, Publius Cornelius. The Annals. Book 15[15.6] at the hands of Francesca
          Bologna from the British Museum in 2021 represents a text written by the ancient Roman historian,
          Publius Cornelius Tacitus.

    In First Order Logic:
        J19(x,y) ⇒ I14(x)
        J19(x,y) ⇒ I10(y)
        J19(x,y) ⇒ J4(x,y)

    """

    j19_that: List[I10ProvenanceStatement] = Field(
        default=None,
        min_length=1,
        description='J19 that (is subject of)',
    )


# ******************************************************************************************************************* #


class J20IsAboutTheProvenanceOf(PropertyMixin):
    """'J20 is about the provenance of (has provenance claim)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J20

    Domain:
        I10 Provenance Statement
    Range:
        E70 Thing
    SubProperty Of:
        E89 Propositional Object. P129 is about (is subject of): E1 CRM Entity
    SuperProperty Of:
        -
    Quantification:
        many to many (0,n:0,n)

    Scope Note:
        This property associates an instance of I10 Provenance Statement with an instance of E70 Thing, the
        provenance of which the statement describes.

    Properties:
        -
    Examples:
        - The statement: "The exemplar of The Merchant of Venice, Quarto 1 (1600) owned by The British Library,
          shelf number BL C.34.k.22 was published in 1600 AD by Thomas Heyes" (I10) *is about the provenance of*
          the exemplar of The Merchant of Venice, Quarto 1 (1600), owned by the British Library, shelf number
          BL C.34.k.22 (E70).

    In First Order Logic:
        J20(x,y) ⇒ I10(x)
        J20(x,y) ⇒ E70(y)
        J20(x,y) ⇒ P129(x,y)

    """

    j20_is_about_the_provenance_of: List[E70Thing] = Field(
        default=None,
        description='J20 is about the provenance of (has provenance claim)',
    )


# ******************************************************************************************************************* #


class J21ConcludedProvenance(PropertyMixin):
    """'J21 concluded provenance (was assessed by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J21

    Domain:
        I15 Provenance Assessment
    Range:
        I14 Provenance Belief
    SubProperty Of:
        I1 Argumentation. J2 concluded that (was concluded by): I2 Belief
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property describes the naming or identification of any real-world item by a name or any other
        identifier.

        This property associates an instance of I15 Provenance Assessment with an instance of I14 Provenance
        Belief that constitutes the conclusion of the assessment. An instance of I15 Provenance Assessment may
        conclude more than one instances of I14 Provenance Belief, typically about different objects considered
        in the same assessment.

    Properties:
        -
    Examples:
        - The assessment by Ernst Pernicka et al. about the provenance of the Nebra Sky Disc (I15) *concluded
          that* Ernst Pernicka et al. believe that the Nebra Sky Disc dates to the Early Bronze Age
          (Pernicka et al. 2020)

    In First Order Logic:
        J21(x,y) ⇒ I15(x)
        J21(x,y) ⇒ I14(y)
        J21(x,y) ⇒ J2(x,y)

    """

    j21_concluded_provenance: List[I14ProvenanceBelief] = Field(
        default=None,
        min_length=1,
        description='J21 concluded provenance (was assessed by)',
    )


# ******************************************************************************************************************* #


class J22InterpretedMeaningOf(PropertyMixin):
    """'J22 interpreted meaning of (was interpreted by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J22

    Domain:
        I16 Meaning Comprehension
    Range:
        E73 Information Object
    SubProperty Of:
        E7 Activity. P16 used specific object (was used for): E70 Thing
    SuperProperty Of:
        -
    Quantification:
        many to many, necessary (1,n:0,n)

    Scope Note:
        This property associates an instance of I16 Meaning Comprehension with the instance of E73 Information
        Object that was the source of or evidence for the interpretation of its intended meaning. If sources are
        fragmentary about or complementary to a specific topic, more than one source may have been used.

    Properties:
        -
    Examples:
        - My understanding of the statements about Emperor Nero's whereabouts in Rome while it was burning
          from July 19 in 64 AD (I16) interpreted meaning of the extant book De Vita Caesarum by Gaius
          Suetonius Tranquillus.

    In First Order Logic:
        J22(x,y) ⇒ I16(x)
        J22(x,y) ⇒ E73(y)
        J22(x,y) ⇒ P16(x,y)

    """

    j22_interpreted_meaning_of: List[E73InformationObject] = Field(
        default=None,
        min_length=1,
        description='J22 interpreted meaning of (was interpreted by)',
    )


# ******************************************************************************************************************* #


class J23InterpretedMeaningAs(PropertyMixin):
    """'J23 interpreted meaning as (was interpretation by)' CRMinf property;

    https://cidoc-crm.org/extensions/crminf/html/CRMinf_v1.0.html#J23

    Domain:
        I16 Meaning Comprehension
    Range:
        I13 Intended Meaning Belief
    SubProperty Of:
        I1 Argumentation. J2 concluded that (was concluded by): I2 Belief
    SuperProperty Of:
        -
    Quantification:
        one to many, necessary, dependent (1,n:1,1)

    Scope Note:
        This property associates an instance of I16 Meaning Comprehension with the instance of I13 Intended
        Meaning Belief that was the result of the interpretation of the intended meaning of the analysed
        source(s).

    Properties:
        -
    Examples:
        - My understanding of the statements about Emperor Nero's whereabouts in Rome while it was burning
          from July 19 in 64 AD (I16) *interpreted meaning as* believing that it meant Nero was singing in
          Rome while it was burning from July 19 in 64 AD (I13).

    In First Order Logic:
        J23(x,y) ⇒ I16(x)
        J23(x,y) ⇒ I13(y)
        J23(x,y) ⇒ J2(x,y)

    """

    j23_interpreted_meaning_as: List[I13IntendedMeaningBelief] = Field(
        default=None,
        min_length=1,
        description='J23 interpreted meaning as (was interpretation by)',
    )
