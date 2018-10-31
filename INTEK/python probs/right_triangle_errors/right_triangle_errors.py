def right_triangle_errors(a, b, c):
    try:
        if not isinstance(a, int) or isinstance(b, int) or isinstance(c, int):
            raise ValueError
        elif a < 0 or b < 0 or c < 0:
            raise ValueError
        else:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or \
                b**2 + c**2 == a**2:
                return True
            else:
                return False
    except ValueError:
        return "Incorrect value"


print(right_triangle_errors(17, 15, 5))
