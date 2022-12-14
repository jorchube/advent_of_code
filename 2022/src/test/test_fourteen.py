from src.fourteen import parse_input


def test_returns_a_cave_when_parsing_input():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
........#.
#########.
"""

    cave = parse_input(input)

    assert cave.draw_for_fun() == expected_output

def test_one_unit_of_sand_comes_to_rest():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.
"""

    cave = parse_input(input)
    cave.fall_one_sand()

    assert cave.draw_for_fun() == expected_output

def test_four_units_of_sand_comes_to_rest():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
.....ooo#.
#########.
"""

    cave = parse_input(input)
    cave.fall_one_sand()
    cave.fall_one_sand()
    cave.fall_one_sand()
    cave.fall_one_sand()

    assert cave.draw_for_fun() == expected_output

def test_pours_sand():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.
"""

    cave = parse_input(input)
    cave.pour_sand()

    assert cave.draw_for_fun() == expected_output

def test_counts_sand_units_at_rest():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    cave = parse_input(input)
    cave.pour_sand()

    assert cave.count_sand_units() == 24

def test_returns_a_cave_with_floor_when_parsing_input():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
........#.
#########.
..........
##########
"""

    cave = parse_input(input, cave_has_floor=True)

    assert cave.draw_for_fun() == expected_output

def test_pours_sand_until_sand_source_is_blocked():
    input = """
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    expected_output = """\
..........o...........
.........ooo..........
........ooooo.........
.......ooooooo........
......oo#ooo##o.......
.....ooo#ooo#ooo......
....oo###ooo#oooo.....
...oooo.oooo#ooooo....
..oooooooooo#oooooo...
.ooo#########ooooooo..
ooooo.......ooooooooo.
######################
"""

    cave = parse_input(input, cave_has_floor=True)
    cave.pour_sand()

    assert cave.draw_for_fun() == expected_output
