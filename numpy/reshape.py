import numpy as np


n1=np.array([[1,2,3],[4,5,6]])

print(n1.shape)

print()
n2=np.array([1,2,3],ndmin=4)
print(n2.ndim)
print()
print(n2.shape)


n3=np.array([1,2,3,4,5,6])
print(n3)
n4=n3.reshape(2,3)
print(n4)


n3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(n3)
n4=n3.reshape(3,2,2)
print(n4)
print(n4.reshape(-1))