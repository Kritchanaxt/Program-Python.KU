
#* 2. Check if a Word is a Palindrome

def palindrome(word):
    return word == word[::-1]

word = input("Enter a word to check: ")
if palindrome(word):
    print(f'"{word}" is a Palindrome')
else:
    print(f'"{word}" is not a Palindrome')