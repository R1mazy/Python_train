a = int(input())
b = int(input())

if (a != 29):
    print("обычный программист")
if ((b % 4 == 0 and b % 100 != 0) or (b % 400 == 0)) and a == 29:
    print("особо ценный программист")
elif a == 29:
    print("мошенник")
