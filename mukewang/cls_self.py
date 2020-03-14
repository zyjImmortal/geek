

class Student:
    name = 'wanger'
    def __init__(self):
        self.age  = 34

    def print_name(self):
        print(Student.name)

    @staticmethod
    def print_age_name():
        print(Student.name)


stu = Student()
stu.print_name()
Student.print_age_name()