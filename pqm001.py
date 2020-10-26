import os
import sys

f = open(os.path.join(sys.path[0], "matrix.txt"), "r")

data = []

for x in f:
    if len(x) > 1:
        for i in x.strip().split(" "):
            data.append(int(i))
    # else:
    #     data.append(" ")
print(data)

lis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


for a in range(0, len(data)):
    if a < 16:
        if data[a] < 16:

            print("01000" + hex(a)[2:].upper() + "000" + hex(data[a])[2:].upper())
        
        else:
            print("01000" + hex(a)[2:].upper() + "00" + hex(data[a])[2:].upper())
    
    else:
        if data[a] < 16:

            print("0100" + hex(a)[2:].upper() + "000" + hex(data[a])[2:].upper())
        
        else:
            print("0100" + hex(a)[2:].upper() + "00" + hex(data[a])[2:].upper())

