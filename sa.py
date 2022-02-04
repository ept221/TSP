import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##########################################################################
# solver class
class Solver:
	def __init__(self):
		self.cities_x_list = []
		self.cities_list = []

		self.solution_x_list = []
		self.solution_y_list = []
		self.solution_cost = 0

		self.temp_x_list = []
		self.temp_y_list = []
		self.temp_cost = 0

		self.best_x_list = []
		self.best_y_list = []
		self.best_cost = 0

		self.num_of_swaps = 2
		self.path_plot = None

		self.T = 0
		self.k = 1

	def plot_cities(self, ax):
		colors = [np.random.rand() for i in range(len(self.cities_x_list))]
		ax.scatter(self.cities_x_list, self.cities_y_list, s=100, c=colors, alpha = 0.8)

	def plot_path(self, ax):
		self.path_plot, = ax.plot(self.solution_x_list,self.solution_y_list)

	def compute_cost(self,x_list,y_list):
		cost = 0
		for i in range(len(x_list)-1):
			dx = x_list[i+1] - x_list[i]
			dy = y_list[i+1] - y_list[i]
			cost += (dx**2 + dy**2)**0.5
		return cost

	def compute_solution_cost(self):
		self.solution_cost = self.compute_cost(self.solution_x_list,self.solution_y_list)

	def compute_temp_cost(self):
		self.temp_cost = self.compute_cost(self.temp_x_list,self.temp_y_list)

	def create_path(self):
		self.solution_x_list = [*self.cities_x_list, self.cities_x_list[0]]
		self.solution_y_list = [*self.cities_y_list, self.cities_y_list[0]]
		self.compute_solution_cost()

		self.best_x_list = self.solution_x_list
		self.best_y_list = self.solution_y_list
		self.best_cost = self.solution_cost

	def swap(self):
		temp = list(zip(self.solution_x_list,self.solution_y_list))
		for i in range(self.num_of_swaps):
			idx = range(len(temp)-1)
			i1,i2 = random.sample(idx,2)
			temp[i1], temp[i2] = temp[i2], temp[i1]
		temp[-1] = temp[0]
		self.temp_x_list, self.temp_y_list = zip(*temp)


	def select(self,frame):
		self.T = frame*self.k + 0.000000000000000001
		if(self.temp_cost < self.solution_cost or np.random.rand() > math.exp((self.solution_cost-self.temp_cost)/self.T)):
			self.solution_x_list = self.temp_x_list
			self.solution_y_list = self.temp_y_list
			self.solution_cost = self.temp_cost

		if(self.solution_cost < self.best_cost):
			self.best_x_list = self.solution_x_list
			self.best_y_list = self.solution_y_list
			self.best_cost = self.solution_cost

	def update_path_plot(self):
		self.path_plot.set_data(self.solution_x_list,self.solution_y_list)
		print("current cost: \t" + str(self.solution_cost))

	def plot_best_path(self):
		self.path_plot.set_data(self.best_x_list,self.best_y_list)
		print("best cost: \t" + str(self.best_cost))
##########################################################################
# create solver and initial list of cities
num_of_cities = 20
solver = Solver()
solver.cities_x_list = [np.random.rand() for i in range(num_of_cities)]
solver.cities_y_list = [np.random.rand() for i in range(num_of_cities)]
##########################################################################
# create the initial plot
fig, ax = plt.subplots()
solver.create_path()
solver.plot_cities(ax)
solver.plot_path(ax)
##########################################################################
# animation update function
def update(frame, max_frames, solver):
	if(frame < (max_frames-1)):
		solver.swap()
		solver.compute_temp_cost()
		solver.select(frame)
		solver.update_path_plot()
	else:
		solver.plot_best_path()
		
	return

##########################################################################
# animate
count = 100000
ani = animation.FuncAnimation(fig, update, frames=count, interval=1, blit=False, repeat=False, fargs=(count,solver))
plt.show()
##########################################################################