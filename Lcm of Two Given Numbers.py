import math
m, n = map(int,input().split())
lcm = (m * n) // math.gcd(m,n)
print(lcm)
