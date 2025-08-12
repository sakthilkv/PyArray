from PyArray import PyArray as array


mat = array(datatype = array, length = 3)
row1 = array(datatype = int, length = 3)
row2 = array(datatype = int, length = 3)
row3 = array(datatype = int, length = 3)

for i in range(3):
    row1.append(i)

for i in range(3,6):
    row2.append(i)

for i in range(6,9):
    row3.append(i)

mat.append(row1)
mat.append(row2)
mat.append(row3)

print(mat)