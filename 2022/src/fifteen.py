import re
from dataclasses import dataclass

LINE_RE = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"

@dataclass
class Beacon:
    x: int
    y: int

@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon

    def get_covered_area(self):
        positions = list()
        print(f"covered area for sensor at ({self.x},{self.y})")
        distance_to_beacon = abs(self.x - self.beacon.x) + abs(self.y - self.beacon.y)
        print(f" distance to beacon: {distance_to_beacon}")
        for radius in range(1, distance_to_beacon+1):
            print(f"  radius: {radius}") if radius % 100 == 0 else None
            for x_distance in range(radius+1):
                y_distance = radius - x_distance
                self._append_to_covered_area(positions, self.x + x_distance, self.y + y_distance)
                self._append_to_covered_area(positions, self.x + x_distance, self.y - y_distance)
                self._append_to_covered_area(positions, self.x - x_distance, self.y - y_distance)
                self._append_to_covered_area(positions, self.x - x_distance, self.y + y_distance)

        return positions

    def _append_to_covered_area(self, positions, x, y):
        if x == self.beacon.x and y == self.beacon.y:
            return

        position = (x, y)
        if position not in positions:
            positions.append(position)

def parse_line(line):
    matcher = re.compile(LINE_RE)
    a_match = matcher.match(line)

    beacon = Beacon(int(a_match.group(3)), int(a_match.group(4)))
    sensor = Sensor(int(a_match.group(1)), int(a_match.group(2)), beacon)

    return sensor

def get_positions_without_beacon(sensors):
    positions = list()
    for sensor in sensors:
        positions.extend(sensor.get_covered_area())

    return positions

def get_positions_without_beacon_at_row(sensors, row):
    positions = get_positions_without_beacon(sensors)

    sensors_positions = [(s.x, s.y) for s in sensors]
    beacons_positions = [(s.beacon.x, s.beacon.y) for s in sensors]

    positions_at_row = list()
    for position in positions:
        if position[1] != row:
            continue
        if position in positions_at_row:
            continue
        if position in sensors_positions:
            continue
        if position in beacons_positions:
            continue
        positions_at_row.append(position)

    return positions_at_row

def parse_input(input):
    lines = input.strip().splitlines()

    return [parse_line(line) for line in lines]

if __name__ == "__main__":
    from input.input_fifteen import INPUT

    sensors = parse_input(INPUT)
    positions_without_beacon = get_positions_without_beacon_at_row(sensors, 2000000)
    print(f"positions_without_beacon: {positions_without_beacon}")
