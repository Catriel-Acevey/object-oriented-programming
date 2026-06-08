class Motor:
    def __init__(self, power):
        self.power = power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, power, wheel_size):
        self.motor = Motor(power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

car1 = Car(200, 30)
car2 = Car(120, 22)

print(car1.motor.power)
for wheel in car1.wheels:    
    print(wheel.size)

print(car2.motor.power)
for wheel in car2.wheels:    
    print(wheel.size)