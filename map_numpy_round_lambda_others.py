#map_numpy_round_lambda_others.py
"""Checking list comprehension, map function, function round(), try map func with ndarray, lambda function."""

import numpy as np

print('Checking list compression.')

list1 = [x for x in range(0,31)]
print(f'list1={list1}')

print()
#---------------------------------------------------------
print('Repeat map function with the list comprehension')
print()

def multiply(n):
    return (n * n) + (5 * n) / 3

result1 = list(map(multiply,list1))
print(f'result1={result1}') #result 1 returns a list
print()


print('result1=',result1)
print(f'len(result1)={len(result1)}')

#trying to round all emlements usinf function round()
#of the list (result1) to hundreds. I can't pass string elements.

print('Using round() function: ')
round_to_hundreths = [round(num, 2) for num in result1]

print(f'round_to_hundreths= {round_to_hundreths}')
print()
#-----------------------------------------------------------------------
#try map() func with Numpy ndarray
print('try map() func with Numpy ndarray')

list2 = np.arange(1,101).reshape(5,20)
print(f'list2={list2}')
print()

#result2 = [round(num,2) for num in list(map(multiply,list2))] ---> it is not working

result2 = list(map(multiply, list2))  # I can't reshape result2
print(f'result2={result2}')

#rounded = [round(num,2) for num in result2]   type numpy.ndarray doesn't define __round__ method
print(3*'---------------------------------')
print('Using lambda function:')     #a lambda expression is an anonymous functio--that is function without name

print(f'lambda1 = {(lambda x: (x * 43 + 1) / 56)(22):.4f}')         #function lambda() with format specifier .4f

add_one = lambda x: x + 1  #function assigned to variable
print(f'add_one = {add_one(3):.5f}')
print()

print('using lambda() with a strings')
#using lambda() with a strings

full_name = lambda first, last: f'Full_name={first.title()} {last.title()}'
full_name2 = full_name('krzysztof','van kozak')
print(full_name('krzysztof','van kozak'))
print(f'full_name2: {full_name2}')

print()
result = (lambda x: x**4/456)(5)
print(f'result = {result:.3f}')
print()
result4 = (lambda x, y: x**8 + y/543)(2,3)
print(f'result4 = {result4:.3f}')




































