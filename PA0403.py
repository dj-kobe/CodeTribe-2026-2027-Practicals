def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin successful.")
        return True

    print("\nInvalid username or password.")
    return False


def capture_student():
    print("\nCAPTURE STUDENT INFORMATION")
    return {
        "student_number": input("Student number: "),
        "name": input("Student name: "),
        "course": input("Course name: "),
        "programming": float(input("Programming mark: ")),
        "database": float(input("Database mark: ")),
        "web_development": float(input("Web Development mark: ")),
    }


def calculate_results(student):
    """Calculate and add total, average, and result to student data."""
    total = student["programming"] + student["database"] + student["web_development"]
    average = total / 3

    student["total"] = total
    student["average"] = average
    student["result"] = "Competent" if average >= 50 else "Not Yet Competent"
    return student


def display_results(student):
    """Display the currently captured student's results."""
    if student is None:
        print("\nNo student information has been captured yet.")
        return

    print("\nSTUDENT RESULTS")
    print("=" * 35)
    print(f"Student Number: {student['student_number']}")
    print(f"Student Name: {student['name']}")
    print(f"Course: {student['course']}")
    print(f"Programming Mark: {student['programming']:.2f}")
    print(f"Database Mark: {student['database']:.2f}")
    print(f"Web Development Mark: {student['web_development']:.2f}")
    print(f"Total: {student['total']:.2f}")
    print(f"Average: {student['average']:.2f}")
    print(f"Result: {student['result']}")


def save_results(student):
    """Save the current student's results to a text file."""
    if student is None:
        print("\nCapture student information before saving.")
        return

    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        for label, key in (
            ("Student Number", "student_number"),
            ("Student Name", "name"),
            ("Course", "course"),
            ("Programming Mark", "programming"),
            ("Database Mark", "database"),
            ("Web Development Mark", "web_development"),
            ("Total", "total"),
            ("Average", "average"),
            ("Result", "result"),
        ):
            value = student[key]
            file.write(f"{label}: {value:.2f}\n" if isinstance(value, float) else f"{label}: {value}\n")

    print(f"\nResults saved to {RESULTS_FILE}.")


def read_results():
    """Read and display previously saved results."""
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            print("\nSAVED STUDENT RESULTS")
            print("=" * 35)
            print(file.read())
    except FileNotFoundError:
        print("\nNo saved results were found.")


def display_menu():
    """Display menu choices and return the user's selection."""
    print("\nSTUDENT RESULTS MANAGEMENT SYSTEM")
    print("1. Capture student information")
    print("2. Display student results")
    print("3. Save results")
    print("4. Read saved results")
    print("5. Exit")
    return input("Enter your choice: ")


def main():
    """Control the program's main flow."""
    if not login():
        return

    student = None
    while True:
        choice = display_menu()

        if choice == "1":
            student = calculate_results(capture_student())
            print("Student information captured.")
        elif choice == "2":
            display_results(student)
        elif choice == "3":
            save_results(student)
        elif choice == "4":
            read_results()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
