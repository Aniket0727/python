class Employee:
    def message(self):
        print('print from Employee')
class department(Employee):
    def message(self):
        print('print from departmet')
emp=Employee()
emp.message()
dept=department()
dept.message()
