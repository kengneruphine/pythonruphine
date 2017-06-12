#program to calculate e^x, 
from __future__ import division
fact = 1
e = 1.0
x = 2 # let x =2

for i in range (1,11):
	number = i
	fact = 1
	while number != 0:
		fact = fact * number
		number = number - 1


	fac = float(2**i/fact)
	e = e + fac
	print "factorial of %d is %d " %(i,fact)


print e