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
        assert A2StratigraphicVolumeUnit.crm_code == 'A2'

    def test_crm_label(self) -> None:
        assert A2StratigraphicVolumeUnit.crm_label == 'A2 Stratigraphic Volume Unit'

    def test_inherits_from_a8(self) -> None:
        assert issubclass(A2StratigraphicVolumeUnit, A8StratigraphicUnit)

    def test_inherits_from_e1(self) -> None:
        assert issubclass(A2StratigraphicVolumeUnit, E1CRMEntity)

    def test_mro_includes_ap11(self) -> None:
        assert AP11HasPhysicalRelationTo in A2StratigraphicVolumeUnit.__mro__

    def test_mro_includes_ap15(self) -> None:
        assert AP15IsOrContainsRemainsOf in A2StratigraphicVolumeUnit.__mro__

    def test_mro_includes_ap21(self) -> None:
        assert AP21Contains in A2StratigraphicVolumeUnit.__mro__

    def test_id_auto_generated(self) -> None:
        entity = make_a2()
        assert entity.id is not None

    def test_id_unique_per_instance(self) -> None:
        a = make_a2()
        b = make_a2()
        assert a.id != b.id

    def test_ap15_field_exists(self) -> None:
        entity = make_a2()
        assert hasattr(entity, 'ap15_is_or_contains_remains_of')

    def test_ap15_accepts_s10(self) -> None:
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

    def test_ap15_rejects_invalid_type(self) -> None:
        with pytest.raises(ValidationError):
            A2StratigraphicVolumeUnit(
                ap15_is_or_contains_remains_of=['invalid'],
                **make_s20_kwargs(),
            )

    def test_ap21_field_exists(self) -> None:
        entity = make_a2()
        assert hasattr(entity, 'ap21_contains')

    def test_ap21_accepts_e18(self) -> None:
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

    def test_ap21_rejects_invalid_type(self) -> None:
        with pytest.raises(ValidationError):
            A2StratigraphicVolumeUnit(
                ap21_contains=['invalid'],
                **make_s20_kwargs(),
            )

    def test_can_be_created_with_appellation(self) -> None:
        entity = A2StratigraphicVolumeUnit(
            p1_is_identified_by=[E41Appellation(p190_has_symbolic_content='Layer A — pumice')],
            **make_s20_kwargs(),
        )
        assert entity.p1_is_identified_by[0].p190_has_symbolic_content.value == 'Layer A — pumice'

    def test_model_dump_includes_properties(self) -> None:
        entity = make_a2()
        data = entity.model_dump()
        assert 'id' in data
        assert 'ap15_is_or_contains_remains_of' in data
        assert 'ap21_contains' in data

    def test_json_serialization(self) -> None:
        entity = make_a2('Layer A — pumice')
        json_str = entity.model_dump_json(by_alias=True)
        assert '@id' in json_str
        assert 'Layer A' in json_str
