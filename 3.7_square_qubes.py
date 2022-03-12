#3.7_square_qubes
"""from ex 2.8:
Write a script that calculates square and cubes of the numbers 0-5 in table format using tab escape sequence
3.7.Use for loops and f string capabilities to produce table with number right aligned.
"""

print('number\tsquare\t cube')

for num in range(0,6):
    print(f'\t{num}\t\t{num**2}\t\t{num**3}')

"""
exc.3.7.
Use for loops and f string capabilities to produce table with number right aligned
"""
print()
print('number\tsquare\t cube')

for num in range(0,6):
    print(f'{num:>6.2f}{num**2:>8.2f}{num**3:>7.2f}')

"""
out:
number	square	 cube
  0.00    0.00   0.00
  1.00    1.00   1.00
  2.00    4.00   8.00
  3.00    9.00  27.00
  4.00   16.00  64.00
  5.00   25.00 125.00
"""