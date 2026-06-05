class Student:
    """Represents a student and provides basic operations.

    Attributes:
        identification (int): Unique student ID.
        name (str): Full student name.
        age (int): Student age.
        semester (int): Current semester.
        grades (list[float]): List of grades.
    """

    def __init__(self, identification: int, name: str, age: int, semester: int, grades: list[float]) -> None:
        self.identification = identification
        self.name = name
        self.age = age
        self.semester = semester
        self.grades = grades

    def get_average(self) -> float:
        """Calculate and return the student's average grade."""
        if not self.grades:
            return 0.0

        average = sum(self.grades) / len(self.grades)
        return average

    def show_information(self) -> None:
        """Print the student's full information."""
        print("Student information:")
        print(f"ID: {self.identification}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Semester: {self.semester}")
        print(f"Grades: {self.grades}")
        average = self.get_average()
        print(f"Average: {average:.2f}")


student1 = Student(123, "Juan Perez", 20, 4, [3.5, 4.0, 2.8])
student2 = Student(456, "Maria Gomez", 22, 6, [4.0, 4.5, 3.9])
student3 = Student(789, "Carlos Sanchez", 19, 2, [2.5, 3.0, 3.2])
students: list[Student] = [student1, student2, student3]

while True:
    option = int(input("""Choose an option:
             1. Enter student data
             2. View a student's average
             3. View a student's information
             0. Exit
             : """))
    if option == 0:
        break
    if option == 1:
        identification = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        semester = int(input("Enter student semester: "))
        print("Enter the student's grades:")
        grades = []
        for i in range(3):
            grades.append(float(input(f"Enter grade {i+1}: ")))

        student = Student(identification, name, age, semester, grades)

        students.append(student)

    elif option == 2 or option == 3:
        identification = int(input("Enter student ID: "))

        for student in students:
            if student.identification == identification and option == 2:
                average = student.get_average()
                print(f"The average for {student.name} is {average:.2f}")
            elif student.identification == identification and option == 3:
                student.show_information()