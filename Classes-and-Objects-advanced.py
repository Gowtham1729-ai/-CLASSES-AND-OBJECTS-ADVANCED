# Advanced Classes and Objects - Python OOPS
# Developed by: Goutham S
# Department: AI & DS
# College: SRM TRP Engineering College

class Person:
    college = "SRM TRP Engineering College"   # Class Variable

    def _init_(self, name, age):
        self.name = name
        self.__age = age     # Private variable (Encapsulation)

    def display_basic(self):
        print(f"Name       : {self.name}")
        print(f"Age        : {self.__age}")
        print(f"College    : {Person.college}")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")


class Student(Person):   # Inheritance
    def _init_(self, name, age, dept, year):
        super()._init_(name, age)
        self.dept = dept
        self.year = year

    def display_student(self):
        self.display_basic()
        print(f"Department : {self.dept}")
        print(f"Year       : {self.year}")


class Skills:
    def show_skills(self):
        print("Skills     : Python (Intermediate), Problem Solving, OOPS")


class Developer(Student, Skills):   # Multiple Inheritance
    def _init_(self, name, age, dept, year, project):
        Student._init_(self, name, age, dept, year)
        self.project = project

    def full_profile(self):
        print("\n------ Student Full Profile ------")
        self.display_student()
        self.show_skills()
        print(f"Project    : {self.project}")


class Utility:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return f"Utility Class : {cls._name_}"


# Main Program
dev = Developer(
    name="Goutham S",
    age=18,
    dept="Artificial Intelligence & Data Science (AI & DS)",
    year="1st Year",
    project="Advanced Classes & Objects System using Python"
)

dev.full_profile()

print("\n------ Encapsulation Test ------")
print("Current Age:", dev.get_age())
dev.set_age(19)
print("Updated Age:", dev.get_age())

print("\n------ Static Method ------")
print("Addition:", Utility.add(25, 35))

print("\n------ Class Method ------")
print(Utility.info())
