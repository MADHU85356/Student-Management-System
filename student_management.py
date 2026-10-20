"""Console-based Student Management System mini project.

Features:
- Add, display, search, update, and delete student records.
- Uses a list of dictionaries and stores records in memory only.
- No third-party dependencies are required.
"""

students = []


def find_student(roll):
    """Return a student record matching roll number, or None."""
    for student in students:
        if student["roll"] == roll:
            return student
    return None


def add_student():
    """Collect and add a student record."""
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number. Please enter a number.")
        return

    if find_student(roll):
        print("A student with that roll number already exists.")
        return

    name = input("Enter student name: ").strip()
    branch = input("Enter branch: ").strip()
    if not name or not branch:
        print("Name and branch cannot be empty.")
        return

    students.append({"roll": roll, "name": name, "branch": branch})
    print("Student added successfully!")


def display_students():
    """Display all student records."""
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 35)
    for student in students:
        print(f"Roll Number: {student['roll']}")
        print(f"Name       : {student['name']}")
        print(f"Branch     : {student['branch']}")
        print("-" * 35)


def search_student():
    """Search for a student by roll number."""
    try:
        roll = int(input("Enter roll number to search: "))
    except ValueError:
        print("Invalid roll number. Please enter a number.")
        return

    student = find_student(roll)
    if student:
        print(f"Found: Roll={student['roll']}, Name={student['name']}, Branch={student['branch']}")
    else:
        print("No student found with that roll number.")


def delete_student():
    """Delete a student by roll number."""
    try:
        roll = int(input("Enter roll number to delete: "))
    except ValueError:
        print("Invalid roll number. Please enter a number.")
        return

    student = find_student(roll)
    if student:
        students.remove(student)
        print("Student deleted successfully.")
    else:
        print("No student found with that roll number.")


def update_student():
    """Update a student's name, branch, or roll number."""
    try:
        roll = int(input("Enter roll number to update: "))
    except ValueError:
        print("Invalid roll number. Please enter a number.")
        return

    student = find_student(roll)
    if not student:
        print("No student found with that roll number.")
        return

    print("1. Update name")
    print("2. Update branch")
    print("3. Update roll number")
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
        name = input("Enter new name: ").strip()
        if name:
            student["name"] = name
            print("Name updated successfully.")
        else:
            print("Name cannot be empty.")
    elif choice == "2":
        branch = input("Enter new branch: ").strip()
        if branch:
            student["branch"] = branch
            print("Branch updated successfully.")
        else:
            print("Branch cannot be empty.")
    elif choice == "3":
        try:
            new_roll = int(input("Enter new roll number: "))
        except ValueError:
            print("Invalid roll number. Please enter a number.")
            return
        if find_student(new_roll):
            print("That roll number is already in use.")
        else:
            student["roll"] = new_roll
            print("Roll number updated successfully.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


def main_menu():
    """Run the main menu until the user chooses Exit."""
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please choose 1-6.")


if __name__ == "__main__":
    main_menu()
