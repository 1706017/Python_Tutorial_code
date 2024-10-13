#create student class that taskes name and marks of 4 subjects as argument 
#in constructor and then create a method to print the highest marks 
#Date: 13th October 2024

class Student:
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def find_highest_marks(self):
        max_marks = self.marks[0]
        for mark in self.marks:
            if mark > max_marks:
                max_marks = mark
        
        print("Maximum MARK IS",max_marks) 

s1 = Student("Amrit",[55,67,89,45])
s1.find_highest_marks()


   
        