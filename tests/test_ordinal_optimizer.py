from app.app import OrdinalOptimizer

def test_1():
    oo = OrdinalOptimizer(["NORTH", "WEST", "EAST", "SOUTH"])
    assert oo.solve() == []

def test_2():
    oo = OrdinalOptimizer([])
    assert oo.solve() == []

def test_3():
    oo = OrdinalOptimizer(["NORTH", "EAST", "SOUTH"])
    assert oo.solve() == ["NORTH", "EAST", "SOUTH"]