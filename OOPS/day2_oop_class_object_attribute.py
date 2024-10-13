#Here we will learn about class and Object Attribute
#So class attribute means that is common attribute across all objects of the class
#Object attribute means that is different for all objects of the class
#Date : 12th October 2024

class Employee:
    company_name = "XYZ LTD"  #class attribute
    
    def __init__(self,emp_name,emp_city):
        self.emp_name = emp_name #object attribute
        self.emp_city = emp_city #Object attribute
    
e1 = Employee("Amrit","Patna")
print(e1.emp_name)
print(e1.emp_city)
print(e1.company_name)


e2 = Employee("Manash","Pune")
print(e2.emp_name)
print(e2.emp_city)   
print(e2.company_name)

