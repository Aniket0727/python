#  Practical No. 13
# Q.3	Write a NumPy program to generate six random integers between 10 and 30.

import numpy as np
x = np.random.randint(low=10, high=30, size=6)
print(x)