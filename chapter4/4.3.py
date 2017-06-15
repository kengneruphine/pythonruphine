# program to implement a fahrenheit function
from __future__ import division

fahr = 0
def fahrenheit(x):
	temp = (9 * x) / 5 + 32
	return temp


print "celcius %14s" % "fahr"
for i in range (0,101):
	fahr = fahrenheit (i)
	print "%7d %14.1f" %(i,fahr)
