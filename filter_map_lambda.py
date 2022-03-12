#filter_map_lambda
"""Using functions filter, map,Pandas Series,
lambda versus combination with list comprehension"""
import pandas as pd

#using filter higher order function
numbers = [10,3,7,1,9,4,2,8,5,6]

def is_odd(x):
    #return True if x  odd
    return x % 2 != 0

filtered = list(filter(is_odd, numbers)) #fiter return iterator (lazy function) so I must iterate through it using function list()
print(f'filtered={filtered}') #filter function returne odd values from vollection
print()

#using higher order map function
mapped = list(map(is_odd, numbers))  #map function return boolean values for the conditional statement !=
print(f'mapped={mapped}')
print()

#we can print number of indexes, values and boolean value for the values in the list usin statement for looping with
#the range and len functions
print(f'numbers={numbers}')

print('index\tvalue\tis_odd')

for x in range(len(numbers)):
    print(f'{x:>5}\t{numbers[x]:>5}\t\t{mapped[x]}')                    #usuing marks >right aligned, format specifier:# field width, format specifier .f

print()
print(3*'-----------------------')

#using Pandas Series to get similar table to above one
print('Using pd.Series')
print('index\tvalue\tis_odd')
mapped_Series = pd.Series(mapped,[x for x in range(len(mapped))])  #mapped from above + using list comprehensive
print(mapped_Series)                                               #unfortunately  I coulden't adjust spacing properly with f string method


####################################################################################################
print(3*'---------------------------')
#using functions filter and mao for simple arithmetic operarion

def add_ones(x):
    return x + 1

filtered2 = list(filter(add_ones, numbers)) #for filter function must take one argument and must return a True, so this function is not working with filter method, which returned unchanged numbers
                                            #in this way function (filter) add_ones doesn't return true so it's not working
mapped2 = list(map(add_ones, numbers))      #map function working with add_ones function and does not need to get the True from add_ones() func

print(f'filtered2={filtered2}')
print(f'mapped2={mapped2}')
######################################################################################################
#using filter() func and map() func for condition for even numbers

def is_even(x):
    return x % 2 == 0

print(f'numbers={numbers}')

filtered3 = list(filter(is_even, numbers))
mapped3 = list(map(is_even, numbers))

print()
print(f'filtered3={filtered3}')
print(f'mapped3={mapped3}')
########################################################################################################
#using filter with lambda functions.
#for simple functions like is_odd() thet return single expression's value(True/False),
# you cam use a lambda expression or simple lambda
#filter works with expressions(functions), which returns True

print()
filtered4 = list(filter((lambda x: x % 2 != 0), numbers)) #using lambda function
print(f'filtered4-->is_odd={filtered4}')

print()

#the sane result you can achieve using list comprehension
filtered5 = [item for item in numbers if is_odd(item)]
print(f'filtered5-->list_cmopr={filtered5}')
print()
#########################################################################################################
#using map() function with lambda expression
#map() returns value with arithmetic ops and return boolean value with functions, which returns True/False

print(f'numbers={numbers}')
mapped4 = list(map((lambda x: x**2), numbers))
print(f'mapped4-->squared={mapped4}')
print()

#the same using list comprehension
squared = [item**2 for item in numbers]
print(f'list_compr-->squared={squared}')
print()
#############################################################################################################
#Combining map and filter versus list comprehension
combined1 = list(map((lambda x: x**2), filter(is_odd, numbers)))  #1st solution
print(f'combined1={combined1}')

combined2 = list(map((lambda x: x**2), filter((lambda x: x % 2 != 0), numbers))) #2nd solution
print(f'combined2={combined2}')

combined3 = [item**2 for item in numbers if item % 2 != 0] #list comprehension
print(f'combined3={combined3}')






























