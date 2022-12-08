import pytest
from src.eight import count_visible_trees_from_outside, calculate_highest_scenic_score

def test_returns_number_of_visible_trees_for_2x2_grid():
    test_input = """\
12
34\
"""

    num_visible_trees = count_visible_trees_from_outside(test_input)

    assert num_visible_trees == 4

@pytest.mark.parametrize(("input", "expected_result"), [
("""\
123
153
123\
""", 9),
("""\
123
155
123\
""", 9),
("""\
123
113
123\
""", 8),
("""\
123
213
123\
""", 8),
])
def test_returns_number_of_visible_trees_for_3x3_grid(input, expected_result):
    num_visible_trees = count_visible_trees_from_outside(input)

    assert num_visible_trees == expected_result

def test_returns_number_of_visible_trees_for_example_grid():
    test_input = """\
30373
25512
65332
33549
35390\
"""
    num_visible_trees = count_visible_trees_from_outside(test_input)

    assert num_visible_trees == 21

@pytest.mark.parametrize(("input", "expected_result"), [
("""\
123
153
123\
""", 1),
("""\
123
155
123\
""", 1),
("""\
123
113
123\
""", 1),
("""\
123
113
213\
""", 1),
])
def test_returns_the_highest_scenic_score_for_3x3_grid(input, expected_result):

    score = calculate_highest_scenic_score(input)

    assert score == expected_result

def test_returns_the_highest_scenic_score_for_example_grid():
    test_input = """\
30373
25512
65332
33549
35390\
"""
    score = calculate_highest_scenic_score(test_input)

    assert score == 8
