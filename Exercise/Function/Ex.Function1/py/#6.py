
#* 6. Create a Chessboard Pattern

size = 8

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()

#* row: แนวนอน 
#* col: แนวตั้ง