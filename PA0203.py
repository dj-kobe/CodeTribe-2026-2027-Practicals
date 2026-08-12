def get_performance_level(average_mark):
    if average_mark >= 75 and average_mark <= 100:
        return "Distinction"
    elif average_mark >= 60 and average_mark <= 74:
        return "Competent"
    elif average_mark >= 50 and average_mark <= 59:
        return "Pass"
    elif average_mark >= 0 and average_mark <= 49:
        return "Not Yet Competent"
    else:
        return "Invalid mark"


passing_average = 56
failing_average = 42

passing_result = get_performance_level(passing_average)
failing_result = get_performance_level(failing_average)

print(f"Average Mark: {passing_average}")
print(f"Performance Level: {passing_result}")

print(f"Average Mark: {failing_average}")
print(f"Performance Level: {failing_result}")
