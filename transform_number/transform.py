def transform(n):
  '''
  This function takes one parameter `n` of type string and return the
  power of two of the middle two numbers and padded with leading zeros.

  Example:
    Given '8649', return '4096'
    Given '0001', return '0000'
  '''
  middle = n[1:3]
  result = int(middle) ** 2
  prefixed = '000' + str(result)
  return prefixed[-4:]

def transform_list(n):
  '''
  This function takes a single parameter `n` of type string and return a
  list of string which contains the transformed numbers in order until the
  next result equals to the last item.

  Example:
    Given '8649', return ['4096', '0081', '0064', '0036', '0009', '0000']
    Given '3025', return ['0004', '0000']
  '''
  list = []
  result = transform(n)

  while not len(list) or not result == list[-1]:
    list.append(result)
    result = transform(result)

  return list
