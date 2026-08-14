
def main():
    print("STUDENT INFORMATION CAPTURE")
    print("=" * 30)

    # Console input
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")
    course = input("Enter course name: ")
    mark = float(input("Enter the student's mark: "))

    # Console output
    print("\nSTUDENT DETAILS")
    print("=" * 30)
    print(f"Student number: {student_number}")
    print(f"Student name: {student_name}")
    print(f"Course: {course}")
    print(f"Mark: {mark:.2f}%")


if __name__ == "__main__":
    main()
