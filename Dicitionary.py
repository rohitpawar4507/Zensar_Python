''' Dictionary :: Collection of different element in key value pairs enclosed in {} seprated by comas
 It is mutable object .
 # Key -- value pair -- Both number and string are used for key as well as value
 '''

# Create a dicitionary
print("The Program for Dictionary!!!")
print("Creating a dictionary and adding element on it..")
d1={1:'Nashik',2:"Pune",3:"Aurangabad"}
print("The Dict is :",d1)

print("Adding element to the dict..")
d1['Nsk']=101
d1['Aug']=108
d1['Pun']=103
print("The dictiionary is ",d1)
print("The element is ",d1[1])
print("The element is ",d1[2])
print("The element is ",d1[3])

d1[4]="Khalapur"
print("The updated dict is..",d1)

print("Creating an empty dictionary..")
d2={}
d2[0]=100
d2[1]=102
print("The Dict is..",d2)

a=d2.get(1)
print(a)

d2[1]=105
print(d2[1])
d1[4]="Jamkhed"
d1[5]="Goa"
print(d1)

#Deleting element from dict
print("Delecting the element in the dictionary")
print("THe original dict is..",d1)

d1.pop(3) # atleast one argument required
print("The dictionary is ",d1)

# Deleting all element in the dictionary / clear()
d3={1:'Rohit',2:"Om",3:"Rahul"}
d3.clear()
print("The dictionary is..",d3)

# Delete the dict by using del()
'''print("Deleting a Dictionary!!!")
d4={1:'Rohan',2:"Omkar",3:"Raj"}
print(d4)
del d4
print("The dictionary is..",d4)
'''
# Iterate a Dicitionary
print("Iterating the Dictionary")
print("Printing the keys using for loop")
for x in d1: # Printing the keys
    print(x,end=' ,')

print("\nPrinting the Values using for loop")
for x in d1.values(): # Printing the values
    print(x,end=' ,')

print("\nPrinting the values using for loop")
for x in d1: # printing the values
    print(d1[x],end=',')

print("\nPrinting the Values and Keys using for loop")
for x,y in d1.items():   # printing the key and value
    print("Key = ",x,"  Value = ",y)

### Assignment ###



#4. convert tuple into dictionary

#8. Return a element with key 101 from student dict
#7. Delete one element from student dict

#9. print only keys from dict student
#10. print only value from dict student
#11. creat a dict employee with ename as key and salary as value.
#12. print the employee dict
#13. delete the employee with salary -10000