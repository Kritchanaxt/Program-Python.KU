

#? Ex.Function1 - #10

numbers = list(map(int, input("Enter numbers: ").split()))
evens = sum(1 for x in numbers if x % 2 == 0)
odds = sum(1 for x in numbers if x % 2 != 0)
print(f"Even numbers: {evens}, Odd numbers: {odds}")
