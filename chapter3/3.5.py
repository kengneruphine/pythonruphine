# program that convert a bnary number to a decimal

number = raw_input("Enter a 5 binary number containing 0s and 1s:")
number = int(number)

#display the number from right to left
a = number % 10
number1 = number / 10
b = number1 % 10
number2 = number1 /10
c = number2 % 10
number3 = number2 / 10
d = number3 % 10
number4 = number3 / 10

print a * 1 + b * 2 + c * 4 + d * 8 + number4 * 16
