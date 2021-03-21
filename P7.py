'''Create a list with at least 10 elements having integer values in it;
       Print all elements
       Perform slicing operations
       Perform repetition with * operator
       Perform concatenation with other list.
'''

str1=input("Enter the list1")
list1=list(str1)
print ("list1=",list1)
list2=list(input("Enter list2 elements"))
print ("list2=",list2)
print ("list1[1:3]=",list1[1:3])
print ("list2[3:-3]=",list2[3:-3])
print ("list1*2=",list1*2)
print ("list1+list2=",list1+list2)