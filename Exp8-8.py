x =int(input("Please input the day of the monkey who eats the peaches:"))
n = 1
while x > 1:
    n = 2 * (n + 1)
    x = x - 1
print(n)
input("Thank you.Press Enter button to exit.")