# Python Set {}

# Unordered collection of various items enclosed.
# The element of set can not be duplicate
# Set is Mutable
# No index attached to the elements of the set, we can not
# We cannot traverse set , We cannot direct access a set

# Create a Set
print("Let us try the set in python...")
print("The following Set is the Set of Days..")
Days={'Mondey','Tuesday','Wednesday','Tuesday','Friday','Saturday','Sunday'}
print("Print the original set is: ",Days)

# type check
print("The type is :",type(Days))
print("Printing the set again: ",Days)

print("Looping through set elements..!")
for i in Days:
    print(i,end=' ')
print("\n The code is complete.")

# Converting list into a Set.
print("Converting a List into a Set")
list1=['Mango','Apple','Chiku']
print("Printing the list ", list1)

number=set(list1)
print("The type of variable is: ",type(number))
print("Converted set is :",number)

# LOOPING
for i in number:
    print(i,end=' ')
print("The code is completed..")

num=set([1,3,4,5,6,4,3,2,1])
print("The set is ",num)

# Adding element to set
print("Adding element to the set.")
number.add("Grapes") # add one element at a time in add function
number.add("Banana")
print("The set after adding elements..",number)

# Adding multiple element using Update()
print("Adding multiple element using Update()")
number.update("Fruit","Favraoute","Market")
print("After adding multiple element..",number)

# Removing the elements
print("Removing the elements using Discard ()")
number.discard("Banana")
print(number)

'''print("Removing the elements using remove ()")
number.remove("Market") # If the element is not present in the set remove gives an error.
print(number)'''

print("Removing the elements using Discard ()")
number.discard("Banana")   # Wont give any error if the element is not present
print(number)

# Removing all elements from the set using Clear().
print("Removing all the element from the set")
number.clear()
print("The set after clear () use:", number)

# Create a new set
day1={'One','Two','Three'}
day2={'Four','Five'}
print("The set 1 ,is:",day1)
print("The set 2 is :",day2)

# Union of both sets
print("The union of two set is: ")
print("Union 1 is ",day1|day2) # another way for union
print("Union 2 is ",day1.union(day2))
print("Union 3 is ",day2|day1)
print("Union 4 is ",day1.union(day2))

# Insertion section of two set
day1={'One','Two','Three','Five','Seven'}
day2={'Four','Five','One','Two'}
print("The set 1 ,is:",day1)
print("The set 2 is :",day2)

print("The Intersection of two set is: ")
print("Intersection 1 is ",day1&day2) # another way for Intersections
print("Intersection 2 is ",day1.intersection(day2))
print("Intersection 3 is ",day2&day1)
print("Intersection 4 is ",day1.intersection(day2))

# Symmetric difference
print("The Symmetric difference of two sets is ")
# either in set 1 or in set 2 , but not in both set
print("Symmetric difference 1 is ",day1^day2) # another way for Symmetric differnce ^ carrot symbol
print("Symmetric difference2 is ",day1.symmetric_difference(day2))
print("Symmetric difference 3 is ",day2^day1)
print("Symmetric difference 4 is ",day1.symmetric_difference(day2))



