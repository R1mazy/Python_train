f_min = float('inf')
s_min = float('inf')
f_max = float('-inf')
s_max = float('-inf')

while True:
    num = int(input())
    if num == 0:
        break
    if num < f_min:
        s_min, f_min = f_min, num
    elif num < s_min:
        s_min = num

    if num > f_max:
        s_max, f_max = f_max, num
    elif num > s_max:
        s_max = num

print(s_min)
print(s_max)