import pytest
from src.two import parse_input, Hand, Play, calculate_my_score, parse_elf_hand_needed_result_input, calculate_my_score_with_elf_result_input_format


def test_returns_list_of_tuples_as_a_result_of_parsing_the_input():
    test_input = """
    A X
    B Y
    C Z
    A Y
    C X
    """

    parsed_input = parse_input(test_input)

    assert parsed_input == [
        Play(elf=Hand.ROCK, me=Hand.ROCK),
        Play(elf=Hand.PAPER, me=Hand.PAPER),
        Play(elf=Hand.SCISSORS, me=Hand.SCISSORS),
        Play(elf=Hand.ROCK, me=Hand.PAPER),
        Play(elf=Hand.SCISSORS, me=Hand.ROCK),
    ]

@pytest.mark.parametrize("test_input, expected_score", [
    ("A Z", 3),
    ("B X", 1),
    ("C Y", 2)
])
def test_returns_my_total_score_for_one_play_when_I_lose(test_input, expected_score):
    my_score = calculate_my_score(test_input)

    assert my_score == expected_score

@pytest.mark.parametrize("test_input, expected_score", [
    ("A X", 4),
    ("B Y", 5),
    ("C Z", 6)
])
def test_returns_my_total_score_for_one_play_when_I_draw(test_input, expected_score):
    my_score = calculate_my_score(test_input)

    assert my_score == expected_score

@pytest.mark.parametrize("test_input, expected_score", [
    ("A Y", 8),
    ("B Z", 9),
    ("C X", 7)
])
def test_returns_my_total_score_for_one_play_when_I_win(test_input, expected_score):
    my_score = calculate_my_score(test_input)

    assert my_score == expected_score

def test_returns_my_total_score_for_many_plays():
    test_input = """
    A Z
    B Y
    C X
    """

    my_score = calculate_my_score(test_input)

    assert my_score == 15

def test_converts_elf_hand_needed_result_input_to_list_of_plays():
    test_input = """
    A X
    A Y
    A Z
    B X
    B Y
    B Z
    C X
    C Y
    C Z
    """

    parsed_input = parse_elf_hand_needed_result_input(test_input)

    assert parsed_input == [
        Play(elf=Hand.ROCK, me=Hand.SCISSORS),
        Play(elf=Hand.ROCK, me=Hand.ROCK),
        Play(elf=Hand.ROCK, me=Hand.PAPER),
        Play(elf=Hand.PAPER, me=Hand.ROCK),
        Play(elf=Hand.PAPER, me=Hand.PAPER),
        Play(elf=Hand.PAPER, me=Hand.SCISSORS),
        Play(elf=Hand.SCISSORS, me=Hand.PAPER),
        Play(elf=Hand.SCISSORS, me=Hand.SCISSORS),
        Play(elf=Hand.SCISSORS, me=Hand.ROCK),
    ]

def test_returns_my_total_score_for_many_plays_with_elf_result_input_format():
    test_input = """
    A Y
    B X
    C Z
    """

    my_score = calculate_my_score_with_elf_result_input_format(test_input)

    assert my_score == 12
