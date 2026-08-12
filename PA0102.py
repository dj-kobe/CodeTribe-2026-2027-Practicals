student_number = 20263135
student_name = "Tshepo"
student_surname = "Louw"
student_age = 24
course_name = "Computer Science"
status = "full time"
programming_mark = "85"
database_mark = "90"
web_development_mark = "80"
registration_fee = 1500.0

full_name = student_name + " " + student_surname
course_name_upper = course_name.upper()
full_name_length = len(full_name)
rounded_registration_fee = round(registration_fee, 2)

programming_mark = float(programming_mark)
database_mark = float(database_mark)
web_development_mark = float(web_development_mark)

print(f"Student Number: {student_number}")
print(f"Full Name: {full_name}")
print(f"Course Name: {course_name_upper}")
print(f"Status: {status}")
print(f"Age: {student_age}")
print(f"Full Name Characters: {full_name_length}")
print(f"Programming Mark: {programming_mark}")
print(f"Database Mark: {database_mark}")
print(f"Web Development Mark: {web_development_mark}")
print(f"Registration Fee: R{rounded_registration_fee:.2f}")
