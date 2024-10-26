
#? Ex.Function2 - #5

text = input("Enter a string: ")
words = text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_count = max(word_count.values())
most_common_words = [word for word, count in word_count.items() if count == max_count]

print("Most frequent word(s):", ' '.join(most_common_words))