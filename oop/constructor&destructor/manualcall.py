class Hello:
    def __init__(self):
        self.a=10
        self.b=20
    def change(s):
        s.a=s.a+1
        s.b=s.b+1
    def display(se):
        print("a=",se.a)
        print("b=",se.b)
    def __del__(self):
        print("destructor called")

def fun():
    hello=Hello()
    hello.display()#10 20
    hello.change()
    hello.display()#11 21
    del hello #destructor called
    hello=Hello()#
    hello.__init__()#
    hello.__del__()#
    hello.display()
fun()
