import matplotlib.pyplot as plt
import numpy as np

print ("lets find, if exists, the junction points of two parabola as y= ax^2 + bx + c")
print ("To start, you will enter the coeffients of the first parabola")
a = float (input("a : "))
b = float (input("b : "))
c = float (input("c : "))

print ("Then, you will enter the coeffients of the second parabola")
d = float (input("d : "))
e = float (input("e : "))
f = float (input("f : "))

r = (b-e)**2 -4*(a-d)*(c-f)

if r > 0:
    x_1 = ((e-b) + np.sqrt(r))/(2*(a-d))
    x_2 = ((e-b) - np.sqrt(r))/(2*(a-d))
    print ("there are two junction points")
    print ("the roots: ", x_1, x_2)
    
elif r == 0:
    x_1 = ((e-b) + np.sqrt(r))/(2*(a-d))
    print ("these parabolas are tangent at x =", x_1)
    
else:
    print ("the parabolas are not intersect")

x_1 = np.linspace(-10,10)
y_1 = a*(x_1**2) + b*x_1 + c

x_3 = np.linspace (-10,10)
y_3 = d*(x_3**2) + e*x_3 + f

plt.plot (x_1, y_1)
plt.plot (x_3, y_3)
plt.grid ()
plt.show()
