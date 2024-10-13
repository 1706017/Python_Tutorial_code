#Date: 13th October 2024
#Here we will Learn about static method

#Static method : it does not use the self parameter to be passed in the method
#as we need to do for normal methods
# as this method works at class level not at individual objects level 

class Student:
    
    @staticmethod    #THIS annotation part is known to be decoraters
    def college_name():
        print("XYZ")
        print("College name is XYZ")
    

s1 = Student()
s1.college_name()


    
    