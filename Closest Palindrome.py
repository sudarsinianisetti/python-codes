n = int(input())
def pal(x):
    return str(x) == str(x)[::-1]
i = 1
while True:
    if pal(n - i) and pal(n + i):
        print(n - i,n + i)
        break
    elif pal(n - i):
        print(n - i)
        break
    elif pal(n + i):
        print(n + i)
        break
    i += 1    
