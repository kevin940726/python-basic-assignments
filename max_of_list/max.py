def max(list):
  '''
  This function takes a single parameter `list` and return the maximum value element.
  If the list doesn't have any item, return `None`

  Example:
    Given [1, 5, 3, 2, 4], return `5`
    Given [], return `None`
  '''
  result = None

  for item in list:
    if item > result:
      result = item

  return result
