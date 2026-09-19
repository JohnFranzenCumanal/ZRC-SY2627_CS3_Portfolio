class Student:
    def __init__(self, student_name):
        self.student_name = student_name


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Example usage
course = Course("Python 101")

# Create 3 students
student1 = Student("Alice")
student2 = Student("Bob")
student3 = Student("Charlie")

# Add all students to the course
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# Print all enrolled students
for student in course.students:
    print(student.student_name)
