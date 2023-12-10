import unittest
from day_09.day_09 import part1

class TestQueue(unittest.TestCase):
    def setUp(self):
        pass

    def test_part1(self):
        x = part1("../day_09/example.txt")
        self.assertEqual(x, 114 )

if __name__ == '__main__':
    unittest.main() 