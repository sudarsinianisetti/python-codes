n = int(input())
if n == 0:
    print("DEFICIENT")
else:
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i != n // i:
                sum_div += n // i
    if sum_div == n:
        print("PERFECT")
    elif sum_div < n:
        print("DEFICIENT")
    else:
        print("ABUNDANT")        
