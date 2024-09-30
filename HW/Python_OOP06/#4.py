
#? 4. Write a program that creates a 10x10 list of random integersbetween 1 and 9.
#* Then do the following:
# (a) Print the list.  
# (b) Find the largest value in the third row.
# (c) Find the smallest value in the sixth column. 

class MatrixOperations:
    def __init__(self, size, min_val, max_val):
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.matrix = [[self.generate_value(row, col) for col in range(size)] for row in range(size)]

    def generate_value(self, row, col):
        return (self.min_val + (row + col) % (self.max_val - self.min_val + 1))

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def find_max_in_row(self, row):
        max_value = max(self.matrix[row])
        print(f"Max value in row {row + 1}: {max_value}")

    def find_min_in_column(self, col):
        min_value = min(row[col] for row in self.matrix)
        print(f"Min value in column {col + 1}: {min_value}")


matrix = MatrixOperations(10, 1, 9)

print("Matrix:")
matrix.print_matrix()

matrix.find_max_in_row(2)

matrix.find_min_in_column(5)
