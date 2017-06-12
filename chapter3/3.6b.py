# program to the value of e
from __future__ import division
fact = 1
e = 1.0

for i in range (1,11):
	number = i
	fact = 1
	while number != 0:
		fact = fact * number
		number = number - 1

	print "factorial of %d is %d " %(i,fact)
	fac =float(1/fact)
	e = e + fac

print e
	

	