# Write a Python class named Student with two attributes student_class, student_name. Add a new attribute student_class. 
# Create a function to display the entire attribute and their values in Student class with exception handling.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def displayStudent(self):
        try:
            for attr, value in self.__dict__.items():
                print(f"{attr}: {value}")
        except Exception as e:
            print("Error occurred:", e)

# Usage
student1 = Student("4", "Param")
student1.student_class = "IT"
# Adding another attribute for demonstration
student1.student_grade = "A"
student1.displayStudent()