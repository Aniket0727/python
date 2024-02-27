# Experiment No.11 
# compute the diameter, circumference, and volume of a sphere using class
import math
class sphere:
     def cal(self):
          radius =float(input("Enter radius: "))
          volume = (4/3) * math.pi * radius**3
          diameter=2*radius
          circumference=2*math.pi*radius
          print("volume of sphere: ",volume)
          print("Diameter of sphere: ",diameter)
          print("Circumference of sphere: ", circumference)
          
s=sphere()
s.cal()