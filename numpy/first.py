import numpy as np

a =np.array([[1, 2, 3, 7,],[1,2,3,4],[1,1,1,1]])
print(a)
print(type(a))

zero=np.zeros((2,5))
print(zero)

arr=np.arange(20)
print(arr)

n=np.arange(156666)
print(type(n))

n2=np.arange(10,100,2)
print(n2)

lin=np.linspace(0,10,6)
print(lin)

emp=np.empty((4,2))
print(emp)
print("****")
emp2=np.empty_like((a))
print(emp2)
print()

num=np.random.randint(1,100,10)     
print(num)

arr=np.arange(1,50)
print(arr)
print(arr.shape)

arr=arr.reshape(7,7)
print(arr)


x=[[1,2,3],[4,5,6],[7,8,9]]
print(x)
print(type(x))
arr=np.array(x)
print(arr)
print(type(arr))
print()
arr=arr.T  #T for transpose Row to column and column to row
print(arr)
print()
for items in arr.flat:  # flat is use to iterate all array elements
    print(items)

print()
print("Array Size: ",arr.size)
arr=arr.ravel()
print()
print(arr)

for i in arr:
    print(i)
print()
arr=arr.reshape(3,3)
print(arr.max())
print(arr.min())
print(arr.sum())

print()
print("non zeros: ",np.count_nonzero(arr),'\n')
print("Array size in system: ")


import sys
py_ar=[0,4,55,2]
np_ar=np.array(py_ar)

print(type(py_ar))
print(type(np_ar))

print(sys.getsizeof(1)*len(py_ar)) #one element required 28 bytes
print(np_ar.itemsize*np_ar.size) #one numpy array element required 4 bytes 


n1=np.array([1,2,3,4])
n2=np.array([1,7,8,4])
n3=np.vstack((n1,n2))
n4=np.hstack((n1,n2))

print(n3)
print()

print(n4)

print(np.intersect1d(n1,n2))
print(np.setdiff1d(n1,n2))

print(n1)
print()

n1=n1+1
print(n1)
print(np.mean(n1))
print(np.median(n1))

np.save('annu',n1)
n3=np.load('annu.npy')
print(n3)


print("************")
n1=[45,60]
n2=[55,40]
s=np.sum([n1,n2],axis=1)
print(s)