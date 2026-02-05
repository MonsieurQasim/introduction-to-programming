import math

a= float (impput("Enter a: "))
b= float (input("Enter b: "))
h= float (input("Enter h: "))
k= float (input("Enter k: "))
m= float (input("Enter m: "))
c= float (input("Enter c: "))

A=b**2+a**2*m**2
B=-2*h*b**2+2*a**2*m*(c-k)
C=b**2*h**2+a**2*(c-k)**2-a**2*b**2

D=B**2-4*A*C

if D>0:
    print("Two intersection points")

elif D==0:
    print("One intersection point")

else:
    print("No intersection points")

