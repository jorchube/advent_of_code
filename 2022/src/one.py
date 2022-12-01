#! /usr/bin/env python

def parse_input(input):
    split_by_elf = input.split("\n\n")
    parsed_input = []
    for elf_calories in split_by_elf:
        calories_list = list(map(int, elf_calories.split()))
        parsed_input.append(calories_list)

    return parsed_input

def calculate_elf_max_calories(input):
    all_elfs_items = parse_input(input)

    max_calories = 0
    for elf_items in all_elfs_items:
        calories = sum(elf_items)
        if calories > max_calories:
            max_calories = calories

    return max_calories

def calculate_top_three_elfs_max_calories(input):
    all_elfs_items = parse_input(input)

    totals_per_elf = map(sum, all_elfs_items)
    sorted_items = sorted(totals_per_elf, reverse=True)

    return sum(sorted_items[0:3])

if __name__ == "__main__":
    from input.input_one import INPUT

    max_calories = calculate_elf_max_calories(INPUT)
    print(f"max_calories: {max_calories}")

    top_three_calories = calculate_top_three_elfs_max_calories(INPUT)
    print(f"top_three_calories: {top_three_calories}")
