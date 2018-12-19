import pytest
from ssz.tree_hash.tree_hash import hash_tree_root
from ssz.sedes import (
    Boolean,
    uint16,
    uint32_list,
    uint512,
)


@pytest.mark.parametrize(
    'value,expected',
    (
        (True, b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
        (False, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
    ),
)
def test_boolean_serialize_values(value, expected):
    sedes = Boolean()
    assert hash_tree_root(value, sedes) == expected


@pytest.mark.parametrize(
    'value,sedes',
    (
        (0, uint16),
        (56, uint16),
        ([123, 456, 789], uint32_list),
        (55665566, uint512),
        ([], uint32_list)
    ),
)
def test_rich_types_of_data(value, sedes):
    assert len(hash_tree_root(value, sedes)) == 32