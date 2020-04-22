#Mason Hamilton & Dylan Nasser
#CST-305-3:20
#Professor Ricardo Citro
#4/19/2020
#Project 7 Part 1
#Our grouped worked with Tanner Williams and Jared group

#Import libraries used below
import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import



#Main defination used to create chaotic model
def Lorenz(x, y, z, t, r, b):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       t, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    Xdot = t * (y - x)
    Ydot = r * x - y - x * z
    Zdot = x * y - b * z
    return Xdot, Ydot, Zdot


dt = 0.01
count = 10000

# Need one more for the initial values

xs = np.empty(count + 1)
ys = np.empty(count + 1)
zs = np.empty(count + 1)

#gets the users inputs for xyz
print("\nx, y, z: are points of interest in three dimensional space")
xInput = input("Enter x, y, z, values: ")
yInput = input()
zInput = input()
#changeing the input into int variables
xIn = int(xInput)
yIn = int(yInput)
zIn = int(zInput)
#assigng the xyz starting values
xs[0], ys[0], zs[0] = (xIn, yIn, zIn)

#getting the users input for t, r, b
print("t, r, b: Are parameters defining the lorenz attractor")
tInput = input("Enter t, r, b, values: ")
rInput = input()
bInput = input()
#changes the inputs into int variables
tIn = float(xInput)
rIn = float(yInput)
bIn = float(zInput)

#xs[0], ys[0], zs[0] = (xIn, yIn, zIn)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(count):
    Xdot, Ydot, Zdot = Lorenz(xs[i], ys[i], zs[i], tIn, rIn, bIn)
    xs[i + 1] = xs[i] + (Xdot * dt)
    ys[i + 1] = ys[i] + (Ydot * dt)
    zs[i + 1] = zs[i] + (Zdot * dt)

# Plotting the figure and calling the above functions
fig = plt.figure()
#setting the projection to 3d
np = fig.gca(projection='3d')
#plotting the x,y,z values with a 0.4 line width
np.plot(xs, ys, zs, lw=0.4)
#x, y, z labels
np.set_xlabel("X-Axis")
np.set_ylabel("Y-Axis")
np.set_zlabel("Z-Axis")
#tittle name
np.set_title("Lorenz Model")
#finally plot fucnion
plt.show()

