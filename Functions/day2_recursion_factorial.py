#Here we will learn about Recursion in Python 
#So Recursion is like when a function calls itself recursively this is call recursion 

#But here the base case place a vital role other wise if there is no base case
# then function call will be for infinite times and that will crash the code
#Date: 12th October 2024


def factorial_num(n):
    if (n==1 or n==0): #Here this is base case or stopping condition
        return 1
    else:
        return n * factorial_num(n-1)

res= factorial_num(3)

print("The factorial of the number is ",res)