#Code with errors
student_name = input("Enter student name: ")
mark = input("Enter student mark: ")
#Validate the mark input to ensure it's a number
if mark >= 50
print(student_name, "has passed")
#Else statement to handle the case when the mark is less than 50
else
print(student_name, "has failed")

#Errors fixed
student_name = input("Enter student name: ")
mark = float(input("Enter student mark: "))
if mark >= 50:
    print(student_name, "has passed")
else:
    print(student_name, "has failed")