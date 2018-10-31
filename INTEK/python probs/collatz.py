def collatz(n):
    count = 0
    if n != int(n) or n < 1:
        return -1
    elif n == 1:
        return count
    else:
        if n % 2 == 0:
            collatz(n/2)
            count += 1
        elif n % 2 != 0:
            collatz(n*3 + 1)
            count += 1
        return count

print(collatz(9))
