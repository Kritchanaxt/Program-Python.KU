
#* 3. Recursive function

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(input("Enter a number: "))
print(f"The factorial of {x} is {fact(x)}")
