
#? Library Management System

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, title):
        if len(self.borrowed_books) < 5 and library.lend_book(title):
            self.borrowed_books.append(title)
            print(f"{self.name} ยืมหนังสือ {title}")
        else:
            print("ไม่สามารถยืมหนังสือได้")

    def return_book(self, library, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            library.return_book(title)
            print(f"{self.name} คืนหนังสือ {title}")
        else:
            print("ไม่มีหนังสือในรายการยืม")

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.title in self.books:
            self.books[book.title].copies += book.copies
        else:
            self.books[book.title] = book
        print(f"เพิ่มหนังสือ {book.title} จำนวน {book.copies} เล่ม")

    def lend_book(self, title):
        if title in self.books and self.books[title].copies > 0:
            self.books[title].copies -= 1
            if self.books[title].copies == 0:
                del self.books[title]
            return True
        return False

    def return_book(self, title):
        if title in self.books:
            self.books[title].copies += 1
        else:
            self.books[title] = Book(title, "Unknown", 1)

    def report(self):
        print("รายงานหนังสือในห้องสมุด:")
        for title, book in self.books.items():
            print(f"{title} - {book.copies} เล่ม")
