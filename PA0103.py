programming_mark = 85
database_mark = 90
web_development_mark = 80

total_mark = programming_mark + database_mark + web_development_mark
average_mark = total_mark / 3
highest_mark = max(programming_mark, database_mark, web_development_mark)
lowest_mark = min(programming_mark, database_mark, web_development_mark)

average_is_pass = average_mark >= 50
all_marks_are_40_or_more = (
    programming_mark >= 40
    and database_mark >= 40
    and web_development_mark >= 40
)
at_least_one_mark_is_75_or_more = (
    programming_mark >= 75
    or database_mark >= 75
    or web_development_mark >= 75
)
no_mark_is_less_than_40 = not (
    programming_mark < 40
    or database_mark < 40
    or web_development_mark < 40
)
programming_equals_85 = programming_mark == 85

print(f"Programming Mark: {programming_mark}")
print(f"Database Mark: {database_mark}")
print(f"Web Development Mark: {web_development_mark}")
print(f"Total Mark: {total_mark}")
print(f"Average Mark: {average_mark:.2f}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")
print(f"Average is greater than or equal to 50: {average_is_pass}")
print(f"All three marks are greater than or equal to 40: {all_marks_are_40_or_more}")
print(f"At least one mark is greater than or equal to 75: {at_least_one_mark_is_75_or_more}")
print(f"No mark is less than 40: {no_mark_is_less_than_40}")
print(f"Programming mark is equal to 85: {programming_equals_85}")
