'''# Initializing numpy array with random numbers

import numpy as np
n1 = np.random.randint(1,200,10)
print(n1)
n2 = np.array(10,100,5)
print(n2)'''

# Joining two numpy arrays

import numpy as np

# vertical stack
n1 = np.array([10,20,30,40])
print(n1)
n2 = np.array([50,60,70,80])
print(n2)
n3 = np.vstack((n2,n1))
print(n3)
print(np.vstack((n1,n2)))

#  horizontal stack
n1 = np.array([10,20,30,40])
print(n1)
n2 = np.array([50,60,70,80])
print(n2)
n3 = np.hstack((n2,n1))
print(n3)
print(np.hstack((n1,n2)))

#  column stack
n1 = np.array([10,20,30,40])
print(n1)
n2 = np.array([50,60,70,80])
print(n2)
n3 = np.column_stack((n2,n1))
print(n3)
print(np.column_stack((n1,n2)))

# Addition of two numpy arrays

#  Adding two numpy array
n1 = np.array([10,20,30,40])
print(n1)
n2 = np.array([50,60,70,80])
print(n2)
n3 = np.sum([n2,n1])
print("The sum of two array :",n3)
# Adding the column values using the axis
n3 = np.sum([n1,n2],axis = 0)
print("The sum of array is:",n3)
n3 = np.sum([n1,n2],axis = 1)
print("The sum of array is:",n3)


print("Mean is:",np.mean(n1))
print("Median is:",np.median(n1))
print("Std is:",np.std(n1))

a = np.arange(6, 20)
print(a)