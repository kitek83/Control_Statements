#compound_interest_after_10_years.py
"""Person invest 1000USD. Calculate and display amount of money in the account
at the end of each year for 10 years. Use the pattern:
a = p(1 + r)**n
p - original amount invested
r - is the annual interest rate
n - number of the years
a - amount of the deposit at the end of the nth year."""

from decimal import Decimal

#data initialization
p = Decimal('1000') #1000 USD
r = Decimal('0.05')

#processing
for n in range(1,11):
    a = p*(1 + r)**n
    print(f'Deposit at the end of {n} year = {a:.5f} USD')  #format specifier .5f
print(3*'------------------------')

print('Using format specifier field width = 2 right aligned > (n:>2) and\n' 
      'and field width = 10 > right aligned (a:>10.2f).')

for n in range(1,11):
    a = p*(1 + r)**n
    print(f'{n:>2}{a:>10.2f}')

print()
#Calculation
print('Result=', end=' ')
print(f"{Decimal('37.45') * Decimal('0.0625'):.2f}")
























