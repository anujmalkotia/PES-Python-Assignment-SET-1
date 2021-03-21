'''Create a list of 5 names and check given name exist in the List.
        a) Use membership operator (IN) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.
'''

#a) Use membership operator ( IN ) to check the presence of an element.
list1=['Sahil','Dushyant','Nikhil','Aayush','Rohan']
#print list1
if ('Ravi') in list1:
  print ("Ravi is present in the list")
else:
  print ("Ravi is not present in the list")

#b) Perform above task without using membership operator.
for i in list1:
  if (i=='Ravi'):
    print ("Ravi is present in the list")
    break
else:
    print ("Ravi is not present in the list")

#c) Print the elements of the list in reverse direction.
list1.reverse()
print ("the elements of list1 in reverse direction are",list1)