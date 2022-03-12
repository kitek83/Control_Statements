#while_for_else.py
"""Checking connection while and for statemts with the else."""

grade = int(input('Enter integer or -1 to finish: '))

while grade != -1:

    for num in range(20):
        print(f'num={num}')

    grade = int(input('Enter integer or -1 to finish'))
else:
    print(f'You entered -1, so program is finished.') # the same I can achieve using only print()

for x in range(20):
    print(x,end='~~')
else:                           #else working however the same result I have with print() only
    print('Loop is finished')

