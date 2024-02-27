class Area:
    def area(self,*args):
        if len(args)==1:
            print(args[0]*args[0])
        else:
            print(args[0]*args[1])
   
a=Area()
a.area(5)
a.area(5,7)
