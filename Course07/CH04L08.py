def sum_nested_list(lst):
  total_size = 0
  for item in lst:
    if type(item) == int:
      total_size += item
    if type(item) == list:
      total_size += sum_nested_list(item)
  return total_size
      
