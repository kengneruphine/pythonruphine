# program to implement the sieve of Eratosthenes to generate prime numbers
def sieve(n):
	not_prime = []
	prime = []
	for i in range (2,n+1):
		if i not in not_prime:
			prime.append(i)
			for j in range (i*i, n+1,i):   # loop to remove multiple of the not_prime numbers
				not_prime.append(j)
	return prime	
	

print sieve(1000)		