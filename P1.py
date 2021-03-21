# Write a program to Add, Subtract, Multiply, and Divide 2 numbers

def add_nos(a,b):
    return a+b

def sub_nos(a,b):
    return a-b

def multiply_nos(a,b):
    return a*b

def divide_nos(a,b):
    return a/b

num1 = int(input("Enter 1st number:::"))
num2 = int(input("Enter 2nd number:::"))
opt=input("Enter option('+' '-' '*' '/' :::")

if(opt=='+'):
    print(add_nos(num1,num2))
elif(opt=='-'):
    print(sub_nos(num1,num2))
elif(opt=='*'):
    print(multiply_nos(num1,num2))
elif(opt=='/'):
    print(divide_nos(num1,num2))
else:
    print("Invalid Option")