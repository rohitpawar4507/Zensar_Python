
import numpy as np

type1 = np.array([1,2,3,4,5,6])
print("Array :",type1)
print(type1.dtype)  # For cheking the type array

type2 = np.array([1.3,45.5,5.5,6.4])
print("Array =",type2)
print(type2.dtype)

type3 = np.array(['a','c','d'])
print("Array =",type3)
print(type2.dtype)

type4 = np.array(["Pune","Solapur"],dtype='U5')
print("Array =",type4)
print(type4.dtype)

type5 = np.array([1,4,5,6],dtype=float) # set datatype to float
print("Array =",type5)
print(type5.dtype)

# Shape of Array
''' The shape method determines the shape of Numpy array
in from of (m,n) i.e (no. of rows) x (no.of columns),'''

# Create a array
array1d = np.array([1,2,3,4,5,6])
print(array1d)
print(array1d.shape)

# Two dimensional
array2d = np.array([[1,2,3],[4,5,6]])
print("_" * 20) # Create a line border
print(array2d)
print(array2d.shape)

# Create 3rd array with 3 Dimensional
array3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("_" * 20)  # Create a line border
print(array3d)
print(array3d.shape)

# Find the Dimension of Array

# Create a array
array1d = np.array([1,2,3,4,5,6])
print("The Dimension of Array is: ",array1d.ndim)

# Two dimensional
array2d = np.array([[1,2,3],[4,5,6]])
print("_" * 20) # Create a line border
print("The Dimension of Array is :",array2d.ndim)

# Create 3rd array with 3 Dimensional
array3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print("_" * 20)  # Create a line border
print("The Dimension of Array is: ",array3d.ndim)


# RESHAPE AN ARRAY :
''' The reshpae method modifies exisiting shape
but original array remains  Unchanged.
'''

thearray = np.array([1,2,3,4,5,6,7,8])
print(thearray)
print(thearray.reshape(2,4)) # Change the dimension of array

print("_" * 20)

thearray = thearray.reshape(4,2)
print(thearray)

print("_" * 20)

thearray = thearray.reshape(8,1)
print(thearray)

# Resize the array

array1 = np.array([1,2,3,4,5,6,7,8])
print(array1)
array1.resize(4) # change size to 4
print("After resizzeing the array ", array1)

print("_" * 20)
array1 = np.array([1,2,3,4,5,6,7,8])
array1.resize(7) # change size to 4
print("After resizzeing the array ", array1)

# Converting list or tuple in array
List = [1,3,4,5,6,7,8]
array1 = np.array(List)
print("The Converted list is",array1)

# Convert tuple into array
tup = ((8,3,4,5,6,7,0))
array2 = np.array(tup)
print("The converted tup is",array2)




