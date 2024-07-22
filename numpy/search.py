import numpy as np

n1=np.array([1,2,3,4,5,6,2,1,4,5])


n2=np.where(n1==2)
print(np.searchsorted(n1,3,side="right"))  #add element in array
n3=np.searchsorted(n1,[4,5,6,7],side="left")  #add element in array
print(n3)
for i in np.nditer(n2):
    print(i)
print()

n4=np.array([[3,2],[2,1],[0,1]])
print(np.sort(n4))