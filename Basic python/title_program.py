# Prcatical No. 8
# Title Program
# Q. Write Python program to perform following operations on
#    Set: Create Set, Access Set elements, Update Set, Delete Set

set={10,30,40,50,60,80,15}  #created set
print(set)     #access set elements

set.add(100) #update set
print(set)
print()
a={10,20,30,60,90}
b={30,40,50,60,80}
# print(a)
# print(b)
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.symmetric_difference_update(b))
print(a.difference_update(b))
print(a.intersection(b))
print(a.isdisjoint(b))
print(a.issubset(b))

set.clear()  #delete set
print(set)