import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
   def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)
def test_subtract(self):
  # COMPLETE HERE
def test_divide(self):
  # COMPLETE HERE
if __name__ == '__main__':
   unittest.main()