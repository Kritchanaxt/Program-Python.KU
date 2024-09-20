
#* 3. Find Prime Numbers in a Range

def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

primes = [num for num in range(start, end + 1) if prime(num)]
print("Prime numbers in the range:", primes)
