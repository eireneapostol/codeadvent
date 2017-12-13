'''
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 277678.
'''

import os
import math
f = open("./inputs/day3-test","r")
f = f.read()
number = int(f)
print(number)
squareroot = int(math.ceil(math.sqrt(int(f))))
square = int(math.pow(squareroot,2))
#a = [[0] * (squareroot)] * (squareroot) #multiplica acelasi rand al matricii
a = [[0] * squareroot for i in range(squareroot)]
rows = squareroot
cols = squareroot
n = square

jos = 0
sus = 0
stanga = 0
dreapta = 0

#functions for each direction
def jos_centru(n, jos, stanga, dreapta):
    for j in reversed(range(stanga, squareroot - dreapta)):
        i = squareroot - jos - 1
        a[i][j] = n
        n -= 1
    return n

def stanga_centru(n, sus, stanga, jos):
    for i in reversed(range(sus, squareroot-jos)):
        j = stanga
        a[i][j] = n
        n -= 1
    return n

def sus_centru(n, sus, stanga, dreapta):
    for j in range(stanga, squareroot - dreapta):
        i = sus
        a[i][j] = n
        n -= 1
    return n

def dreapta_centru(n, sus, jos, dreapta):
    for i in range(sus, squareroot - jos):
        j = squareroot - dreapta - 1
        a[i][j] = n
        n -= 1
    return n

#fill the matrix

while n > 0:
    if squareroot % 2 == 0:
        #sus
        n = sus_centru(n, sus, stanga, dreapta) 
        sus += 1
        #dreapta
        n = dreapta_centru(n, sus, jos, dreapta)
        dreapta += 1
        #jos
        n = jos_centru(n,jos, stanga, dreapta)
        jos += 1
        #stanga
        n = stanga_centru(n, sus, stanga, jos)
        stanga += 1
    
    else:
        #jos
        n = jos_centru(n,jos, stanga, dreapta)
        jos += 1
        #stanga
        n = stanga_centru(n, sus, stanga, jos)
        stanga += 1
        #sus
        n = sus_centru(n, sus, stanga, dreapta) 
        sus += 1 
        #dreapta
        n = dreapta_centru(n, sus, jos, dreapta)
        dreapta += 1
#print spiral matrix
#for row in a:
#    print(' '.join(['{0:3s}'.format(str(elem)) for elem in row]))

i = 0
j = 0
i_poz = 0
j_poz = 0
ii = 0
jj = 0
while i < squareroot:
    if a[i][j] == number:
        i_poz = i
        j_poz = j
    if a[i][j] == 1:
        ii = i
        jj = j
    if j == (squareroot - 1):
        j = 0
        i += 1
    else:
        j += 1
print("Position of number 1:\n",ii,jj)
#print number of steps from input to number 1
print("Number of steps:\n",abs(ii-i_poz)+abs(jj-j_poz))

## PART TWO ##
'''
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

Your puzzle input is still 277678.
'''

def neighbours(i,j):
    suma = 0

    if i > 0:
        suma += b[i-1][j]
        if j > 0:
            suma += b[i-1][j-1]
        if j < (squareroot - 1):
            suma += b[i-1][j+1]

    if i < (squareroot - 1):
        suma += b[i+1][j]
        if j > 0:
            suma += b[i+1][j-1]
        if j < (squareroot - 1):
            suma += b[i+1][j+1]
    if j > 0:
        suma += b[i][j-1]
    if j < (squareroot - 1):
        suma += b[i][j+1]
    return suma

b = [[0] * squareroot for i in range(squareroot)]
b[ii][jj] = 1

#in matrix B we take the numbers in spiral mode, so we can simply search the values in matrix A and find the position
z = 2
suma = 0
while suma < number:
    for i in range(squareroot):
        for j in range(squareroot):
            if a[i][j] == z:
                ii = i
                jj = j
    suma = neighbours(ii,jj)
    b[ii][jj] = suma
    #print matrix for each new sum
    for row in b:
        print(' '.join(['{0:3s}'.format(str(elem)) for elem in row]))
    print()
    
    z += 1 #value to search for in matrix A

print("Highest first neighbour:\n",suma)