import unittest
from test_day2 import TestDay2
from test_day5 import TestDay5
from test_day7 import TestDay7
from test_day9 import TestDay9


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestDay2('test'))

    suite.addTest(TestDay5('test'))

    suite.addTest(TestDay7('test_part1'))
    suite.addTest(TestDay7('test_part2'))

    suite.addTest(TestDay9('test'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
