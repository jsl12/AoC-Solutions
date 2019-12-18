import unittest

from context import intcode, aoc_input


MAZE = aoc_input.read(15)


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.droid = intcode.MazeDroid(MAZE)

    def test_probe(self):
        self.droid.probe_all()
        with self.subTest():
            self.assertEqual(self.droid.pos, [0, 0])
        with self.subTest():
            self.assertEqual(self.droid.path, [])

        with self.subTest():
            self.droid.move(3)
            pos = self.droid.pos[:]
            self.droid.probe_all()
            self.assertEqual(pos, self.droid.pos)

    def test_move(self):
        for res in self.droid.move_straight(3):
            pass
        with self.subTest():
            self.assertEqual(self.droid.path, [3, 3, 3, 3])


if __name__ == '__main__':
    unittest.main()
