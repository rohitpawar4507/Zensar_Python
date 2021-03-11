print("Reading the file")
f1=open("file2.txt","r")

if f1:
    print("File created successfully")
else:
    print("file is not created")

print("Reading the file")
# Read the number of character from file
#data=f1.read() # Read entire field
data = f1.read(10) # Read upto 10 character
print("The Data in the file is...!")
print(data)
f1.close()
print("File is closed..!")