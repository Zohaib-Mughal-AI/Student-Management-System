from student_manager import StudentManager


def main():

    manager = StudentManager()

    while True:

        print("\n")
        print("===================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("===================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search by ID")
        print("4. Search by Name")
        print("5. Search by Department")
        print("6. Update Student")
        print("7. Delete Student")
        print("8. Student Count")
        print("9. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            manager.add_student()

        elif choice == "2":

            manager.view_students()

        elif choice == "3":

            manager.search_by_id()

        elif choice == "4":

            manager.search_by_name()

        elif choice == "5":

            manager.search_by_department()

        elif choice == "6":

            manager.update_student()

        elif choice == "7":

            manager.delete_student()

        elif choice == "8":

            manager.student_count()

        elif choice == "9":

            print("Thank you for using Student Management System.")
            break

        else:

            print("Invalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()
