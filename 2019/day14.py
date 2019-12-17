import math
import re


class ReactionSystem:
    def __init__(self, input: str):
        self.reactions = [Reaction(line) for line in input.splitlines()]
        self.reaction_table = {r.output[1]: r for r in self.reactions}
        self.reset()

    def reset(self):
        self.on_hand = {}

    def __repr__(self):
        return f'{len(self.reactions)} reaction system'

    def ore_needed(self, compound, amount_needed=1, reset=True, use_leftovers=True):
        if reset:
            self.reset()

        if use_leftovers:
            if compound in self.on_hand:
                available = self.on_hand[compound]
                if amount_needed < available:
                    self.on_hand[compound] -= amount_needed
                    amount_needed = 0
                elif amount_needed == available:
                    amount_needed = 0
                    self.on_hand.pop(compound)
                elif amount_needed > available:
                    amount_needed -= available
                    self.on_hand.pop(compound)


        reaction = self.reaction_table[compound]
        num_reactions = math.ceil(amount_needed / reaction.output[0])
        ore_total = 0
        for input_amount, input_name in reaction.input:
            input_total_amount = input_amount * num_reactions
            if input_name == 'ORE':
                ore_total += input_total_amount
            else:
                ore_total += self.ore_needed(input_name, input_total_amount, reset=False)

        if use_leftovers:
            leftover = (num_reactions * reaction.output[0]) - amount_needed
            if leftover > 0:
                if compound not in self.on_hand:
                    self.on_hand[compound] = leftover
                else:
                    self.on_hand[compound] += leftover

        return ore_total


class Reaction:
    regex = re.compile('([\d]+) ([\w]+)')
    def __init__(self, input: str):
        self.str = input
        input, output = input.split(' => ')
        self.input = [(int(res[0]), res[1]) for res in self.regex.findall(input)]
        m = self.regex.search(output)
        self.output = (int(m.group(1)), m.group(2))

        # g = reduce(math.gcd, self.amounts)
        return

    def __repr__(self):
        return self.str

    @property
    def amounts(self):
        return [r[0] for r in self.input] + [self.output[0]]

def part1(input):
    """
    >>> import aoc_input as inp; part1(inp.read(14))
    220019
    """
    rs = ReactionSystem(input)
    return rs.ore_needed('FUEL')


def part2(input):
    return


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import aoc_input as inp

    DAY = 14
    # print(part1(inp.read(DAY)))
    print(part2(inp.read(DAY)))
