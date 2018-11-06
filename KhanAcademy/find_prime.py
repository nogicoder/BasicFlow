#Applying binary search algorithm


lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def find_prime(n, lst, min, max):
    i = round((min + max) / 2)
    if min > max:
        return "damn"
    elif lst[i] == n:
        return i
    else:
        if lst[i] < n:
            min = i + 1
        elif lst[i] > n:
            max = i - 1
    return find_prime(n, lst, min, max)


print(find_prime(47, lst, 0, len(lst) - 1))
