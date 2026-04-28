p,c,b,m,cs=map(int,input().split())
percentage=(p+c+b+m+cs)/5
if percentage>=90:
    print("Grade A")
elif percentage>=80:
    print("Grade B")
elif percentage>=70:
    print("Grade C")
elif percentage>=60:
    print("Grade D")
elif percentage>=50:
    print("Grade E")
else:
    print("Grade F")                    
