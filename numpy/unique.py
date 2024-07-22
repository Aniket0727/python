import numpy as np


n1=np.array([1,2,3,2,1,5,6])

n2=np.unique(n1,return_index=True,return_counts=True) 
print(n2)