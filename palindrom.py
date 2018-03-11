#!/usr/bin/env python3.5
import math
from sys import argv
import random

def isPal(a):
	s=str(a)
	for i in range(int(math.floor(len(s)/2))):
		if s[i]!=s[len(s)-i-1]:
			return False
	return True

dict={}
for i in range(100):
	key=random.randint(100, 10000)
	dict[key]=isPal(key)

print(dict)
