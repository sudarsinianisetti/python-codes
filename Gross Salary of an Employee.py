salary=float(input())
hra=float(input())
da=float(input())
tax=salary*0.12
net_salary=salary+hra+da+tax
print("{:.2f}".format(tax))
print("{:.2f}".format(net_salary))
