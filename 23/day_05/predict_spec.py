import unittest
from day_05 import part1, part2

class TestQueue(unittest.TestCase):

    def test_part1(self):
        x = part1("example.txt")
        self.assertEqual(x, 35 )

    def test_part2(self):
        x = part2("example.txt")
        self.assertEqual(x, 46 )

if __name__ == '__main__':
    unittest.main() 
    # ls day_05.py | entr -s "python3 -m unittest predict_spec.py"