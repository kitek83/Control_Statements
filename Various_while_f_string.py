#various_while_f_strring.py
""" Display an f-string in which you insert the values
of the variables number1(7) and number2(5) and their product."""

number1 = 7
number2 = 5

print(f'{number1} times {number2} is {number1 * number2}')
############################################################
#Conditional expresion if...else statement.
print(3*'-----------01------------')
grade1 = 85

if grade1 >= 60:
    result1 = 'Passed'
else:
    result1 = 'Failed'

print(f'Result1 is {result1}.')
#################################################
print(3*'------02------')
print('Using concise conditional expression.')

grade = 34

result = ('Passed' if grade >= 60 else 'Failed')
print(f'Concise result for grade={grade} is {result}')
##############################################
print(3*'-----------03------------')

if 1:
    print('Non zero values are True.')

if 0:
    print('Zero values are false, so it will not be printed.')

print(3*'------------04------------')
######################################
"""Let's use a while statement to find first power 3 larger than 50."""

number = 3

counter = 0
while number <= 50:
    counter += 1
    number *= 3
    print(f'Power_{counter}={number}')

print()
print(number)
print(3*'-------------05-------------')
#########################################
"""Write statement to determine first power of 7 greater than 1000."""
product = 7

count = 0
while product <= 1000:
    count += 1
    product *= 7
    print(f'Power_{count}={product}')

print()
print(f'Final product={product}')

print()
print(3*'---------------06-------------')
###############################################
"""Usin keyword argument sep and end"""
print('sep:')
print(10,20,30,40, sep='~~~~~~~~')
print(10,20,30,40)
print('usind sep and end:')
print(10,20,30,40,50, sep='****', end='-----------') #end='' - concatenating next row
print(50,50,50,50,50, sep='_____')

print(3*'----------07---------------')
#################################################
"""String is a sequence of invidual characters."""

string = 'Programming'
print(f'String = {string}')

for charachter in string:
    print(charachter, end='    ')
print()

print(3*'------------08-------------')




































