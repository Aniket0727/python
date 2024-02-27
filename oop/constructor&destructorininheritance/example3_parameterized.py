class Person:
    def __init__(self,n,a):
        print("Constructor of Base class")
        self.name=n
        self.age=a
    def __del__(self):
        print("Destructor of class A ")
class Employee(Person):
    def __init__(self,n,a,s):
        Person.__init__(self,n,a)# self parameter is required. Person.__init__('Anuradha', 32)
        #super().__init__(name,age) # self parameter is not required.
        print("Constructor of Derived Class")
        self.salary=s
    def __del__(self):
        Person.__del__(self)# self parameter is required.
        #super().__init__() # self parameter is not required.
        print("Destructor of class B")
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
def fun():
    print("start")
    e=Employee("Anuradha",32,6790)
    e.display()
    print("End")

fun()