import numpy as np 


num1=np.array([[1,2,3],
               [4,5,6]])

#swapaaxes converts row into column and column into row
print(np.swapaxes(num1,0,1))
print()

num2=np.matrix([[1,2],[3,4]])

print(np.linalg.inv(num2))   #inverse
print("pow")
print(np.linalg.matrix_power(num2,2))   #power of multiplication


