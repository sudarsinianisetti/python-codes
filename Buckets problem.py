n = int(input())
t = int(input())

tasks = [int(input()) for _ in range(t)]
total = 0
odd = 0
even = 0
for x in tasks:
    if x == 1:
        total = n
        odd = (n+1) // 2
        even = n // 2
    elif x == 2:
        total -= even
        even = 0
    elif x == 3:
        total -= odd
        odd = 0
    elif x == 4:
        total = odd = even = 0
print(total)        
