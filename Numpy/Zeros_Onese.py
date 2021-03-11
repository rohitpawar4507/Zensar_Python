'''
Zeros()
ones()
'''
import numpy as np

array1 = np.zeros(3)
array3 = np.zeros((3,3))
array2 = np.ones(3)

print(array1)
print(array2)
print(array3)

array1 = np.zeros((5,5))
print(array1)

# Initialize the numpy array with the same numbers

array1 = np.full((2,2),10)
array3 = np.full((3,3),5)


print(array1)
print(array3)

# Initialize numpy array with a range
'''n1 = np.array(10,20)
print(n1)

n2 = np.array(10,50,5)
print(n2)
'''

# Initializing numpy array with random numbers

import numpy as np
n1 = np.random.randint(1,200,10)
print(n1)

n2 = np.array(10,100,5)
print(n2)