name=input("Please enter your name:")
print("Hello,%s.This is a tiny tool to calculate your bmi."%name)
height=float(input("Please enter your height(m):"))
weight=float(input("Please enter your weight(kg):"))
bmi=weight/(height*height)
if bmi<=18.5:
    print("result:Underweight")
elif bmi<=25:
    print("result:Normal weight")
elif bmi<=30:
    print("result:Overweight")
else:
    print("result:Obese")
input("Thank you.Press Enter button to exit.")
