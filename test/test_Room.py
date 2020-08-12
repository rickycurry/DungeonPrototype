import unittest
from unittest import TestCase

import Room
from Utils import Pos


class TestRectangleRoom(unittest.TestCase):
    def test_init_bad_corners(self):
        with self.assertRaises(ValueError):
            Room.RectangleRoom(1, Pos(5, 5), Pos(4, 4))

    def test_get_area_offsets(self):
        rectangle_room = Room.RectangleRoom(1, Pos(1, 1), Pos(4, 4))
        self.assertEqual(16, len(rectangle_room.get_area_offsets()))

    def test_max_doors(self):
        room = Room.RectangleRoom(1, Pos(0, 0), Pos(1, 1))
        self.assertEqual(4, room.max_doors())


class TestCircleRoom(unittest.TestCase):
    def test_get_area_offsets(self):
        circle_room = Room.CircleRoom(1, Pos(3, 8), 5)
        self.assertEqual(97, len(circle_room.get_area_offsets()))
