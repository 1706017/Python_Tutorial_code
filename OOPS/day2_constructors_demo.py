#Constructors or __init__() method this is called as soon as object is initialized
#Whether we write or not the __init__() method is already being called internally
#Date: 12th October 2024

class Bike():
    
    def __init__(self): # this is called default constructor
        pass
    
    
    def __init__(self,model_name): #here self parameter is referenced to the object instance
        self.model_name = model_name #this is called parameterized constructor
        print("New Bike model added to garage!!")
        print("Name of the model is",model_name)
    
b1 = Bike("Apache RTR") #Object is initialized
print(b1.model_name)

b2 = Bike("Hayabusha")

b3 = Bike("Splendor")



