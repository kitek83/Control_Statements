#triangle.py
"""Draw below triangles for 'for' statement understanding"""

for x in range(1):
    count = 1
    for y in range(1,11,1):
        print(count*'*')
        count += 1

print('2')
for x in range(1):
    for y in range(10,0,-1):
        print(y*'*')

print('3')
for x in range(1):
    for y in range(10,0,-1):
        print(f"{y*'*':>10}")

print('4')
for x in range(1):
    for y in range(1,11):
        print(f"{y*'*':>10}")

"""
output:
*
**
***
****
*****
******
*******
********
*********
**********
2
**********
*********
********
*******
******
*****
****
***
**
*
3
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
4
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********

"""