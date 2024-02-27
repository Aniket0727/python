class Employee:
    __count=0
    def __init__(self):
        Employee.__count=Employee.__count+1
    def display(self):
        print("The number of employees", Employee.__count)
emp1=Employee()
emp2=Employee()
print(emp1.__count)
emp1.display()
emp2.display()
