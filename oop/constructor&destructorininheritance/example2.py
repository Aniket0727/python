class A:
    def __init__(self):
        print("Constructor of class A")
    def __del__(self):
        print("Destructor of class A ")

class B(A):
    def __init__(self):
        #A.__init__(self)# self parameter is required.
        super().__init__() # self parameter is not required.
        print("Constructor of class B")
    def __del__(self):
        A.__del__(self)# self parameter is required.
        #super().__init__() # self parameter is not required.
        print("Destructor of class B")

def fun():
    print("start")
    b=B()
    print("End")

fun()
