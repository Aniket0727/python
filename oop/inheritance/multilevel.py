# Python program to demonstrate multilevel inheritance
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		
                # invoking constructor of Grandfather class
		super().__init__(grandfathername)

class Son(Father):
	def __init__(self,sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		super().__init__(fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

# Driver code
s1 = Son('ABC', 'PQR', 'XYZ')
#print(s1.grandfathername)
s1.print_name()
