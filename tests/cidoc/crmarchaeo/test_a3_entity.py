# -*- coding: utf-8 -*-

"""Tests for A3 Stratigraphic Interface;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import (
    make_a2,
    make_a3,
    make_a8,
    make_s20_kwargs,
)

from pyheritage.cidoc.core.entities import E1CRMEntity, E41Appellation
from pyheritage.cidoc.crmarchaeo.entities import (
    A2StratigraphicVolumeUnit,
    A3StratigraphicInterface,
    A8StratigraphicUnit,
)
from pyheritage.cidoc.crmarchaeo.properties import (
    AP11HasPhysicalRelationTo,
    AP12Confines,
)


class TestA3StratigraphicInterface:

    def test_crm_code(self) -> None:
        """Verify CRM code is A3;"""
        assert A3StratigraphicInterface.crm_code == 'A3'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A3 Stratigraphic Interface;"""
        assert A3StratigraphicInterface.crm_label == 'A3 Stratigraphic Interface'

    # ------------------------- #

    def test_inherits_from_a8(self) -> None:
        """Verify A3 inherits from A8 Stratigraphic Unit;"""
        assert issubclass(A3StratigraphicInterface, A8StratigraphicUnit)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A3 inherits from E1 CRM Entity;"""
        assert issubclass(A3StratigraphicInterface, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap11(self) -> None:
        """Verify AP11 Has Physical Relation To mixin is in A3 MRO;"""
        assert AP11HasPhysicalRelationTo in A3StratigraphicInterface.__mro__

    # ------------------------- #

    def test_mro_includes_ap12(self) -> None:
        """Verify AP12 Confines mixin is in A3 MRO;"""
        assert AP12Confines in A3StratigraphicInterface.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a3()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a3()
        b = make_a3()

        assert a.id != b.id

    # ------------------------- #

    def test_ap12_field_exists(self) -> None:
        """Verify ap12_confines field exists;"""
        entity = make_a3()
        assert hasattr(entity, 'ap12_confines')

    # ------------------------- #

    def test_ap12_accepts_a2(self) -> None:
        """Verify AP12 accepts A2 Stratigraphic Volume Unit instances;"""
        svu = make_a2('Confined SVU')
        entity = A3StratigraphicInterface(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Interface [19]')],
            **make_s20_kwargs(),
            ap12_confines=[svu],
        )

        assert entity.ap12_confines is not None
        assert len(entity.ap12_confines) == 1
        assert isinstance(entity.ap12_confines[0], A2StratigraphicVolumeUnit)

    # ------------------------- #

    def test_ap12_rejects_a8_not_a2(self) -> None:
        """Verify AP12 rejects A8 that is not an A2;"""
        plain_a8 = make_a8('Generic SU')
        with pytest.raises(ValidationError):
            A3StratigraphicInterface(
                ap12_confines=[plain_a8],
                **make_s20_kwargs(),
            )

    # ------------------------- #

    def test_ap12_rejects_invalid_type(self) -> None:
        """Verify AP12 raises ValidationError for non-A2 values;"""
        with pytest.raises(ValidationError):
            A3StratigraphicInterface(
                ap12_confines=['invalid'],
                **make_s20_kwargs(),
            )

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify A3 can be created with an E41 Appellation;"""
        entity = A3StratigraphicInterface(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Interface [19]')],
            **make_s20_kwargs(),
        )

        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Interface [19]'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id and AP12 fields;"""
        entity = make_a3()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap12_confines' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a3('Interface [19]')
        json_str = entity.model_dump_json(by_alias=True)

        assert '@id' in json_str
        assert 'Interface' in json_str
