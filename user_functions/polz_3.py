def solve_quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        roots = (min(x1, x2), max(x1, x2))
        return 2, roots
    elif D == 0:
        x = -b / (2 * a)
        roots = (x,)
        return 1, roots
    else:
        return 0, ()

result = solve_quadratic_equation(2, -3, -20)
print(result)