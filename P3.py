#Write a program to find given number is odd or Even

def odd_even(a):
    if(a%2==0):
        print(a,'is Even')
    else:
        print(a,'is Odd')

num = int(input("Enter Number:::"))

odd_even(num)