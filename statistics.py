#statistics.py
"""Using statistics module with functions mean. median,mode
mean - average of values, median-the middle value, mode-most frequent value"""

import statistics

grades = [85, 93, 45, 89, 85]

#calulating mean - average with built in sum and len methods
sum1 = sum(grades)
print(f'grades={grades}')
print(f'sum of grades={sum1}')

mean1 = sum(grades) / len(grades)
print(f'mean={mean1}')

mean2 = statistics.mean(grades)
print(f'mean2={mean2}')

