
#? Ex.Function1 - #2

def palindrome(word):
    return word == word[::-1]

word = input("Enter a word to check: ")
if palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")