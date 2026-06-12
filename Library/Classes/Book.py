class Book:

    ISBN: str
    title: str
    author: str
    publication_year: str
    state: int

    def __init__(self, ISBN, title, author, publication_year, state=1) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.state = state

    def actualizar_libro():
        pass

    def show(self):
        print(f"ISBN: {self.ISBN}")
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"publication_year: {self.publication_year}")
        print(f"state: {self.state}")