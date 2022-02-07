import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
##########################################################################
# city class
class City:
	def __init__(self, x, y):
		self.x = x
		self.y = y

##########################################################################
# solver class
class Solver:
	def __init__(self, cities, iterations):

		self.cities = cities

		self.solution = []
		self.solution_cost = 0

		self.temp = []
		self.temp_cost = 0

		self.best = []
		self.best_cost = 0
		self.best_time = 0;

		self.num_of_swaps = 1
		self.path_plot = None

		self.T = 0
		self.k = 0.5

		self.iterations = iterations

		self.cost_history = []
		self.time = []
		self.cost_plot = None
		##################################################################
		self.fig, self.ax = plt.subplots(2)

		self.create_path()
		self.plot_cities()
		self.plot_path()

	def create_path(self):
		self.solution = [*self.cities, self.cities[0]]
		self.compute_solution_cost()
		self.best = self.solution
		self.best_cost = self.solution_cost

	def update(self, frame, max_frames):
		self.time.append(frame)
		if(frame < (max_frames-1)):
			self.swap()
			self.compute_temp_cost()
			self.select(frame)
			self.update_path_plot(self.solution)
			self.cost_history.append(self.solution_cost)
		else:
			self.update_path_plot(self.best)
			self.cost_history.append(self.best_cost)
			self.plot_cost()

	def swap(self):
		self.temp = self.solution.copy()
		for i in range(self.num_of_swaps):
			idx = range(len(self.temp)-1)
			i1,i2 = random.sample(idx,2)
			self.temp[i1], self.temp[i2] = self.temp[i2], self.temp[i1]
		self.temp[-1] = self.temp[0]

	def compute_solution_cost(self):
		self.solution_cost = self.compute_cost(self.solution)

	def compute_temp_cost(self):
		self.temp_cost = self.compute_cost(self.temp)

	def compute_cost(self, path):
		cost = 0
		for i in range(len(path)-1):
			dx = path[i+1].x - path[i].x
			dy = path[i+1].y - path[i].y
			cost += (dx**2 + dy**2)**0.5
		return cost

	def compute_T(self,frame):
		self.T = frame*self.k + 0.000000000000000001

	def select(self,frame):
		self.compute_T(frame)
		if(self.temp_cost < self.solution_cost or np.random.rand() > math.exp((self.solution_cost-self.temp_cost)/self.T)):
			self.solution = self.temp
			self.solution_cost = self.temp_cost
		else:
			return

		if(self.solution_cost < self.best_cost):
			self.best = self.solution
			self.best_cost = self.solution_cost
			self.best_time = frame

	def update_path_plot(self, path):
		x_list = [city.x for city in path]
		y_list = [city.y for city in path]
		self.path_plot.set_data(x_list,y_list)

	def plot_cities(self):
		cities_x_list = [city.x for city in self.cities]
		cities_y_list = [city.y for city in self.cities]
		colors = [np.random.rand() for i in range(len(self.cities))]
		self.ax[0].scatter(cities_x_list, cities_y_list, s=100, c=colors, alpha = 0.8)

	def plot_path(self):
		solution_x_list = [city.x for city in self.solution]
		solution_y_list = [city.y for city in self.solution]
		self.path_plot, = self.ax[0].plot(solution_x_list,solution_y_list)

	def plot_cost(self):
		self.cost_plot, = self.ax[1].plot(self.time,self.cost_history,c='r')
		self.best_plot = self.ax[1].scatter([self.best_time],[self.best_cost],c='b')

	def init_animate(self):
		pass

	def animate(self):
		ani = animation.FuncAnimation(self.fig, self.update, init_func=self.init_animate, frames=self.iterations, interval=1, blit=False, repeat=False, fargs=(self.iterations,))
		plt.show()
##########################################################################
# create solver and initial list of cities
num_of_cities = 20
cities = [City(np.random.rand(),np.random.rand()) for i in range(num_of_cities)]

solver = Solver(cities,3000)
solver.animate()
##########################################################################