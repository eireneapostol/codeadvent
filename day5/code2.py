'''
Now, the jumps are even stranger: after each jump, if the offset was three or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
'''

f = open("./inputs/day5","r")

array = []
for line in f:
    #print(line)
    array.append(int(line))
index = 0
count = 0
while (len(array)>index >= 0):
    jumps = array[index]
    if array[index] > 2 :
        array[index] -= 1
    else:
        array[index] += 1
    index += jumps
    count += 1
print(count)