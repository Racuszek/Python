from math import sqrt
class Wektor3D:
	def __init__(self, x=1, y=1, z=1):
		self.x=x
		self.y=y
		self.z=z
	def __str__(self):
		return '['+str(self.x)+', '+str(self.y)+', '+str(self.z)+']'
	def __add__(self, other):
		if isinstance(other, Wektor3D):
			return Wektor3D(self.x+other.x, self.y+other.y, self.z+other.z)
		else:
			return None
	__radd__=__add__
	def __sub__(self, other):
		if isinstance(other, Wektor3D):
			return Wektor3D(self.x-other.x, self.y-other.y, self.z-other.z)
		else:
			return None
	def __mul__(self, other):
		if isinstance(other, Wektor3D):
			skalar=self.x*other.y+self.y*other.y+self.z+other.z
			wektor=Wektor3D(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)
			return (skalar, wektor)
		elif isinstance(other, (float, int)):
			return Wektor3D(self.x*other, self.y*other, self.z*other)
		else:
			return None
	def len(self):
		return sqrt(self.x+self.y+self.z)
	def __eq__(self, other):
		if isinstance(other, Wektor3D):
			if self.x!=other.x or self.y!=other.y or self.z!=other.z:
				return False
			else:
				return True
		else:
			return None
