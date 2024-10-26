
#? Ex.OOP1 - #8

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")

print("\n")
print("-" * 60)
library.add_book(book1)
library.add_book(book2)

print("-" * 60)
searched_title = "1984"
found_book = library.find_book_by_title(searched_title)

print(f"Found: {found_book}" if found_book else f"Book titled '{searched_title}' not found.")
print("\n")

