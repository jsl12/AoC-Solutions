import unittest
from context import day12

PART1 = '<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>'


class TestDay12(unittest.TestCase):
    def test_gravity(self):
        ps = day12.PlanetSystem(PART1)
        for i in range(3):
            ps.simulate_dimension(i, 10)
        self.assertEqual(ps.total_energy, 179)

    def test_cycle(self):
        ps = day12.PlanetSystem(PART1)
        total = ps.total_cycle_time()
        self.assertEqual(total, 2772)

if __name__ == '__main__':
    unittest.main()
