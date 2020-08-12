import numpy as np


class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y
        return False


class Renderer:
    # we want to render walls as —, |, +,
    # doors as = (e-w) or || (n-s),
    # and rooms as  1, 56, etc.
    # small example:
    # +----+---------+
    # | 01 = 02   02 |
    # |    |         |
    # | 01 | 02   02 |
    # +-||-+---------+
    # | 03 |
    # |    |
    # | 03 |
    # +----+

    EVEN_H_WALL = "----"
    CORNER = "+"
    V_WALL = "|"
    H_DOOR = "="
    V_DOOR = "-||-"
    ODD_H_WALL = "-"
    ODD_COLUMN_SPACE = " "
    EVEN_COLUMN_SPACE = "    "

    # Odd rows are corners, h-walls, v-walls, and v-doors
    # Even rows are v-walls, h-doors, and room codes
    # Odd columns (1-wide) are corners, v-walls, h-doors, and odd-column-spaces
    # Even columns (4-wide) are even-h-walls, even-column-spaces, v-doors, and room codes
    # Now it should be easy to build the ascii room render!
    @staticmethod
    def code_to_string(code: int) -> str:
        return f" {str(code % 100).zfill(2)} "

    @staticmethod
    def upper_left_wall(ul: int, ur: int, ll: int, lr: int) -> str:
        horizontal_wall = ul != ll or ur != lr
        vertical_wall = ul != ur or ll != lr
        if horizontal_wall and vertical_wall:
            return Renderer.CORNER
        elif ur == lr and ll != lr:
            return Renderer.V_WALL
        elif ur != lr and ll == lr:
            return Renderer.ODD_H_WALL
        else:
            return Renderer.ODD_COLUMN_SPACE

    @staticmethod
    def upper_wall(lower_door: int, upper_door: int, lower_room: int, upper_room: int) -> str:
        if lower_room == upper_room:
            return Renderer.EVEN_COLUMN_SPACE
        elif lower_door == upper_door and lower_door != 0:
            return Renderer.V_DOOR
        else:
            return Renderer.EVEN_H_WALL

    @staticmethod
    def left_wall(left_door: int, right_door: int, left_room: int, right_room: int) -> str:
        if left_room == right_room:
            return Renderer.ODD_COLUMN_SPACE
        elif left_door == right_door and right_door != 0:
            return Renderer.H_DOOR
        else:
            return Renderer.V_WALL

    @staticmethod
    def central_space(room_code: int) -> str:
        if room_code == 0:
            return Renderer.EVEN_COLUMN_SPACE
        else:
            return Renderer.code_to_string(room_code)

    @staticmethod
    def render_map(grid: np.array, filename: str = "map.txt") -> None:
        with open(filename, 'w') as f:
            for row in range(1, grid.shape[0]):
                str_list_odd = []
                str_list_even = []
                for col in range(1, grid.shape[1]):
                    # grab a 2x2 grid with the cell we care about in the bottom right
                    two_by_two = grid[row - 1:row + 1, col - 1:col + 1]
                    two_by_two_rooms = get_room_code(two_by_two)
                    two_by_two_doors = get_door_code(two_by_two)
                    str_list_odd.append(Renderer.upper_left_wall(two_by_two_rooms[0, 0],
                                                                 two_by_two_rooms[0, 1],
                                                                 two_by_two_rooms[1, 0],
                                                                 two_by_two_rooms[1, 1]))
                    str_list_odd.append(Renderer.upper_wall(two_by_two_doors[1, 1],
                                                            two_by_two_doors[0, 1],
                                                            two_by_two_rooms[1, 1],
                                                            two_by_two_rooms[0, 1]))
                    str_list_even.append(Renderer.left_wall(two_by_two_doors[1, 0],
                                                            two_by_two_doors[1, 1],
                                                            two_by_two_rooms[1, 0],
                                                            two_by_two_rooms[1, 1]))
                    str_list_even.append(Renderer.central_space(two_by_two_rooms[1, 1]))
                f.write("".join(str_list_odd))
                f.write('\n')
                f.write("".join(str_list_even))
                f.write('\n')


def get_room_code(number: np.uint16):
    return number & 255  # should return lowest 8 bits


def get_door_code(number: np.uint16):
    return number >> 8
