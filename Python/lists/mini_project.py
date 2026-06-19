students = []

while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print("Student removed.")
        else:
            print("Student not found.")

    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print("Student found.")
        else:
            print("Student not found.")

    elif choice == "4":
        print("\nStudent List:")
        if len(students) == 0:
            print("No students available.")
        else:
            for student in students:
                print(student)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")