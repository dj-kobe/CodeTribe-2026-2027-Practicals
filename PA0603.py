import os
from datetime import datetime
import math


RESULTS_FILE = "student_results.txt"
RECORDS_FOLDER = "student_records"


def get_result_value(label):
    with open(RESULTS_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in reversed(lines):
        if line.startswith(label):
            return float(line.split(":", 1)[1].strip().rstrip("%"))

    raise ValueError(f"{label.rstrip(':')} was not found in {RESULTS_FILE}.")


def main():
    # Operating-system operations
    print("OPERATING-SYSTEM OPERATIONS")
    print(f"{RESULTS_FILE} exists: {os.path.exists(RESULTS_FILE)}")
    print(f"Current working directory: {os.getcwd()}")

    if not os.path.exists(RECORDS_FOLDER):
        os.mkdir(RECORDS_FOLDER)
        print(f"Created folder: {RECORDS_FOLDER}")
    else:
        print(f"Folder already exists: {RECORDS_FOLDER}")

    # Date operations
    current_date_time = datetime.now()
    results_created_date = current_date_time

    print("\nDATE OPERATIONS")
    print(f"Current date and time: {current_date_time}")
    print(f"Student results created on: {results_created_date.strftime('%d %B %Y')}")

    # Mathematical operations
    average_mark = get_result_value("Average:")
    total_mark = get_result_value("Total:")

    print("\nMATHEMATICAL OPERATIONS")
    print(f"Average rounded up: {math.ceil(average_mark)}")
    print(f"Average rounded down: {math.floor(average_mark)}")
    print(f"Square root of total mark: {math.sqrt(total_mark):.2f}")


if __name__ == "_main_":
    main()
