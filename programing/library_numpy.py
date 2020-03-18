import numpy as np
import time
import sys

# # Python program for
# # Creation of Arrays
#
# # Creating a rank 1 array from list
# arr = np.array([1, 2, 3])
# print("Array with Rank 1: \n", arr)
#
# # Creating a rank 2 array from list of list
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print("Array with Rank 2: \n", arr)
#
# # Creating a rank 1 array from tuple
# arr = np.array((1, 3, 2))
# print("\nArray created using passed tuple:\n", arr)
#
# # Creating a rank 2 array from list of list
# arr = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]])
# print("Initial Array: \n", arr)
#
# # slicing
# sliced_arr = arr[:2]
# print("\nsliced array: \n", sliced_arr)
#
# # Printing elements at
# # specific Indices
# Index_arr = arr[[1, 1, 0, 3], [3, 2, 1, 0]]
# print("\nElements at indices (1, 3), (1, 2), (0, 1), (3, 0):\n", Index_arr)
#
#
# # Basic Array Operations
#
# a = np.array([[1, 2], [3, 4]])
#
# b = np.array([[5, 6], [7, 8]])
#
# print(a + 1)
# print(b - 2)
#
# print(a.sum())
#
# print(a + b)
#
# arr = np.array([[1, 2, 3], [4, 2, 5]])
# print("array type: ", type(arr), "\n array dimension: ", arr.ndim, "\narray shape: ", arr.shape,\
# "\narray size: ", arr.size)
#
# np.zeros(4)


import numpy as np

# print(np.__version__)
# np.show_config()
# data = np.zeros(10)
# data[4] = 1
# print(data)

# print(np.array(range(10, 50)))
# arr = np.array(range(10, 50))
# print(arr[::-1])  # reverse
# print(arr[:-1])  # exclude last element
# print(arr[-1:])  # only last element
# print(arr[-1::])  # only last element

# arr = np.array(range(9)).reshape(3, 3)
# print(arr)

# 9. find the indices of non zero elements
# arr_tuple = np.array((2, 3, 0, 9, 0, 0, 2, 7))
# arr_list = np.array((0, 3, 0, 9, 0, 8, 0, 7))
# print(np.nonzero(arr_tuple))
# print(np.nonzero(arr_list))

# 10. creating 3 x 3 identity matrix
# z = np.eye(3)
# print(z)

# 11. creating
# z = np.random.rand(3, 3, 3,)
# print(z)

# 12.
# z = np.random.randn(10, 10)
# zmin, zmax = z.min(), z.max()
# print(zmin, zmax)

# 13. create
# z = np.random.randn(30)
# zmean = z.mean()
# print(zmean)

# arr1 = np.array([[1, 4, 6, 5], [5, 6, 7, 8]])
# print(arr1)
# arr2 = np.array(((2, 4, 4, 5), (4, 6, 7, 7)))
# print(arr2)
# arr3 = np.array((3, 5, 7, 7))
# arr4 = np.array([9, 7, 8, 5])
# arr5 = np.array(((7, 6, 7, 4), [4, 5, 7, 8]))
# arr5 = np.array([(7, 6, 7, 4), [4, 5, 7, 8]])
# print(arr3)
# print(arr4)
# print(arr5)

# ran = range(1000)
# print(sys.getsizeof(5) * len(ran))
#
# data = np.array(range)
# print(data.size * data.itemsize)

import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,3*np.pi,0.1)
y=np.tan(x)
plt.plot(x,y)
plt.show()