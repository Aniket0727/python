# Practical No. 14
# Exercise Q.2
class Area:
    def cal(self,*args):
        if len(args)==1:
            print("Area of squre: ",args[0]*args[0])
        else:
            print("Area os rectangle: ",args[0]*args[1])
    
a=Area()
a.cal(10)
a.cal(20,30)
