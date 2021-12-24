from dataclasses import dataclass

@dataclass
class Crab:
    position: int
    
    def scuttle(self, destination: int):
        return abs(destination - self.position)

    def long_scuttle(self, ):
        return 
    
def factorial_gen(n: int):
    res = 0
    for i in range(n):
        res += i
        yield res
        
def factorials(n: int):
    return {v: f for v, f in zip(range(n), factorial_gen(n))}
        
def part1(inp):
    crabs = list(map(int, inp.split(',')))
    rng = min(crabs), max(crabs) + 1
    return min([sum(map(lambda x: abs(i - x), crabs)) for i in range(*rng)])

def part2(inp):
    crabs = list(map(int, inp.split(',')))
    rng = min(crabs), max(crabs) + 1
    facts = factorials(max(crabs) - min(crabs))
    return min([sum(map(lambda x: facts[i - x], crabs)) for i in range(*rng)])
    