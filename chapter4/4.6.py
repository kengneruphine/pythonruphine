import random

def generateNumber():
	number1 = random.randrange(0,10)
	number2 = random.randrange(0,10)
	product1 = number1 * number2

	st1 = str(number1)
	st2 = str(number2)

	print "How much is %s times %s" %(st1,st2)
	return product1


while True:
	product = generateNumber()	

	answer = int(raw_input("Enter the answer:"))
	if answer == product:
		print "very good"
		product = generateNumber()
		answer = int(raw_input("Enter the answer:"))

	while (answer!=product):
		print "No,please try again"	
		answer = int(raw_input("Enter the answer:"))