math_score = float(input('Enter Math score'))
physics_score = float(input('Enter Physics score'))
chemistry_score = float(input('Enter Chemistry score'))
student_grade=0
math_grade = ''
chemistry_grade = ''
physics_grade = ''

if math_score < 36:
    math_grade='Failed '
elif math_score <= 59:
    math_grade='Math: C '
    student_grade += math_score
elif math_score <= 69:
    math_grade='Math: B '
    student_grade += math_score
else:
    math_grade='Math: A '
    student_grade += math_score

if physics_score < 36:
    physics_grade=('Failed ')
elif physics_score <= 59:
    physics_grade=('Physics: C ')
    student_grade += physics_score
elif physics_score <= 69:
    physics_grade=('Physics: B ')
    student_grade += physics_score
else:
    physics_grade=('Physics: A ')
    student_grade += physics_score

if chemistry_score < 36:
    chemistry_grade=('Failed ')
elif chemistry_score <= 59:
    chemistry_grade=('Chemistry: C ')
    student_grade += chemistry_score
elif chemistry_score <= 69:
    chemistry_grade=('Chemistry: B ')
    student_grade += chemistry_score
else:
    chemistry_grade=('Chemistry: A ')
    student_grade += chemistry_score

student_grade = student_grade/3

print(math_grade,physics_grade,chemistry_grade)
print('Students final grade is ', student_grade)
