'''Write a program to find the biggest of 4 numbers.
   a) Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
(PS: Use IF and IF & Else, If and ELIf, and Nested IF)
'''

a=int(input("Enter number 1:::"))
b=int(input("Enter number 2:::"))
c=int(input("Enter number 3:::"))
d=int(input("Enter number 4:::"))

greatest=0
if (a>b)&(a>c)&(a>d):
    print("the greatest no of the first 4 is",a)
    greatest=a
elif (b>a)&(b>c)&(b>d):
    print("the greatest no of the first 4 is",b)
    greatest=b
elif (c>a)&(c>b)&(c>d):
    print("the greatest no of the first 4 is",c)
    greatest=c
else:
    print("the greatest no of the first 4 is",d)
    greatest=d
e=int(input("Enter 5th number"))

if(e>greatest):
    print(" The biggest of all 5 nos is",e)