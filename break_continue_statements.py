#break_continue_statements.py
"""Using break and continue statements."""

#using break statement
for num in range(100):
    print(num)

    if num == 10:
        break
#or the same but different sequence of nested if..statement
print()

for num in range(100):

    if num == 10:
        break

    print(num)

print()
####################################################################
#simple using of continue statement

for num in range(10):

    if num == 5:          #5 will not be printed out
        continue

    print(num, end=' ')