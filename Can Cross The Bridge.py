import sys
data = list(map(int,sys.stdin.read().strip().split()))
x,y,z = data[0],data[1],data[2]
result = (z-y) // x
print(result)
