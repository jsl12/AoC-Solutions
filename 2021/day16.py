import itertools

from dataclasses import dataclass, field


def to_bits(input_str: str):
    chars = {f'{i:x}'.upper(): f'{i:04b}' for i in range(16)}
    return ''.join(chars[c] for c in input_str)


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def str_grouper(base_str, n):
    yield from (''.join(chunk) for chunk in grouper(base_str, n, fillvalue=''))


def value_from_bits(bits):
    def gen():
        for group in str_grouper(bits, 5):
            yield group[1:]
            if group[0] == '0':
                break

    groups = list(gen())
    return int(''.join(groups), 2), len(groups)


@dataclass
class Packet:
    bits: str
    nbits: int = field(init=False)
    version: int = field(init=False)
    type: int = field(init=False)

    def __post_init__(self):
        self.nbits = len(self.bits)
        self.version = int(self.bits[:3], 2)
        self.type = int(self.bits[3:6], 2)

    def length_type(self):
        return int(self.bits[6])

    def length(self):
        if self.length_type() == 0:
            return int(self.bits[7:7 + 15], 2)
        elif self.length_type() == 1:
            return int(self.bits[7:7 + 11], 2)
        else:
            raise ValueError(f'Invalid length type: {self.length_type()}')

    def payload_start(self):
        starts = {
            0: 7 + 15,
            1: 7 + 11
        }
        return starts[self.length_type()]

    @property
    def payload_slice(self):
        return slice(
            self.payload_start(),
            self.payload_start() + self.length(),
        )

    @property
    def payload(self):
        return self.bits[self.payload_slice]

    @staticmethod
    def from_hex(input_str):
        bits = to_bits(input_str)
        return Packet.from_bits(bits)

    @staticmethod
    def from_bits(bits):
        def gen():
            base_packet = Packet(bits)

            if base_packet.type == 4:
                yield ValuePacket(bits)
            else:
                yield base_packet
                if base_packet.length_type() == 0:
                    print(f'Payload: {base_packet.length()}bits, {base_packet.payload}')
                    remaining_payload = base_packet.payload[:]
                    while len(remaining_payload) > 0:
                        sub_packet = Packet.from_bits(remaining_payload)[0]
                        yield sub_packet
                        remaining_payload = remaining_payload[sub_packet.len:]
                elif base_packet.length_type() == 1:
                    remaining_payload = base_packet.bits[base_packet.payload_start():]
                    for i in range(base_packet.length()):
                        sub_packet = Packet.from_bits(remaining_payload)[0]
                        yield sub_packet
                        remaining_payload = remaining_payload[sub_packet.len:]

        return list(gen())


@dataclass
class ValuePacket(Packet):
    value: int = field(init=False)

    def __post_init__(self):
        self.value, ngroups = value_from_bits(self.bits[6:])
        self.len = 6 + (5 * ngroups)
        self.bits = self.bits[:self.len]
        super().__post_init__()
        assert self.type == 4
