total = 0

for number in range(1, 6):
    total = total + number

print(f"Total for range(1, 6): {total}")

# 1. The loop will execute 5 times.
# 2. The numbers that will be added are 1, 2, 3, 4, and 5.
# 3. The final output will be 15.
# 4. If range(1, 6) is changed to range(1, 10), the numbers 1 to 9 will be added,
#    and the final output will be 45.

total = 0

for number in range(1, 10):
    total = total + number

print(f"Total for range(1, 10): {total}")
