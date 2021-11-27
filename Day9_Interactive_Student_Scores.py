student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

# Usung Dictionary.items()
# for k, v in student_scores.items():
#     if v >= 91:
#         student_grades[k] = "Outstanding"
#     elif v >= 81:
#         student_grades[k] = "Exceeds Expectations"
#     elif v >= 71:
#         student_grades[k] = "Acceptable"
#     else:
#         student_grades[k] = "Fail"

# Using what we know so far in class
for k in student_scores:
    if student_scores[k] >= 91:
        student_grades[k] = "Outstanding"
    elif student_scores[k] >= 81:
        student_grades[k] = "Exceeds Expectations"
    elif student_scores[k] >= 71:
        student_grades[k] = "Acceptable"
    else:
        student_grades[k] = "Fail"


print(student_grades)
