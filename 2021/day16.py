import itertools


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
