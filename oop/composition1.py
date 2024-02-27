class Department:
    def set_department(self):
        self._id=input("Enter Department ID: ")
        self._name=input('Enter Department Name: ')
    def display_department(self):
        print('Department ID is: ',self._id)
        print('Department Name is: ',self._name)

class Employee:
    def set_employee(self):
        self._eid=input("Enter Employee ID: ")
        self._ename=input("Enter Employee Name: ")
        self._deptobj=Department()
        self._deptobj.set_department()
    def display_employee(self):
        print('Employee ID: ',self._eid)
        print('Employee Name: ',self._ename)
        self._deptobj.display_department()

obj=Employee()
obj.set_employee()
obj.display_employee()
        
        
