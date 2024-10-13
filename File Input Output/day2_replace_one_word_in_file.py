#create a file and write the below data to that file 
#Here we do not require to use f.close() because it will close the file automatically
#Date: 12th October 2024


#with open("data.txt","w") as f:
#    f.write(" Hello World! \n This is me Learning Python \n")
#    f.write(" this is easy to learn")

#print("The file got created successfully")

#Now we will replace the word Python with java

with open("data.txt","r") as f:
    data=f.read()
    print("Previous version of file content was ", data)
    new_data = data.replace("Python","Java")
    print("New Version of file content is ",new_data)

with open("data.txt","w") as f:
    f.write(new_data)

print("Replacing the word executed")


    