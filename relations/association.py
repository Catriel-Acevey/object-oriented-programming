class Department:
    def __init__(self, name, code) -> None:
        self.name = name
        self.code = code
        self.teachers = []

class Teacher:
    def __init__(self, name) -> None:
        self.name = name
        self.department = None

    def add_department(self, department: Department) -> None:
        self.department = department
        department.teachers.append(self)


#Create department and teachers
department1 = Department("Computer Science 2", "0023")
teacher1 = Teacher("John")
teacher2 = Teacher("Jane")


#Ascociate teachers with department
teacher1.add_department(department1)

print(teacher1.name)
print(teacher1.department.name)

print(department1.code)

for teacher in department1.teachers:
    print(teacher.name)