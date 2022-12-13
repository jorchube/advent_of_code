import json

class Packet:
    def __init__(self, data):
        self.data = data

    def __lt__(self, other):
        return is_pair_ordered(self.data, other.data)

def parse_pair(pair):
    packets = pair.strip().splitlines()
    return (json.loads(packets[0]), json.loads(packets[1]))

def parse_input(input):
    pairs = input.strip().split("\n\n")

    return [parse_pair(pair) for pair in pairs]

def are_same_input(e1, e2):
    return e1 == e2

def is_pair_ordered(left, right):
    if type(left) == type(right) == int:
        if left == right:
            return None
        return left < right

    if type(left) == int:
        left = [left]

    if type(right) == int:
        right = [right]

    for elements in zip(left, right):
        e0 = elements[0]
        e1 = elements[1]
        ordered = is_pair_ordered(e0, e1)
        if ordered == None:
            continue

        return ordered

    if len(left) == len(right):
        return None

    return len(left) < len(right)

def get_ordered_pairs_indexes(input):
    pairs = parse_input(input)

    ordered_pairs_indexes = list()
    for index, pair in enumerate(pairs, start=1):
        if is_pair_ordered(pair[0], pair[1]):
            ordered_pairs_indexes.append(index)

    return ordered_pairs_indexes

def sort_packets(input):
    pairs = parse_input(input)
    packets = list()

    for pair in pairs:
        packets.append(Packet(pair[0]))
        packets.append(Packet(pair[1]))

    packets.append(Packet([[2]]))
    packets.append(Packet([[6]]))

    sorted_packets = sorted(packets)

    return [packet.data for packet in sorted_packets]

def get_decoder_key(input):
    packets = sort_packets(input)

    index1 = packets.index([[2]]) + 1
    index2 = packets.index([[6]]) + 1

    return index1 * index2

if __name__ == "__main__":
    from input.input_thirteen import INPUT

    ordered_pairs_indexes = get_ordered_pairs_indexes(INPUT)
    print(f"sum ordered_pairs_indexes: {sum(ordered_pairs_indexes)}")

    decoder_key = get_decoder_key(INPUT)
    print(f"decoder_key: {decoder_key}")
