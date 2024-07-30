
#1. 
x = int(input("Enter a number: "))
if (x % 3 == 0 and ((x >= -75 and x <= -25) or (x >= 50 and x <= 75))):
    print("Correct input")
else:
    print("Incorrect input")