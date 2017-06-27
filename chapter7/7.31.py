#create a class called complex number for performing arithmetic with complex numbers
class Complex:
	def __init__ (self,realpart = 0.0,imaginarypart = 0.0):
		self.realpart = realpart
		self.imaginarypart = imaginarypart

	def addComplexNumber(self,first):
		real= self.realpart + first.realpart
		imaginary = self.imaginarypart + first.imaginarypart
		return real , imaginary

	def subtractComplexNumber(self,first):
		real= self.realpart - first.realpart
		imaginary = self.imaginarypart - first.imaginarypart
		return real , imaginary

	def printComplexNumber(self):
		print "(%0.1f,%0.1f)" %(self.realpart,self.imaginarypart)
		return ''


complex1 = Complex(2.0,4.0)
complex2 = Complex(4.0,9.0)

print " The two complex number"

print complex1.realpart,"+" ,complex1.imaginarypart,"i"
print complex2.realpart,"+" ,complex2.imaginarypart,"i"
print "The first complex number is",Complex.printComplexNumber(complex1)
print "The second complex number is",Complex.printComplexNumber(complex2)
print "The sum of this complex numbers is ", Complex.addComplexNumber(complex1,complex2)
print "The difference of this complex numbers is ", Complex.subtractComplexNumber(complex1,complex2)