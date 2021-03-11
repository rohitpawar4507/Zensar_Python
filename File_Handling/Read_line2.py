'''print("Reading the file")
f1=open("file2.txt","r")

if f1:
    print("File created successfully")
else:
    print("file is not created")

print("Reading the file")
# Read the number of character from file
#data=f1.read() # Read entire field
data = f1.readline() # Read upto 10 character
print("The Data in the file is...!")
print(data)
print(f1.readline()) # read entire line in the file
f1.close()
print("File is closed..!")'''

print("Reading the file")
f1=open("file2.txt","r")

if f1:
    print("File created successfully")
else:
    print("file is not created")

print("Reading the file")
# Read the number of character from file
#data=f1.read() # Read entire field
data = f1.readlines() # Read multiple line in the form of list
print("The Data in the file is...!")
print(data)
#print(f1.readline()) # read entire line in the file
f1.close()
print("File is closed..!")