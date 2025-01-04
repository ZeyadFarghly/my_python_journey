student_heights = input().split()
sum = 0
len = 0
for student_height in student_heights:
    sum += int(student_height)
    len += 1
print(f"total hieght = {sum}")
print(f"number of students = {len}")
average = float(sum / len)
print(f"averate height = {average}")
