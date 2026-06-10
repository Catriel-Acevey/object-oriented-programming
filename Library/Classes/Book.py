class Book:

    ISN: str
    title: str
    author: str
    publication_year: str
    state: int

    def __init__(self, ISN, title, author, publication_year, state=1) -> None:
        self.ISN = ISN
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.state = state

    def actualizar_libro():
        pass

    def show(self):
        print(f"ISN: {self.ISN}")
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"publication_year: {self.publication_year}")
        print(f"state: {self.state}")

b1 = Book("ISBN001", "Harry Potter", "J.K. Rowling", "1997", 2)

b1.show()