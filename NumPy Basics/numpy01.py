import numpy as np
import time


# # Numpy basics
# a = np.array([1, 2, 3, 4])
# print(a)
# print("Type:", type(a))
# print("Shape:", a.shape) #this method describe a lenght of array and dimention
# print("lenght:", len(a))




# # Finding diference b/w array and lists

# L = list(range(10000000))
# A = np.array(L)


# start = time.time()
# [L[item]**2 for item in range(len(L))]
# print("List time:", time.time() - start)


# start = time.time()
# print(A**2)
# print("NumPy time:", time.time() - start)



# # Some usefull methods of NumPy
# print(np.zeros((2, 3)))         # 2x3 matrix of 0s
# print(np.ones((3, 3)))          # 3x3 matrix of 1s
# print(np.arange(0, 10, 2))      # [0 2 4 6 8]
# print(np.linspace(0, 1, 5))     # 5 values from 0 to 1
# print(np.random.rand(2, 2))     # 2x2 matrix with random values




# # NumPy Array operations
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# print("Add:", a + b)
# print("Multiply:", a * b)
# print("Mean:", np.mean(a))
# print("Dot Product:", np.dot(a, b))



# # # reshape and flatten
# arr = np.array([[1, 2, 3],[4, 5, 6]])
# # reshaped = arr.reshape((3, 2))
# # print("Reshaped:\n", reshaped)

# flat = arr.flatten()
# print("Flattened:", flat)

# # where method returns index of elements
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4) 
# print(x)


# # Sorting from an array
# arr = np.array([3, 2, 0, 1])

# # assending
# print(np.sort(arr))
# # descending
# print(np.sort(arr)[::-1])


# # array filter
# arr = np.array([41, 44, 43, 44])

# value = int(input("find out number: "))
# # Create an empty list
# filter_arr = []

# # go through each element in arr
# for element in arr:
#   # if the element is higher than 42, set the value to True, otherwise False:
#   if element == value:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)

# newarr = arr[filter_arr]
# print(newarr)
# print(filter_arr)


# filter directly
arr = np.array([41, 42, 43, 44])

filter_arr = arr == 41

newarr = arr[filter_arr]

print(newarr)

[[1,2,3,4,5], 
 [6,7,8,9,10]]

