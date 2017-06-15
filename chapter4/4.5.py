# program to determine whether a number is perfect

def perfect(n):
	sum= 0
	for i in range (1,(n/2 + 1)):
		if n % i==0:
			print "%d,is a factor of %d"%(i,n)
			sum += i
	

	if sum == n:
		print "\n"
		print "%d is perfect number" %n
	

	else:

		print '',


for i in range (1,30):
	print perfect(i)