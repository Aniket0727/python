# The reshape method returns a new array with a specified shape, without modifying the original array. 
# The resize method changes the shape of the array in place and modifies the original array


import numpy as np

n3=np.array([1,2,3,4,5,6])
print(n3)
print()
print(np.resize(n3,(2,5)))
n4=np.resize(n3,(2,5))


# flatten always returns a copy of the original array data.
# ravel returns a view of the original array whenever possible,
print()
print(n4.flatten(order="F"))  #conver one diamentional array

print(n4.ravel(order="F"))  #conver one diamentional array

# print(np.reshape(n3,(2,5))) #error does not modify original array
