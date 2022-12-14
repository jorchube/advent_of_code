from copy import deepcopy
from itertools import chain


class Coordinate:
    def __init__(self, raw_coordinate):
        components = raw_coordinate.split(",")
        self.x = int(components[0].strip())
        self.y = int(components[1].strip())

    def __str__(self):
        return f"{self.x},{self.y}"

class SandUnit:
    def __init__(self, coordinate):
        self.x = coordinate.x
        self.y = coordinate.y
        self.out_of_bounds = False

    def fall(self, cave):
        if self._can_fall_vertically(cave):
            self.y += 1
            return

        if self._can_fall_to_the_left(cave):
            self.y += 1
            self.x -= 1
            return

        if self._can_fall_to_the_right(cave):
            self.y += 1
            self.x += 1
            return

    def _can_fall_vertically(self, cave):
        try:
            return cave.get_tile(self.x, self.y+1) == "."
        except IndexError:
            return True

    def _can_fall_to_the_left(self, cave):
        try:
            return cave.get_tile(self.x-1, self.y+1) == "."
        except IndexError:
            return True

    def _can_fall_to_the_right(self, cave):
        try:
            return cave.get_tile(self.x+1, self.y+1) == "."
        except IndexError:
            return True

    def is_out_of_bounds(self, cave):
        return (
            self.x < 0 or
            self.x > cave.max_x or
            self.y < 0 or
            self.y > cave.max_y
        )

    def is_at_rest(self, cave):
        return (
            not self._can_fall_vertically(cave) and
            not self._can_fall_to_the_left(cave) and
            not self._can_fall_to_the_right(cave)
        )

class Cave:
    def __init__(self, coordinates):
        self.sand_source = Coordinate("500,0")
        normalized_coordiniates = self._normalize(coordinates)
        self.grid = self._build_from_coordinates(normalized_coordiniates)

    @property
    def max_x(self):
        return len(self.grid[0]) - 1

    @property
    def max_y(self):
        return len(self.grid) - 1

    def fall_one_sand(self):
        sand = SandUnit(self.sand_source)
        while not sand.is_at_rest(self) and not sand.is_out_of_bounds(self):
            sand.fall(self)

        if not sand.is_out_of_bounds(self):
            self.grid[sand.y][sand.x] = "o"

    def pour_sand(self):
        previous_sand_units = 0
        self.fall_one_sand()
        current_sand_units = self.count_sand_units()
        while previous_sand_units != current_sand_units:
            self.fall_one_sand()
            previous_sand_units = current_sand_units
            current_sand_units = self.count_sand_units()

    def count_sand_units(self):
        count = 0
        for row in self.grid:
            for tile in row:
                if tile == "o":
                    count += 1
        return count

    def __getitem__(self, index):
        return self.grid[index]

    def get_tile(self, x, y):
        return self.grid[y][x]

    def _normalize(self, coordinates):
        x_components = [coord.x for coord in chain(*coordinates, [self.sand_source])]
        y_components = [coord.y for coord in chain(*coordinates, [self.sand_source])]

        min_x = min(x_components)
        min_y = min(y_components)

        self.sand_source.x -= min_x
        self.sand_source.y -= min_y

        for line in coordinates:
            for coordinate in line:
                coordinate.x -= min_x
                coordinate.y -= min_y

        return coordinates

    def _build_from_coordinates(self, coordinates):
        grid = self._create_grid(coordinates)
        self._draw_rock_paths(coordinates, grid)
        self._draw_sand_source(grid)
        return grid

    def _draw_sand_source(self, grid):
        grid[self.sand_source.y][self.sand_source.x] = "+"

    def _draw_rock_paths(self, coordinates, grid):
        for line in coordinates:
            self._draw_path(line, grid)

    def _draw_path(self, line, grid):
        start = line[0]
        for end in line[1:]:
            self._draw_line(start, end, grid)
            start = end

    def _draw_line(self, line_start, line_end, grid):
        if line_start.x == line_end.x:
            start, end = sorted([line_start.y, line_end.y])
            for y in range(start, end+1):
                grid[y][line_start.x] = "#"

        if line_start.y == line_end.y:
            start, end = sorted([line_start.x, line_end.x])
            for x in range(start, end+1):
                grid[line_start.y][x] = "#"

    def _create_grid(self, coordinates):
        x_components = [coord.x for coord in chain(*coordinates)]
        y_components = [coord.y for coord in chain(*coordinates)]

        width = max(x_components) + 1
        height = max(y_components) + 1

        grid = list()
        for _ in range(height):
            grid.append(["."] * width)

        return grid

    def draw_for_fun(self):
        return self._draw_grid(self.grid)

    def _draw_grid(self, grid):
        out = ""
        for row in grid:
            for tile in row:
                out = f"{out}{tile}"
            out = f"{out}\n"
        return out


class CaveWithFloor(Cave):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self._fill_bottom_rows()

    def fall_one_sand(self):
        if self.grid[self.sand_source.y][self.sand_source.x] != "o":
            return super().fall_one_sand()

    def pour_sand(self):
        while self.grid[self.sand_source.y][self.sand_source.x] != "o":
            self.fall_one_sand()

    def _fill_bottom_rows(self):
        width = self.max_x + 1
        self.grid.append(["."] * width)
        self.grid.append(["#"] * width)

    def get_tile(self, x, y):
        if x < 0:
            self._extend_to_the_left()

        if x > self.max_x:
            self._extend_to_the_right()

        return super().get_tile(x, y)

    def _extend_to_the_left(self):
        for row in self.grid:
            row.insert(0, ".")

        self.grid[self.max_y][0] = "#"
        self.sand_source.x += 1

    def _extend_to_the_right(self):
        for row in self.grid:
            row.append(".")

        self.grid[self.max_y][self.max_x] = "#"

def parse_input(input, cave_has_floor=False):
    lines = input.strip().splitlines()

    coordinates = [
        [Coordinate(raw_coordinate) for raw_coordinate in line.split(" -> ")] for line in lines
    ]

    if cave_has_floor:
        return CaveWithFloor(coordinates)
    return Cave(coordinates)

if __name__ == "__main__":
    from input.input_fourteen import INPUT

    cave = parse_input(INPUT)
    cave.pour_sand()
    # print(cave.draw_for_fun())
    number_of_sand_units_at_rest = cave.count_sand_units()
    print(f"number_of_sand_units_at_rest: {number_of_sand_units_at_rest}")

    cave = parse_input(INPUT, cave_has_floor=True)
    cave.pour_sand()
    # print(cave.draw_for_fun())
    number_of_sand_units_at_rest_with_floor = cave.count_sand_units()
    print(f"number_of_sand_units_at_rest_with_floor: {number_of_sand_units_at_rest_with_floor}")
