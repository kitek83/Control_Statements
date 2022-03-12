#exc3.13_factorials
"""Write a script, that inputs non negative integer and computes and display its factorial.
1.Iteretive factorial approach with for statement with the use of locale module for large factorials.
2.Implementing recursive Factorial function with the for statement."""

#You canr calculate integer! iteratively with a for statement, as in:
import locale   # for large numbers

integer = int(input('Enter the integer: '))
factorial = 1

for number in range(integer,0,-1):

    print(f'factorial={number}*{factorial}={factorial*number}')
    factorial *= number


print()
locale.setlocale(locale.LC_ALL, 'en_US')  #printing number with commas as thosands separators
print(f'{integer}! = {locale.format_string("%d",factorial,grouping=True)}')
print(3*'-----------------------------------')

#Implementing recursive Factorial function.
def factorial(number):

    if number <= 1:
        return 1

    return number * factorial(number -1)

for num in range(integer+1):
    print(f'{num}! = {locale.format_string("%d",factorial(num),grouping=True)}')

"""
out:
Enter the integer: 5
factorial=5*1=5
factorial=4*5=20
factorial=3*20=60
factorial=2*60=120
factorial=1*120=120

5! = 120
---------------------------------------------------------------------------------------------------------
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120

"""



























