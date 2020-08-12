import unittest
import MapGrid
import Room
import Door
from Utils import Pos


class TestMapGrid(unittest.TestCase):
    def setUp(self) -> None:
        self.map_grid = MapGrid.MapGrid()
        self.square_room = Room.RectangleRoom(1, Pos(3, 4), Pos(10, 12))
        self.rectangle_room = Room.RectangleRoom(2, Pos(8, 10), Pos(18, 22))
        self.circle_room = Room.CircleRoom(3, Pos(55, 55), 14)

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

    def test_can_place_door_one_room_success(self):
        self.map_grid.add_room(self.square_room)
        self.assertTrue(self.map_grid.add_door(Door.Door(1, Pos(10, 10), Pos(11, 10))))

    def test_can_place_door_two_rooms_success(self):
        self.map_grid.add_room(self.square_room)
        self.map_grid.add_room(Room.RectangleRoom(2, Pos(11, 4), Pos(14, 9)))
        self.assertTrue(self.map_grid.add_door(Door.Door(1, Pos(10, 8), Pos(11, 8))))

    def test_cannot_place_door_inside_room_failure(self):
        self.map_grid.add_room(self.square_room)
        self.assertFalse(self.map_grid.add_door(Door.Door(1, Pos(5, 6), Pos(6, 7))))

    def test_cannot_place_door_outside_room_failure(self):
        self.map_grid.add_room(self.square_room)
        self.assertFalse(self.map_grid.add_door(Door.Door(1, Pos(22, 22), Pos(23, 22))))

    def test_bounding_box_empty(self):
        with self.assertRaises(ValueError):
            self.map_grid.bounding_box()

    def test_bounding_box_simple(self):
        self.map_grid.add_room(self.square_room)
        bounding_box = self.map_grid.bounding_box()
        self.assertEqual(bounding_box[0], Pos(3, 4))
        self.assertEqual(bounding_box[1], Pos(10, 12))
