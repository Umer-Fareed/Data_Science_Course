#indexing and slicing 
import numpy as np
a = np.array([1,2,3,4])
print(a[0:2])
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a[1,2]) #take the element from 1th row and 2nd column            
print(a[0:2,2])
print(a[:,1:3])
for row in a :
  print(row)
#stacking 2 arrays togther 
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print (a)
print (b)
print(np.vstack((a,b)))#to join to arrays in a single array vertically
print(np.hstack((a,b)))#....................................horizontally
c = np.arange(30).reshape(2,15)
print(c)
result = np.hsplit(c,3)#to split the array in three horizontal arrays
result = np.vsplit(c,2)#this is for vertically
print(result[0])
#indexing with boolean arrays
a = np.arange(12).reshape(3,4)
b = a>4
a[b]=-1
print(b)




