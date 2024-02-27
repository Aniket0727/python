# Prcatical No. 8
# Q.2 Write a Python program to perform following operations on set: intersection of
#     sets, union of sets, set difference, symmetric difference, clear a set.
set1 = {10,20,40,90};
set2 = {20,30,50,60,70,90};
  
print(set1.union(set2))
  
print(set1.intersection(set2))
  
print(set1.difference(set2))
# print(set1-set2)
  
print(set1.symmetric_difference(set2))

set1.clear() 
print(set1)