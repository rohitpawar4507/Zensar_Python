print("Writing data on Multiple lines Using "" ")

# creating file in write mode
f1=open("file1.txt","w")  # Create a new file

if f1:
    print("File create Successfully..!")
else:
    print("File is Not created..")

print("Writing data into file ")
f1.write(''' This is the first file we created,
This is second line of the file
we are writing the data on multiple lines.
  files operation are good...''')

print("The write operation is completed")
f1.close()
print("File is closed..")

'''# Read the file
f1=open("file1.txt","w")

if f1:
    print("File create Successfully..!")
else:
    print("File is Not created..")
print("Reading the files")
print(f1.read())
f1.close()
print("File is closed..")'''