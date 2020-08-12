import unittest
import GameInstance
import Door
import Room
from Utils import Pos

BASE_FILENAME = "../.idea/ascii_renders/"


class TestGameInstanceRendering(unittest.TestCase):
    def setUp(self) -> None:
        self.gi = GameInstance.GameInstance()
        self.gi.grid.add_room(Room.RectangleRoom(1, Pos(3, 3), Pos(6, 6)))
        self.gi.grid.add_room(Room.RectangleRoom(2, Pos(4, 7), Pos(6, 9)))
        self.gi.grid.add_door(Door.Door(1, Pos(6, 6), Pos(6, 7)))
        self.gi.ascii_render(BASE_FILENAME + "test0.txt")

    def test_render(self):
        self.gi.grid.add_door(Door.Door(2, Pos(6, 5), Pos(7, 5)))
        self.gi.ascii_render(BASE_FILENAME + "test1.txt")
        self.gi.grid.add_door(Door.Door(3, Pos(3, 3), Pos(2, 3)))
        self.gi.grid.add_room(Room.RectangleRoom(3, Pos(-3, -2), Pos(2, 5)))
        self.gi.ascii_render(BASE_FILENAME + "test2.txt")

    def test_render_circle(self):
        self.gi.grid.add_room(Room.CircleRoom(3, Pos(-3, -3), 6))
        self.gi.ascii_render(BASE_FILENAME + "test3.txt")

    def test_render_door_on_left(self):
        self.gi.grid.add_door(Door.Door(2, Pos(3, 4), Pos(2, 4)))
        self.gi.ascii_render(BASE_FILENAME + "test4.txt")

    def test_render_cool_simple_dungeon(self):
        self.gi.grid.add_room(Room.CircleRoom(3, Pos(-3, -3), 6))
        self.gi.grid.add_door(Door.Door(2, Pos(-3, 3), Pos(-3, 4)))
        self.gi.grid.add_room(Room.RectangleRoom(4, Pos(-3, 4), Pos(-3, 5)))
        self.gi.grid.add_door(Door.Door(3, Pos(-3, 5), Pos(-2, 5)))
        self.gi.grid.add_room(Room.RectangleRoom(5, Pos(-2, 5), Pos(2, 5)))
        self.gi.grid.add_door(Door.Door(4, Pos(2, 5), Pos(3, 5)))
        self.gi.ascii_render(BASE_FILENAME + "test5.txt")
