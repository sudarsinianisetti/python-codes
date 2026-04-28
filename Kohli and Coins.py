x=int(input())
if x%5!=0:
    print(-1)
else:
    tens=x//10
    remainder=x%10
    fives=remainder//5
    print(tens+fives)    
