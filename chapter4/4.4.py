# program to print prime numbers
def prime(n):
 	count = 0
 	for i in range(2,n/2):
 		if n % i == 0:
 			count += 1
 			break
 		
 	if count == 0 and n != 1:
 		return True
 		
for j in range (2,1001):
 	if prime(j):
 		print j
