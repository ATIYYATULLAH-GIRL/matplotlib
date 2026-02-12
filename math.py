import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([0,6])
ypoints=np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()

x_points=np.array([5,45])
y_points=np.array([7,5])

plt.plot(x_points,y_points)
plt.show()

x_points=np.array([5,45,5,6,98])
y_points=np.array([7,5,12,34,6])

plt.plot(x_points,y_points)
plt.show()

x_point=np.array([5,45,4,7,90,3])
y_point=np.array([7,5,0,8,7,5])

plt.plot(x_point,y_point,"o")
plt.show()

y_points=np.array([7,5,12,34,6,5,9,0])

plt.plot(y_points, marker="o", ms=10, mec="r", linestyle="dotted")
plt.show()

y_points=np.array([7,5,12,34,6,5,9,0])

plt.plot(y_points, marker="o", ms=10, mec="r")
plt.show()

plt.plot(y_points, marker="o", ms=10, mec="r", linestyle="dashed")
plt.show()


plt.plot(y_points, marker="o", ms=10, mec="r", linestyle="dotted", color="g",linewidth="5")
plt.show()

# multiple plots
y1=np.array([3,9,90,6,7,8,9,0])
y2=np.array([15,5,5,6,4,8,9,2])

plt.plot(y1)
plt.plot(y2)
plt.title("Multiple Plots")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

x1=np.array(0,1,2,3,4,5)
y1=np.array([10,20,30,40,50,60])

plt.bar(x1,y1)
plt.show()