"""Tests for A2 Stratigraphic Volume Unit;

"""

# pylint: disable=E0401,C0116,W0612

import pytest
from pydantic import ValidationError
from tests.cidoc.crmarchaeo.helpers import make_a2, make_s20_kwargs

from pyheritage.cidoc.core.entities import (
    E1CRMEntity,
    E18PhysicalThing,
    E41Appellation,
    E53Place,
    E57Material,
)
from pyheritage.cidoc.crmarchaeo.entities import (
    A2StratigraphicVolumeUnit,
    A8StratigraphicUnit,
)
from pyheritage.cidoc.crmarchaeo.properties import (
    AP11HasPhysicalRelationTo,
    AP15IsOrContainsRemainsOf,
    AP21Contains,
)
from pyheritage.cidoc.crmsci.entities import S10MaterialSubstantial


class TestA2StratigraphicVolumeUnit:

    def test_crm_code(self) -> None:
        """Verify CRM code is A2;"""
        assert A2StratigraphicVolumeUnit.crm_code == 'A2'

    # ------------------------- #

    def test_crm_label(self) -> None:
        """Verify CRM label matches A2 Stratigraphic Volume Unit;"""
        assert A2StratigraphicVolumeUnit.crm_label == 'A2 Stratigraphic Volume Unit'

    # ------------------------- #

    def test_inherits_from_a8(self) -> None:
        """Verify A2 inherits from A8 Stratigraphic Unit;"""
        assert issubclass(A2StratigraphicVolumeUnit, A8StratigraphicUnit)

    # ------------------------- #

    def test_inherits_from_e1(self) -> None:
        """Verify A2 inherits from E1 CRM Entity;"""
        assert issubclass(A2StratigraphicVolumeUnit, E1CRMEntity)

    # ------------------------- #

    def test_mro_includes_ap11(self) -> None:
        """Verify AP11 Has Physical Relation To mixin is in A2 MRO;"""
        assert AP11HasPhysicalRelationTo in A2StratigraphicVolumeUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap15(self) -> None:
        """Verify AP15 Is or Contains Remains Of mixin is in A2 MRO;"""
        assert AP15IsOrContainsRemainsOf in A2StratigraphicVolumeUnit.__mro__

    # ------------------------- #

    def test_mro_includes_ap21(self) -> None:
        """Verify AP21 Contains mixin is in A2 MRO;"""
        assert AP21Contains in A2StratigraphicVolumeUnit.__mro__

    # ------------------------- #

    def test_id_auto_generated(self) -> None:
        """Verify UUID @id is auto-generated on creation;"""
        entity = make_a2()
        assert entity.id is not None

    # ------------------------- #

    def test_id_unique_per_instance(self) -> None:
        """Verify each instance gets a unique UUID;"""
        a = make_a2()
        b = make_a2()

        assert a.id != b.id

    # ------------------------- #

    def test_ap15_field_exists(self) -> None:
        """Verify ap15_is_or_contains_remains_of field exists;"""
        entity = make_a2()
        assert hasattr(entity, 'ap15_is_or_contains_remains_of')

    # ------------------------- #

    def test_ap15_accepts_s10(self) -> None:
        """Verify AP15 accepts S10 Material Substantial instances;"""
        remains = S10MaterialSubstantial(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Volcanic ash')],
            o15_occupied=E53Place(p157_is_at_rest_relative_to=[]),
        )
        entity = A2StratigraphicVolumeUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Layer A')],
            **make_s20_kwargs(),
            ap15_is_or_contains_remains_of=[remains],
        )

        assert entity.ap15_is_or_contains_remains_of is not None
        assert isinstance(entity.ap15_is_or_contains_remains_of[0], S10MaterialSubstantial)

    # ------------------------- #

    def test_ap15_rejects_invalid_type(self) -> None:
        """Verify AP15 raises ValidationError for non-S10 values;"""
        with pytest.raises(ValidationError):
            A2StratigraphicVolumeUnit(
                ap15_is_or_contains_remains_of=['invalid'],
                **make_s20_kwargs(),
            )

    # ------------------------- #

    def test_ap21_field_exists(self) -> None:
        """Verify ap21_contains field exists;"""
        entity = make_a2()
        assert hasattr(entity, 'ap21_contains')

    # ------------------------- #

    def test_ap21_accepts_e18(self) -> None:
        """Verify AP21 accepts E18 Physical Thing instances;"""
        find = E18PhysicalThing(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Stone tool')],
            p45_consists_of=[E57Material()],
            p53_has_former_or_current_location=[],
            p196_defines=make_s20_kwargs()['p196_defines'],
        )
        entity = A2StratigraphicVolumeUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Layer A')],
            **make_s20_kwargs(),
            ap21_contains=[find],
        )

        assert entity.ap21_contains is not None
        assert isinstance(entity.ap21_contains[0], E18PhysicalThing)

    # ------------------------- #

    def test_ap21_rejects_invalid_type(self) -> None:
        """Verify AP21 raises ValidationError for non-E18 values;"""
        with pytest.raises(ValidationError):
            A2StratigraphicVolumeUnit(
                ap21_contains=['invalid'],
                **make_s20_kwargs(),
            )

    # ------------------------- #

    def test_can_be_created_with_appellation(self) -> None:
        """Verify A2 can be created with an E41 Appellation;"""
        entity = A2StratigraphicVolumeUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Layer A — pumice')],
            **make_s20_kwargs(),
        )

        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Layer A — pumice'

    # ------------------------- #

    def test_model_dump_includes_properties(self) -> None:
        """Verify model_dump includes id, AP15, and AP21 fields;"""
        entity = make_a2()
        data = entity.model_dump()

        assert 'id' in data
        assert 'ap15_is_or_contains_remains_of' in data
        assert 'ap21_contains' in data

    # ------------------------- #

    def test_json_serialization(self) -> None:
        """Verify JSON serialization with by_alias includes @id;"""
        entity = make_a2('Layer A — pumice')
        json_str = entity.model_dump_json(by_alias=True)
        assert '@id' in json_str
        assert 'Layer A' in json_str
