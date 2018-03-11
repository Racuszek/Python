#!usr/bin/env python3.5
from sys import argv
from sys import exit
from copy import deepcopy
if len(argv)==1:
	print("Prosze podac argumenty!")
	exit()
else:
	s=''.join(argv[1:])
	print(s)
lower=[x for x in s if x.islower()]
upper=[x for x in s if x.isupper()]
digits=[x for x in s if x.isdigit()]
notchar=[x for x in s if not x.isalpha()]

print(lower)
print(upper)
print(digits)
print(notchar)

unique_lower=[]
for x in lower:
	if x not in unique_lower:
		unique_lower.append(x)
	
tuples=[(x, lower.count(x)) for x in unique_lower]
print(tuples)

tuples.sort(key=lambda x: x[1])
print(tuples)

vowel_str='aeiouyAEIOUY'
vows=sum(1 for x in s if x in vowel_str)
cons=len(upper)+len(lower)-vows
param_str=[(float(x), vows*float(x)+cons) for x in digits]
print(param_str)

meanx=float(sum(x for x, y in param_str))/len(param_str)
meany=float(sum(y for x, y in param_str))/len(param_str)
d=sum((param_str[x][0]-meanx)**2 for x in range(len(param_str)))
print(d)
a=(1/d)*sum(y*(x-meanx) for x, y in param_str)
b=meany-a*meanx
print(a, b)