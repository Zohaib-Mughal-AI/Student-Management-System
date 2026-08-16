import json


class Student:
    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "department": self.department
        }


class StudentManager:

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    # -------------------------
    # LOAD STUDENTS
    # -------------------------
    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    self.students = data
                else:
                    self.students = []

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("Warning: JSON file is invalid.")
            self.students = []

    # -------------------------
    # SAVE STUDENTS
    # -------------------------
    def save_students(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.students, file, indent=4)

        except OSError:
            print("Error: Could not save student data.")

    # -------------------------
    # ADD STUDENT
    # -------------------------
    def add_student(self):

        student_id = input("Enter Student ID: ").strip()

        if not student_id:
            print("Student ID cannot be empty.")
            return

        for student in self.students:
            if student["student_id"] == student_id:
                print("Student ID already exists.")
                return

        name = input("Enter Student Name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        try:
            age = int(input("Enter Student Age: "))

            if age <= 0 or age > 100:
                print("Please enter a valid age.")
                return

        except ValueError:
            print("Age must be a number.")
            return

        department = input("Enter Department: ").strip()

        if not department:
            print("Department cannot be empty.")
            return

        student = Student(
            student_id,
            name,
            age,
            department
        )

        self.students.append(student.to_dict())

        self.save_students()

        print("Student added successfully.")

    # -------------------------
    # VIEW STUDENTS
    # -------------------------
    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\n========== STUDENTS ==========")

        for student in self.students:

            print(
                f"ID: {student['student_id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Department: {student['department']}"
            )

        print("==============================")

    # -------------------------
    # SEARCH BY ID
    # -------------------------
    def search_by_id(self):

        student_id = input("Enter Student ID: ").strip()

        for student in self.students:

            if student["student_id"] == student_id:

                print("\nStudent Found")
                print(f"ID: {student['student_id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Department: {student['department']}")

                return

        print("Student not found.")

    # -------------------------
    # SEARCH BY NAME
    # -------------------------
    def search_by_name(self):

        name = input("Enter Student Name: ").strip().lower()

        found = False

        for student in self.students:

            if name in student["name"].lower():

                print(
                    f"ID: {student['student_id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Department: {student['department']}"
                )

                found = True

        if not found:
            print("Student not found.")

    # -------------------------
    # SEARCH BY DEPARTMENT
    # -------------------------
    def search_by_department(self):

        department = input("Enter Department: ").strip().lower()

        found = False

        for student in self.students:

            if department in student["department"].lower():

                print(
                    f"ID: {student['student_id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Department: {student['department']}"
                )

                found = True

        if not found:
            print("No students found in this department.")

    # -------------------------
    # UPDATE STUDENT
    # -------------------------
    def update_student(self):

        student_id = input("Enter Student ID to update: ").strip()

        for student in self.students:

            if student["student_id"] == student_id:

                print("Leave field empty to keep old value.")

                new_name = input(
                    f"New Name [{student['name']}]: "
                ).strip()

                new_age = input(
                    f"New Age [{student['age']}]: "
                ).strip()

                new_department = input(
                    f"New Department [{student['department']}]: "
                ).strip()

                if new_name:
                    student["name"] = new_name

                if new_age:

                    try:
                        new_age = int(new_age)

                        if new_age <= 0 or new_age > 100:
                            print("Invalid age.")
                            return

                        student["age"] = new_age

                    except ValueError:
                        print("Age must be a number.")
                        return

                if new_department:
                    student["department"] = new_department

                self.save_students()

                print("Student updated successfully.")

                return

        print("Student not found.")

    # -------------------------
    # DELETE STUDENT
    # -------------------------
    def delete_student(self):

        student_id = input("Enter Student ID to delete: ").strip()

        for student in self.students:

            if student["student_id"] == student_id:

                confirm = input(
                    f"Delete {student['name']}? (y/n): "
                ).strip().lower()

                if confirm == "y":

                    self.students.remove(student)

                    self.save_students()

                    print("Student deleted successfully.")

                else:

                    print("Delete cancelled.")

                return

        print("Student not found.")

    # -------------------------
    # STUDENT COUNT
    # -------------------------
    def student_count(self):

        print(
            f"Total Students: {len(self.students)}"
        )
