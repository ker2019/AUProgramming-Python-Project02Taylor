#!/usr/local/bin/python3.6

#to create range
import numpy
#to build and show plot sin(x)
import matplotlib.pyplot as pyplot

#calculate sin(x) with precision d
def _sin(x, d):
	#partial sum of Taylor row
	sum=0
	#common member of row
	item=x
	#number of member
	n = 1
	#up approximation of precision
	while item*n >= d*(n - x) or item*n <= -d*(n - x):
		sum += item
		#member with number (n + 1) is zero
		n += 2
		item = -item * x * x
		item = (item / n) / (n - 1)
	return sum
	
#calculate sin with precision 0.001
def sin(x):
	return _sin(x, 0.001)

#calculate exp(x) with precision d
def _exp(x, d):
	#partial sum of Taylor row
	sum=0
	#common member of row
	item=1
	#number of member
	n = 0
	#up approximation of precision
	while item*n >= d*(n - x) or item*n <= -d*(n - x):
		sum += item
		n += 1
		item = item * x
		item = item / n
	return sum
	
#calculate exp with precision 0.001
def exp(x):
	return _exp(x, 0.001)

#do if only this module is main
if __name__=='__main__':
	#range {0;0.1;0.2;...;10}
	args = numpy.r_[0:10:0.1]
	pyplot.plot(
		args,
		[sin(x) for x in args],
	)
	pyplot.show()
	
	args = numpy.r_[-5:5:0.1]
	pyplot.plot(
		args,
		[exp(x) for x in args],
	)
	pyplot.show()
