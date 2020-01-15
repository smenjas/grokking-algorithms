def sum(arr):
  total = 0
  if len(arr) == 0:
    return 0
  return arr.pop() + sum(arr)

print sum([1, 2, 3, 4])
