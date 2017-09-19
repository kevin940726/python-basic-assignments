import unittest
from max import max

class Max(unittest.TestCase):
  def test_max_of_list(self):
    'it should return the maximum value'
    actual = max([1, 5, 3, 2, 4])
    expected = 5
    self.assertEqual(actual, expected)

  def test_max_of_empty_list(self):
    'it should return None to empty list'
    actual = max([])
    expected = None
    self.assertEqual(actual, expected)

  def test_max_of_complex_numbers(self):
    'it should return the maximum among negative and floating point numbers'
    actual = max([-1, 0, 2.22, -3.5])
    expected = 2.22
    self.assertEqual(actual, expected)

  def test_max_of_one_item(self):
    'it should return the only item in the list'
    actual = max([-1])
    expected = -1
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()