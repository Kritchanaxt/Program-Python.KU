
#* 2. Find the Longest Word in a Sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == longest_length]

print("Longest word(s):", ' '.join(longest_words))
