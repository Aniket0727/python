class Multiply:
    def product(self,*args):
        if len(args)==2:
            print(args[0]*args[1])
        else:
            print(args[0]*args[1]*args[2])
x=Multiply()
x.product(4,5)
x.product(4,5,5)
