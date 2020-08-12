import numpy as np
import Room
import Door
from Utils import Pos, get_room_code, get_door_code

GRID_SIZE = 1000


class MapGrid:
    def __init__(self):
        self.size = GRID_SIZE
        self.grid = np.zeros((self.size, self.size), dtype=np.uint16)  # should only occupy 2 MB, not bad!

    # let's say (0, 0) is halfway. [500, 500].
    def pos_to_index(self, pos: Pos):
        x = pos.x + int(self.size / 2)
        y = pos.y + int(self.size / 2)
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise IndexError("Position extends beyond grid boundary.")
        return int(y), int(x)  # because indexing is (row, col)

    def index_to_pos(self, x: int, y: int):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise IndexError("Index extends beyond grid boundary.")
        return Pos(x - int(self.size / 2), y - int(self.size / 2))

    def add_room(self, room: Room) -> bool:
        if not self.can_place_room(room):
            return False
        position_list: list = room.get_area_offsets()
        for pos in position_list:
            index = self.pos_to_index(pos)
            self.grid[index] |= room.code
        return True

    def can_place_room(self, room: Room) -> bool:
        position_list: list = room.get_area_offsets()
        for pos in position_list:
            index = self.pos_to_index(pos)
            if get_room_code(self.grid[index]) != 0:
                return False
        return True

    def add_door(self, door: Door) -> bool:
        # We'll mark door codes on the grid as 8 big bits and rooms as 8 small bits (up to 256 of each for now).
        # Note that this approach enforces only one door per grid cell, which might be bad!
        # There has to be a room on at least one of the two door positions.
        if not self.can_place_door(door):
            return False
        index_one = self.pos_to_index(door.pos_one)
        index_two = self.pos_to_index(door.pos_two)
        self.grid[index_one] |= door.code << 8
        self.grid[index_two] |= door.code << 8
        return True

    def can_place_door(self, door: Door) -> bool:
        index_one = self.pos_to_index(door.pos_one)
        index_two = self.pos_to_index(door.pos_two)
        code_one = self.grid[index_one]
        code_two = self.grid[index_two]
        # need both spaces to be door-less and at least one needs to be a room
        # AND both room codes cannot be the same
        return get_door_code(code_one) == 0 and get_door_code(code_two) == 0 \
            and (get_room_code(code_one) != 0 or get_room_code(code_two) != 0) \
            and (get_room_code(code_one)) != get_room_code(code_two)

    def bounding_box(self) -> tuple:
        nonzero_indices = np.nonzero(self.grid)
        if nonzero_indices[0].shape == (0,):
            raise ValueError("Attempting to get bounding box of empty grid.")
        left = np.amin(nonzero_indices[1])
        right = np.amax(nonzero_indices[1])
        top = np.amin(nonzero_indices[0])
        bottom = np.amax(nonzero_indices[0])
        return self.index_to_pos(left, top), self.index_to_pos(right, bottom)
