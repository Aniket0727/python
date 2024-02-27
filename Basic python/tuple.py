# Practical no. 7
# Title program:- Write a python program following operations on Tuples: Create Tuple,
#                 Access Tuple, Update Tuple, Delete Tuple

t1=("Java","Android","HTML","Python","Javascript") #create tuple
t2=(1,5,6,8,3)

print(t1) #access tuple
print(t2[1:4])

l=list(t2)
l[0]=20; #update tuple
t2=tuple(l)
print(t2)

del t2 #delete tuple
# print(t2) NameError
