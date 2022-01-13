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
    version: int = field(init=False)
    type: int = field(init=False)

    def __post_init__(self):
        self.version = int(self.bits[:3], 2)
        self.type = int(self.bits[3:6], 2)


@dataclass
class ValuePacket(Packet):
    value: int = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        assert self.type == 4
        self.value, ngroups = value_from_bits(self.bits[6:])
