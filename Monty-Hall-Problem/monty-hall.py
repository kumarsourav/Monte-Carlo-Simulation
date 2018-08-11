import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Monty_hall:
	#init monty hall problem with 3 doors
	def __init__(self, total_doors = 3, prize = 0, mydoor = 0):
		self.total_doors = total_doors
		self.doors = [i for i in range(1, total_doors+1)]
		self.prize = prize
		self.mydoor = mydoor

	def remove(self, x):
		try:
			self.doors.remove(x)
		except ValueError:
			pass

	def setPrize(self):
		#randomly select a door to setup prize behind it
		self.prize = np.random.randint(1, (self.total_doors+1))
		
	def setMyDoor(self):
		#randomly select a door as your initial choice
		self.mydoor = np.random.randint(1, (self.total_doors+1))
		#remove that door from the list so that remaining two doors
		#can be used by monty hall 
		self.remove(self.mydoor)
		
	def getData(self):
		return self.prize, self.mydoor
		
	def selDoor(self):
		while True:
			#let monty hall select a door randomly and open it.
			door = np.random.choice(self.doors)
			#selected door must not contain the prize
			if door != self.prize:
				break
		#remove this door from list		
		self.remove(door)
		return door

	def switchDoor(self):
		#if you select to switch door, this is the door you get
		return self.doors
def simulate():
	#Total number of times you are going to play
	total_plays = 3000
	#Total number of doors
	total_doors = 3
	#Total number of times you won when you selected to switch
	win_switch = 0
	#Total number of times you won when you selected to stick with initial choice
	win_fix = 0
	for i in range (1, total_plays):
		mh = Monty_hall(total_doors)
		mh.setPrize()
		mh.setMyDoor()
		prize, mydoor = mh.getData()
		monty_choice = mh.selDoor()
		if mydoor == prize:
			win_fix += 1
		newdoor, = mh.switchDoor()
		if newdoor == prize:
			win_switch += 1
		yield i, win_fix,  win_switch

#Animate the simulation 		
def init():
	ax.set_ylim(0.0, 1.0)
	ax.set_yticks(np.arange(0, 1, step = 0.1))
	ax.set_ylabel('Proportion of wins') 
	ax.set_xlim(0,100)
	ax.set_xlabel('Total number of plays')
	ax.axhline(2/3, linestyle = '--', color = 'green', label = 'Switch wins Theoretical probability')
	ax.axhline(1/3, linestyle = '--', color = 'brown', label = 'Fixed Wins Theoretical probability')
	ax.legend(fontsize='x-small')
	del xdata[:]
	del ydata1[:]
	del ydata2[:]
	line1.set_data(xdata, ydata1)
	line2.set_data(xdata, ydata2)
	return line1, line2

def run(data):
	x, fix, switch = data
	xdata.append(x)
	ydata1.append(switch/x)
	ydata2.append(fix/x)
	xmin, xmax = ax.get_xlim()
	if x >= xmax:
		ax.set_xlim(xmin, 2*xmax)
		ax.figure.canvas.draw()
	line1.set_data(xdata, ydata1)
	line2.set_data(xdata, ydata2)
	return line1, line2

if __name__ == "__main__":
	fig, ax = plt.subplots()
	line1, = ax.plot([], [], lw=1, label='switch wins')
	line2, = ax.plot([], [], lw=1, label='fixed wins')
	xdata, ydata1, ydata2 = [], [], []
#start animaton	
	ani = animation.FuncAnimation(fig, run, simulate, blit=False, interval=10,
					repeat=False, init_func=init, save_count = 300)
	plt.show()
