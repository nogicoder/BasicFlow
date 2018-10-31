def geometric_seq(numlist):
    a = True
    while True:
        for i in numlist:
            if str(i) in numlist:
                return "Invalid Value"
                a = False
    while a == True:
        for i in range(len(numlist)):
            while True:
                if 0 in numlist:
                    return False
                elif 0 not in numlist:
                    if numlist[i+2] / numlist[i+1] == numlist[i+1] / numlist[i]:
                        return True
                    else:
                        return False
