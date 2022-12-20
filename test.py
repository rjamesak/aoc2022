import unittest
from day4 import rangeIsFullyContained


class TestCase(unittest.TestCase):

    def rangeTest(self):
        self.assertTrue(rangeIsFullyContained(6, 6, 4, 6))


if __name__ == '__main__':
    unittest.main()
