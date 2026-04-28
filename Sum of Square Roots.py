import math
a, b = map(int, input().split())

total = 0
for i in range(a, b+1):
    total += math.sqrt(i)
print(f"{total:.2f}")
