#Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.

import math
a = 10
b = 20
c = a & b;
print ("Value of c (a&b) is ", c)
c = a | b;
print ("Value of c (a|b) is ", c)
c = a ^ b;
print ("Value of c (a^b) is ", c)
c = ~a;
print ("Value of c (~a) is ", c)
c = a << 2;
print ("Value of c (a<<2) is ", c)
c = a >> 2;
print ("Value of c (a>>2) is ", c)