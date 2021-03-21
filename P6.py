#Write a program to read string and print each character separately.
str1=input("Enter the string")
for character in str1:
  print (character)
str1=input("Enter the string")
str2=str1[1:-1]
print ("str2=",str2)
print ("str1=",str1)
print ("str1*100 times=",str1*100)
str3=str1+" hello India"
print ("str3 =",str3)