#function_range_deeper_look.py
"""Use for and range to sum the even integers from 2 through 100."""
print('Solution nr1:')

total = 0 #initializing total
count = 0

for integer in range(2,101,2): #processing
    count += 1
    total += integer
    print(f'Total{count} for integer={integer} = {total}')


#termination and display
print()
print(f'Sum of even integers = {total}')
print(3*'-----------------------------------')
########################################################
print('Solution nr2 with nested if statement.')

total = 0
count = 0

for integer in range(2,101):

    if integer % 2 == 0:
        count += 1
        total += integer
        print(f'Total{count} for integer={integer} = {total}')

print()
print(f'Sum of even integers = {total}')
