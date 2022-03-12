#type_decimal.py
"""Using type decimal for Monetary amounts"""

amount = 123.31

print(f'amount={amount}')
print()
print(f'amount with 20 digits of precision\namount = {amount:.20f}')
print(3*'-----------------------------------')
################################################################
#using decimal
from decimal import *

num1 = Decimal('1000.00')
print(f'num1={num1}')
num2 = Decimal(1000.003)
print(f'num2= {num2}')
num3 = Decimal('1000.003')
print(f'num3={num3}')

getcontext().prec = 6 # changin precision to 6
print('Precision=6')
print(f'num1={num1}')

print(Decimal(1)/Decimal(7))
print(f'num2={num2}')
print(Decimal('1000.003'))

print(Decimal(1000.003))
print('Prec=28')

getcontext().prec = 28
print(Decimal(3)/Decimal(5))
calc = Decimal(4) / Decimal(9)
print(f'calc={calc:.28f}')

print('String decimal with f format cpecifier')
print(f'num3={num3:.10f}')

print(getcontext())

num4 = Decimal('3.14')
print(f'num4={num4}')
num5 = Decimal(3.14)
print(f'num5={num5}')















