#nested_controlled_statement.py
"""Using nested controlled statement to analyze examination results."""

#intialization phase - initialize variables
passed = 0 #number of passes
failed = 0 #number of failed

#process 10 students
for student in range(1,11):
    #get one exam result
    result = int(input(f'Student nr{student} enter 1 if passed exam or 2 if failed: '))

    if result == 1:  #nested if...else controlled statement
        passed += 1
    else:
        failed += 1

#termination phase
print()
print(f'Nr passed students = {passed}')
print(f'Nr failed students = {failed}')
print()

if passed >= 8:
    print(f'Passed={passed} so bonus for the teacher.')

