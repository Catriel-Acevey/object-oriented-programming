import json
from User import User
from Book import Book

class Librarian(User):
    
    rol: str
    
    def __init__(self, name, email, rol) -> None:
        super().__init__(name, email)

        self.rol = rol

    def update_data(self, data: dict):
        for attr, value in data.items():
            setattr(self, attr, value)

    def book_register(self, book: Book):
        try:
            with open("/home/catrielwsl/Projects/poo/Library/database/db_book.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            books=[]
        books.append(vars(book))
        with open("/home/catrielwsl/Projects/poo/Library/database/db_book.json", "w") as file:
            json.dump(books, file, indent=4)

    def delete_book(self, ISBN: str):
        try:
            with open("/home/catrielwsl/Projects/poo/Library/database/db_book.json", "r") as file:
                books= json.load(file)
        except FileNotFoundError:
            print("Unable to read the file")
            return False
        updated_books = [book for book in books if book["ISBN"] != ISBN]

        if len(updated_books) == len(books):
            print("The book to be deleted was not found")
            return False
        with open("/home/catrielwsl/Projects/poo/Library/database/db_book.json", "w") as file:
            json.dump(updated_books, file, indent=4)

        print("The book was deleted")
        return True


l1 = Librarian("Jesus", "jesus@gmail.com", "admin")
b1 = Book("ISBN006", "Pride and Prejudice", "Jane Austen", "1813", 1)