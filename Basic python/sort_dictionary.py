# Practical No. 9
# Exerise Question 
# Q1. Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
dict={'Python':98,'Java':96,'PHP':95,'Android':98,'Javascript':89,'MGT':88,'EST':91}
print("Origional Dictionary")
print(dict)
print()
asen = sorted(dict.items(), key=operator.itemgetter(1))
print("Ascending Dictionary")
print(asen)
print()
print("Descending Dictionary")
dsen = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print(dsen)