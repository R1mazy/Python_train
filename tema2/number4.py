in1, out1, in2, out2 = int(input()), int(input()), int(input()), int(input())

if out1 == in2:
    print("Отрезки пересекаются в точке ", out1)
if in1 == out2:
    print("Отрезки пересекаются в точке ", in1)
if out1 < in2 or in1 > out2:
    print("Отрезки не пересекаются")
