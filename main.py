# person class
class Person:
    name = ""
    age = 1
    height = 0.0
    gender = ""

    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender

    def walk(self):
        return f"Hello, I'm {self.name} and I am walking..."

    def speak(self):
        return f"Hello, I'm {self.name} and I am speaking..."

found_people = []
while True:
    option = int(input("""Choose an option:
             1. Enter data
             2. View people list
             0. Exit
             : """))
    if option == 0:
        break
    if option == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        height = float(input("Enter height: "))
        gender = input("Enter gender: ")

        person = Person(name, age, height, gender)
        found_people.append(person)
    else:
        for person in found_people:
            print(person.name)