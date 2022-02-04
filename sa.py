import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##########################################################################
# city class
class City:

	def __init__(self):
		self.x = np.random.rand()
		self.y = np.random.rand()
		self.size = 100
		self.color = np.random.rand()

##########################################################################
# create list of cities
num_of_cities = 10
cities = [City() for i in range(num_of_cities)]
##########################################################################
# create the initial plot
x_list = [city.x for city in cities]
y_list = [city.y for city in cities]
size_list = [city.size for city in cities]
color_list = [city.color for city in cities]

fig, ax = plt.subplots()
scatter = ax.scatter(x_list, y_list, s=size_list, c=color_list, alpha=0.8)

x_path = [*x_list,x_list[0]]
y_path = [*y_list,y_list[0]]
path, = ax.plot(x_path,y_path)
##########################################################################
# animation update function
smallest  = 100
def update(frame, cities):

	global smallest

	temp = cities

	idx = range(len(temp))
	i1,i2 = random.sample(idx, 2)
	temp[i1], temp[i2] = temp[i2], temp[i1]

	x_list = [city.x for city in temp]
	y_list = [city.y for city in temp]

	x_path = [*x_list,x_list[0]]
	y_path = [*y_list,y_list[0]]

	##################################################
	# calculate cost
	distance = 0
	for i in range(len(temp)-1):
		distance += (((temp[i].x - temp[i+1].x)**2 + (temp[i].y - temp[i+1].y)**2)**0.5)
	distance += (((temp[0].x - temp[-1].x)**2 + (temp[0].y - temp[-1].y)**2)**0.5)
	#print(distance)
	##################################################

	T = 1/(0.1*frame + 0.0001)
	print("Temp = " + str(T))
	if(distance > smallest and (np.random.rand() < math.exp(smallest - distance)/T)):
		return
	smallest = distance
	cities = temp

	path.set_data(x_path,y_path)
	return

##########################################################################
# animate
ani = animation.FuncAnimation(fig, update, frames=10000, interval=1, blit=False, repeat=False, fargs=(cities,))
plt.show()
##########################################################################