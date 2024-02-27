# Experiment No.7 Program to map two lists into a dictionary

list1=[0,1,2,3,4,5,6,7,8,9]
list2=["zero","one","two","three","four","five","six","seven","eight","nine"]
dict1={}

print("Using zip method: ")
dict1=dict(zip(list1,list2))
print(dict1)
print()
print("Using for in loop: ")
for key in list1:
     for value in list2:
          dict1[key]=value
          list2.remove(value)
          break
print(dict1)
