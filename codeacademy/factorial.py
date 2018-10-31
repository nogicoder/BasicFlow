def factorial(x):
	result = 1
	for i in range (1, x+1):
		result *= i
	return result


def factorial(x):
  result = x
  while x > 1:
    result *= x-1
    x -= 1
  return result
