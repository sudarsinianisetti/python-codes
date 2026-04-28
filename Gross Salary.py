basic=int(input())
if basic <= 10000:
    da = basic*0.80
    hra = basic*0.20
elif basic<=20000:
    da = basic*0.90
    hra = basic*0.25
else:
    da = basic*0.95
    hra = basic*0.30
gross = basic+da+hra
print(f"{gross:.2f}")            
