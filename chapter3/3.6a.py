# program to calculate the factorial of a nonnegative number
number = raw_input("Enter the number:")
number = int(number)
fact = 1

if number == 0 or number == 1:
	print "factorial of %d is 1" %number

while number != 0:
	fact = fact * number
	number = number - 1

print "factorial is %d " %fact	