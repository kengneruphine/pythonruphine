#program that determines whether the first number is a multiple of the second
firstNumber = raw_input("Enter the first number \n")
firstNumber = int(firstNumber)

secondNumber = raw_input("Enter the second number \n")
secondNumber = int(secondNumber)

if(firstNumber % secondNumber) == 0:
	print "%d is a multiple of %d" %(firstNumber,secondNumber)

if(firstNumber % secondNumber) != 0:
	print "%d is not a multiple of %d" %(firstNumber,secondNumber)