matrix = []
n = int(input("Введите размерность квадратной матрицы: "))
for i in range(n):
    row = []
    for j in range(n):
        element = float(input(f"Введите элемент [{i}, {j}]: "))
        row.append(element)
    matrix.append(row)