#itrete over numpy array using nditer
import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
for row in a:
    for cell in row:
      print(cell)
#fletn list into an array 
for cell in a.flatten():
   print(cell)
#nditer function
for x in np.nditer(a,order='c'):#"c" it will go row by row for 
    #colunm by colunm use "f" funcrion instead of "c".
    print(x)  