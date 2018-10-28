check = True
while check:
    x = int(input("Please input a number:"))
    if x == 0:
        print("Zero")
        break
    if x < 0:
        print("Negative")
    if x > 0:
        print("Positive")