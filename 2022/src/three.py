#! /usr/bin/env python

ITEMS = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Group:
    def __init__(self, rucksacks):
        self.rucksacks = rucksacks

    def find_badge(self):
        rucksack_1_items = self.rucksacks[0].items
        rucksack_2_items = self.rucksacks[1].items
        rucksack_3_items = self.rucksacks[2].items

        for item in rucksack_1_items:
            if item in rucksack_2_items and item in rucksack_3_items:
                return item

class Rucksack:
    def __init__(self, input_line):
        compartment_size = int(len(input_line)/2)
        self.items = input_line
        self.compartment_a = input_line[0:compartment_size]
        self.compartment_b = input_line[compartment_size:]

    def find_misplaced_item(self):
        for item in self.compartment_a:
            if item in self.compartment_b:
                return item

def get_priority_for_item(item):
    return ITEMS.index(item)

def parse_rucksacks_from_input(input):
    lines = input.strip().splitlines()
    return [Rucksack(line.strip()) for line in lines]

def calculate_misplaced_items_priority(input):
    rucksacks = parse_rucksacks_from_input(input)

    misplaced_items = [rucksack.find_misplaced_item() for rucksack in rucksacks]
    misplaced_items_priority = map(get_priority_for_item, misplaced_items)

    return sum(misplaced_items_priority)

def group_rucksacks(rucksacks):
    num_rucksacks = len(rucksacks)
    groups = list()

    for index in range(0, num_rucksacks, 3):
        group = Group([rucksacks[index], rucksacks[index+1], rucksacks[index+2]])
        groups.append(group)

    return groups

def calculate_badges_priority(input):
    rucksacks = parse_rucksacks_from_input(input)
    groups = group_rucksacks(rucksacks)

    badges = [group.find_badge() for group in groups]
    badges_priority = map(get_priority_for_item, badges)

    return sum(badges_priority)

if __name__ == "__main__":
    from input.input_three import INPUT

    priorities = calculate_misplaced_items_priority(INPUT)
    print(f"misplaced items priorities: {priorities}")

    badges_priority = calculate_badges_priority(INPUT)
    print(f"badges priority: {badges_priority}")
