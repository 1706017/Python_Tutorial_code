#Date: 13th October 2024
# Here we will learn about del keyword 
#It is simply use to delete the object or objects attribute
#As we know that each object occupies some memory space 

class Student:
    
    def __init__(self,name):
        self.name = name

s1 = Student("Amrit")
print(s1)
print(s1.name)

del s1.name
del s1
print(s1)
print(s1.name) 

