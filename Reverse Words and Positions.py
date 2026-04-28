s = input().split()
res = []
for w in s:
    res.append(w[::-1])
res = res[::-1]
print(" ".join(res))
