class Student:
    def __init__(self, student_id, student_name, student_class):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class

    def display_student(self):
        try:
            print("Student ID:", self.student_id)
            print("Student Name:", self.student_name)
            print("Student Class:", self.student_class)
        except Exception as e:
            print("Error:", e)


def main():
    student1 = Student(4, "Param", "IT")

    student1.display_student()

    print()

    student2 = Student(10, "Aditya", "DS")

    student2.display_student()


main()
