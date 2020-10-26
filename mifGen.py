import os, sys

# reading matrix data
f = open(os.path.join(sys.path[0], "matrix.txt"), "r")
data = []
for x in f:
    if len(x) > 1:
        for i in x.strip().split(" "):
            data.append(int(i))
f.close()
print(data)

# generating the mif code
WIDTH=16
DEPTH=256
ADDRESS_RADIX="HEX"
DATA_RADIX="BIN"

mif_data=[]

mif_data.append("WIDTH=16;")
mif_data.append("DEPTH=256;")
#mif_data.append("")
mif_data.append("ADDRESS_RADIX=HEX;")
mif_data.append("DATA_RADIX=BIN;")
#mif_data.append("")
mif_data.append("CONTENT BEGIN")
for each in range(0, len(data)):
    addr = "    " + (3 - len(hex(each)[2:].upper())) * '0' + hex(each)[2:].upper()
    dat =  ((16 - len(bin(data[each])[2:])) * '0') + bin(data[each])[2:] + ';'
    mif_data.append(addr + "  :  " + dat)
mif_data.append("   " + "[" + (3 - len(hex(len(data))[2:].upper())) * '0' + (hex(len(data))[2:].upper()) + ".." + (3 - len(hex(DEPTH-1)[2:].upper())) * '0' + hex(DEPTH-1)[2:].upper() + "]" + " : "  + (16 * '0') + ';')
mif_data.append("END;")

# creating .mif as .txt
fileData = open("data.txt","w")
for each in mif_data:
    print(each)
    fileData.write(each)
    fileData.write('\n')
fileData.close()

# converting to mif file
dataIn = 'data.txt'
base = os.path.splitext(dataIn)[0]
os.rename(dataIn, base + '.mif')


