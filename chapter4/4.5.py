# program to determine whether a number is perfect

def perfect(n):
	sum= 0

	for i in range (1,n):
		if n % i==0:
			sum += i
			continue
	

	if sum == n:
		print "%d is perfect number" %n
	


for i in range (1,1001):
	 perfect(i)