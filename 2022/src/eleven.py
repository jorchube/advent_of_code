import re
import math

RE_MONKEY = r"""Monkey \d+:
.*Starting items:(.*)
.*Operation: new = old (.*)
.*Test: divisible by (\d+)
.*If true: throw to monkey (\d+)
.*If false: throw to monkey (\d+)"""

class Monkey:
    def __init__(self, start_items, worry_level, test_divisible_by, if_true_throw_to, if_false_throw_to, worry_level_decrease_factor=3):
        self.items = start_items
        self.operation = worry_level
        self.test_divisible_by = test_divisible_by
        self.if_true_throw_to = if_true_throw_to
        self.if_false_throw_to = if_false_throw_to
        self.worry_level_decrease_factor = worry_level_decrease_factor
        self.inspections = 0

    def set_lcm(self, lcm):
        self.lcm = lcm

    def throw_items(self, monkeys):
        while self.items:
            item = self.items.pop(0)
            self._inspect_and_throw(item, monkeys)

    def _inspect_and_throw(self, item, monkeys):
        self.inspections += 1
        worry_level = self.operation(item)

        if self.worry_level_decrease_factor:
            worry_level = int(worry_level / self.worry_level_decrease_factor)
        else:
            worry_level = worry_level % self.lcm

        if worry_level % self.test_divisible_by == 0:
            target = self.if_true_throw_to
        else:
            target = self.if_false_throw_to

        monkeys[target].catch_item(worry_level)

    def catch_item(self, item):
        self.items.append(item)

    def get_number_of_inspections(self):
        return self.inspections

    def __eq__(self, other):
        return (
            self.items == other.items and
            self.operation(1) == other.operation(1) and
            self.test_divisible_by == other.test_divisible_by and
            self.if_true_throw_to == other.if_true_throw_to and
            self.if_false_throw_to == other.if_false_throw_to
        )

def _parse_worry_level(worry_level_input):
    if worry_level_input == "* old":
        return lambda old: old * old

    tokens = worry_level_input.split(" ")
    if tokens[0] == "*":
        return lambda old: old * int(tokens[1])

    if tokens[0] == "+":
        return lambda old: old + int(tokens[1])

def parse_monkeys(input, worry_level_decrease_factor=3):
    matcher = re.compile(RE_MONKEY)

    monkeys = list()

    matches = matcher.finditer(input)
    for match in iter(matches):
        start_items = list(map(int, match.group(1).split(",")))
        worry_level = _parse_worry_level(match.group(2))
        test_divisible_by = int(match.group(3))
        if_true_throw_to = int(match.group(4))
        if_false_throw_to = int(match.group(5))
        monkey = Monkey(
            start_items,
            worry_level,
            test_divisible_by,
            if_true_throw_to,
            if_false_throw_to,
            worry_level_decrease_factor
        )

        monkeys.append(monkey)

    lcm = math.prod(list(map(lambda monkey: monkey.test_divisible_by, monkeys)))
    for monkey in monkeys:
        monkey.set_lcm(lcm)

    return monkeys

def play_keep_away(monkeys, number_of_rounds):
    for i in range(number_of_rounds):
        for monkey in monkeys:
            monkey.throw_items(monkeys)

    return monkeys

def calculate_monkey_business(input, rounds, worry_level_decrease_factor):
    monkeys = parse_monkeys(input, worry_level_decrease_factor)
    monkeys = play_keep_away(monkeys, rounds)

    inspections = list(map(lambda monkey: monkey.get_number_of_inspections(), monkeys))
    top_two = sorted(inspections, reverse=True)[0:2]

    return math.prod(top_two)

if __name__ == "__main__":
    from input.input_eleven import INPUT

    monkey_business = calculate_monkey_business(INPUT, 20, 3)
    print(f"monkey_business: {monkey_business}")

    monkey_business = calculate_monkey_business(INPUT, 10000, None)
    print(f"monkey_business 10000 rounds: {monkey_business}")
