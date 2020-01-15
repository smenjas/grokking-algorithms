def squarePlots(x, y):
  # Make sure x >= y.
  if x < y:
    a = x
    x = y
    y = a
  # Base case: Is x a multiple of y?
  if x % y == 0:
    return y
  # Recursive case: x is not a multiple of y.
  print x-y
  return squarePlots(y, x-y)

print squarePlots(640, 1680)
