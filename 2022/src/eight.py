class Grid:
    def __init__(self, input):
        self.grid = self._parse_grid(input)

    def get_tree_height(self, row, column):
        return self.grid[row][column]

    @property
    def num_rows(self):
        return len(self.grid)

    @property
    def num_columns(self):
        return len(self.grid[0])

    @property
    def max_row_index(self):
        return self.num_rows - 1

    @property
    def max_column_index(self):
        return self.num_columns - 1

    def get_column_trees(self, column_index):
        return [self.grid[idx][column_index] for idx in range(self.num_rows)]

    def get_row_trees(self, row_index):
        return [self.grid[row_index][idx] for idx in range(self.num_columns)]

    def _parse_grid(self, input):
        lines = input.strip().splitlines()
        grid = list()

        for line in lines:
            grid.append(list(map(int, line)))

        return grid

    def __str__(self):
        out = ""

        for row in self.grid:
            for tree in row:
                out = f"{out}{tree}"
            out = f"{out}\n"

        return out

def is_tree_visible(grid, row_index, column_index):
    if row_index == 0 or column_index == 0:
        return True

    if row_index >= grid.max_row_index or column_index >= grid.max_column_index:
        return True

    tree_height = grid.get_tree_height(row_index, column_index)
    row_trees = grid.get_row_trees(row_index)
    column_trees = grid.get_column_trees(column_index)

    visible_from_left = all([height < tree_height for height in row_trees[:column_index]])
    visible_from_right = all([height < tree_height for height in row_trees[column_index+1:]])
    visible_from_top = all([height < tree_height for height in column_trees[:row_index]])
    visible_from_bottom = all([height < tree_height for height in column_trees[row_index+1:]])

    is_visible = any([
        visible_from_left,
        visible_from_right,
        visible_from_top,
        visible_from_bottom
    ])

    return is_visible

def calculate_scenic_score(grid, row_index, column_index):
    left_score = 0
    right_score = 0
    top_score = 0
    bottom_score = 0

    tree_height = grid.get_tree_height(row_index, column_index)
    row_trees = grid.get_row_trees(row_index)
    column_trees = grid.get_column_trees(column_index)

    if column_index < grid.max_column_index:
        for height in reversed(row_trees[:column_index]):
            left_score += 1
            if height >= tree_height:
                break

    if column_index > 0:
        for height in row_trees[column_index+1:]:
            right_score += 1
            if height >= tree_height:
                break

    if row_index < grid.max_row_index:
        for height in reversed(column_trees[:row_index]):
            top_score += 1
            if height >= tree_height:
                break

    if row_index > 0:
        for height in column_trees[row_index+1:]:
            bottom_score += 1
            if height >= tree_height:
                break

    return left_score * right_score * top_score * bottom_score

def count_visible_trees_from_outside(input):
    grid = Grid(input)

    number_of_visible_trees = 0

    for row_index in range(grid.num_rows):
        for column_index in range(grid.num_columns):
            if is_tree_visible(grid, row_index, column_index):
                number_of_visible_trees += 1

    return number_of_visible_trees

def calculate_highest_scenic_score(input):
    grid = Grid(input)

    highest_scenic_score = 0
    for row_index in range(grid.num_rows):
        for column_index in range(grid.num_columns):
            score = calculate_scenic_score(grid, row_index, column_index)
            if score > highest_scenic_score:
                highest_scenic_score = score

    return highest_scenic_score


if __name__ == "__main__":
    from input.input_eight import INPUT

    visible_trees_from_outside_count = count_visible_trees_from_outside(INPUT)
    print(f"visible_trees_from_outside_count: {visible_trees_from_outside_count}")

    highest_scenic_score = calculate_highest_scenic_score(INPUT)
    print(f"highest_scenic_score: {highest_scenic_score}")
