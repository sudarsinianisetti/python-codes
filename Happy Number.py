def is_happy(n):
    seen =set()
    while n != 1 and n != 7:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return True
num = int(input())
print(is_happy(num))            
