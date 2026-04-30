n=int(input())
arr=list(map(int,input().split()))
even_sum=0
for num in arr:
    if num%2==0:
        even_sum+=num
print(even_sum)
