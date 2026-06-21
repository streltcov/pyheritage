# -*- coding: utf-8 -*-

"""Tests for D11 Digital Measurement Event;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_s4_kwargs

from pyheritage.cidoc.core.entities import E1CRMEntity
from pyheritage.cidoc.crmdig.entities import (
    D7DigitalMachineEvent,
    D9DataObject,
    D11DigitalMeasurementEvent,
)
from pyheritage.cidoc.crmdig.properties import L20HasCreated
from pyheritage.cidoc.crmsci.entities import S21Measurement


class TestD11DigitalMeasurementEvent:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D11';"""
        assert D11DigitalMeasurementEvent.crm_code == 'D11'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D11 Digital Measurement Event';"""
        assert D11DigitalMeasurementEvent.crm_label == 'D11 Digital Measurement Event'

    # ------------------------- #

    def test_inherits_from_d7(self) -> None:
        """Verify D11 inherits from D7 Digital Machine Event;"""
        assert issubclass(D11DigitalMeasurementEvent, D7DigitalMachineEvent)

    # ------------------------- #

    def test_inherits_from_s21(self) -> None:
        """Verify D11 inherits from S21 Measurement;"""
        assert issubclass(D11DigitalMeasurementEvent, S21Measurement)

    # ------------------------- #

    def test_mro_includes_l20(self) -> None:
        """Verify L20 (has created) mixin is in D11 MRO;"""
        assert L20HasCreated in D11DigitalMeasurementEvent.__mro__

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify D11 ultimately inherits from E1 CRM Entity;"""
        assert issubclass(D11DigitalMeasurementEvent, E1CRMEntity)

    # ------------------------- #

    def test_l20_can_set_value(self) -> None:
        """Verify L20 (has created) accepts D9 Data Object;"""
        obj = D11DigitalMeasurementEvent(**make_s4_kwargs('D11'))
        data = D9DataObject()
        obj.l20_has_created = [data]
        assert obj.l20_has_created == [data]

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D11 can be instantiated with required kwargs;"""
        kwargs = make_s4_kwargs('D11')
        obj = D11DigitalMeasurementEvent(**kwargs)
        assert obj.id is not None
