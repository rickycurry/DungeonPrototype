from enum import Enum
from Utils import Pos


class Orientation(Enum):
    north_south = 1
    east_west = 2


class DoorConnectedness(Enum):
    single = 1
    double = 2


class Door:
    def __init__(self, code: int, pos_one: Pos, pos_two: Pos) -> None:
        self.code = code
        self.pos_one = pos_one
        self.pos_two = pos_two
        # check to make sure that pos_one and pos_two are adjacent
        x_diff = pos_one.x - pos_two.x
        y_diff = pos_one.y - pos_two.y
        if x_diff == 1 or x_diff == -1:
            self.orientation = Orientation.east_west
        elif y_diff == 1 or y_diff == -1:
            self.orientation = Orientation.north_south
        else:
            raise ValueError("Door positions are not adjacent.")

    def generate_room(self):
        if self.connectedness == DoorConnectedness.double:
            raise ValueError("Attempting to attach to a door that already has two rooms.")
        # The room we generate here needs to contain self.pos_two. I think maybe this needs to
        # make a call to the MapGrid so that it has the spatial information it needs to
        # generate a new room. Alternatively, we can pass in a grid slice of some "max" size
        # as an argument to this function so the logic can happen here, but it probably makes
        # more sense to keep the logic in the grid.

        # Instead of having this function, we'll make an "add_room(room)" function that just
        # takes the room the grid generates and attaches it to the door.
