
#* 5. Find the Most Frequent Word in a String

from collections import Counter

text = input("Enter a string: ")
words = text.split()
word_count = Counter(words)
most_common_words = [word for word, count in word_count.items() if count == max(word_count.values())]

print("Most frequent word(s):", ' '.join(most_common_words))
