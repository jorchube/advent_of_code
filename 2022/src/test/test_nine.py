from src.nine import Rope, parse_input, LongRope

def test_rope_is_at_initial_position():
    rope = Rope()

    assert rope.get_head_position() == (0, 0)
    assert rope.get_tail_position() == (0, 0)


def test_head_moves_one_step():
    rope = Rope()

    rope.move_head(delta_x=1, delta_y=0)

    assert rope.get_head_position() == (1, 0)
    assert rope.get_tail_position() == (0, 0)


def test_head_moves_two_steps_and_pulls_the_tail():
    rope = Rope()

    rope.move_head(delta_x=1, delta_y=0)
    rope.move_head(delta_x=1, delta_y=0)

    assert rope.get_head_position() == (2, 0)
    assert rope.get_tail_position() == (1, 0)

def test_head_moves_two_steps_vertically_and_pulls_the_tail():
    rope = Rope()

    rope.move_head(delta_x=0, delta_y=-1)
    rope.move_head(delta_x=0, delta_y=-1)

    assert rope.get_head_position() == (0, -2)
    assert rope.get_tail_position() == (0, -1)

def test_head_moves_given_input_with_one_line_and_pulls_tail():
    test_input = "R 4"
    rope = Rope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.get_head_position() == (4, 0)
    assert rope.get_tail_position() == (3, 0)

def test_head_moves_given_input_with_many_lines_and_pulls_tail():
    test_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    rope = Rope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.get_head_position() == (2, 2)
    assert rope.get_tail_position() == (1, 2)

def test_returns_count_of_different_positions_tail_has_been_for_one_input_line():
    test_input = """
R 4
"""
    rope = Rope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.count_tail_positions() == 4

def test_returns_count_of_different_positions_tail_has_been():
    test_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    rope = Rope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.count_tail_positions() == 13

def test_returns_count_of_different_positions_tail_has_been_for_one_input_line_given_a_long_rope():
    test_input = """
R 5
"""
    rope = LongRope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.count_tail_positions() == 1

def test_returns_count_of_different_positions_tail_has_been_given_a_long_rope():
    test_input = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
    rope = LongRope()

    moves = parse_input(test_input)
    rope.bulk_move_head(moves)

    assert rope.count_tail_positions() == 36
