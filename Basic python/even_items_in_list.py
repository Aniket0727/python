# Practical no.6
# Q.7 Write a Python program to select the even items of a list.

l=[1,5,6,7,8,9]
list=[]
for i in (l):
    if(i%2==0):
        list.append(i)
print("Even items in list: ",list)
