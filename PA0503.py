
def get_student_details():
    student_number = input("Enter student number: ")
    student_name = input("Enter student name: ")

    # Handle letters entered instead of an age.
    while True:
        try:
            age = int(input("Enter student age: "))

            if age < 0:
                raise ValueError("Age cannot be negative.")

        except ValueError as error:
            print("Invalid age:", error)
            print("Please enter a valid number.")

        else:
            print("Age accepted.")

            break

        finally:
            print("Age entry process completed.")

    return student_number, student_name, age


def capture_marks(number_of_subjects):
    marks = []

    for subject in range(1, number_of_subjects + 1):

        while True:
            try:
                # Convert the user's input into a number.
                mark = float(input(f"Enter mark for Subject {subject}: "))

                # Check whether the mark is within the valid range.
                if mark < 0 or mark > 100:
                    raise ValueError("Mark must be between 0 and 100.")

            except ValueError as error:
                print("Invalid input:", error)
                print("Please enter a mark between 0 and 100.")

            else:
                print("Mark accepted.")
                marks.append(mark)
                break

            finally:
                print("Mark entry process completed.")

    return marks


def calculate_total(marks):
    return sum(marks)


def calculate_average(total, number_of_subjects):
    try:
        # Prevent division by zero.
        if number_of_subjects == 0:
            raise ZeroDivisionError("Cannot divide by zero subjects.")

        average = total / number_of_subjects

    except ZeroDivisionError as error:
        print("Calculation error:", error)
        return 0

    else:
        return average

    finally:
        print("Average calculation completed.")



def display_results(student_number, student_name, age, marks):


    total = calculate_total(marks)

    # Calculate the average using the number of subjects.
    average = calculate_average(total, len(marks))

    grade = determine_grade(average)

    print("\n" + "=" * 45)
    print("          STUDENT RESULTS")
    print("=" * 45)

    print(f"Student Number : {student_number}")
    print(f"Student Name   : {student_name}")
    print(f"Student Age    : {age}")

    print("-" * 45)

    for number, mark in enumerate(marks, start=1):
        print(f"Subject {number}     : {mark:.2f}%")

    print("-" * 45)
    print(f"Total          : {total:.2f}")
    print(f"Average        : {average:.2f}%")
    print(f"Grade          : {grade}")

    print("=" * 45)


def save_results(student_number, student_name, age, marks):

    try:
        total = calculate_total(marks)
        average = calculate_average(total, len(marks))
        grade = determine_grade(average)

        # Open the results file in append mode.
        with open("student_results.txt", "a") as file:

            file.write("\n" + "=" * 45 + "\n")
            file.write("STUDENT RESULTS\n")
            file.write("=" * 45 + "\n")

            file.write(f"Student Number: {student_number}\n")
            file.write(f"Student Name: {student_name}\n")
            file.write(f"Student Age: {age}\n")

            for number, mark in enumerate(marks, start=1):
                file.write(f"Subject {number}: {mark:.2f}%\n")

            file.write(f"Total: {total:.2f}\n")
            file.write(f"Average: {average:.2f}%\n")
            file.write(f"Grade: {grade}\n")

    except FileNotFoundError:
        # Handle a missing results file.
        print("Error: The results file could not be found.")

    except OSError as error:
        print("File error:", error)

    else:
        print("\nResults successfully saved.")

    finally:
        print("File saving process completed.")


def main():
    
print("=" * 45)
    print("    STUDENT RESULTS MANAGEMENT SYSTEM")
    print("=" * 45)

    # Capture student details.
    student_number, student_name, age = get_student_details()

    # Get the number of subjects from the user.
    while True:
        try:
            number_of_subjects = int(input("Enter number of subjects: "))

            if number_of_subjects <= 0:
                raise ValueError(
                    "Number of subjects must be greater than zero."
                )

        except ValueError as error:
            print("Invalid input:", error)

        else:
            break

        finally:
            print("Subject number entry process completed.")

    # Capture the student's marks.
    marks = capture_marks(number_of_subjects)

    # Display the final results.
    display_results(
        student_number,
        student_name,
        age,
        marks
    )

    # Ask whether the user wants to save the results.
    save_choice = input("\nDo you want to save the results? (Y/N): ")

    if save_choice.upper() == "Y":
        save_results(
            student_number,
            student_name,
            age,
            marks
        )
    else:
        print("Results were not saved.")


# Start the program.
if __name__ == "__main__":
    main()