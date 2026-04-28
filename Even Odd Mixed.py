num = input().strip()
print("Even" if all(int(d)%2==0 for d in num) else "Odd" if all(int(d)%2==1 for d in num) else "Mixed")
