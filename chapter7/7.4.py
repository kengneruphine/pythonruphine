#program to create a class called ratonal numbers
from __future__ import division
from fractions import *
class RationalNumbers:
	"Rational Numbers"
	def __init__(self,numerator=0,denominator=1):
		self.numerator = numerator
		self.denominator = denominator

	def addRationalNumber(self,first):
		f1= Fraction(self.numerator , self.denominator)
		f2 = Fraction(first.numerator,first.denominator)
		print "%s + %s = %s" %(f1,f2,f1+f2)
		return ' '

	def subtractRationalNumber(self,first):
		f1= Fraction(self.numerator , self.denominator)
		f2 = Fraction(first.numerator,first.denominator)
		print "%s - %s = %s" %(f1,f2,f1-f2)
		return ' '

	def multiplyRationalNumber(self,first):
		f1=Fraction(self.numerator , self.denominator)
		f2 =Fraction(first.numerator,first.denominator)
		print "%s * %s = %s" %(f1,f2,f1*f2)
		return ' '

	def divideRationalNumber(self,first):
		f1=Fraction(self.numerator , self.denominator)
		f2 = Fraction(first.numerator,first.denominator)
		print "%s / %s = %s" %(f1,f2,f1/f2)
		return ' '

	def printRationalNumber(self):
		print "%d / %d" %(self.numerator ,self.denominator)	
		return ' '

	def floatformat(self):
		f1 = Fraction(self.numerator ,self.denominator)
		return float(f1)	
        
	

print "Printing the two fractional numbers"

number1 = RationalNumbers(4,6)
number2 = RationalNumbers(9,4)

print "The first fractional number",RationalNumbers.printRationalNumber(number1)
print "The second fractional number",RationalNumbers.printRationalNumber(number2)
print "The first number in floating-point format",RationalNumbers.floatformat(number1)
print "The second number in floating-point format",RationalNumbers.floatformat(number2)
print "\n"
print "The sum of this fraction is",RationalNumbers.addRationalNumber(number1,number2)
print "The difference of this fraction is",RationalNumbers.subtractRationalNumber(number1,number2)
print "The product of this fraction is",RationalNumbers.multiplyRationalNumber(number1,number2)
print "The quotient of this fraction is",RationalNumbers.divideRationalNumber(number1,number2)

