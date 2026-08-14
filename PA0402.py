
def calculate_average(mark1, mark2, mark3):
    # Add all three marks together before calculating the average.
    total = mark1 + mark2 + mark3

    # Divide by the number of marks entered.
    return total / 3


def display_result(student_name, average):
    # A student is competent when their average is at least 50 percent.
    result = "Competent" if average >= 50 else "Not Yet Competent"

    print(f"Student: {student_name}")
    print(f"Average: {average:.2f}%")
    print(f"Result: {result}")


# Sample marks used to demonstrate the documented functions.
programming_mark = 78
database_mark = 65
web_development_mark = 72

average_mark = calculate_average(
    programming_mark, database_mark, web_development_mark
)
display_result("Thabo Molefe", average_mark)
