file2 = open("file2.txt","r")

# Initially the file pointer is at location 0.
print("The filePointer is at byte :",file2.tell())

# Reading the content of the file
content = file2.read(15)
print("The file data is: ",content)

# after the read operation file pointer modifies
print("After reading, the file pointer is at:",file2.tell())
file2.close()
print("File is closed")

## Assignment
''' 
1.Wap to read the number of characters in a file.
2.Wap to read data from one file and write the same
to other file
3.Wap to print only the numbers from the file on screen
4.Wap to print only character (excluding numbers) from file
5.Wap to print total number of lines in file
6.Wap to print the data in reverse order from the file
7.Wap to count number of times letter 'x' appears in the 
file
8. Wap to count total blank spaces in the file
9. Wap to print every word in the file with initial capital
letter
'''