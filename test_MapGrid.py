import unittest
import MapGrid
import Room
from Utils import Pos


class TestMapGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.map_grid = MapGrid.MapGrid()
        self.square_room = Room.RectangleRoom(1, Pos(3, 4), Pos(10, 12))
        self.rectangle_room = Room.RectangleRoom(2, Pos(8, 10), Pos(18, 22))
        self.circle_room = Room.CircleRoom(3, Pos(55.5, 55.5), 14.5)

    def test_add_room(self):
        self.assertTrue(self.map_grid.add_room(self.circle_room))

    def test_add_two_rooms_success(self):
        self.assertTrue(self.map_grid.add_room(self.circle_room))
        self.assertTrue(self.map_grid.add_room(self.square_room))

    def test_add_two_rooms_success_then_failure(self):
        self.assertTrue(self.map_grid.add_room(self.square_room))
        self.assertFalse(self.map_grid.add_room(self.rectangle_room))

    def test_can_place_room_failure(self):
        self.map_grid.add_room(self.square_room)
        self.assertFalse(self.map_grid.can_place_room(self.rectangle_room))
