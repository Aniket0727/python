class Base: 
    def method(self): 
        print('in Base Class method') 

class Derived(Base): 
    def method(self):                        
        print('starting Derived Class method')          
        Base.method(self)                   
        print('Ending Derived Class method') 

       

x = Derived()                
x.method()
