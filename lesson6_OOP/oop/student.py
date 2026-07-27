class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("John", 25)
student1 = Student("Jane", 22)
print(student.name, student.age)
print(student1.name, student1.age)
