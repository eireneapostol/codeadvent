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

squareroot = int(math.ceil(math.sqrt(int(f))))
square = int(math.pow(squareroot,2))
#a = [[0] * (squareroot)] * (squareroot)
a = [[0] * squareroot for i in range(squareroot)]
rows = squareroot
cols = squareroot
n = square

#seteaza marginile:

#jos
i = squareroot-1
for j in reversed(range(squareroot)):
    a[i][j] = n
    n -= 1

#stanga
j = 0
for i in reversed(range(squareroot-1)):
    a[i][j] = n
    n -= 1

#sus
i = 0
for j in range(1,squareroot):
    a[i][j] = n
    n -= 1

#dreapta
j = squareroot-1
for i in range(1, squareroot - 1):
    a[i][j] = n
    n -= 1

for row in a:
    print(' '.join([str(elem) for elem in row]))
'''
while n > 0:
    for i in reversed(range(rows)):
        a[i][j] = n
        n -= 1
        '''





