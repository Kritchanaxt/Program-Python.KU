
#? Ex.Function2 - #9

memo = {}

def factorial(n):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = n * factorial(n - 1)
    return memo[n]

n = int(input("Enter a number to calculate factorial: "))
print("Factorial:", factorial(n))