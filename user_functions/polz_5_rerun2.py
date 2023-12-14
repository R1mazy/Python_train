def is_power(num, d=2):
    if d == 1 and num != 1:
        return False
    elif num == 1 or (d == 1 and num == 1):
        return True
    elif num % d != 0:
        return False
    else:
        return is_power(num // d, d)

result = is_power(1, 1)
print(result)