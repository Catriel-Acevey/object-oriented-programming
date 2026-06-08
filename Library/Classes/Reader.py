from User import User

class Reader(User):

    register_date: str
    
    def __init__(self) -> None:
        super().__init__()
    
    def check_loan(self):
        pass

    def make_loan(self):
        pass