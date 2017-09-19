def sum(list):
  '''
  This function takes a single argument `list` and return the sum
  of all the elements.

  Example:
    Given [1, 2, 3, 4, 5], return `15`
    Given [], return `0`
  '''
  result = 0

  for item in list:
    result += item

  return result
