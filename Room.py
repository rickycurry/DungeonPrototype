import Door
from Utils import Pos
from enum import Enum
import abc
import numpy as np


class Room(abc.ABC):
    def __init__(self, code: int):
        self.code = code

    @abc.abstractmethod
    def get_area_offsets(self) -> list:
        pass

    @abc.abstractmethod
    def max_doors(self) -> int:
        pass


class RectangleRoom(Room):
    def __init__(self, code: int, upper_left: Pos, lower_right: Pos):
        if upper_left.x > lower_right.x or upper_left.y > lower_right.y:
            raise ValueError("Attempting to instantiate a rectangle room with impossible corner positions.")
        super().__init__(code)
        self.upper_left = upper_left
        self.lower_right = lower_right

    def get_area_offsets(self) -> list:
        ret = []
        for x in range(self.upper_left.x, self.lower_right.x + 1):
            for y in range(self.upper_left.y, self.lower_right.y + 1):
                ret.append(Pos(x, y))
        return ret

    def max_doors(self) -> int:
        ns_edge_length = self.lower_right.y - self.upper_left.y + 1
        ew_edge_length = self.lower_right.x - self.upper_left.x + 1
        return 2 * (ns_edge_length + ew_edge_length) - 4  # corners are double-counted


class CircleRoom(Room):
    def __init__(self, code: int, center: Pos, radius: int):
        super().__init__(code)
        self.center = center
        self.radius = radius

    def get_area_offsets(self) -> list:
        ret = []
        sqr_radius = float(self.radius + 0.5)**2
        for x in range(self.center.x - self.radius, self.center.x + self.radius + 1):
            for y in range(self.center.y - self.radius, self.center.y + self.radius + 1):
                sqr_dist = (x - self.center.x)**2 + (y - self.center.y)**2
                if sqr_dist <= sqr_radius:
                    ret.append(Pos(int(x), int(y)))
        return ret

    def max_doors(self) -> int:
        return 4  # The four cardinal walls are the only places we can put doors
