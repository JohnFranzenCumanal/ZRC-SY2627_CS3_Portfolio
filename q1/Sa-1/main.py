class AssignmentSubmission:

    def __init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = True
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score: float):
        if score > 0 and score <= 100:
            return True
        else:
            print("Grade must be between 0 and 100.")

    def __check_submission_status(self):
        if self.__is_submitted:
            return True
        else:
            return False

    def __is_duplicated(self, filename: str):
        if filename in self.__submitted_files:
            return True
        else:
            return False

    def add_file(self, filename: str):
        if self.__check_submission_status():
            if not self.__is_duplicated(filename):
                self.__submitted_files.append(filename)
                print(f"--> [Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")
            else:
                print(f"--> [Success] '{filename}' is already attached!")
        else:
            print("Cannot add files. Assignment has not been submitted.")

    def remove_file(self, filename: str):
        if self.__grade is not None:
            print(f"--> [Warning] {self.student_name} cannot remove files. Assignment already graded.")
        elif self.__check_submission_status():
            if filename in self.__submitted_files:
                self.__submitted_files.remove(filename)
                print(f"--> [Success] {self.student_name} removed '{filename}'.")
            else:
                print(f"{filename} not found in the submission.")
        else:
            print(f"Cannot remove files. Assignment has not been submitted.")

    def assign_grade(self, score: float):
        if not self.__submitted_files:
            print(f"--> [Error] Cannot grade. No files submitted for {self.student_name}")
        elif self.__validate_grade(score):
            self.__grade = score
            print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")

        else:
            print(f"Cannot assign grade. Assignment has not been submitted.")

    def get_grade(self):
        if self.__check_submission_status():
            return self.__grade
        else:
            print(f"Cannot retrieve grade. Assignment has not been submitted.")

    def view_files(self):
        if self.__check_submission_status():
            return ", ".join(self.__submitted_files)
        else:
            print(f"Cannot view files. Assignment has not been submitted.")

    def get_status_report(self):
        status = (f"Submitted ({len(self.__submitted_files)} files)"
              if self.__submitted_files else "Missing")
        grade = self.__grade if self.__grade is not None else "Not Graded"
        return (f"ID: {self.student_id} | Name: {self.student_name.title():<16}| "
            f"Status: {status:<19} | Grade: {grade}")

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-103", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-103", due_date="2026-10-01")
print()

print("--- TEXT SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEXT SCENARIO 2: Removing files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEXT SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEXT SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf") # Blocked by grading status
print()

print("--- TEXT SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
