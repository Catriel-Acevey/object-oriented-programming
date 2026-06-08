class Book:
    def __init__(self, att_title, att_author):
        self.title = att_title
        self.author = att_author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

book1 = Book("1984", "George Orwell")
book2 = Book("cien años de soledad", "Gabriel García Márquez")

library1 = Library()
library1.add_book(book1)
library1.add_book(book2)

for book in library1.books:
    print(book.title)