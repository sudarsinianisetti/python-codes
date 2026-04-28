N,M=map(int,input().split())
online_price=N*0.9
if online_price<M:
    print("ONLINE")
elif online_price>M:
    print("DINING")
else:
    print("EITHER")        
