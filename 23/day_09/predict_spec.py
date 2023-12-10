import unittest
from day_09 import part1

class TestQueue(unittest.TestCase):

    def test_part1(self):
        x = part1("example.txt")
        self.assertEqual(x, 114 )

if __name__ == '__main__':
    unittest.main() 
    # ls day_09.py | entr -s "python3 -m unittest predict_spec.py"