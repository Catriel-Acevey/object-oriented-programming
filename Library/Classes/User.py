from abc import ABC, abstractmethod

class User(ABC):
    __ID: int
    nombre: str
    email: str
    
    def __init__(self, name, email)->None:
        super().__init__()
        self.name = name
        self.email = email

    @abstractmethod
    def update_data(self):
        pass