
# Section 2: 
summations = []

def calculate_summation(number):
    global summations
    digits = [int(digit) for digit in number]
    
    summations = [sum(digits[i:i+3]) for i in range(len(digits) - 2)]
    
    total_sum = summations[-1] if summations else 0
    return total_sum

number = input("Please enter an integer with at least 6 digits: ")

if len(number) < 6 or not number.isdigit():
    print("The number must have at least 6 digits")
else:
    total_sum = calculate_summation(number)
    
    print("Total sum:", total_sum)
    print("Data list:", summations)