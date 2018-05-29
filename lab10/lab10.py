#1
class Fibo:
	def __init__(self, n):
		self.a=0
		self.b=1
		self.c=0
		self.n=n
		self.i=0
	def __iter__(self):
		return self
	def __next__(self):
		if self.i>self.n:
			raise StopIteration
		self.i+=1
		if self.i==1:
			return 1
		self.c=self.a+self.b
		self.a=self.b
		self.b=self.c
		return self.c

iter1=Fibo(3)
# for i in iter1:
# 	for j in iter1:
# 		print(i, j)
# print('')

class Fibo2:
	def __init__(self, n):
		self.n=n
	def __iter__(self):
		return Fibo3(self.n)

class Fibo3:
	def __init__(self, n):
		self.a=0
		self.b=1
		self.c=0
		self.n=n
		self.i=0
	def __next__(self):
		if self.i>self.n:
			raise StopIteration
		self.i+=1
		if self.i==1:
			return 1
		self.c=self.a+self.b
		self.a=self.b
		self.b=self.c
		return self.c

# iter2=Fibo2(3)
# for i in iter2:
# 	for j in iter2:
# 		print(i, j)

#2
from scipy.misc import derivative
from math import sin
def foo(x):
#	return 2*pow(x, 3)+4*x+1
	return sin(x)-pow(.5*x, 2)
class Newton:
	def __init__(self, fun, eps, a):
		self.fun=fun
		self.eps=eps
		self.x=a
	def __iter__(self):
		return self
	def __next__(self):
		if abs(self.fun(self.x))<self.eps:
			raise StopIteration
		self.x=self.x-self.fun(self.x)/derivative(self.fun, self.x, 1e-5)
		return self.x
# iter3=Newton(foo, 1e-5, 1.5)
# for i in iter3:
# 	print(i)

#3
from random import random
class MyRandom:
	def __init__(self, n):
		self.x=1
		self.n=n
		self.i=0
	def __iter__(self):
		return self
	def __next__(self):
		if self.i>self.n:
			raise StopIteration
		self.i+=1
		self.x=((pow(7, 5)*self.x)%(pow(2, 30)-1))
		return self.x/(pow(2, 30)-1)

iter4=MyRandom(20000)
pairs1=[(next(iter4), next(iter4)) for i in range(10000)]
pairs2=[(random(), random()) for i in range(10000)]

for i in range(1, 11):
	print('{}. Kwadrat o boku {:.1f}'.format(i, .1*i))
	print('Iterator zaimplementowany:')
	a, b=0, len(pairs1)
	for j, k in pairs1:
		if j<.1*i and k<.1*i:
			a+=1
	print(a/b)

	print('Iterator wbudowany:')
	a, b=0, len(pairs2)
	for j, k in pairs2:
		if j<.1*i and k<.1*i:
			a+=1
	print(a/b)