from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def accelerate():
        pass

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors) -> None:  # child class constructor
        super().__init__(brand, model)  # parent class constructor
        self.num_doors = num_doors
    
    def accelerate():
        print("acelerando...")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, displacement) -> None:
        super().__init__(brand, model)
        self.displacement = displacement

    def accelerate():
        print("acclerating a motorcycle...")

car = Car("RRR", "2020", 4)
motorcycle = Motorcycle("TTT", "2021", 100)