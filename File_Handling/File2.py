# Create file in write mode
f1 = open("file1.txt","w")  # create a new file

print(f1)

if f1:
    print("File created Successfully")
else:
    print("The file is not created")

print("Writing data to the file...!")
# writing a data into a file
f1.write("This is the first file we created. File operations are goood")
f1.write("\nThis is the second line of the file..")

print("The write operation is close")
f1.close() # Close the file
print("File is closed")