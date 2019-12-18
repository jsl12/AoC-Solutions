import unittest
from context import day10


CASES = {
    (0, 2): 45,
    (2, 2): 135,
    (2, 0): 225,
    (0, 0): 315
}

class TestDay10(unittest.TestCase):
    def test_samples(self):
        field = '.#..#\n.....\n#####\n....#\n...##'
        f = day10.Field(field)
        base, visible_ast_count = f.max_visible()
        self.assertEqual(visible_ast_count, 8)

    def test_angles(self):
        base = (1,1)
        for coords, angle in CASES.items():
            with self.subTest():
                self.assertEqual(day10.Asteroid(coords).angle(*base), angle)

if __name__ == '__main__':
    unittest.main()