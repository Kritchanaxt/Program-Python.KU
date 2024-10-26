

#? Ex.Function2 - #10

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encoded = caesar_cipher(text, shift)
decoded = caesar_cipher(encoded, -shift)

print("Encoded: ", encoded)
print("Decoded: ", decoded)