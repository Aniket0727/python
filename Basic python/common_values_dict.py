# Practical No. 9
# Exerise Question
# Q3. Write a Python program to combine two dictionary adding values for common
# keys.
# a. d1 = {'a': 100, 'b': 200, 'c':300}
# b. d2 = {'a': 300, 'b': 200, 'd':400}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
print("Common Values Added in new Dictionary: ")
for i,j in d1.items():
    for a,b in d2.items():
        if i==a:
            b=b+j
            d3.update({i:b})
print(d3)
     