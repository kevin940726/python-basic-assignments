import unittest
from sum import sum

class Sum(unittest.TestCase):
  def test_sum_of_list(self):
    '''
    it should sum up list
    '''
    actual = sum([1, 2, 3, 4, 5])
    expected = 15
    self.assertEqual(actual, expected)

  def test_sum_of_empty_array(self):
    '''
    it should sum up empty array to 0
    '''
    actual = sum([])
    expected = 0
    self.assertEqual(actual, expected)

  def test_sum_of_complex_numbers(self):
    '''
    it should sum up the list with negative and floating point number
    '''
    actual = sum([-1, 0, 2.22, -3.5])
    expected = -2.28
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()