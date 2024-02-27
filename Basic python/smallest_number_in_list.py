# Practical no.6
# Q.4 Write a Python program to get the smallest number from a list.

l=[10,90,30,40]
# a=min(l)
min=l[0]
for i in l:
    if i<min:
        min=i
print("Smallest number in list is: ",min)