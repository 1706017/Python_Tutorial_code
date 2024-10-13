#Date: 13th October 2024
#Private methods and attributes are meants to be used only 
#inside class and are not accessible from outside the class 

class Account:
    
    def __init__(self,acc_number,acc_pwd):
        self.acc_number = acc_number
        self.__acc_pwd = acc_pwd #here using __ before the attribute making it private attribute
        
    def change_password(self):
        self.__acc_pwd = "abc"
        print("New password", self.__acc_pwd) #here it will not through error as we are trying to access the private attribute within class scope

acc1 = Account("12345","xyz")
acc1.change_password()
print(acc1.acc_number)
print(acc1.__acc_pwd)  #here it will through error as we are trying to access the private attribute outside the class scope


