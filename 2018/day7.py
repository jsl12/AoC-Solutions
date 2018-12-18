import re

REGEX = re.compile('Step (\w) must be finished before step (\w) can begin.')

def parse(line):
    match = REGEX.match(line)
    return match.group(1), match.group(2)

def create_steps(input):
    steps = {}
    for i in [parse(line) for line in input.splitlines()]:
        if i[1] in steps:
            steps[i[1]].append(i[0])
        else:
            steps[i[1]] = [i[0]]
    return steps

def find_start(steps):
    s = next(iter(steps.keys()))
    while s in steps:
        s = steps[s][0]
    return s

def find_ready(steps, done):
    res = sorted([s for s in steps if all([ps in done for ps in steps[s]])])
    return res[0]

def part1(input):
    steps = create_steps(input)
    done = list(find_start(steps))
    n = len(steps)
    while len(done) <= n:
        done.append(find_ready(steps, done))
        steps.pop(done[-1])
    return ''.join(done)

class Manager:
    def __init__(self, input, workers=5):
        self.steps = create_steps(input)
        self.n = len(self.steps)
        self.t = 0
        self.starts = {find_start(self.steps): 0}
        self.workers = workers

    def find_done(self):
        res = [s for s in self.starts if self.t >= self.end_time(s)]
        [self.steps.pop(s) for s in res if s in self.steps]
        return res

    def end_time(self, step_id):
        return self.starts[step_id] + 61 + ord(step_id) - ord('A')

    def find_ready(self):
        done = self.find_done()
        return [s for s in self.steps if all(ps in done for ps in self.steps[s])]

    def find_active(self):
        res = [s for s in self.starts if self.starts[s] < self.t < self.end_time(s)]
        return len(res)

    def run(self):
        done = self.find_done()
        while len(done) < len(self.steps):
            self.t += 1
            ready = self.find_ready()
            if self.find_active() < self.workers and len(ready) > 0:
                pass
            self.find_done()

def part2(input):
    m = Manager(input)
    m.run()
    return

if __name__ == '__main__':
    import input as inp
    DAY = 7
    input = inp.read(DAY)
    # print(part1(input))
    print(part2(input))