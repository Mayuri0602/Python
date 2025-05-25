# Create an array using numpy.

import numpy as np
a = [1,11,21,31,41]
b = np.array(a)
print(b)


# Create an array of 10 random integers.

import numpy as np
arr = np.random.randint(1,50,10)
print(arr)


# Create an array of elements from 10-20.

import numpy as np
arr = np.arange(10,21)
print(arr)


# Create an array which contains value 5, 10 times.

import numpy as np
arr = np.repeat(5, 10)
print(arr)

# Create a 1-D array and convert that into 3*3 matrix.

import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
matrix = a.reshape(3,3)
print(matrix)


# Create a 2-D array of size 3*3 but all the elements should be between 0 to 1.

import numpy as np
arr = np.random.rand(3,3)
print(arr)


# Concatenate 2-D array horizontally and vertically.

import numpy as np
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
horizontal = np.hstack((arr1, arr2))
vertical = np.vstack((arr1, arr2))
print("Horizontal concatenation:\n",horizontal)
print("Vertical concatenation:\n",vertical)