from Reader import Reader
from Book import Book

class Loan:
    ID_loan: int
    loan_date: str
    back_date: str
    state: int
    books: list[Book]
    reader:Reader

    def __init__(self) -> None:
        pass
    def back_register(self, book: Book):
        pass