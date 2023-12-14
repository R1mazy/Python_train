x, y = map(int, input().split())
w, z = map(int, input().split())

print(" " * 7, end="")
for i in range(w, z+1):
    print(f"{i:7d}", end="")
print()
for i in range(x, y+1):
    print(f"{i:7d}", end="")
    for j in range(w, z+1):
        print(f"{i*j:7d}", end="")
    print()