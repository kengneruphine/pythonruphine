# program to determine the sides right angle triangle
# k=hypothenuse , j= side1, i=sides2

for k in range (1,20,1):
	for j in range (1,20,1):
		for i in range (1,20,1):
			if k**2 == j**2 + i**2:
				print "pythagorean triples are %d,%d,%d" %(k,j,i)
