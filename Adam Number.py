n = int(input())
def reverse_num(x):
    return int(str(x)[::-1])
square_n = n ** 2
rev_n = reverse_num(n)
square_rev_n = rev_n ** 2
is_adam = square_n == reverse_num(square_rev_n)    
print(is_adam)
