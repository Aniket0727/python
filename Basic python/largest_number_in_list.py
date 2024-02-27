# Practical no.6
# Q.3 Write a Python program to get the largest number from a list.

l=[10,90,30,40]
# max=max(l)
max=l[0]
for i in l:
    if i>max:
        max=i

print("large",max)