cp,sp = map(int,input().split())
loss=((cp-sp) / cp) * 100
print(f"{loss:.2f}")
