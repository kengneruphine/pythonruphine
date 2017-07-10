#comlpex number class
class Complex:
	"""complex numbers of the form realPart + imaginaryPart *i"""

	def __init__(self,real=0,imaginary=0):
		"""Assigns values to realpart and imaginarypart"""
		self.realPart = real
		self.imaginaryPart = imaginary

	def __add__(self,other):
		"""returns the sum of two complex instances"""
		real = self.realPart + other.realPart
		imaginary = self.imaginaryPart + other.imaginaryPart

		#create and return new complexnumber
		return real,imaginary

	def __sub__(self,other):
		"""returns the difference of two complex instance"""
		real = self.realPart - other.realPart
		imaginary = self.imaginaryPart - other.imaginaryPart

		#create and return complexNumber
		return real,imaginary

	def __mul__(self,other):
		"""returns the product of two complex number"""
		real = (self.realPart * other.realPart) - (self.imaginaryPart * other.imaginaryPart)
		imaginary = (self.realPart*other.imaginaryPart) + (self.imaginaryPart * other.realPart)

		# create and return complexNumber
		return real,imaginary


	def __eq__(self,other):
		"""overloaded == operator"""

		if self.realPart != other.realPart and self.imaginaryPart !=other.imaginaryPart:
			return 0 # not equal

		return 1 # are equal

	def __str__(self):
		"""string representation"""
		return "%s + %s", self.realPart,self.imaginaryPart
		#return self.realPart ,"+",self.imaginaryPart,"i"

# test program
complex1 = Complex(3,4)
complex2 = Complex(5,3)

x = complex1 + complex2
print "The sum of the two complex number is", x

y = complex1 * complex2
print "The product is",y	

if complex1 == complex2:
	print "Are equal"
else:
	print "Not equal"		






























