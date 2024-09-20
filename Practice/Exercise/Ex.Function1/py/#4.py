
#* 4. Count Characters in a String

text = input("Enter a string 👍🏿 : ")
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(f"'{char}' appears {count} times")

print(char_count) 