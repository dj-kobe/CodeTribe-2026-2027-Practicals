def get_mark():
    while True:
        try:
            mark = float(input("Enter student mark (0-100): "))

            if not 0 <= mark <= 100:
                raise ValueError

        except ValueError:
            print("Invalid mark. Enter a number between 0 and 100.")
        else:
            return mark


def read_results_file():
    try:
        with open("student_results.txt", "r", encoding="utf-8") as file:
            print("\nSaved results:")
            print(file.read())
    except FileNotFoundError:
        print("The student_results.txt file does not exist yet.")
    finally:
        print("File read operation finished.")


def main():
    student_name = input("Enter student name: ")
    mark = get_mark()

    try:
        result = "passed" if mark >= 50 else "failed"
        print(f"{student_name} has {result} with a mark of {mark:.2f}%.")
    except TypeError:
        # This prevents the program from crashing if mark is not numeric.
        print("The mark could not be processed.")

    read_results_file()


if __name__ == "__main__":
    main()
