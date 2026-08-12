student_number = 20263135
student_name = "Tshepo"
student_surname = "Louw"
student_age = 24
course_name = "Computer Science"
status = "full time"
programming_mark = 85
database_mark = 90
web_development_mark = 80
registration_fee = 1500.00

print(f'{student_name} {student_surname} ({student_number}) is a {status} student enrolled in the {course_name} program. At the age of {student_age}, they have achieved the following marks: Programming - {programming_mark}, Database - {database_mark}, Web Development - {web_development_mark}. The registration fee for the course is R{registration_fee:.2f}.')

#Display the data type of each variable
print(f'Data type of student_number: {type(student_number)}')
print(f'Data type of student_name: {type(student_name)}')
print(f'Data type of student_surname: {type(student_surname)}')
print(f'Data type of student_age: {type(student_age)}')
print(f'Data type of course_name: {type(course_name)}')
print(f'Data type of status: {type(status)}')
print(f'Data type of programming_mark: {type(programming_mark)}')
print(f'Data type of database_mark: {type(database_mark)}')
print(f'Data type of web_development_mark: {type(web_development_mark)}')
print(f'Data type of registration_fee: {type(registration_fee)}')

#Convert one string to integer
student_number = int(student_number)
#One interger value to a float
student_age = float(student_age)
#one number to a string
course_name = str(course_name)