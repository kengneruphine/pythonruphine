# using square root of n as the upper limit
from math import sqrt
def prime(n):
 	count = 0
 	for i in range(2,int(sqrt(n))+1):
 		if n % i == 0:
 			count += 1
 			break
 		
 	if count == 0 and n != 1:
 		return True
 		
for j in range (2,1000):
 	if prime(j):
 		print j
