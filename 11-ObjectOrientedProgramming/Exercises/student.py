# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.field_of_study = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.field_of_study = "Computer Science"
    student2.name = "Olivia"
    student2.age = 21
    student2.field_of_study = "Economics"
    student3.name = "Jakub"
    student3.age = 20
    student3.field_of_study = "Applied Computer Science"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.field_of_study}')
    print(f'{student2.name}, {student2.age} years old, {student2.field_of_study}')
    print(f'{student3.name}, {student3.age} years old, {student3.field_of_study}')

if __name__ == "__main__":
    main()
