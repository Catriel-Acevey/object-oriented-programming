from User import User
from Book import Book

class Reader(User):

    register_date: str
    
    def __init__(self) -> None:
        super().__init__()
    
    def update_data(self):
        
        for attr, value in data.items():
            setattr(self, attr, value)

    def check_loan(self):
        pass

    def make_loan(self, book: Book):
        pass