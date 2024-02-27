# Practical No.6
# Title program - Write Python program to perform following operations on Lists:Create
#                    list,Access list, Update list(Add item,Remove item),Delete list


list=["Java","PHP","Android","Python","HTML"]  #create list
list.append("CSS") 
list.insert(1,"Javascript")
list.remove("Javascript")
print(list)
list[0]="Angular" #update list
list + ["bootstrap"]
list.pop() #delete last element
list.reverse() #reverse list
list.sort() #sorting list
print(list)
print (len(list)) #length of list
print(min(list))  #minimun value in list
print(max(list))  #maximun value in list
print(list[::-1]) #reverse list
print(list)
print(list*4) #Multiply by list
print(list[2:5])
print(list.index("PHP"))  # search in the whole list
print(list.index("Python",0,5))  # search from 1th to 5nd position
list.clear() #Delete list
print(list)


