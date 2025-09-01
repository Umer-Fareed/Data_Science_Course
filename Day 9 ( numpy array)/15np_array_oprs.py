import numpy as np
a = np.array([23,34,23])
a[2]
print(a[2])
a = np.array([[23,43,54],
              [54,65,34],
              [43,54,24],
              [87,56,45]], dtype=float)
print(a)
print(a.min())#to take the minimun element of array
print(a.max())#to take the maximun element of array 
print(a.sum())#to take the sum of an array 
print(a.sum(axis=0))#to take the sum of columns
print(a.sum(axis=1))#to take the sum of rows
print(np.sqrt(a))#to take the sqrt of an array 
print(np.std(a))#to take the standert deviation of an array 

a = a.reshape(3,4)# to reshape your array rows and columns
print(a)
print(a.ndim)#to check the dimension of array 
print(a.itemsize)#to check the memory size of array 
print(a.size)#to check number of element in array
print(a.shape)#to check the shape of array 
b = np.arange(1,5,.2)#to add some difference 
print(b)
c = np.linspace(1,12,10)
print(c)
d = np.array([[1,2],
             [3,4]])
e = np.array([[5,6],
             [7,8]])
f = d + e
print(f)
