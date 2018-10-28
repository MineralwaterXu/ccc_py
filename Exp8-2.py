def sum_odd(x):
    sum_odd = 0
    n = 1
    while n < x:
        sum_odd = sum_odd + n
        n = n + 2
    return sum_odd
def sum_even(x):
    sum_even = 0
    n = 0
    while n < x + 1:
        sum_even = sum_even + n
        n = n + 2
    return sum_even
x = int(input("Please input the number:" ))
print("sum_odd:",sum_odd(x))
print("sum_even:",sum_even(x))
input("Thank you.Press Enter button to exit.")