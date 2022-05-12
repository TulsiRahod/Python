student={"Harry":81,"Ron":78,"Harmione":99,"Draco":74,"Neville":62}

student_grade={}

for x in student:
    if student[x]>90:
        student_grade[x]="Outstanding"
    elif student[x]>80:
        student_grade[x]="Exceed Expactations"
    elif student[x]>70:
        student_grade[x]="Acceptable"
    else:
        student_grade[x]="Fail"

print(student_grade)