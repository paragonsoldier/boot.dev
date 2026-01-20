def factorial_r(x):
  if x <= 1:
    return 1
  x *= factorial_r(x - 1)
  return x
