inp_num = int(input())
right_num = inp_num // 1000
left_num = (inp_num % 10) * 100 + (inp_num // 10 % 10) * 10 + (inp_num // 100 % 10)
print(1 - min(1, abs(left_num - right_num)))

