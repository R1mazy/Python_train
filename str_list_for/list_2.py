in_list = input()
in_list_new = in_list.split()
k = 0

for i in range(1, len(in_list_new) - 1):
    if int(in_list_new[i]) > int(in_list_new[i-1]) and int(in_list_new[i]) > int(in_list_new[i+1]):
        k += 1

print(k)