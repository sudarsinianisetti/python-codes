A,B,X,Y=map(int,input().split())
messi=2*A+B
ronaldo=2*X+Y
if messi>ronaldo:
    print("Messi")
elif ronaldo>messi:
    print("Ronaldo")
else:
    print("Equal")        
