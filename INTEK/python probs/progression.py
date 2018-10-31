from function import round_up


def progression(n):
    sum = 0
    numlist = []
    if n == str(n) or n != int(n):
        return "Invalid Value"
    elif n == 1:
        return 0.5
    else:
        for i in range(1, n+1):
            sum += (i / (i + 1))
    return round_up(sum)
