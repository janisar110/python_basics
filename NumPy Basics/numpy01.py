import numpy as np


# # Numpy basics
# a = np.array([1, 2, 3, 4])
# print(a)
# print("Type:", type(a))
# print("Shape:", a.shape)


# # Finding diference b/w array and lists

# import time

# L = list(range(1000000))
# A = np.array(L)

# start = time.time()
# [L[i]**2 for i in range(len(L))]
# print("List time:", time.time() - start)

# start = time.time()
# A**2
# print("NumPy time:", time.time() - start)



# Some usefull methods of NumPy
print(np.zeros((2, 3)))         # 2x3 matrix of 0s
print(np.ones((3, 3)))          # 3x3 matrix of 1s
print(np.arange(0, 12, 2))      # [0 2 4 6 8]
print(np.linspace(0, 1, 5))     # 5 values from 0 to 1
print(np.random.rand(2, 2))     # 2x2 matrix with random values
