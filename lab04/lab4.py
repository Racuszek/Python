from time import time
from sys import version
import random
from functools import reduce
from math import sqrt
from operator import add

#1 OK
powt=1000
N=10000
		
def tester(foo):
	t1=time()
	for i in range(powt):
		foo()
	t2=time()
	return t2-t1

def forStatement():
	my_list=[]
	for i in range(N):
		#my_list.append(i)
		my_list.append(i**2)

def listComprehension():
	#my_list=[i for i in range(N)]
	my_list=[i**2 for i in range(N)]

def mapFunction():
	#my_list=list(map(my_list.append, range(N)))
	my_list=map(lambda x: x**2, range(N))

def generatorExpression():
	#my_list=list((i for i in range(N)))
	my_list=(i**2 for i in range(N))
'''
print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
	print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
'''
#2 OK
def integral(f, a, b, steps):
	step=(b-a)/steps
	return (sum(map(f, (a+i*step for i in range(1, steps))))+(f(a)+f(b))*0.5)*step

#print(integral(lambda x: 3*x+1, 2, 4, 20))

#3 OK
def pi(num):
	return 4*len(list(filter(lambda x: x[0]**2+x[1]**2<1, ((random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(num)))))/num
	pass

#print(pi(1000000))

#5
def stats(xList, yList):
	meanX=sum(xList)/len(xList)
	meanY=sum(yList)/len(yList)
	d=reduce(add, map(lambda x: (x-meanX)**2, xList))
	a=(1/d)*sum(map(lambda x, y: y*(x-meanX), xList, yList))
	b=meanY-a*meanX
	deltaY=sqrt(sum(map(lambda x, y: (y-a*x+b)**2, xList, yList))/(len(xList)-2))
	deltaA=deltaY/sqrt(d)
	deltaB=deltaY*sqrt(1/len(xList)+meanX**2/d)
	return a, b, deltaA, deltaB


listA=[1, 2, 3, 4]
listB=[3, 5, 7, 9]
print(stats(listA, listB))

#4
s=4
matrix1=[[random.randint(0, 6) for i in range(s)] for j in range(s)]
matrix2=[[random.randint(0, 6) for i in range(s)] for j in range(s)]

print(matrix1)
print(matrix2)
print([reduce(max, i) for i in matrix1])
print([reduce(max, i) for i in zip(*matrix1)])
print([[matrix1[i][j]+matrix2[i][j] for j in range(4)] for i in range(4)])


