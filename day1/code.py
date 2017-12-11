import os
f = open("./inputs/day1","r") 
suma=0
for line in f:
    for n in range(len(line)-1):
        if (line[n]==line[n+1]):
            suma+=int(line[n])
if (line[0] == line[len(line)-1]):
    suma+=int(line[0])
print(suma)
