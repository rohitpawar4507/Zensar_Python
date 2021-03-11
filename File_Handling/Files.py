print("Creating a file for the first time.")
#If you open a file in mode x , the file is created and opened for writing – but only if it doesn't already exist
'''f1 = open("file1.txt","x")  # create a new file

print(f1)

if f1:
    print("File created Successfully")
else:
    print("The file is not created")
    '''
# Create file in write mode  -> if file already present
# it does give error
'''f1 = open("file2.txt","w")  # create a new file

print(f1)

if f1:
    print("File created Successfully")
else:
    print("The file is not created")
'''
# Create file in append mode
f1 = open("file2.txt","r")  # create a new file

print(f1)

if f1:
    print("File created Successfully")
else:
    print("The file is not created")