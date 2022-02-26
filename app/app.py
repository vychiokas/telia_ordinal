from enum import Enum, auto
from typing import List


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))


class Ordinal(ExtendedEnum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


def two_ordinal_cancel_each_other(ordinal_1: str, ordinal_2: str) -> bool:
    if not all(i in Ordinal.list() for i in [ordinal_1, ordinal_2]):
        raise ValueError
    if (ordinal_1 == Ordinal(1).name and ordinal_2 == Ordinal(2).name) or (
        ordinal_1 == Ordinal(2).name and ordinal_2 == Ordinal(1).name
    ):
        return True
    elif (ordinal_1 == "EAST" and ordinal_2 == "WEST") or (
        ordinal_1 == "WEST" and ordinal_2 == "EAST"
    ):
        return True
    else:
        return False


class OrdinalOptimizer:
    def __init__(self, coordinates: List[str]):
        self.coordinates = coordinates

    def solve(self):
        if len(self.coordinates) == 0:
            return []

        new_list = []
        i = 0
        while(i < len(self.coordinates)):

            current = self.coordinates[i]
            try:
                next = self.coordinates[i+1]
            except IndexError:
                next = None
            
            if next is not None:
                if two_ordinal_cancel_each_other(current, next):
                    i = i + 1
                else:
                    new_list.append(current)
            else:
                new_list.append(current)
            i = i + 1
            
        if len(new_list) == len(self.coordinates):
            return new_list
        
        else:
            self.coordinates = new_list
            return self.solve()

oo = OrdinalOptimizer(["NORTH", "WEST", "EAST", "SOUTH"])
print(oo.solve())