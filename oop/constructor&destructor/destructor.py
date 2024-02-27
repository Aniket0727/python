# Python program to illustrate destructor
class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.')
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')
#def fun():
obj = Employee()
#It is also possible to call constructor and desctructor manually
obj.__init__()
obj.__del__()
#fun()
