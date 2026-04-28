import sys
data = list(map(int,sys.stdin.read().split()))
A, B = data[0], data[1]
def is_self_dividing(n):
    for d in str(n):
        if d == '0' or n % int(d) != 0:
            return False
    return True       
res = [i for i in range(A, B+1) if is_self_dividing(i)]
print(*res)     
