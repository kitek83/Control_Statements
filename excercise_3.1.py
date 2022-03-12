#excercise_3.1.py
"""Write a program to summarise result. You have been given a list of 10 students
Next to each name is wwritten a 1 if the student passed exam and 2 if student failed
Count the number of results each type. Display summary of the result passed and failed.
If passed student >= 8, bonus for teacher. If the value entered is other than 1 or 2,
keep looping untile the user enter correct value: 1 or 2."""

#intializing the veriables, which work like counter
passed = 0
failed = 0

#processing
for student in range(1,11):
    grade = int(input(f'Student{student} enter the result from the exam (1=passed, 2=failed): '))

    while grade != 1 and grade != 2:            #nested while loop is working with boolean operator and, when using  opearator or, the seconf condition also was working, so it coused infinite loop
        grade = int(input(f'Student{student} enter the result from the exam (1=passed, 2=failed): '))

    if grade == 1:
        passed += 1 #using augmented assignmend
    else:
        failed += 1

#termination
print(f'passed={passed}')
print(f'failed={failed}')

if passed >= 8:
    print('Bonus for the teacher.')
