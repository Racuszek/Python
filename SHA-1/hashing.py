from sys import argv
from time import time
from functools import reduce
string=' '.join(argv[1:])
h0='01100111010001010010001100000001'
h1='11101111110011011010101110001001'
h2='10011000101110101101110011111110'
h3='00010000001100100101010001110110'
h4='11000011110100101110000111110000'

def rotate(input, d):
    first = input[0:d]
    second = input[d:]
    return second+first

bList=[format(ord(char), 'b') for char in string]
binList=list(map(lambda s: '0'*(8-len(s))+s, bList))
msg=''.join(binList)
binString=msg+'1'
while len(binString)%512!=448:
	binString+='0'
lenStr=format(len(msg), 'b')
lenStr=(64-len(lenStr))*'0'+lenStr
binString+=lenStr
chunksList=[binString[i:i+512] for i in range(0, len(binString), 512)]

chunksList=[[chunk[i:i+32] for i in range(0, len(chunk), 32)] for chunk in chunksList]

def xor(str1, str2):
	w1=[0 if c=='0' else 1 for c in str1]
	w2=[0 if c=='0' else 1 for c in str2]
	return ''.join([str(i^j) for i, j in zip(w1, w2)])

def OR(str1, str2):
	w1=[0 if c=='0' else 1 for c in str1]
	w2=[0 if c=='0' else 1 for c in str2]
	return ''.join([str(i|j) for i, j in zip(w1, w2)])

def AND(str1, str2):
	w1=[0 if c=='0' else 1 for c in str1]
	w2=[0 if c=='0' else 1 for c in str2]
	return ''.join([str(i&j) for i, j in zip(w1, w2)])

def NOT(str1):
	w1=[1 if c=='0' else 0 for c in str1]
	return ''.join([str(w) for w in w1])
	
i=16
for chunk in chunksList:
	while i<80:
		words=[chunk[i-3], chunk[i-8], chunk[i-14], chunk[i-16]]
		#--------- XOR -----------
		res=reduce(xor, words)
		#------ rotate left ------
		res=rotate(res, 1)
		chunk.append(res)
		i+=1

A, B, C, D, E=h0, h1, h2, h3, h4
def foo1():
	global F
	F=OR(AND(B, C), AND(NOT(B), D))
	global K
	K='01011010100000100111100110011001'
def foo2():
	global F
	F=reduce(xor, [B, C, D])
	global K
	K='01101110110110011110101110100001'

def foo3():
	global F
	F=OR(OR(AND(B, C), AND(B, D)), AND(C, D))
	global K
	K='10001111000110111011110011011100'
def foo4():
	global F
	F=reduce(xor, [B, C, D])
	global K
	K='11001010011000101100000111010110'
#---------- The main loop -------------
def binAdd(str1, str2):
	return format(int(str1, 2)+int(str2, 2), 'b')

funList=[foo1, foo2, foo3, foo4]

for chunk in chunksList:
	for i in range(4):
		for word in chunk[(20*i):(20+20*i)]:
			funList[i]()
			temp=(reduce(binAdd, [rotate(A, 5), F, E, K, word]))
			temp=temp[-32:]
			while len(temp)<32:
				temp=''.join(['0', temp])
			A, B, C, D, E=temp, A, rotate(B, 30), C, D

h0=binAdd(h0, A)
h1=binAdd(h1, B)
h2=binAdd(h2, C)
h3=binAdd(h3, D)
h4=binAdd(h4, E)
hexList=[]
for var in [h0, h1, h2, h3, h4]:
	while len(var)<32:
		var=''.join(['0', var])
	var=var[-32:]
	hexList.append(hex(int(var, 2))[2:])
print(''.join(hexList))