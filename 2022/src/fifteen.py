import re
from tqdm import tqdm
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

    def distance_to_position(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def distance_to_beacon(self):
        return self.distance_to_position(self.beacon.x, self.beacon.y)

    def get_covered_area_perimeter_vertices(self):
        distance_to_beacon = self.distance_to_beacon()
        perimeter = list()

        perimeter.append((self.x - distance_to_beacon, self.y))
        perimeter.append((self.x, self.y + distance_to_beacon))
        perimeter.append((self.x + distance_to_beacon, self.y))
        perimeter.append((self.x, self.y - distance_to_beacon))

        return perimeter

    def get_surrounding_positions(self):
        vertices = self.get_covered_area_perimeter_vertices()
        positions = set()

        left_vertex = vertices[0]
        top_vertex = vertices[1]
        right_vertex = vertices[2]
        bottom_vertex = vertices[3]

        current_position = (left_vertex[0]-1, left_vertex[1])
        target_position = (top_vertex[0], top_vertex[1]+1)
        while current_position != target_position:
            positions.add(current_position)
            current_position = (current_position[0]+1, current_position[1]+1)

        current_position = target_position
        target_position = (right_vertex[0]+1, right_vertex[1])
        while current_position != target_position:
            positions.add(current_position)
            current_position = (current_position[0]+1, current_position[1]-1)

        current_position = target_position
        target_position = (bottom_vertex[0], bottom_vertex[1]-1)
        while current_position != target_position:
            positions.add(current_position)
            current_position = (current_position[0]-1, current_position[1]-1)

        current_position = target_position
        target_position = (left_vertex[0]-1, left_vertex[1])
        while current_position != target_position:
            positions.add(current_position)
            current_position = (current_position[0]-1, current_position[1]+1)

        return positions

    def positions_covered_for_row(self, row):
        positions = set()
        distance_to_beacon = self.distance_to_beacon()

        if abs(row - self.y) > distance_to_beacon:
            return positions

        start_position = (self.x, row)
        x_offset = 0
        coverage_completed = False
        while not coverage_completed:
            left_added = False
            right_added = False

            position_to_the_left = (start_position[0] - x_offset, start_position[1])
            if self.distance_to_position(position_to_the_left[0], position_to_the_left[1]) <= distance_to_beacon:
                positions.add(position_to_the_left)
                left_added = True

            position_to_the_right = (start_position[0] + x_offset, start_position[1])
            if self.distance_to_position(position_to_the_right[0], position_to_the_right[1]) <= distance_to_beacon:
                positions.add(position_to_the_right)
                right_added = True

            x_offset += 1

            if (left_added and right_added) is False:
                coverage_completed = True

        return positions

    def get_covered_area(self):
        positions = list()
        distance_to_beacon = self.distance_to_beacon()
        for radius in range(1, distance_to_beacon+1):
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

def _discard_positions_occupied_by_sensors_and_beacons(positions, sensors):
    for sensor in sensors:
        sensor_position = (sensor.x, sensor.y)
        beacon_position = (sensor.beacon.x, sensor.beacon.y)

        positions.discard(sensor_position)
        positions.discard(beacon_position)

    return positions

def get_positions_without_beacon_at_row(sensors, row):
    positions = set()
    print("Getting positions without beacon:")
    for sensor in tqdm(sensors):
        positions.update(sensor.positions_covered_for_row(row))

    positions = _discard_positions_occupied_by_sensors_and_beacons(positions, sensors)

    return positions

def _position_is_outside_all_sensor_areas(sensors, position):
    x = position[0]
    y = position[1]

    return all([sensor.distance_to_beacon() < sensor.distance_to_position(x, y) for sensor in sensors])

def _calculate_frequency(position):
    x = position[0]
    y = position[1]

    return (x * 4000000) + y

def get_beacon_frequency(sensors, max_x, max_y):
    candidate_positions = set()
    print("Getting candidate positions:")
    for sensor in tqdm(sensors):
        surrounding_positions = sensor.get_surrounding_positions()
        for position in surrounding_positions:
            if position[0] >= 0 and position[0] <= max_x and position[1] >= 0 and position[1] <= max_y:
                candidate_positions.add(position)

    print("Searching position outside all sensor areas:")
    for position in tqdm(candidate_positions):
        if _position_is_outside_all_sensor_areas(sensors, position):
            return _calculate_frequency(position)

def locate_beacon(sensors, frequency, max_x, max_y):
    x_base = 4000000
    candidate_positions = set()

    for x in range(max_x):
        x_component = x * x_base
        if x_component > frequency:
            break
        y = frequency - x_component
        candidate_positions.add((x, y))

    positions = _discard_positions_occupied_by_sensors_and_beacons(candidate_positions, sensors)

    assert len(positions) == 1
    return positions[0]

def get_positions_without_beacon_at_row__slow_as_fuck(sensors, row):
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
    print(f"num positions_without_beacon: {len(positions_without_beacon)}")

    sensors = parse_input(INPUT)
    beacon_frequency = get_beacon_frequency(sensors, 4000000, 4000000)
    print(f"beacon_frequency: {beacon_frequency}")
