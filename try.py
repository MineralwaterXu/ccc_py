def sum(N):
    sum = 0
    x = 1
    while x < N + 1:
        sum = sum + x
        x = x + 1
    return sum
N = int(input("Please input the number:" ))
print(sum(N))
input("Thank you.Press Enter button to exit.")