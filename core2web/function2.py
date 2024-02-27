def  outer():
    
    def inner1():
        print("Inner function1")
        
    def inner2():
        print("Inner function2")
    
    return inner1,inner2
        
obj1,obj2=outer()
print(obj1,obj2) #function address
obj1()
obj2()