class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
    def anual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,n,a,p,b):
        self.name=n
        self.age=a
        self.ansal=Salary(p,b)
    def display_tot_salary(self):
        print("Anual Salary:  ",self.ansal.anual_salary())

e=Employee('xyz',23,12000,10000)
e.display_tot_salary()
