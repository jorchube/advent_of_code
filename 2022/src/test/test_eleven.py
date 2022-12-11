from src.eleven import Monkey, parse_monkeys, play_keep_away, calculate_monkey_business


def test_parses_input_for_one_monkey():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""

    monkeys = parse_monkeys(input)

    assert len(monkeys) == 1
    assert monkeys[0] == Monkey(start_items=[79, 98], worry_level=lambda old: old * 19, test_divisible_by=23, if_true_throw_to=2, if_false_throw_to=3)

def test_parses_input_for_many_monkeys():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

    monkeys = parse_monkeys(input)

    assert len(monkeys) == 4
    assert monkeys[0] == Monkey(start_items=[79, 98], worry_level=lambda old: old * 19, test_divisible_by=23, if_true_throw_to=2, if_false_throw_to=3)
    assert monkeys[1] == Monkey(start_items=[54, 65, 75, 74], worry_level=lambda old: old + 6, test_divisible_by=19, if_true_throw_to=2, if_false_throw_to=0)
    assert monkeys[2] == Monkey(start_items=[79, 60, 97], worry_level=lambda old: old * old, test_divisible_by=13, if_true_throw_to=1, if_false_throw_to=3)
    assert monkeys[3] == Monkey(start_items=[74], worry_level=lambda old: old + 3, test_divisible_by=17, if_true_throw_to=0, if_false_throw_to=1)

def test_worry_levels_after_one_round():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

    monkeys = parse_monkeys(input)
    monkeys = play_keep_away(monkeys, 1)

    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

def test_worry_levels_after_twenty_rounds():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

    monkeys = parse_monkeys(input)
    monkeys = play_keep_away(monkeys, 20)

    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []

def test_returns_number_of_inspections_after_20_rounds():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

    monkeys = parse_monkeys(input)
    monkeys = play_keep_away(monkeys, 20)

    assert monkeys[0].get_number_of_inspections() == 101
    assert monkeys[1].get_number_of_inspections() == 95
    assert monkeys[2].get_number_of_inspections() == 7
    assert monkeys[3].get_number_of_inspections() == 105

def test_returns_monkey_business_level():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
    monkey_business = calculate_monkey_business(input, 20, 3)

    assert monkey_business == 10605

def test_returns_monkey_business_level_after_10000_rounds_with_no_worry_level_decrease():
    input = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
    monkey_business = calculate_monkey_business(input, 10000, None)

    assert monkey_business == 2713310158
