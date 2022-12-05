import re

NO_CRATE = "/"

class Procedure:
    def __init__(self, quantity, source, destination):
        self.quantity = quantity
        self.source = source
        self.destination = destination

def parse_stacks(input):
    raw_lines = input.splitlines()
    stack_names = raw_lines[-1].split()
    lines = (
        input
            .replace("]    ", f"] [{NO_CRATE}]")
            .replace("    [", f"[{NO_CRATE}] [")
            .replace("    \n", f" [{NO_CRATE}]\n")
            .replace("     ", f" [{NO_CRATE}] ")
            .replace("   ", f"[{NO_CRATE}]")
            .strip()
            .splitlines()
    )

    stacks = dict()
    for i in range(len(stack_names)):
        stacks[stack_names[i]] = list()
        for line in lines[:-1]:
            crates = line.split()
            if crates[i][1] == NO_CRATE:
                continue
            stacks[stack_names[i]].insert(0, crates[i][1])

    return stacks

def parse_procedure(input):
    regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

    matches = list(map(regex.match, input.splitlines()))

    return [(int(a_match.group(1)), a_match.group(2), a_match.group(3)) for a_match in matches]

def split_input(input):
    return input.split("\n\n")

def parse_input(input):
    stacks, procedure = split_input(input)

    return parse_stacks(stacks), parse_procedure(procedure)

def top_crates_after_procedure(input):
    stacks, _procedures = parse_input(input)
    procedures = [Procedure(*p) for p in _procedures]

    for p in procedures:
        for _ in range(p.quantity):
            crate = stacks[p.source].pop()
            stacks[p.destination].append(crate)

    top_crates = list()
    for stack in stacks.values():
        top_crates.append(stack[-1])

    return "".join(top_crates)

def top_crates_after_procedure_with_cratemover_9001(input):
    stacks, _procedures = parse_input(input)
    procedures = [Procedure(*p) for p in _procedures]

    for p in procedures:
        crates = list()
        for _ in range(p.quantity):
            crates.append(stacks[p.source].pop())

        crates.reverse()
        stacks[p.destination].extend(crates)

    top_crates = list()
    for stack in stacks.values():
        top_crates.append(stack[-1])

    return "".join(top_crates)


if __name__ == "__main__":
    from input.input_five import INPUT

    top_crates = top_crates_after_procedure(INPUT)
    print(f"top crates: {top_crates}")

    top_crates_with_cratemover_9001 = top_crates_after_procedure_with_cratemover_9001(INPUT)
    print(f"top_crates with cratemover 9001: {top_crates_with_cratemover_9001}")
