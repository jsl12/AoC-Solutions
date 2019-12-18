import unittest
from context import day3

CASES = {
    'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83': (159, 610),
    'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7': (135, 410)
}


class TestDay3(unittest.TestCase):
    def test_part1(self):
        for input_seq, (part1_res, part2_res) in CASES.items():
            with self.subTest():
                self.assertEqual(day3.part1(input_seq), part1_res)
            with self.subTest():
                self.assertEqual(day3.part2(input_seq), part2_res)

if __name__ == '__main__':
    unittest.main()