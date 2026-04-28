m, n = map(int,input().split())

count = 0
for i in range(m, n+1):
    if i % 2 ==0 and i % 3 == 0:
        count += 1
print(count)
