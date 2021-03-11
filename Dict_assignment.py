### Assignment ###

d1={1:'Nashik',2:"Pune",3:"Aurangabad"}

#1.Find the length of dictionary
print("The length of dictionary is ..",len(d1))

#2.print dict in sorted manner

#print("The dictionary in sorted manners..",sorted(d1))

#3.Check whether the value is present in dictionary
value="Pune"
if value in d1.values():
    print(f"The given value is exits '{value}':")
else:
    print(f"The given value does not exits '{value}:")


#4. convert tuple into dictionary
tup=((1,'a'),(3,'b'))
print(dict(tup))

#5. Create a dictionary student with student details.
student={1:"Rohit",2:"Man",3:"Raj",4:"Vijay"}
print(student)

#6. add elements to student dict
d1[5]="Ram"
d1[6]="Sham"
print(d1)

#7. Delete one element from student dict
'''d1.pop("Ram")
print("Dict after deleting one elements,",d1)
'''
#8. Return a element with key 101 from student dict
value="Rohit"
if value in student.values():
    print(f"The given value is exits '{value}':")
else:
    print(f"The given value does not exits '{value}:")

#9. print only keys from dict student
print("Printing the keys using for loop")
for x in student: # Printing the keys
    print(x,end=' ,')
#10. print only value from dict student
print("\nPrinting the Values using for loop")
for x in student.values(): # Printing the values
    print(x,end=' ,')