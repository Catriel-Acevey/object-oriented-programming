class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.age = age
        self.gender = gender
    
    @property  # getter method
    def name(self):
        return self.__name
    
    @name.setter  # setter method
    def name(self, value):
        if value == "":
            print("The name cannot be empty")
            return
        if len(value) < 3:
            print("The name must have at least 3 characters")
            return
        self.__name = value


person1 = Person("Jesus", 22, "m")

print(person1.name)
person1.name = "J"
print(person1.name)