##Area of trinagle

import math
# l = int(input("enter the length of triangle:"));
# b = int(input("Enter the breadth of triangle:"));
# a=(1/2)*l*b;
# print("For given length",l," and breadth",b,":")
# print("The area of triangle is :",a)

##area with function

#le = int(input("enter the length of triangle:"));
# br = int(input("Enter the breadth of triangle:"));

# def area(l, b):
#     return (1 / 2) * l * b
#
# print(area(le,br))
# ##lambda function
#
# A =  lambda l , b: (1/2)*l*b
# print(A(le,br))


##area of triangle when sides are given

from math import *

print("enter the sides of triangle")

n1=int(input("enter the side1 of triangle:"));
n2=int(input("enter the side2 of triangle:"));
n3=int(input("enter the side3 of triangle:"));
p=n1+n2+n3
area =math.sqrt(p*(p-n1)*(p-n2)*(p-n3))
print("The area of triangle is :",area)


