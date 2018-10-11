def round_up(n):
    n_list = []
    result = []
    n = str(n)
    n1 = n.split(".")
    for i in n1[1]:
        n_list.append(i)
    a = int(n_list[2])
    b = int(n_list[0] + n_list[1])
    if a > 5 or a == 5:
        b += 1
    elif a < 5:
        pass
    c = n1[0] + "." + str(b)
    return float(c)
