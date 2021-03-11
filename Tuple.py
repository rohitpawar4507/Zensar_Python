
print("Learning Tuple")
'''tup=()  # Empty tuple
print(tup)'''

tup1=(1,2,3,4,5,6,7)  # Tuple with number
print(tup1)

tup2=('one','two','three','four','five')  # Tuple with character
print(tup2)

print(tup2[0])
print(tup1[3])

# Iterate a tuple using for loop
for element in tup1:
    print(element)

# Check if item exit or not
if 1 in tup1:
    print("present")
else:
    print("Not exits")

if 'one' in tup2:
    print("present")
else:
    print("Not exits")
# Delete tuple using del func
'''del tup
print(tup)
'''

# Using Sorted() function
a=sorted(tup1)  # return a list of sorted elements
print(a)

# Concatnet two tuple
b=tup1+tup2
print(b)

# Finding the index of element
idx=tup1.index(3)
print(idx)

list1=tuple([2,4,5,6,6]) # in tuple we can add list and vice versa  # Casting
print(type(list1))

tup5=tup1+list1
print(tup5)

print(len(tup5))