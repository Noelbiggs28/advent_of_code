import unittest
from day_10 import part1

class TestQueue(unittest.TestCase):

    def test_part1_simple(self):
        x = part1("example.txt")
        self.assertEqual(x, 4 )
    def test_part1_simple_extra(self):
        x = part1("example2.txt")
        self.assertEqual(x, 4 )
    def test_part1_complex(self):
        x = part1("example3.txt")
        self.assertEqual(x, 8 )
    def test_part1_complex_extra(self):
        x = part1("example4.txt")
        self.assertEqual(x, 8 )
if __name__ == '__main__':
    unittest.main() 
# echo "day_10.py" | entr -c sh -c "python3 -m unittest predict_spec.py"
# echo "day_10.py" | entr python3 day_10.py