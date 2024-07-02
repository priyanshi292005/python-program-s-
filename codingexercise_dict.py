student_marks={
    'Meeta': 93,
    'Shyam': 95,
    'Ram': 53,
    'Seeta': 43,
    'Geeta': 75,
    'Mohan': 81,
    'Harry': 35
}

student_grades={}
for student in student_marks:   #shyam
    marks=student_marks[student]  #95
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student] = "A"
    elif marks>70:
        student_grades[student] = "B+"
    elif marks>60:
        student_grades[student] = "B"
    elif marks>50:
        student_grades[student] = "C"
    elif marks>40:
        student_grades[student] = "D"
    else:
        student_grades[student] = "F"
print(student_grades)