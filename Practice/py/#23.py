

#? Python_OOP06

class WordSorter:
    def __init__(self, word):
        self.word = word

    def sort_word(self):
        sorted_chars = sorted(self.word)
        sorted_word = ''
        for char in sorted_chars:
            sorted_word += char
        print(f"Sorted word: {sorted_word}")

user_word = input("Enter a word: ")
sorter = WordSorter(user_word)
sorter.sort_word()