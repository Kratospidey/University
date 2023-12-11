# WAP to create a Derived class from 2 Parent classes. The derived class should override one of the parent class' methods.
class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_personal_info(self):
        print()
        print("Personal info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Student():
    def __init__(self, rollno, gpa):
        self.rollno = rollno
        self.gpa = gpa

    def show_academic_info(self):
        print("I am an university student!")
        print(f"Roll No: {self.rollno}")
        print(f"University Name: {self.uniname}")
        print(f"GPA: {self.gpa}")

class SVKMStudent(Person, Student):
    def __init__(self, name, age, gender, rollno, gpa, college, degree, stream, year, sapid):
        # Call the constructors of the parent classes
        Person.__init__(self, name, age, gender)
        Student.__init__(self, rollno, gpa)

        # Initialize SVKMStudent's own attributes
        self.college = college
        self.degree = degree
        self.stream = stream
        self.year = year
        self.sapid = sapid

      
    def show_academic_info(self):
        print()
        print("Academic Info: ")
        # Print information from the Student parent class
        print(f"Roll No: {self.rollno}")
        print(f"GPA: {self.gpa}")

        # Print SVKMStudent's own academic information
        print(f"College: {self.college}")
        print(f"Degree: {self.degree}")
        print(f"Stream: {self.stream}")
        print(f"Year: {self.year}")
        print(f"SAP ID: {self.sapid}")

        
      
stud = SVKMStudent("Param", "18", "Male", "F004", "3.0", "MPSTME", "BTI", "IT", "3", "70372100050")
stud.show_academic_info()
stud.show_personal_info()