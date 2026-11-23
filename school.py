students = []

def add_student():
    print("\n--- Student Admission ---")

    roll = input("Enter Roll Number: ")

    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    student_class = input("Enter Class: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "class": student_class,
        "attendance": 0,
        "marks": 0,
        "fees": 0
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            print("-------------------")
            print("Roll Number:", s["roll"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Class:", s["class"])


def search_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found!")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Class:", s["class"])
            return

    print("Student not found!")


def attendance():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            s["attendance"] += 1
            print("Attendance marked successfully!")
            return

    print("Student not found!")


def results():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            marks = int(input("Enter Student Marks: "))

            s["marks"] = marks

            print("Result Updated!")
            print("Student Name:", s["name"])
            print("Marks:", marks)

            if marks >= 40:
                print("Result: Pass")
            else:
                print("Result: Fail")

            return

    print("Student not found!")


def fee_management():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            fee = float(input("Enter Fee Amount: "))

            s["fees"] += fee

            print("Fee deposited successfully!")
            print("Total Fees Paid:", s["fees"])
            return

    print("Student not found!")


while True:

    print("\n==============================")
    print("   SCHOOL MANAGEMENT SYSTEM")
    print("==============================")

    print("1. Student Admission")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Student Attendance")
    print("5. Examination Results")
    print("6. Fee Management")
    print("7. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        attendance()

    elif choice == "5":
        results()

    elif choice == "6":
        fee_management()

    elif choice == "7":
        print("Thank You for Using School Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
