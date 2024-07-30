
#* 16.

total = 0
def sum(arg1, arg2):
    "Add both the parameters"
    total = arg1 + arg2
    print("Inside the function local total:", total)
    return total
    
sum(10, 20)
print("Outside the function local total:",total)