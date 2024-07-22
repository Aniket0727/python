import numpy as np


n1 =np.array([[1,2,3],[4,5,6]])
n2 =np.array([[10,20,30],[40,50,60,]])

n3=np.concatenate((n1,n2))
n3=np.stack((n1,n2))

print(n3)

