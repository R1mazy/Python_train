x = input("Введите число x: ")
y = input("Введите число y: ")
z = input("Введите число z: ")
x = float(x)
y = float(y)
z = float(z)
result = x ** 2 * (y ** 0.5 + z ** 0.5) * (1 / ((x ** 6 + y ** 0.5) ** 0.5)) - (3 * x) ** 0.5 + z ** 11
result_f = f'{result:.3f}'
print(result_f)