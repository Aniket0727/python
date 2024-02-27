class A:
    def __init__(self):
        print("Constructor of class A")
    def __del__(self):
        print("Destructor of class A ")

class B(A):
    def __init__(self):
        print("Constructor of class B")
    def __del__(self):
        print("Destructor of class B")

def fun():
    print("start")
    b=B()
    print("End")

fun()
