# Experiment No.10  Program to find the length of a list using recursion.
def len(list1,count):  
     if not list1:
          print("Length Of List: ",count)
     for i in list1:
          count=count+1
          list1.remove(i)
          len(list1,count)

list1=["one","two","three","four","five"]
count=0
print("List is: ",list1)
l=len(list1,count)