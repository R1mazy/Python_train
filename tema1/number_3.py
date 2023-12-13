minutes = int(input())
hour = (minutes // 60) % 24
minute = minutes % 60

print(f'{hour:02}:{minute:02}')
