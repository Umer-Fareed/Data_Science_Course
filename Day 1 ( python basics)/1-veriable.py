import numpy as np
import time
import sys
# create python list
l = range(1000)
print(sys.getsizeof(2)*len(l))
#creating numpy array 
array = np.arange(1000)
print(array.size*array.itemsize) 
##############################################
SIZE = 100000
#PHTHON LIST"
L1 = range(SIZE)
L2 = range(SIZE)
start = time.time()
result = [(x*y) for x,y in zip(L1,L2)]
print("python list took: ",(time.time()-start)*1000)
#NUMPY ARRAY 
a1 = np.arange(SIZE)
a2 = np.arange(SIZE)
start = time.time()
result = a1 + a2
print("numpy array took: ", (time.time()-start)*1000)
###################################################
print("the version of numpy is ",np.__version__)
#1D array 
arr = np.array([1,2,3,4,5])
print(arr)
#2D array 
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
arr = np.array([[[1,2,3],[4,5,6]],[[2,4,4],[4,3,2]]])
print(arr)
a = np.array((4,3))
print(a.ndim)

arr = np.array([1,2,3,4],ndmin=5)
print(arr.ndim)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])