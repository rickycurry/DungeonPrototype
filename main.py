import sys
import random
import MapGrid
import Room
from Utils import Pos

if __name__ == '__main__':
    # seed = sys.argv[1] if len(sys.argv) > 0 else random.getrandbits(8)  this crashes because of out of range index
    seed = random.getrandbits(8)
    random.seed(seed)
    map_grid = MapGrid.MapGrid()
    circle_room = Room.CircleRoom(1, Pos(2.5, 2.5), 2.5)
    map_grid.add_room(circle_room)
    print(map_grid.grid[498:507, 498:507])
    rectangle_room = Room.RectangleRoom(2, Pos(3, 3), Pos(7, 7))
    print(map_grid.can_place_room(rectangle_room))
    rectangle_room_placeable = Room.RectangleRoom(2, Pos(5, 5), Pos(9, 9))
    print(map_grid.can_place_room(rectangle_room_placeable))
