average = 68

if average >= 75:
    result = "Distinction"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"

print(result)

# 1. The output displayed will be Pass.
# 2. Pass will be displayed because 68 is less than 75, but it is greater than or equal to 50.
# 3. If the average is changed to 48, the output will be Fail.
# 4. If the average is changed to 80, the output will be Distinction.
