num = int(input())
num_str = str(num)
total = sum(int(digit) ** (i+1) for i, digit in enumerate(num_str))
print(total == num)
