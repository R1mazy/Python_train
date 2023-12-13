number = int(input())
s_schisl = int(input())
nabor = "0123456789ABCDEF"
result = ""

while number > 0:
    num = number % s_schisl
    result = nabor[num] + result
    number = number // s_schisl
print(result)