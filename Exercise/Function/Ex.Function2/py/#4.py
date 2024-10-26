
#* 4. Generate Fibonacci Sequence Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms in Fibonacci sequence: "))

for i in range(n):
    print(fibonacci(i), end=" ")
print()

#? ตัวอย่างการคำนวณ:
#* fibonacci(0) = 0
#* fibonacci(1) = 1
#* fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
#* fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
#* fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
#* fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5
#? ลำดับที่ได้จะเป็น: 0, 1, 1, 2, 3, 5, 8, 13, ...