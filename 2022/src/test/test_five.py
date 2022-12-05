from src.five import split_input, parse_stacks, parse_procedure, top_crates_after_procedure, top_crates_after_procedure_with_cratemover_9001


def test_split_input_in_starting_stacks_and_rearrangement_procedure():
    test_input = (
"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)

    stacks, procedure = split_input(test_input)

    assert stacks == (
"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3\
"""
)

    assert procedure == (
"""\
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)

def test_returns_stacks_for_one_stack_with_one_crate():
    test_input = (
"""
[A]
1\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == { "1": ["A"] }

def test_returns_stacks_for_two_stack_with_one_crate_each():
    test_input = (
"""
[A] [B]
 1   2\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == {
        "1": ["A"],
        "2": ["B"]
    }

def test_returns_stacks_for_one_stack_without_crates():
    test_input = (
"""
    \n\
 1\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == {
        "1": [],
    }

def test_returns_stacks_for_many_stack_without_crates():
    test_input = (
"""
    [A]     [B]    \n\
 1   2   3   4   5\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == {
        "1": [],
        "2": ["A"],
        "3": [],
        "4": ["B"],
        "5": []
    }

def test_returns_stacks_for_one_stack_with_many_crates():
    test_input = (
"""
[A]
[B]
[C]
1\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == { "1": ["C", "B", "A"] }

def test_returns_stacks_for_many_stack_with_many_crates():
    test_input = (
"""
    [D]    \n\
[N] [C]    \n\
[Z] [M] [P]
 1   2   3\
"""
)
    stacks = parse_stacks(test_input)

    assert stacks == {
        "1": ["Z", "N"],
        "2": ["M", "C", "D"],
        "3": ["P"]
    }

def test_parse_procedure_with_one_step():
    test_input = "move 1 from 2 to 3"

    procedure = parse_procedure(test_input)

    assert procedure == [ (1, "2", "3") ]

def test_parse_procedure_with_many_steps():
    test_input = """\
move 1 from 2 to 3
move 4 from 5 to 6
"""

    procedure = parse_procedure(test_input)

    assert procedure == [
        (1, "2", "3"),
        (4, "5", "6")
    ]

def test_returns_top_crates_after_rearrange_procedure_for_two_stacks_and_one_procedure_step_with_one_crate():
    test_input = (
"""
    [D]
[N] [C]
[Z] [M]
 1   2

move 1 from 2 to 1
"""
)
    result = top_crates_after_procedure(test_input)

    assert result == "DC"

def test_returns_top_crates_after_rearrange_procedure_for_two_stacks_and_one_procedure_step_with_many_crate():
    test_input = (
"""
    [D]
[N] [C]
[Z] [M]
 1   2

move 2 from 2 to 1
"""
)
    result = top_crates_after_procedure(test_input)

    assert result == "CM"

def test_returns_top_crates_after_rearrange_procedure_for_many_stacks_and_many_procedure_step_with_many_crates():
    test_input = (
"""
    [D]    \n\
[N] [C]    \n\
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)

    result = top_crates_after_procedure(test_input)

    assert result == "CMZ"

def test_returns_top_crates_after_rearrange_procedure_for_two_stacks_and_one_procedure_step_with_one_crate_with_cratemover_9001():
    test_input = (
"""
    [D]
[N] [C]
[Z] [M]
 1   2

move 1 from 2 to 1
"""
)
    result = top_crates_after_procedure_with_cratemover_9001(test_input)

    assert result == "DC"

def test_returns_top_crates_after_rearrange_procedure_for_two_stacks_and_one_procedure_step_with_many_crates_with_cratemover_9001():
    test_input = (
"""
    [D]
[N] [C]
[Z] [M]
 1   2

move 2 from 2 to 1
"""
)
    result = top_crates_after_procedure_with_cratemover_9001(test_input)

    assert result == "DM"

def test_returns_top_crates_after_rearrange_procedure_for_many_stacks_and_many_procedures_step_with_many_crates_with_cratemover_9001():
    test_input = (
"""
    [D]    \n\
[N] [C]    \n\
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
)
    result = top_crates_after_procedure_with_cratemover_9001(test_input)

    assert result == "MCD"
