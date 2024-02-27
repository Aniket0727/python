# Practical No.7
# Q.2 Write a Python program to find the repeated items of a tuple

t1=(3,4,6,2,3,9,3,3,3,4)  #create tuple
l=[] #create empty list
t={} #create empty set
for i in t1:
    count=t1.count(i)
    if count > 1: 
        l.append(i)

print(t1)
t=set(l) #list convert into set
for i in t:
    c=t1.count(i) #count how many times repeate item in tuple 
    print(i,"is repeated",c,"times in tuple")