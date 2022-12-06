class Marker:
    LENGTH = None

    def __init__(self):
        self.buffer = list()

    def add_char(self, char):
        self.buffer.insert(0, char)
        if len(self.buffer) > self.LENGTH:
            self.buffer.pop()

    def is_valid(self):
        return len(set(self.buffer)) == self.LENGTH

class PacketMarker(Marker):
    LENGTH = 4

class MessageMarker(Marker):
    LENGTH = 14

def _count_characters_processed_before_first_marker(marker, input):
    for count, char in enumerate(input, start=1):
        marker.add_char(char)
        if marker.is_valid():
            return count

def count_characters_processed_before_first_packet_marker(input):
    marker = PacketMarker()
    return _count_characters_processed_before_first_marker(marker, input)

def count_characters_processed_before_first_message_marker(input):
    marker = MessageMarker()
    return _count_characters_processed_before_first_marker(marker, input)

if __name__ == "__main__":
    from input.input_six import INPUT

    characters_processed_before_first_packet_marker = count_characters_processed_before_first_packet_marker(INPUT)
    print(f"characters processed before first packet marker: {characters_processed_before_first_packet_marker}")

    characters_processed_before_first_message_marker = count_characters_processed_before_first_message_marker(INPUT)
    print(f"characters processed before first message marker: {characters_processed_before_first_message_marker}")
