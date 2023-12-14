def tribonacci(n):
    a1, a2, a3 = 0, 0, 1
    for i in range(n+1):
        yield a1
        a1, a2, a3 = a2, a3, a1 + a2 + a3
print(list(tribonacci(3)))
print(list(tribonacci(7)))