
# Section 1: 
number = input("Please enter an integer with at least 6 digits: ")

if len(number) < 6 or not number.isdigit():
    print("The number must have at least 6 digits")
else:
    digits = [int(digit) for digit in number]
    
    summations = [sum(digits[i:i+3]) for i in range(len(digits) - 2)]
    
    total_sum = summations[-1] if summations else 0
    
    print("Total sum:", total_sum)
    print("Data list:", summations)




