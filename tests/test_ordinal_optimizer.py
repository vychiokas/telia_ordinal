from app.app import TeliaChallenge


def test_1():
    oo = TeliaChallenge(["NORTH", "WEST", "EAST", "SOUTH"])
    assert oo.path_reduce() == []


def test_2():
    oo = TeliaChallenge([])
    assert oo.path_reduce() == []


def test_3():
    oo = TeliaChallenge(["NORTH", "EAST", "SOUTH"])
    assert oo.path_reduce() == ["NORTH", "EAST", "SOUTH"]