import re

class CRT:
    def draw(self, x_values):
        out = ""

        for index in range(len(x_values)):
            if index == 0:
                out = f"{out}#"
                continue

            x_position = index % 40
            x_value = x_values[index-1]

            if x_position in [x_value-1, x_value, x_value+1]:
                out = f"{out}#"
            else:
                out = f"{out}."

            if (index+1) % 40 == 0:
                out = f"{out}\n"

        return out

class CPU:
    ADDX_INSTRUCTION_RE = re.compile(r"addx (-?\d+)")

    def __init__(self, input):
        self.x_value = 1
        self.x_values = []
        self.instructions = self._parse_input(input)

    def run(self):
        for instruction in self.instructions:
            self._run_instruction(instruction)

    def get_signal_strength_during_key_cycles(self):
        key_cycles = [20, 60, 100, 140, 180, 220]
        signal_strengths = list()
        for cycle in key_cycles:
            index = cycle - 2
            x_value = self.x_values[index]
            signal_strength = cycle * x_value
            signal_strengths.append(signal_strength)

        return signal_strengths

    def get_signal_strength_sum(self):
        return sum(self.get_signal_strength_during_key_cycles())

    def _run_instruction(self, instruction):
        if instruction == "noop":
            self._noop()

        addx_match = self.ADDX_INSTRUCTION_RE.match(instruction)
        if addx_match:
            self._addx(int(addx_match.group(1)))

    def _addx(self, value):
        self._end_cycle()
        self.x_value += value
        self._end_cycle()

    def _noop(self):
        self._end_cycle()

    def _end_cycle(self):
        self.x_values.append(self.x_value)

    def get_x_values(self):
        return self.x_values

    def _parse_input(self, input):
        return input.strip().splitlines()

if __name__ == "__main__":
    from input.input_ten import INPUT

    cpu = CPU(INPUT)
    cpu.run()
    signal_strength_sum = cpu.get_signal_strength_sum()
    print(f"signal_strength_sum: {signal_strength_sum}")

    crt = CRT()
    print(crt.draw(cpu.get_x_values()))
