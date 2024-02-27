# def fun():
#     print("annu")
    
# fun()


# def add(x,y,z):
#     x=x+10
#     y=y+10
#     z=z+10
#     return x,y,z    

# a=add(1,2,3)

# print(2)
      
# a:int=10
# print(a)

# def fun(*a):
#     print(type(a))
#     print(a)

# fun(1,2,3,4,5)

      
# def fun(a,b,*args):
#     print(a)
#     print(b)
#     print(args)
    
      
# fun(a=1,b=2,c=3)

def outer(x,y):
    def inner():
        print("inner")
    print("outer")
    return inner

obj=outer(10,20)
print(obj)
obj()