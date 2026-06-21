# -*- coding: utf-8 -*-

"""Tests for D10 Software Execution;

"""

# pylint: disable=E0401,C0116,W0612

from tests.cidoc.crmdig.helpers import make_e7_kwargs

from pyheritage.cidoc.crmdig.entities import (
    D7DigitalMachineEvent,
    D10SoftwareExecution,
)
from pyheritage.cidoc.crmdig.properties import (
    L2UsedAsSource,
    L13UsedParameters,
    L24CreatedLogfile,
)


class TestD10SoftwareExecution:

    def test_crm_code(self) -> None:
        """Verify CRM code is 'D10';"""
        assert D10SoftwareExecution.crm_code == 'D10'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label is 'D10 Software Execution';"""
        assert D10SoftwareExecution.crm_label == 'D10 Software Execution'

    # ------------------------- #

    def test_inherits_from_d7(self) -> None:
        """Verify D10 inherits from D7 Digital Machine Event;"""
        assert issubclass(D10SoftwareExecution, D7DigitalMachineEvent)

    # ------------------------- #

    def test_mro_includes_l2(self) -> None:
        """Verify L2 (used as source) mixin is in D10 MRO;"""
        assert L2UsedAsSource in D10SoftwareExecution.__mro__

    # ------------------------- #

    def test_mro_includes_l13(self) -> None:
        """Verify L13 (used parameters) mixin is in D10 MRO;"""
        assert L13UsedParameters in D10SoftwareExecution.__mro__

    # ------------------------- #

    def test_mro_includes_l24(self) -> None:
        """Verify L24 (created logfile) mixin is in D10 MRO;"""
        assert L24CreatedLogfile in D10SoftwareExecution.__mro__

    # ------------------------- #

    def test_can_instantiate(self) -> None:
        """Verify D10 can be instantiated with required kwargs;"""
        obj = D10SoftwareExecution(**make_e7_kwargs('D10'))
        assert obj.id is not None
