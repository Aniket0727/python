class first:
    a=10
    def f(self):
        print("first")

class second:
    b=20
    def se(self):
        print("second")

class third(first,second):
    def msg(self):
        print("third")

t=third()
t.f()
t.se()
t.msg()