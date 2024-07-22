import numpy as np


n1=np.array([1,2,3,4])
print(n1.dtype)


n2=np.array(['a','s'])
print(n2.dtype)
print()

n3=np.array([1,2],dtype=np.float64)
print(n3.dtype)
print(n3)
print()

n4=np.array(['a','b',1.2,2.3])
print(n4.dtype)