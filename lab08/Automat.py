from copy import deepcopy
class Automat:
	def __init__(self, size, begin, iters):
		self.size=size
		self.begin=begin
		self.iters=iters
		self.cells=[[0]*size for j in range(size)]
		for i in range(size//2-begin//2, size//2+begin//2+1):
			for j in range(size//2-begin//2, size//2+begin//2+1):
				self.cells[i][j]=1

	def printState(self):
		for line in self.cells:
			for val in line:
				if val:
					print('o', end=' ')
				else:
					print('-', end=' ')
			print('\n')

	def howManyNbs(self, x, y):
		self.aliveNbs=0
		for line in range(x-1, x+2):
			for row in range(y-1, y+2):
				if not (line==x and row==y):
					self.aliveNbs+=self.cells[(line+self.size)%self.size][(row+self.size)%self.size]
					#print(self.aliveNbs)

		return self.aliveNbs
	
	def evolve(self):
		new=[[0 for i in range(self.size)] for j in range(self.size)]
		for iteration in range(self.iters):
			new=deepcopy(self.cells)
			self.printState()
			print('\n')
			for i in range(self.size):
				for j in range(self.size):
					if self.cells[i][j]==0 and self.howManyNbs(i, j)==3:
						new[i][j]=1
					if self.cells[i][j]==1 and (self.howManyNbs(i, j)>3 or self.howManyNbs(i, j)<2):
						new[i][j]=0
			self.cells=deepcopy(new)

	def nbsTest(self):
		self.printState()
		for i in range(self.size):
			for j in range(self.size):
				print('komorka {}x{}, alive nbs: {}'.format(i, j, self.howManyNbs(i, j)))


