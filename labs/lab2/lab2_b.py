import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

a= float (input("Enter a: "))
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

# Create figure and axels
fig, ax = plt.subplots()

#  Create ellipse center point (5, 5), width 10, height 5, angle 30 degrees
ellipse = Ellipse((h, k), width=2*a, height=2*b, angle=0, color='green')

#  Add ellipse to drawing area
ax.add_patch(ellipse)

#  set limits to exis
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

#  Define line 
#  linspace creates x values 
#  from selected range
x = np.linspace(h-3*a, h+3*a, 30)
#  Line's equation to get y values
y = m*x + c

#  Draw line

plt.plot(x, y, color='red')

#  Figure's title and axis titles
plt.title("Line and ellipse")
plt.xlabel("x")
plt.ylabel("y")
#  Show grid
plt.grid(True)

# Show figure
plt.show()
