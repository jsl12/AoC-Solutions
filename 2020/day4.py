import aoc_input
import numpy as np
from typing import Iterable
from functools import reduce
import operator
import re

class Passport:
    def __init__(self, input_str):
        pairs = input_str.replace('\n', ' ').split(' ')
        self.dict = {key: value for key, value in (pair.split(':') for pair in pairs)}
        if not 'cid' in self.dict:
            self.dict['cid'] = None

    def __getitem__(self, item):
        return self.dict[item]

    @property
    def valid(self):
        return (len(self.dict.keys()) == 8)

    @property
    def valid_fields(self):
        return all([self.validate_field(field) for field in self.dict])

    def validate_field(self, field):
        val = self[field]
        if field == 'byr':
            return (1920 <= int(val) <= 2002)
        elif field == 'iyr':
            return (2010 <= int(val) <= 2020)
        elif field == 'eyr':
            return (2020 <= int(val) <= 2030)
        elif field == 'hgt':
            unit = val[-2:]
            if unit == 'cm':
                return (150 <= int(val[:-2]) <= 193)
            elif unit == 'in':
                return (59 <= int(val[:-2]) <= 76)
        elif field == 'hcl':
            if val[0] == '#':
                try:
                    int(val[1:], 16)
                except:
                    pass
                else:
                    return True
        elif field == 'ecl':
            return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif field == 'pid':
            if len(val) == 9:
                try:
                    int(val)
                except:
                    pass
                else:
                    return True
        elif field == 'cid':
            return True
        return False



def part1(lines):
    passports = [Passport(p) for p in lines.split('\n\n')]
    return len([p for p in passports if p.valid])


def part2(lines):
    passports = [Passport(p) for p in lines.strip().split('\n\n')]
    valid = [
        p for p in passports
        if p.valid and p.valid_fields
    ]
    return len(valid)


if __name__ == '__main__':
    DAY = 4

    print(part1(aoc_input.read(DAY)))
    print(part2(aoc_input.read(DAY)))