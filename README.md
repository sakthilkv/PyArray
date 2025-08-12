# PyArray

A very concise and properly implemented implementation of an array in Python. It is blazingly fast (it’s not) and 20 times faster than NumPy’s array (made that up for dramatic purposes).

## Usage Example

```python
from PyArray import PyArray as array

# Create a 3x3 matrix as an array of arrays
mat = array(datatype=array, length=3)

# Create 3 rows with integers
row1 = array(datatype=int, length=3)
row2 = array(datatype=int, length=3)
row3 = array(datatype=int, length=3)

# Append values to each row
for i in range(3):
    row1.append(i)

for i in range(3, 6):
    row2.append(i)

for i in range(6, 9):
    row3.append(i)

# Append rows to the matrix
mat.append(row1)
mat.append(row2)
mat.append(row3)

print(mat)
```

## Output

```python
[[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```
