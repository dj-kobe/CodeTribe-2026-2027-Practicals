def calculate_average(total, number_of_subjects):
    if number_of_subjects == 0:
        return 0

    return total / number_of_subjects


def determine_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


def get_student_details():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")

    return student_number, student_name


def capture_marks(number_of_subjects):
    marks = []

    for subject in range(1, number_of_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter mark for Subject {subject}: "))

                # Ensure that the mark is between 0 and 100.
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a mark between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return marks


def calculate_total(marks):
    return sum(marks)


def display_results(student_number, student_name, marks):
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    grade = determine_grade(average)

    print("\n" + "=" * 40)
    print("       STUDENT RESULTS")
    print("=" * 40)
    print(f"Student Number : {student_number}")
    print(f"Student Name   : {student_name}")

    for number, mark in enumerate(marks, start=1):
        print(f"Subject {number}     : {mark:.2f}%")

    print("-" * 40)
    print(f"Total          : {total:.2f}")
    print(f"Average        : {average:.2f}%")
    print(f"Grade          : {grade}")
    print("=" * 40)


def save_results(student_number, student_name, marks):
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    grade = determine_grade(average)

    # Open the file in append mode so existing results are not deleted.
    with open("student_results.txt", "a") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write("STUDENT RESULTS\n")
        file.write("=" * 40 + "\n")
        file.write(f"Student Number: {student_number}\n")
        file.write(f"Student Name: {student_name}\n")

        for number, mark in enumerate(marks, start=1):
            file.write(f"Subject {number}: {mark:.2f}%\n")

        file.write(f"Total: {total:.2f}\n")
        file.write(f"Average: {average:.2f}%\n")
        file.write(f"Grade: {grade}\n")

    print("\nResults successfully saved to student_results.txt.")


def main():
    print("=" * 40)
    print(" STUDENT RESULTS MANAGEMENT SYSTEM")
    print("=" * 40)

    # Capture student information.
    student_number, student_name = get_student_details()

    while True:
        try:
            number_of_subjects = int(input("Enter number of subjects: "))

            if number_of_subjects > 0:
                break

            print("Number of subjects must be greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")

   
    marks = capture_marks(number_of_subjects)

    
    display_results(student_number, student_name, marks)

    save_choice = input("\nDo you want to save the results? (Y/N): ")

    if save_choice.upper() == "Y":
        save_results(student_number, student_name, marks)
    else:
        print("Results were not saved.")


# Start the program.
if 'name' == "main":
    main()