import numpy as np


n1=np.array([1,2,3])
n2=np.array([4,5,6])
print(n1+n2)
print(n1)
n1=n1+2
print(n1)
print()
n3=np.array([1,2,3])
print()
print(np.min(n3),np.argmin(n3))
print(np.max(n3),np.argmax(n3))

print()
n4=np.array([[1,2,3,4],
             [5,6,7,8]])
print(np.min(n4,axis=1))
print()
print(np.sqrt(n4))
print(np.cumsum(n4))
