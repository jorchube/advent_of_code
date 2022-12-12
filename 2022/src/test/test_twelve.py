from src.twelve import parse_input, shortest_path, Position, shortest_path_from_any_a

def test_parses_input():
    input = """
Sa
zE
"""

    grid = parse_input(input)

    assert grid[0][0] == Position(height="S", row=0, column=0)
    assert grid[0][1] == Position(height="a", row=0, column=1)
    assert grid[1][0] == Position(height="z", row=1, column=0)
    assert grid[1][1] == Position(height="E", row=1, column=1)

def test_returns_shortest_path_to_destination_for_one_row():
    input = "SbcdefghijklmnopqrstuvwxyE"

    grid = parse_input(input)
    path = shortest_path(grid)

    assert len(path) == 26

def test_returns_shortest_path_to_destination_for_many_rows():
    input = """
zzzzzzzzzjkzzzzzqrstuvwxyE
SbcdefghijkzzzzzzrszzzzzzE
zzzzzzzzzjklmnopqrszzzzzzE
"""

    grid = parse_input(input)
    path = shortest_path(grid)

    assert len(path) == 29

def test_returns_shortest_path_to_destination_for_many_rows_with_going_to_lower_heights():
    input = """
zzzzzzzzzjkzdefghijklmnzzzE
SbcdefghijkzcbzzzrsrqpozzzE
zzzzzzzzzjklmazzzqrstuvwxyE
"""

    grid = parse_input(input)
    path = shortest_path(grid)

    assert len(path) == 38

def test_returns_minimum_moves_to_destination_for_example_input():
    input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

    grid = parse_input(input)
    path = shortest_path(grid)

    moves = len(path) - 1

    assert moves == 31

def test_returns_minimum_moves_to_destination_from_any_a_height_position_for_example_input():
    input = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

    grid = parse_input(input, reverse=True)
    path = shortest_path_from_any_a(grid)

    moves = len(path) - 1

    assert moves == 29
