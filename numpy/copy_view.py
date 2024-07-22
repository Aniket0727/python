# Copy: The data is independent. Modifying the copied array does not affect the original array.
# View: The data is shared. Modifying the view affects the original array and vice versa.

import numpy as np


n1 =np.array( [1, 2,3, 4])
n2=n1.view()  #shallow copy
n1[0]=10
print(n1)
print(n2)
print()

n3 =np.array( [1, 2,3, 4])
n4=n3.copy()  #deepcopy
n3[0]=10
print(n3)
print(n4)
 
