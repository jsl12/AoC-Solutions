import unittest
from context import day10
from day10 import get_asteroids, compute_sightlines


CASES = {
    (0, 2): 45,
    (2, 2): 135,
    (2, 0): 225,
    (0, 0): 315
}
field = '.#..#\n.....\n#####\n....#\n...##'


class TestDay10(unittest.TestCase):
    def test_samples(self):
        a = compute_sightlines(get_asteroids(field))
        visible_ast_count = max(a.values(), key=lambda ast: ast.visible_count).visible_count
        self.assertEqual(visible_ast_count, 8)

    def test_angles(self):
        base = (1,1)
        for coords, angle in CASES.items():
            with self.subTest():
                self.assertEqual(day10.Asteroid(coords).angle(*base), angle)


if __name__ == '__main__':
    unittest.main()
