# The list stores the marks obtained for three subjects.
marks = [65, 72, 80]

# Start the total at zero before adding each mark.
total = 0

# The loop goes through every mark in the list, one at a time.
for mark in marks:
    # Add the current mark to total, producing the sum of all marks.
    total += mark

# Divide the total by the number of marks to calculate the average.
average = total / len(marks)

# If the average is 50 or more, the student passes; otherwise, the student fails.
if average >= 50:
    print("Pass")
else:
    print("Fail")

# Expected output: Pass, because the average is 72.33, which is above 50.
