n = int(input())
s = input()

count = 0
for i in range(1, n-1):
    if s[i].isalpha():
        if(not s[i-1].isalnum()) and (not s[i+1].isalnum()):
            count += 1
print(count)            
