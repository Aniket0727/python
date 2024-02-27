# Practical No. 9
# Exerise Question

# Q.2 Write a Python script to concatenate following dictionaries to create a new one.
#  a. Sample Dictionary:
#  b. dic1 = {1:10, 2:20}
#  c. dic2 = {3:30, 4:40}
#  d. dic3 = {5:50,6:60}
print("Concatination of Dictionary: ")
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4={}
dic2.update(dic1)
dic3.update(dic2)
dic4.update(dic3)
print(dic4)
