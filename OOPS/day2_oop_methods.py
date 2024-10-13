#Here we will learn about methods in class 
#so methods are same as functions only the difference is that methods are 
#in reference for each objects
#Date: 12th October 2024


class Student:
    college_name = "ABC"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def hello(self): #passing self to the methods is mandatory
        print("Hello",self.name)
        
    def get_marks(self):
        print("You have got ",self.marks, " marks")
        

s1 = Student("Amrit",98)
s1.hello()
s1.get_marks()




