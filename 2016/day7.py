import re


class Program:
    def __init__(self, line):
        self.line = line
        nre = re.compile('[a-z]+')
        wre = re.compile('[0-9]+')
        matches = nre.findall(line)
        self.name = matches[0]
        self.subs = matches[1:]
        self.weight = int(wre.search(line).group())


class ProgStruct:
    def __init__(self, filename):
        self.input = self.read_input(filename)
        self.progs = [Program(line) for line in self.input]
        self.prog_names = [p.name for p in self.progs]
        self.root = self.find_root()
        self.total_weight = self.get_weight(self.root)

    def read_input(self, filename):
        with open(filename, 'r') as file:
            return [line.rstrip() for line in file.readlines()]

    def get_prog(self, program_name):
        try:
            return self.progs[self.prog_names.index(program_name)]
        except IndexError:
            return None

    def find_parent(self, program):
        for i, p in enumerate(self.progs):
            if program.name in p.subs:
                return self.progs[i]
        return program

    def find_root(self):
        self.path = []
        p = self.progs[0]
        self.path.append(p)
        while p != self.find_parent(p):
            p = self.find_parent(p)
            self.path.append(p)
        return p

    def get_weight(self, program):
        if program.subs:
            sub_weights = [self.get_weight(self.get_prog(sub)) for sub in program.subs]
            program.valid = len(set(sub_weights)) == 1
            res = sum(sub_weights) + program.weight
        else:
            program.valid = True
            res = program.weight
        program.final_weight = res
        return program.final_weight

    def find_invalids(self):
        invalids = [i for i, p in enumerate(self.progs) if not p.valid]
        return [self.progs[i] for i in invalids]

    def find_highest_invalid(self):
        inv = self.find_invalids()
        inv_names = [i.name for i in inv]
        for p in inv:
            if not any([name in p.subs for name in inv_names]):
                return p


ps = ProgStruct('day7_input.txt')
print(ps.root.name)
print([p.name for p in ps.path])

highest = ps.find_highest_invalid()
print(highest.name)

subs = [ps.get_prog(name) for name in highest.subs]
print([s.name for s in subs])

sub_weights = [s.final_weight for s in subs]
max_index = sub_weights.index(max(sub_weights))
print(sub_weights)
print(subs[max_index].weight)
