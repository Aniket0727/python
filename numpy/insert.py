import numpy as np 


n1=np.array([1,2,3,4])

print(np.insert(n1,1,10))
print(np.insert(n1,(2,4),20))

print(np.insert(n1,1,1.5)) #float value not add because array is int (it add only int degits)

print(np.insert(n1,(2),(10,20,30)))

print()
print(np.append(n1,111))

print("Delete")
n2=np.array([1,2,3,4])
del1=np.where(n2==4)   #where return index number of element
print(np.delete(n2,del1))
# print(n1)