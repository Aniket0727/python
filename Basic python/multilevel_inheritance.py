class first:
    a=10
    def f(self):
        print("first")
        
class second(first):
    b=20
    def s(self):
        print("second")
        
class third(second):
    c=30
    def t(self):
        print("third")    
        
s=second()
print(s.a)
        
t=third()
t.f()
t.s()
t.t()

print(t.a)
print(t.b)
print(t.c)
    