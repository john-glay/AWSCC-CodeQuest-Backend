class Student:
    def __init__(self, name, age, 
        is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses

    # add a new class to the student
    def add_class(self, new_class):
        self.classes.append(new_class)

student1 = Student("John Glay C. Bunao", 20, True, [], [])
student1.add_class("Computer Science")

print(f"\nName: {student1.name}")
print(f"Age: {student1.age}")
print(f"Status: {'Enrolled' if student1.is_enrolled else 'Not Enrolled Yet'}")
print(f"Classes: {student1.classes}")
print(f"Offenses: {student1.offenses}\n")