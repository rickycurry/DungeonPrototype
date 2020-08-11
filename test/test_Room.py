import unittest
import Room
from Utils import Pos


class TestRectangleRoom(unittest.TestCase):
    def test_init_bad_corners(self):
        with self.assertRaises(ValueError):
            Room.RectangleRoom(1, Pos(5, 5), Pos(4, 4))

    def test_get_area_offsets(self):
        rectangle_room = Room.RectangleRoom(1, Pos(1, 1), Pos(4, 4))
        self.assertEqual(len(rectangle_room.get_area_offsets()), 16)


class TestCircleRoom(unittest.TestCase):
    def test_init_not_half_coord(self):
        with self.assertRaises(ValueError):
            Room.CircleRoom(1, Pos(2, 8), 5.5)

    def test_init_not_half_radius(self):
        with self.assertRaises(ValueError):
            Room.CircleRoom(1, Pos(3.5, 8.5), 4)

    def test_get_area_offsets(self):
        circle_room = Room.CircleRoom(1, Pos(3.5, 8.5), 5.5)
        self.assertEqual(len(circle_room.get_area_offsets()), 109)
