
#* Encapsulation2

class Library:
    def __init__(self, books):
        self._books = books
 
    def add_book(self, book):
        self._books.append(book)
 
    def remove_book(self, title):
        book_to_remove = self.search_book(title)
        if book_to_remove:
            self._books.remove(book_to_remove)
        else:
            print("Book not found")
 
    def search_book(self, title):
        for book in self._books:
            if book.title == title:
                return book
        return None
 
 
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
 
    def __repr__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
 
 
library = Library([
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949)
])
 
library.add_book(Book("Pride and Prejudice", "Jane Austen", 1813))
print(library.search_book("1984"))  # Output: 1984 by George Orwell, published in 1949

library.remove_book("The Great Gatsby")  # Output: Book not found
