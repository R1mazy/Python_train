x = int(input())
y = int(input())
z = int(input())

max_n = max(x, y, z)
min_n = min(x, y, z)
average = (x + y + z) - (max_n + min_n)

if (x < (y + z)) and (y < (x + z)) and (z < (y + x)):
    if (max_n ** 2 > (min_n ** 2 + average ** 2)):
        print("Тупоугольный треугольник")
    elif (max_n ** 2 == (min_n ** 2 + average ** 2)):
        print("Прямоугольный треугольник")
    elif (max_n ** 2 < (min_n ** 2 + average ** 2)):
        print("Остроугольный треугольник")
else:
    print("Треугольник с такими сторонами не существует ")