students_score = {
    "Harry": 81,
    "Ron": 78,
    "hermonica": 99,
    "Draco": 74,
    "Neville": 62
}

students_grade = {}

for key in students_score:
    if students_score[key] >= 91:
        students_grade[key] = "Outstanding"
    elif students_score[key] >=81:
        students_grade[key] = "Exceed Expectations"
    elif students_score[key] >= 71:
        students_grade[key] = "Acceptable"
    else:
        students_grade[key] = "Fail"

print(students_grade)
