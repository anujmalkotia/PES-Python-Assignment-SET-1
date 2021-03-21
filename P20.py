'''
Write a program to generate a Fibonacci series of numbers.
Starting numbers are 0 and 1,  new number in the series is generated by adding previous two numbers in the series.
Example : 0, 1, 1, 2, 3, 5, 8,13,21,.....
   a) Number of elements printed in the series should be N numbers, Where N is any +ve integer.
   b) Generate the series until the element in the series is less than Max number.

'''

nterms=int(input("Enter the no of terms"))
a=0
b=1
if nterms<=0:
  print("please enter positive number")
elif nterms==1:
  print("Fibonacci series:",a)
elif nterms==2:
  print (a)
  print (b)
else:
  print (a)
  print (b)
  while(nterms>2):
    numnext=a+b
    print (numnext)
    a=b
    b=numnext
    nterms=nterms-1