# Practical No. 9
# Exerise Question

# 4. Write a Python program to print all unique values in a dictionary.
# a. Sample Data: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
l3=[]
l2=[]
for i in l:
	p = list(i.values())
	l3.append(p)
for j in l3:
	if l3.count(j)==1:
		l2.append(j)
print("Unique Values: ")
print(l2)