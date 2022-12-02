#! /usr/bin/env python

from collections import namedtuple

Play = namedtuple("Play", ["elf", "me"])

class Hand:
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

class Result:
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"

hand_score = {
    Hand.ROCK: 1,
    Hand.PAPER: 2,
    Hand.SCISSORS: 3
}

my_hand_given_elf_and_result_map = {
    Hand.ROCK: {
        Result.LOSE: Hand.SCISSORS,
        Result.DRAW: Hand.ROCK,
        Result.WIN: Hand.PAPER,
    },
    Hand.PAPER: {
        Result.LOSE: Hand.ROCK,
        Result.DRAW: Hand.PAPER,
        Result.WIN: Hand.SCISSORS,
    },
    Hand.SCISSORS: {
        Result.LOSE: Hand.PAPER,
        Result.DRAW: Hand.SCISSORS,
        Result.WIN: Hand.ROCK,
    },
}

def _parse_hand(raw_hand):
    if raw_hand in ["A", "X"]:
        return Hand.ROCK

    if raw_hand in ["B", "Y"]:
        return Hand.PAPER

    return Hand.SCISSORS

def parse_input(input):
    parsed_input = []

    raw_plays = [play.split() for play in input.strip().splitlines()]

    for play in raw_plays:
        elf_hand = _parse_hand(play[0])
        me_hand = _parse_hand(play[1])
        parsed_play = Play(elf=elf_hand, me=me_hand)
        parsed_input.append(parsed_play)

    return parsed_input

def _is_a_draw(play):
    return play.me == play.elf

def _I_win(play):
    elf_hand = play.elf
    my_hand = play.me

    return (
        (my_hand == Hand.ROCK and elf_hand == Hand.SCISSORS) or
        (my_hand == Hand.PAPER and elf_hand == Hand.ROCK) or
        (my_hand == Hand.SCISSORS and elf_hand == Hand.PAPER)
    )

def _calculate_play_score(play):
    if _is_a_draw(play):
        return 3

    if _I_win(play):
        return 6

    return 0


def _calculate_score_for_plays(plays):
    score = 0

    for play in plays:
        score += hand_score[play.me]
        score += _calculate_play_score(play)

    return score

def calculate_my_score(input):
    plays = parse_input(input)
    score = _calculate_score_for_plays(plays)
    return score

def _parse_elf_hand_needed_result(raw_play):
    elf_hand = _parse_hand(raw_play[0])
    needed_result = raw_play[1]
    my_hand = my_hand_given_elf_and_result_map[elf_hand][needed_result]

    return Play(elf=elf_hand, me=my_hand)

def parse_elf_hand_needed_result_input(input):
    raw_plays = [play.split() for play in input.strip().splitlines()]

    plays = []
    for raw_play in raw_plays:
        play = _parse_elf_hand_needed_result(raw_play)
        plays.append(play)

    return plays

def calculate_my_score_with_elf_result_input_format(input):
    plays = parse_elf_hand_needed_result_input(input)
    score = _calculate_score_for_plays(plays)
    return score

if __name__ == "__main__":
    from input.input_two import INPUT

    my_total_score = calculate_my_score(INPUT)
    print(f"my total score: {my_total_score}")

    my_total_score_with_elf_result_input_format = calculate_my_score_with_elf_result_input_format(INPUT)
    print(f"my total score with elf result input format: {my_total_score_with_elf_result_input_format}")
