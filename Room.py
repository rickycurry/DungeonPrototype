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


class CircleRoom(Room):
    def __init__(self, code: int, center: Pos, radius: float):
        if center.x % 1 != 0.5 or center.y % 1 != 0.5:
            raise ValueError("Circle center position should be a half-position (x.5, y.5).")
        if radius % 1 != 0.5:
            raise ValueError("Circle radius should be x.5")
        super().__init__(code)
        self.center = center
        self.radius = radius

    def get_area_offsets(self) -> list:
        ret = []
        sq_radius = self.radius**2
        for x in range(int(self.center.x - self.radius), int(self.center.x + self.radius)):
            for y in range(int(self.center.y - self.radius), int(self.center.y + self.radius)):
                # Check all four corners of unit square (also think of a better way to do this)
                sq_dist_ll = (float(x) - self.center.x)**2 + (float(y) - self.center.y)**2
                sq_dist_ul = (float(x) - self.center.x)**2 + (float(y + 1) - self.center.y)**2
                sq_dist_lr = (float(x + 1) - self.center.x)**2 + (float(y) - self.center.y)**2
                sq_dist_ur = (float(x + 1) - self.center.x)**2 + (float(y + 1) - self.center.y)**2
                if sq_dist_ll < sq_radius or sq_dist_ul < sq_radius or sq_dist_lr < sq_radius or sq_dist_ur < sq_radius:
                    ret.append(Pos(int(x), int(y)))
        return ret
