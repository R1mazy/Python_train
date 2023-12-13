def is_power(num, d=2):
    if num == 1:
        return True
    elif num < d or d == 1:
        return False
    else:
        return is_power(num / d, d)


print(is_power(1, 1))