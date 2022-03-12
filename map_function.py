#mup_function.py
"""map() function returns a map object(which is an iterator) of the results
after applying the given function to each item of a given iterable (list, tuple etc.)"""

def addition(n):
    return n + n

lis1 = [1,2,3,4,5]

result = list(map(addition,lis1))

print(result)