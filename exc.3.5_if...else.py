#exc.3.5_if...else.py
"""if...else statement created logic error"""

num1 = int(input('Enteger integer1: '))
num2 = int(input('Enter integer2: '))

if num1 == num2:
    print(f'{num1} is equal to {num2}')
else:
    print(f'{num1} is not equal to {num2}')

if num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num1} is less than {num2}')  #if num1=20 and num2=20, else statement creating logic error

if num1 <= num2:
    print(f'{num1} is less than or equal to {num2}')
else:
    print(f'{num1} is greater then or equal to {num2}')

"""
out:
Enteger integer1: 5
Enter integer2: 5
5 is equal to 5
5 is less than 5   if num1=20 and num2=20, else statement creating logic error
5 is less than or equal to 5
"""