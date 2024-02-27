class Employee:
    def accept(myself,n='abc',a=0,s=0.0):
        myself.name=n
        myself.age=a
        myself.salary=s
    def display(myself):
        print(myself.name)
        print(myself.age)
        print(myself.salary)

e1=Employee()
e1.accept()
e1.display()
e2=Employee()
e2.accept('pqr',34,5687.78)
e2.display()#error bcoz data members are added to e1 , but not to e2.
e2.name='xyz'
print(e2.name) #xyz
