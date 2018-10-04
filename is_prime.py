def is_prime(x):
  n = 0
  if x < 2:
    return False
  elif x == 2:
    return True
  else:
    for i in range (2, x):
      if x % i == 0 :
        n += 1
    if n == 0:
      return True
    else:
      return False
