class Employee:
    name='abc'
    age=0
    salary=0.0
    def accept(self,n,a,s):
        self.name=n
        self.age=a
        self.salary=s
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
e1=Employee()
e1.accept('xyz',45,1988.4)
e1.display()
e2=Employee()
e2.display()#No error now, bcoz the name, age & salary are data members of class
            # and even if we dont accept it, it takes default values.
