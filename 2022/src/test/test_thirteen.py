import pytest
from src.thirteen import get_ordered_pairs_indexes, sort_packets, get_decoder_key

@pytest.mark.parametrize(("input", "expected_output"),[
    ("[1]\n[2]", [1]),
    ("[2]\n[1]", []),
])
def test_returns_indexes_of_ordered_pairs_for_plain_lists_of_one_element(input, expected_output):
    indexes = get_ordered_pairs_indexes(input)

    assert indexes == expected_output

@pytest.mark.parametrize(("input", "expected_output"),[
    ("[1, 2]\n[2, 3]", [1]),
    ("[2, 1]\n[1, 2]", []),
    ("[1, 1]\n[1, 2]", [1]),
    ("[1, 2, 3]\n[1, 2]", []),
    ("[1, 2]\n[1, 2, 3]", [1]),
    ("[1, 2, 3]\n[2, 2]", [1]),
    ("[2, 2]\n[1, 2, 3]", []),
    ("[]\n[1, 2, 3]", [1]),
    ("[2, 2]\n[]", []),
])
def test_returns_indexes_of_ordered_pairs_for_plain_lists_of_many_elements(input, expected_output):
    indexes = get_ordered_pairs_indexes(input)

    assert indexes == expected_output

@pytest.mark.parametrize(("input", "expected_output"),[
    ("[[1]]\n[[2]]", [1]),
    ("[[3]]\n[[2]]", []),
    ("[[1, 2]]\n[[1, 3]]", [1]),
    ("[[2, 2]]\n[[1, 3]]", []),
    ("[[1]]\n[[1, 2]]", [1]),
    ("[[1, 2]]\n[[1]]", []),
    ("[[1],[1]]\n[[1],[2]]", [1]),
    ("[[1],[3]]\n[[1],[2]]", []),
    ("[[1],[1, 1]]\n[[1],[1]]", []),
    ("[[1],[1]]\n[[1],[1, 1]]", [1]),
])
def test_returns_indexes_of_ordered_pairs_for_lists_of_lists(input, expected_output):
    indexes = get_ordered_pairs_indexes(input)

    assert indexes == expected_output

@pytest.mark.parametrize(("input", "expected_output"),[
    ("[[1]]\n[2]", [1]),
    ("[[2]]\n[1]", []),
    ("[[1, 1]]\n[1]", []),
    ("[[1]]\n[1, 1]", [1]),
    ("[[[1], 2]]\n[[1, 1]]", [])
])
def test_returns_indexes_of_ordered_pairs_for_mix_of_lists_and_integers(input, expected_output):
    indexes = get_ordered_pairs_indexes(input)

    assert indexes == expected_output

def test_returns_indexes_of_ordered_pairs_for_example_input():
    input = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    indexes = get_ordered_pairs_indexes(input)

    assert indexes == [1, 2, 4, 6]

def test_sum_of_indexes_of_ordered_pairs_for_example_input():
    input = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    indexes = get_ordered_pairs_indexes(input)

    input = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    sorted_packets = sort_packets(input)

    assert sorted_packets == [
    [],
    [[]],
    [[[]]],
    [1,1,3,1,1],
    [1,1,5,1,1],
    [[1],[2,3,4]],
    [1,[2,[3,[4,[5,6,0]]]],8,9],
    [1,[2,[3,[4,[5,6,7]]]],8,9],
    [[1],4],
    [[2]],
    [3],
    [[4,4],4,4],
    [[4,4],4,4,4],
    [[6]],
    [7,7,7],
    [7,7,7,7],
    [[8,7,6]],
    [9]
]

def test_returns_decoder_key():
    input = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""

    key = get_decoder_key(input)

    assert key == 140
