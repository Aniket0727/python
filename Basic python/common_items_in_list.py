# Practical no.6
# Q.6 Write a Python program to find common items from two lists.


l1=[10,20,30]
l2=[20,40,50,10]
lis=[]

for i in l1:
    for j in l2:
        if(i==j):
            lis.append(i)
print("Common items in both list is: ",lis)