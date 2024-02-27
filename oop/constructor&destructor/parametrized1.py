class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
    def display(self):  
        print("ID: %d \tName: %s" % (self.id, self.name))  

emp1 = Employee("ABC", 101)  
emp2 = Employee("XYZ", 102)  
emp1.display()  
emp2.display() 