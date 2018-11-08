import random

# l = random.randint(0, 300)

def guess(l, n, min, max):
    gs = round((min+max)/2)
    if min:
        return "dude"
    elif gs == l:
        return gs
    else:
        if gs < l:
            min = gs + 1
        elif gs > l:
            max = gs
    return guess(l, n, min, max)


print(guess(0, 300, 0, 300))
