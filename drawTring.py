import numpy as np
import mpl_toolkits.axisartist as ast
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

date = np.linspace(-10,10,100)
x,y = np.meshgrid(date,date)
z = x**2+y**2-x*y
fig = plt.figure
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z,rstride=4,cstride=4)
plt.title("3Dpicture")
plt.show()
