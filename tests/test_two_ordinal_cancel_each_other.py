from app.app import two_ordinal_cancel_each_other
import pytest


def test_north_south_returns_true():
    assert two_ordinal_cancel_each_other("NORTH", "SOUTH") is True


def test_north_east_returns_false():
    assert two_ordinal_cancel_each_other("NORTH", "EAST") is False


def test_west_east_returns_false():
    assert two_ordinal_cancel_each_other("WEST", "EAST") is True


def test_south_east_returns_false():
    assert two_ordinal_cancel_each_other("SOUTH", "EAST") is False


def test_raises_exception_with_incorrect_values():
    with pytest.raises(ValueError):
        two_ordinal_cancel_each_other(1, "EAST")
