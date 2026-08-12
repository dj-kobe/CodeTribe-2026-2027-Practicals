subjects = {
    "Programming": 78,
    "Database": 65,
    "Web Development": 72,
}

total_mark = 0
number_of_subjects = 0

for subject, mark in subjects.items():
    print(f"{subject}: {mark}")
    total_mark = total_mark + mark
    number_of_subjects = number_of_subjects + 1

average_mark = total_mark / number_of_subjects

print(f"Total Mark: {total_mark}")
print(f"Number of Subjects: {number_of_subjects}")
print(f"Average Mark: {average_mark:.2f}")
