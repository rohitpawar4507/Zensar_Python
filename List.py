# List is Data structure -->collection of Object
# List is Heterogeneous collection of elements enclosed within a pair of square brackets seprated by comma,
# It is mutable -> we can modified ,changes.or access

# Create a list
print(" A Demo for the list:")
list1 =[1,2,32,4,5,6,7,8,9] # List of number
print("The list we have is .. ",list1)

print("The element from the list is:",list1[0])
print("The element from the list is:",list1[2])
print("The element from the list is:",list1[4])
print("The element from the list is:",list1[5])
print("The element from the list is:",list1[7])

list2 =['Pune','Baramati','Nashik','Thane'] # List of number
print("The list we have is .. ",list2)

print("The element from the list is:",list2[0])
print("The element from the list is:",list2[1])
print("The element from the list is:",list2[2])
print("The element from the list is:",list2[3])
#print("The element from the list is:",list2[4])

# Updating a list element
print("The original list ",list2)
print("Trying to update a list...")
list2[3]='Jaipur'
print("The updated list is,,",list2)

print("Trying to update a list...")
list2[1]='Delhi'
print("The updated list is,,",list2)

# Genrating list using for loop

number=[x+6 for x in [1,2,3,4,5]]
print("The list is ",number)

# Creating a list using for loop and range function

number=[x+6 for x in range(1,12)]
print("The list is ",number)

number=[x for x in range(1,10)]
print("The list is ",number)

# Convert a String into List
str='Rohit'
print(str)

abc='Rohit Pawar'
print(list(abc))

# Search/Finding the element in list by using membership operator
list3=[1,2,3,4,'Pune','Delhi',65,'Thane']
for element in list3:
    print(element)
if 'Pune' in list3:  # Membership opeartor for searching
    print("The element exit in the list.")
else:
    print("The element does not exit ")

# Adding the element to List using append()
list1 =[1,2,32,4,5,6,7,8,9] # List of number
print(list1)
list1.append("Ro-Hit")
print(list1)

# Using Insert()
list2 =['Pune','Baramati','Nashik','Thane'] # List of number
print(list2)
list2.insert(3,"Jamkhed")
print(list2)

# remove the element using remove method
list2 =['Pune','Baramati','Nashik','Thane'] # List of number
list2.remove('Baramati')
print("After Removing element the list is..",list2)

# Also we can used pop func for deleting list element
list2.pop()
print(list2)

# remove the occurance of element in the list
list4=[1,2,3,4,5,5,6,7,3,3,56]
print("The Original list is ",list4)

print("Remove all the occurances of 3 from the list.")

for i in list4:
    if i==3:
      print("The loop Completed")
print("The final list after removing element is ",list4)