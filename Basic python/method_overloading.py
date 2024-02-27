# Practical No.14
# Method Overloading
class one:
    def product(self,a, b):
        p = a * b
        print(p)

class two:      
    def product(self,a, b, c):
        p = a * b*c
        print(p)

obj1=one()
obj1.product(2,2)

obj2=two()
obj2.product(2,3,3)

