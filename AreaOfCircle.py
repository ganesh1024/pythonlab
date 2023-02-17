##Area of Circle
pi = 3.14;
rad=int(input("enter the radii  of circle:"));
Area = pi*rad**2;
print("Area of the Circle:",Area)

def area(rad):
    return pi*rad**2;

print(area(rad));

Areac = lambda r: pi*rad**2
print(Areac(rad))