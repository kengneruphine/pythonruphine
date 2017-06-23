# Program to create a dictionary of 20 random values
import random

emptydic = {}
for i in range (0,20):
	rand1 = random.randrange (1,100)
	dic = {i : rand1}
	emptydic.update(dic)
	

print emptydic
vals = emptydic.values() #return the values as a list

vals.sort()
print " Values are :"
print vals	

duplicate = False
for i in range (len(vals)-1):
	if vals[i] == vals[i + 1]:
		duplicate = True
	



if duplicate:
	print "duplicate values found"
else:
	print "No duplicates"

