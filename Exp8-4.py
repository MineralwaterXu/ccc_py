import math
r = float(input("Please input the radius:"))
def perimeter(r):
    perimeter = 2 * math.pi * r
    return perimeter
print(perimeter(r))
input("Thank you.Press Enter button to exit.")