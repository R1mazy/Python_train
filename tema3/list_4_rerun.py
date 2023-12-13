a = int(input())
b = int(input())

if a < b:
    a, b = b, a

a1 = a
b1 = b

while b != 0:
    a, b = b, a % b
nod = a
nok = a1 // nod * b1

print("НОД введенных чисел: " + str(nod))
print("НОК введенных чисел: " + str(nok))

