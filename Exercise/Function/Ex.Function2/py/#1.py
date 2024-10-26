
#* 1. Convert Decimal to Binary Without Using bin()

decimal = int(input("Enter a decimal number: "))
binary = ""

if decimal == 0:
    binary = "0"

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal //= 2

print("Binary representation:", binary)

#! ตัวเลขฐานสิบ (decimal number)