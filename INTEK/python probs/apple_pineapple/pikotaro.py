def apple_pen(first_ingredient, second_ingredient):
    if first_ingredient == "pen" and second_ingredient == "apple":
            return "I have a pen, I have a apple\\nUh! Apple-Pen!'"
    elif first_ingredient == "pen" and second_ingredient == "pineapple":
        return "I have a pen, I have a pineapple\\nUh! Pineapple-Pen!"
    elif first_ingredient == "pen" and second_ingredient == "pen":
        return "I have a pen, I have a pen\\nUh! Long pen!"
    else:
        raise ValueError("It is not in the lyrics")


print(apple_pen('apple', 'pen'))
