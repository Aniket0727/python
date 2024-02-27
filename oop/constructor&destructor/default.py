class Student:  
    # Constructor - non parametrized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()
student.__init__()
student.show("John")      
