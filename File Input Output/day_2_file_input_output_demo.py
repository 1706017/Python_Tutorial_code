#File Input Output In Python 
#Date: 12th October 2024

#Here using python we can read files do some operations on them and then we 
# can write those files

#Types of FILES:
# .tx,.log,.docs,.mp4,.mov,.png,.jpeg etc...

#Open a file 
#So before reading or writing a file we need to first open a file 
#Syntax will be like
# open("file_name","mode")
# file_name shoule be the complete path to the file if not in same directory
# mode will be like read mode or write mode denoted by r or w
# if we do not pass any mode then by default it will be read mode only 
f = open("demo.txt","r")
data = f.read()
data1 = f.read(5) # to read only the first 5 characters
print(data)
print(data1)
print(type(data))
print(len(data))
f.close() # always a good practice to close the file


#to read line by line

f=open("demo.txt","r")
line1 = f.readline()
print("Line 1 is",line1)

line2 = f.readline()
print("Line 2 is",line2)

f.close()


#Writing to the file 
# It has two mode one is write mode and other is append mode 

#f= open("demo.txt","w")
#f.write("This is my line to update the file")
#f.close()

#f= open("demo.txt","a")
#f.write(" \nThis is my third line")
#f.close()

#deleting a file using the os module 
#module is just a program already written by someone and we are just using that module or set of code to perform the task

import os

os.remove("sample.txt")


