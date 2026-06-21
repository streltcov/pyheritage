# -*- coding: utf-8 -*-

"""Tests for D29 Annotation Object;

"""

# pylint: disable=E0401,C0116,W0612

from pyheritage.cidoc.core.entities import E1CRMEntity, E89PropositionalObject
from pyheritage.cidoc.crmdig.entities import D29AnnotationObject
from pyheritage.cidoc.crmdig.properties import L43Annotates


class TestD29AnnotationObject:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D29';"""
        assert D29AnnotationObject.crm_code == 'D29'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D29 Annotation Object';"""
        assert D29AnnotationObject.crm_label == 'D29 Annotation Object'

    # ------------------------- #

    def test_inherits_from_e89(self) -> None:
        """Verify D29 inherits from E89 Propositional Object;"""
        assert issubclass(D29AnnotationObject, E89PropositionalObject)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D29 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D29AnnotationObject, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_l43(self) -> None:
        """Verify L43 (annotates) mixin is in D29 MRO;"""
        assert L43Annotates in D29AnnotationObject.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D29 can be instantiated with auto-generated ID;"""
        obj = D29AnnotationObject()
        assert obj.id is not None
