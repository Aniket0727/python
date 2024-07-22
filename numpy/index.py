import numpy as np

n1=np.array([[1,2,3],[4,5,6],[7,8,9]])

print(n1[2,1:])
print(n1[0][1])

n2=np.array([1,2,3,4,5])
print(n2[::2])
for i in (n1):
    for j in (i):
        print(j)
        
for i in np.nditer(n1,flags=['buffered'],op_dtypes=['float64']):
    print(i)
    
for i,j in np.ndenumerate(n1):
    print(i,j)