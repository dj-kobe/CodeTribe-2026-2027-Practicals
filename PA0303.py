from datetime import datetime
from os import name


def save_results(student_number, full_name, course, programming, database, web_development):
    """Calculate and save one student's results to student_results.txt."""
    total = programming + database + web_development
    average = total / 3
    result = "Competent" if average >= 50 else "Not Yet Competent"
    date_saved = datetime.now().strftime("%d %B %Y")

    with open("student_results.txt", "w", encoding="utf-8") as file:
        file.write(f"Student Number: {student_number}\n")
        file.write(f"Student Name: {full_name}\n")
        file.write(f"Course: {course}\n")
        file.write(f"Programming: {programming}\n")
        file.write(f"Database: {database}\n")
        file.write(f"Web Development: {web_development}\n")
        file.write(f"Total: {total}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Result: {result}\n")
        file.write(f"Date Saved: {date_saved}\n")


def read_results():
    """Read student_results.txt and display its contents."""
    try:
        with open("student_results.txt", "r", encoding="utf-8") as file:
            print("\nStudent results")
            print("-" * 30)
            print(file.read())
    except FileNotFoundError:
        print("No results file was found. Save results first.")


def main():
    student_number = input("Enter student number: ")
    full_name = input("Enter full name: ")
    course = input("Enter course: ")
    programming = float(input("Enter Programming mark: "))
    database = float(input("Enter Database mark: "))
    web_development = float(input("Enter Web Development mark: "))

    save_results(
        student_number,
        full_name,
        course,
        programming,
        database,
        web_development,
    )
    print("\nResults saved to student_results.txt.")
    read_results()


if name == " main":
    main()
