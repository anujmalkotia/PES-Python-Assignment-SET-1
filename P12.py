#Read 10 numbers from user and find the average of all.

a=int(input("Enter number 1:::"))
b=int(input("Enter number 2:::"))
c=int(input("Enter number 3:::"))
d=int(input("Enter number 4:::"))
e=int(input("Enter number 5:::"))
f=int(input("Enter number 6:::"))
g=int(input("Enter number 7:::"))
h=int(input("Enter number 8:::"))
i=int(input("Enter number 9:::"))
j=int(input("Enter number 10:::"))


avg = (a + b + c + d + e + f + g + h + i + j) / 10
countBig = 0
countSmall = 0
countEqual = 0
print
"Average of the 10 nos is =", avg
print
"Numbers smaller than the Average are below:"
if a < avg:
    print ("a=", a)
    countSmall += 1
elif a > avg:
    # print "a=",a, "is bigger than avg=",avg
    countBig += 1
else:
    # print "a=",a, "is equal to avg=",avg
    countEqual += 1

if b < avg:
    print ("b=", b)
    countSmall += 1
elif b > avg:
    # print "b=",b, "is bigger than avg=",avg
    countBig += 1
else:
    # print "b=",b, "is equal to avg=",avg
    countEqual += 1

if c < avg:
    print ("c=", c)
    countSmall += 1
elif c > avg:
    # print "c=",c, "is bigger than avg=",avg
    countBig += 1
else:
    # print "c=",c, "is equal to avg=",avg
    countEqual += 1

if d < avg:
    print ("d=", d)
    countSmall += 1
elif d > avg:
    # print "d=",d, "is bigger than avg=",avg
    countBig += 1
else:
    # print "d=",d, "is equal to avg=",avg
    countEqual += 1

if e < avg:
    print ("e=", e)
    countSmall += 1
elif e > avg:
    # print "e=",e, "is bigger than avg=",avg
    countBig += 1
else:
    # print "e=",e, "is equal to avg=",avg
    countEqual += 1

if f < avg:
    print ("f=", f)
    countSmall += 1
elif f > avg:
    # print "f=",f, "is bigger than avg=",avg
    countBig += 1
else:
    # print "f=",f, "is equal to avg=",avg
    countEqual += 1

if g < avg:
    print ("g=", g)
    countSmall += 1
elif g > avg:
    # print "g=",g, "is bigger than avg=",avg
    countBig += 1
else:
    # print "g=",g, "is equal to avg=",avg
    countEqual += 1

if h < avg:
    print ("h=", h)
    countSmall += 1
elif h > avg:
    # print "h=",h, "is bigger than avg=",avg
    countBig += 1
else:
    # print "h=",h, "is equal to avg=",avg
    countEqual += 1

if i < avg:
    print ("i=", i)
    countSmall += 1
elif i > avg:
    # print "i=",i, "is bigger than avg=",avg
    countBig += 1
else:
    # print "i=",i, "is equal to avg=",avg
    countEqual += 1

if j < avg:
    print ("j=", j)
    countSmall += 1
elif j > avg:
    # print "j=",j, "is bigger than avg=",avg
    countBig += 1
else:
    # print "j=",j, "is equal to avg=",avg
    countEqual += 1
print ("the total count of nos bigger than average is ", countBig)
print ("the total count of nos smaller than average is=", countSmall)
print ("the total count of nos equal to the average is=", countEqual)