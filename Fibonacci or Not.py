n = int(input())
a, b = 0,1

while a < n:
    a, b = b, a + b
if a == n:
    print("True")
else:
    print("False")        
