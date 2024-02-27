# Practical No. 9
# Exerise Question
# 5. Write a Python program to find the highest 3 values in a dictionary.
import operator
dict={'Python':99,'Java':96,'PHP':95,'Android':98,'Javascript':89,'MGT':88,'EST':91}
print("Dictionary: ")
print(dict)
print()
dsen = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print("Highest Three Values In dictionary: ")
n=0
for i,j in dsen:
    if(n<3):
        print(j,end=" ")
        n=n+1