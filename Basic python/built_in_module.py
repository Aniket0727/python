# Practical No. 12
# Title Program - 1
# Built-in-module

import keyword
import math
import numbers
import operator

# keyword module
print (keyword.iskeyword('True'))
print (keyword.iskeyword('fal'))
# print (keyword.kwlist)

# math module
print (math.pow(4,2))
print (math.degrees(2))
print (math.radians(60))
print (math.sin(2))
print (math.cos(0.5)) 
print (math.tan(0.23)) 
print (math.factorial(4))

# number module
n1=10
n2=20
print (n1.__add__(n2))
print (n1.__eq__(n2))
print (n1.__ne__(n2))
print (n2.__neg__())
print (n1.__sub__(n2))


# operator module
a=5
b=8

print (operator.add(a,b))
print (operator.sub(a,b))
print (operator.mul(a,b))
