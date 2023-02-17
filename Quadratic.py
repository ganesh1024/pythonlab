import math as m

print("Quadratic equation: a*(x**2)+b*x+c")
a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('Enter c:'))

d=m.sqrt((b**2)-(4*a*c));
d=float(d)
if d >0 :
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print("The roots are:")
    print("root1 ,root2 :",r1,r2)

elif d==0:
    r1=(-b)/(2*a)
    r2=(-b)/(2*a)
    print("The roots are:")
    print("root1 ,root2 :", r1, r2)
else:
    print('the roots are imaginary !!!')


