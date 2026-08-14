
def capture_student():
    """Ask the user for student details and display them clearly."""
    student_number = input("Enter student number: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = int(input("Enter age: "))
    course = input("Enter course name: ")
    programming_mark = float(input("Enter Programming mark: "))
    database_mark = float(input("Enter Database mark: "))
    web_development_mark = float(input("Enter Web Development mark: "))

    print("\nSTUDENT INFORMATION")
    print("=" * 35)
    print(f"Student Number: {student_number}")
    print(f"Student Name: {name} {surname}")
    print(f"Age: {age}")
    print(f"Course: {course}")
    print(f"Programming Mark: {programming_mark:g}")
    print(f"Database Mark: {database_mark:g}")
    print(f"Web Development Mark: {web_development_mark:g}")


capture_student()
