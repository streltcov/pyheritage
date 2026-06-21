# -*- coding: utf-8 -*-

"""Tests for D30 Annotation Event;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e7_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity, E65Creation
from pyheritage.cidoc.crmdig.entities import D29AnnotationObject, D30AnnotationEvent
from pyheritage.cidoc.crmdig.properties import L48CreatedAnnotation


class TestD30AnnotationEvent:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D30';"""
        assert D30AnnotationEvent.crm_code == 'D30'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D30 Annotation Event';"""
        assert D30AnnotationEvent.crm_label == 'D30 Annotation Event'

    # ------------------------- #

    def test_inherits_from_e65(self) -> None:
        """Verify D30 inherits from E65 Creation;"""
        assert issubclass(D30AnnotationEvent, E65Creation)

    # ------------------------- #

    def test_mro_includes_l48(self) -> None:
        """Verify L48 (created annotation) mixin is in D30 MRO;"""
        assert L48CreatedAnnotation in D30AnnotationEvent.__mro__

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D30 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D30AnnotationEvent, E1CRMEntity)

    # ------------------------- #

    def test_l48_can_set_value(self) -> None:
        """Verify L48 (created annotation) accepts D29 Annotation Object;"""
        obj = D30AnnotationEvent(**make_e7_kwargs('D30'))
        ann = D29AnnotationObject()
        obj.l48_created_annotation = [ann]
        assert obj.l48_created_annotation == [ann]

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D30 can be instantiated with required kwargs;"""
        obj = D30AnnotationEvent(**make_e7_kwargs('D30'))
        assert obj.id is not None
