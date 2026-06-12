from User import User
from Book import Book
from datetime import datetime
import random

class Reader(User):

    register_date: str
    
    def __init__(self, name, email) -> None:
        super().__init__(name, email)
    
    def update_data(self, data: dict):
        for attr, value in data.items():
            setattr(self, attr, value)

    def make_loan(self, books: list[Book]):
        loan = Loan(reader = self, books = books)
        return loan

    def check_loan(self, id=None):
        if id:
            found = False
            for loan in db_loans:
                if loan.ID_loan == id:
                    print(f"""
                        ID: {loan.ID_loan}
                        date: {loan.loan_date}""")
                    found = True
                    break
            if not found:
                print(f"the loan with id {id} not found")
        else:
            for loan in db_loans:
                if loan.reader.email == self.email:
                    print(f"""
                        ID: {loan.ID_loan}
                        name: {loan.reader.name}
                        date: {loan.loan_date}""")


class Loan:
    ID_loan: int
    loan_date: str
    back_date: str
    state: int
    books: list[Book]
    reader: Reader

    def __init__(self, reader: Reader, books: list[Book]) -> None:
        self.ID_loan = random.randint(1000, 9999)
        self.loan_date = datetime.today()
        self.state = 1
        self.reader = reader
        self.books = books
    def back_register(self, book: Book):
        pass

db_loans: list[Loan] = []


# reader1 = Reader("John Doe", "john@gmail.com")
# reader2 = Reader("Jane Smith", "jane@gmail.com")
# reader3 = Reader("Michael Brown", "michael@gmail.com")
# book1 = Book("ISBN006", "Pride and Prejudice", "Jane Austen", "1813", 1)
# book2 = Book("ISBN001", "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "1997", 1)

# loan1 = reader1.make_loan([book1])

# db_loans.append(loan1)

# loan2 = reader2.make_loan([book1, book2])

# db_loans.append(loan2)

# loan3 = reader3.make_loan([book2])

# db_loans.append(loan3)

# for loan in db_loans:
#     print("---------")
#     print(f"Loan ID: {loan.ID_loan}")
#     print(f"Reader: {loan.reader.name}")
#     print(f"Loan Date: {loan.loan_date}")
#     print(f"Books: {[book.title for book in loan.books]}")
#     print(f"State: {loan.state}")
#     print("---------")

# reader3.check_loan()