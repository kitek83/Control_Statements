#Sentinel_controlled-iteration.py
"""Class average program with sentinel-controlles iteration."""

#initializasion phase
total = 0
grade_counter =0

#processing phase
grade = float(input('Enter the grade or -1 to finish: '))

while grade != -1:
    total += grade
    grade_counter += 1
    grade = float(input('Enter the grade or -1 to finish: '))

#termination phase
if grade_counter != 0:
    average = total / grade_counter
    print()
    print(f'Average = {average:.2f}') #:-it is replacement-text expression. .2f - format specifier - format the average with 2 digits to the right.
else:
    print('No grades were entered.')

