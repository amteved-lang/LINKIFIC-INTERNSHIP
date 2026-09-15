# Student Record Management System
# Task 3 - AI/ML Internship

FILE_NAME = "students.txt"


# ==========================================
# ADD STUDENT
# ==========================================

def add_student():
    print("\n===== Add Student =====")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(
            f"{student_id}|{name}|{age}|{course}|{marks}\n"
        )

    print("Student record added successfully!")


# ==========================================
# VIEW STUDENTS
# ==========================================

def view_students():
    print("\n===== Student Records =====")

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found.")
                return

            for record in records:
                data = record.strip().split("|")

                print("--------------------------------")
                print("Student ID :", data[0])
                print("Name       :", data[1])
                print("Age        :", data[2])
                print("Course     :", data[3])
                print("Marks      :", data[4])

    except FileNotFoundError:
        print("No records file found.")


# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student():
    print("\n===== Search Student =====")

    search_id = input("Enter Student ID: ")

    try:
        with open(FILE_NAME, "r") as file:

            for record in file:
                data = record.strip().split("|")

                if data[0] == search_id:
                    print("\nStudent Found!")
                    print("Student ID :", data[0])
                    print("Name       :", data[1])
                    print("Age        :", data[2])
                    print("Course     :", data[3])
                    print("Marks      :", data[4])
                    return

        print("Student not found.")

    except FileNotFoundError:
        print("No records file found.")


# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n================================")
        print(" STUDENT RECORD MANAGEMENT")
        print("================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()