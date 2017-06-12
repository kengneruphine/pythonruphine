#program that determine whether a number is a palindrome

number = raw_input("Enter a five-digit integer:")
number = int(number)

a = number % 10 # to get the last number
number1 = number /10 # number left
b = number1 % 10  # number before last
number2 = number1 / 10 # third number
c = number2 % 10
number3 = number2 /10
d = number3 % 10
number4 = number3 /10 # first number

if a == number4 and b == d:  # compare first and last,second and fouth
	print "%d is a palindrom" %number

else:
	print "%d is not a palindrome" %number
