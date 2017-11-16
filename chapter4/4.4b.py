# program to determine whether a number is prime
import math
def prime(n):
	if n >= 2:
		for i in range (2,n):
			if n % i == 0:
				return False
	else:
		return False
	return True

for i in range (1000):
	if prime(i):
		print i


