from copy import deepcopy

class Position:
    def __init__(self, height, row, column):
        self.height = height
        self.row = row
        self.column = column
        self.previous_node = None
        self.moved_to_nodes = list()
        self._is_start = False

    def set_is_start(self):
        self._is_start = True

    def is_start(self):
        return self._is_start

    def can_move_to(self, other):
        return other._height_value() - self._height_value() <= 1

    def already_moved_to(self, other):
        return other in self.moved_to_nodes

    def move_to(self, other):
        self.moved_to_nodes.append(other)

        if other.is_start():
            return

        if other.previous_node is None:
            other.previous_node = self
            return

        if len(other.get_path_from_start()) > len(self.get_path_from_start()) + 1:
            other.previous_node = self

    def get_path_from_start(self):
        path = list()

        node = self
        while node:
            path.insert(0, node)
            node = node.previous_node

        return path

    def _height_value(self):
        if self.height == "S":
            return ord("a")

        if self.height == "E":
            return ord("z")

        return ord(self.height)

    def __eq__(self, other):
        return (
            self.height == other.height and
            self.column == other.column and
            self.row == other.row
        )

class Area:
    def __init__(self, grid):
        self.grid = deepcopy(grid)
        self.max_row = len(self.grid) - 1
        self.max_column = len(self.grid[0]) - 1

    def get_node(self, row, column):
        return self.grid[row][column]

    def get_start_position(self):
        for row_index, row in enumerate(self.grid):
            for column_index, position in enumerate(row):
                if position.height == "S":
                    return row_index, column_index

    def get_next_move_candidates(self, node):
        row = node.row
        column = node.column

        candidates = list()
        if row > 0:
            candidates.append(self.grid[row - 1][column])
        if row < self.max_row:
            candidates.append(self.grid[row + 1][column])
        if column > 0:
            candidates.append(self.grid[row][column - 1])
        if column < self.max_column:
            candidates.append(self.grid[row][column + 1])

        return candidates

class ReverseArea(Area):
    def get_start_position(self):
        for row_index, row in enumerate(self.grid):
            for column_index, position in enumerate(row):
                if position.height == "E":
                    return row_index, column_index


class ReversePosition(Position):
    def can_move_to(self, other):
        return self._height_value() - other._height_value() <= 1


def shortest_path_from_position(area, row, column, end_height=["E"]):
    nodes_to_evaluate = [area.get_node(row, column)]
    while nodes_to_evaluate:
        node = nodes_to_evaluate.pop(0)
        next_move_candidates = area.get_next_move_candidates(node)
        for candidate in next_move_candidates:
            if node.can_move_to(candidate) and not node.already_moved_to(candidate):
                node.move_to(candidate)
                nodes_to_evaluate.append(candidate)
                if candidate.height in end_height:
                    return candidate.get_path_from_start()

def shortest_path(grid):
    area = Area(grid)
    row, column = area.get_start_position()

    area.get_node(row, column).set_is_start()

    return shortest_path_from_position(area, row, column)

def shortest_path_from_any_a(grid):
    area = ReverseArea(grid)
    row, column = area.get_start_position()

    area.get_node(row, column).set_is_start()

    return shortest_path_from_position(area, row, column, end_height=["a", "S"])

def parse_input(input, reverse=False):
    lines = input.strip().splitlines()

    grid = list()

    for row, line in enumerate(lines):
        if reverse:
            row = [ReversePosition(char, row, column) for column, char in enumerate(line)]
        else:
            row = [Position(char, row, column) for column, char in enumerate(line)]
        grid.append(row)

    return grid

if __name__ == "__main__":
    from input.input_twelve import INPUT

    grid = parse_input(INPUT)
    path = shortest_path(grid)
    moves = len(path) - 1
    print(f"fewest moves: {moves}")

    grid = parse_input(INPUT, reverse=True)
    path = shortest_path_from_any_a(grid)
    moves = len(path) - 1
    print(f"fewest moves from any a: {moves}")
