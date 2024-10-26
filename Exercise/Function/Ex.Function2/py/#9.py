
#* 9. Calculate Factorial Using Memoization

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

#? ตัวอย่างการใส่ข้อมูล:
#* ถ้าใส่ 5 จะได้ผลลัพธ์ Factorial: 120 เพราะ 5! = 5 × 4 × 3 × 2 × 1 = 120