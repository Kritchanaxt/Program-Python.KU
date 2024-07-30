
#4. 
start = -75
while (True):
    if (start % 3 == 0 and ((start >= -75 and start <= -25) or (start >= 50 and start <= 75))):
        print("Number: ", start)
    start += 1
    if (start > 75):
        break