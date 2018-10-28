def multiply(x):
    multiply = 1
    n = 1
    while n < x + 1:
        multiply = multiply * n
        n = n + 1
    return multiply
x = int(input("Please input a number:"))
print(multiply(x))
input("Thank you.Press Enter button to exit.")