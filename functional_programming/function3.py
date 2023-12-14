input_numbers = input()

res_0 = list(map(int, filter(lambda x: x.is_integer(), list(map(float, input_numbers.split())))))
res_1 = sorted(res_0, key=lambda x: (x <= 0, x))
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))
res_2 = sorted(res_0, key=lambda x: (sum_of_digits(abs(x)), x))
res_3 = sorted(res_0, key=lambda x: (x % 2 != 0, x if x % 2 == 0 else -x))
print(f'{res_1}\n{res_2}\n{res_3}')