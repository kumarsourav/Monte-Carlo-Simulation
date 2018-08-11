import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#coin bias
bias = 0.5
class Coin:
	def __init__(self, pheads = 0.5):
		self.pheads = pheads
		self.ptails = 1 - pheads
		# 0 -  Heads 1 - Tails
		self.sides = [0, 1]

	def toss(self):
		#select between 0(heads) and 1(tails) with respective probabilities in
		#list p
		result = np.random.choice(self.sides, p=[self.pheads, self.ptails])
		return result

def simulate():
	total_tosses = 1000
	total_heads = 0
	total_tails = 0
	#create coin with bias
	coin = Coin(bias)
	
	for i in range(1, 1000):
		#toss the coin
		result = coin.toss()
		if result == 0:
			total_heads += 1
		else:
			total_tails += 1
		yield i, total_heads

#Animate the simulation
def init():
	ax.set_ylim(0.0, 1.0)
	ax.set_yticks(np.arange(0, 1, step = 0.1))
	ax.set_ylabel('Proportion of Heads')
	ax.set_xlim(0, 100)
	ax.set_xlabel('Total number of Toss')
	ax.axhline(bias, linestyle = '--', color = 'green', label = 'Heads Theoretical Probability')
	ax.legend(fontsize = 'x-small')
	del xdata[:]
	del ydata[:]
	line.set_data(xdata, ydata)
	return line

def run(data):
	x, y = data
	xdata.append(x)
	ydata.append(y/x)
	xmin, xmax = ax.get_xlim()
	if x >= xmax:
		ax.set_xlim(xmin, 2*xmax)
		ax.figure.canvas.draw()
	line.set_data(xdata, ydata)
	return line
	
if __name__ == "__main__":
	try:
		bias = float(input('Press Enter for default(0.5)\nEnter probability of Heads between 0 and 1:\n'))
	except ValueError:
		print('setting default: 0.5')
		bias = 0.5
	fig, ax = plt.subplots()
	line, = ax.plot([], [], lw=1, label='Heads')
	xdata, ydata = [], []

	ani = animation.FuncAnimation(fig, run, simulate, blit=False, interval=10,
					repeat=False, init_func=init, save_count=500)
	plt.show()
