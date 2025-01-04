student_scores = input().split()
highest = 0
for student_score in student_scores:
    if highest < int(student_score):
        highest = int(student_score)
print(highest)