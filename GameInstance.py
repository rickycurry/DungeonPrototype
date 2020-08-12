import MapGrid
import Room
from Utils import Pos, Renderer
import Door


class GameInstance:
    def __init__(self):
        self.rooms = []
        self.doors = []
        self.room_counter = 1
        self.door_counter = 1
        self.grid = MapGrid.MapGrid()
        # Here we'll also generate the first room and door(s).

    def ascii_render(self, filename: str):
        bounding_box = self.grid.bounding_box()
        top_left = self.grid.pos_to_index(bounding_box[0])
        bottom_right = self.grid.pos_to_index(bounding_box[1])
        grid_slice = self.grid.grid[top_left[0] - 1:bottom_right[0] + 2, top_left[1] - 1:bottom_right[1] + 2]
        Renderer.render_map(grid_slice, filename)
