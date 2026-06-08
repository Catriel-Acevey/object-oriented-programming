from abc import ABC, abstractmethod

class User(ABC):
    ID: int
    nombre: str
    email: str
    
    def __init__(self)->None:
        super().__init__()

    @abstractmethod
    def update_data(self):
        pass