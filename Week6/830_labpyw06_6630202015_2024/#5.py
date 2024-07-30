
#5. 

def count_matrix_elements(matrix):
    count = 0
    for row in  matrix:
      for element in row:
         count += 1
    return count

table = [[5,2,6], [4,6,0], [9,1,8], [7,3,8]]
count = count_matrix_elements(table)
print("Number of elements in the matrix: ", count)