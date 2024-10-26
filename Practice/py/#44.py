
#? Ex.Function2 - #7

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []
for i in range(n):
    row = list(map(int, input(f"Enter row {i+1} : ").split()))
    matrix.append(row)

matrix_sum = sum(sum(row) for row in matrix)
print("Sum matrix:", matrix_sum)