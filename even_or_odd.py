#even_or_odd.py
"""Use for statement to input 2 integers. Use nested if...else statement to
display whether each value is even or odd."""

for counter in range(1,3):
    number = int(input('Enter an integer: '))

    if number % 2 == 0:
        print(f'Number{counter} is even.')
    else:
        print(f'Number{counter} is odd.')

    print()