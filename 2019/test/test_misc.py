import unittest

from test_day3 import TestDay3
from test_day10 import TestDay10
from test_day12 import TestDay12
from test_day14 import TestDay14

def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestDay3('test_part1'))

    suite.addTest(TestDay10('test_samples'))
    suite.addTest(TestDay10('test_angles'))

    suite.addTest(TestDay12('test_gravity'))
    suite.addTest(TestDay12('test_cycle'))

    suite.addTest(TestDay14('test_part1'))
    suite.addTest(TestDay14('test_part2'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
