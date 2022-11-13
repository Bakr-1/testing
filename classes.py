class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(self.age)


student1 = [student("John", 20), student("Mary", 21), student("Bob", 22)]
student.print_name(student1[0])
student.print_age(student1[0])
student.print_name(student1[1])
student.print_age(student1[1])
student.print_name(student1[2])
student.print_age(student1[2])
