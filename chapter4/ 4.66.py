# program to help in multiplication

import random

def generateNumber():
	number1 = random.randrange(0,10)
	number2 = random.randrange(0,10)
	product1 = number1 * number2

	st1 = str(number1)
	st2 = str(number2)

	print "How much is %s times %s" %(st1,st2)
	return product1


product = generateNumber()
answer = int(raw_input("Enter the answer:"))

passed = False;

while True:
	if passed:
		passed = False
		product = generateNumber()
		answer = int(raw_input("Enter the answer:"))

	while not passed:
		if product == answer :
			print "very good"
			passed = True

		else :
			print "NO, please try again"
			passed = False
			answer = int(raw_input("Enter the answer:"))

#while 1:
#	while product == answer :
#		print "very good"
#        product = generateNumber()
#       answer = int(raw_input("Enter the answer:"))

#	while product !):
#		print "NO, please try again"
#   	answer = int(raw_input("Enter the answer:"))


	
		
		


