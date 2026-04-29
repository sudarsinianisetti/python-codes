n, x = map(int,input().split())
cows = list(map(int,input().split()))

white_costs = []
for i in range(10):
    if cows[i] == 0:
        white_costs.append(i + 1)
white_costs.sort()
count = 0
total = 0        
for cost in white_costs:    
    if total + cost <=n:
        total += cost
        count += 1
    else:
        break
if count >=x:
    print("Happy")
else:
    print("Sad")            
