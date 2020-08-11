import numpy as np
import Room
from Utils import Pos


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
        return x, y

    def index_to_pos(self, x: int, y: int):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            raise IndexError("Index extends beyond grid boundary.")
        return Pos(x - self.size / 2, y - self.size / 2)

    def add_room(self, room: Room) -> bool:
        if self.can_place_room(room):
            position_list: list = room.get_area_offsets()
            for pos in position_list:
                x, y = self.pos_to_index(pos)
                self.grid[x, y] = room.code
            return True
        else:
            return False

    def can_place_room(self, room: Room) -> bool:
        position_list: list = room.get_area_offsets()
        for pos in position_list:
            x, y = self.pos_to_index(pos)
            if self.grid[x, y] != 0:
                return False
        return True
