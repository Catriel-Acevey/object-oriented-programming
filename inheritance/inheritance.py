class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def show_info(self):
        print(f"Battery capacity: {self.battery_capacity} kWh")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors) -> None:  # child class constructor
        super().__init__(brand, model)  # parent class constructor
        self.num_doors = num_doors
    
    def door_count(self):
        print(f"The car has {self.num_doors} doors")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, displacement) -> None:
        super().__init__(brand, model)
        self.displacement = displacement

    def show_info(self):
        super().show_info()
        print(f"Displacement: {self.displacement} cc")

class ElectricCar(Car, Electric):
    def __init__(self, brand, model, num_doors, battery_capacity) -> None:
        Car.__init__(self, brand, model, num_doors)
        Electric.__init__(self, battery_capacity)

    def show_info(self):
        Car.show_info(self)
        Electric.show_info(self)

class PickupTruck(Car):
    def __init__(self, brand, model, num_doors, cargo_capacity) -> None:
        super().__init__(brand, model, num_doors)
        self.cargo_capacity = cargo_capacity

    def show_info(self):
        super().show_info()
        print(f"Cargo capacity: {self.cargo_capacity} kg")


electric_car = ElectricCar("Tesla", "Model S", 4, "100")
electric_car.show_info()

pickup = PickupTruck("Ford", "F-150", 4, 1000)
pickup.show_info()


