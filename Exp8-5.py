a = float(input("Please input the length of side a:"))
b = float(input("Please input the length of side b:"))
c = float(input("Please input the length of side c:"))
def area_of_triangle(a,b,c):
    p = (a + b + c)/2
    area_of_triangle = pow((p * (p - a) * (p - b) * (p - c)),1/2)
    return area_of_triangle
print(area_of_triangle(a,b,c))
input("Thank you.Press Enter button to exit.")