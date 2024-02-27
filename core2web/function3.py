def  outer():
    
    def inner1():
        print("Inner function1")
    
    
    return inner1
    print("outer")
        
obj1=outer()
print(obj1) #function address
obj1()
