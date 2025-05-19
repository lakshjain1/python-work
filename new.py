student_grades = {}

while True:
    print("\nMenu:")
    print("1. Add new student")
    print("2. Update existing student")
    print("3. Print all students and grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists with grade {student_grades[name]}.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"{name} added with grade {grade}.")

    elif choice == '2':
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"{name} not found.")

    elif choice == '3':
        if not student_grades:
            print("No student records found.")
        else:
            print("\nStudent Grades:")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
