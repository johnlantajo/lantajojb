 
class Student:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        return f"Hello! My name is {self.name}. I am {self.age} years old, and I am studying {self.course}."


def print_introductions(students):
    for student in students:
        print(student.introduce())


students = [
    Student("John Benedict L. Lantajo", 20, "Computer Science"),
    Student("Bobby", 22, "Programming"),
    Student("Ronne;", 21, "Logic")
]


print_introductions(students)

