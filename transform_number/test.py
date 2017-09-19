import unittest
from transform import transform, transform_list

class Transform(unittest.TestCase):
  def test_transform_8649(self):
    actual = transform('8649')
    expected = '4096'
    self.assertEqual(actual, expected)

  def test_transform_3025(self):
    actual = transform('3025')
    expected = '0004'
    self.assertEqual(actual, expected)

  def test_transform_0000(self):
    actual = transform('0000')
    expected = '0000'
    self.assertEqual(actual, expected)

  def test_transform_1001(self):
    actual = transform('1001')
    expected = '0000'
    self.assertEqual(actual, expected)

  def test_transform_list_8649(self):
    actual = transform_list('8649')
    expected = ['4096', '0081', '0064', '0036', '0009', '0000']
    self.assertEqual(actual, expected)

  def test_transform_list_3025(self):
    actual = transform_list('3025')
    expected = ['0004', '0000']
    self.assertEqual(actual, expected)

  def test_transform_list_0000(self):
    actual = transform_list('0000')
    expected = ['0000']
    self.assertEqual(actual, expected)

  def test_transform_list_1001(self):
    actual = transform_list('1001')
    expected = ['0000']
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()