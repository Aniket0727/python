import array as ar
from array import *



# a=ar.array('i',{1,2,3})  #i is type of array
# print(id(a))
# print((a))

# data=ar.array('i',[1])
# data2=ar.array('b',[1])
# data3=ar.array('f',[1.5]) 
# data4=ar.array('l',[1])
# data5=ar.array('L',[1000])
# data6=ar.array('h',[1000])
# data7=ar.array('u',['a','b'])

# print(data7)

# print(data.itemsize)

# print(id(a[1]))
# print(id(a[2]))

# arr=ar.array('i',[1,2,3,4,5,1,1])
# print(arr)

# arr.append(6)
# print(arr)
# print(arr.buffer_info())  #it show address and items
# print(id(arr))
# print()

# print(arr.count(1))

# arr.extend([10,20,30])
# print(arr)

ar1=[1,2,3,4,5]
ar2=ar.array('i',[6,7,8,9])

# ar2.fromlist(ar1)
# print(ar2)

# print(ar1.index(5))  #index show the postion of element


# ar1.insert(1,10)  #insert(elemet,postion in array)
# print(ar1)
# print(ar1.pop())   #pop return pop element
# print(ar1)
# print(ar1.remove(1)) #remove return none
# print(ar1)

# print(ar1)
# print(ar1.reverse()) #remove return none
# print(ar1)


# print(ar1)
# ar3=ar2.tolist()  #tolist perform copy without data type of array
# print(ar3)

# print(ar1)
# ar3=ar2
# print(ar3)


for i in ar2[5:1:-2]:   #array clising  for loop show all elements and direct printing array it show array outoff index(when we given index out off array index)
    print(i)

