#Modify the Rational class
def gcd(x,y):
	"""compute greatest common divisor of two values"""
	while y:
		z = x
		x = y
		y = z % y
	return x
	
class Rational:
	"""Representation of rational number"""
	def __init__(self,top =1,bottom = 1):
		"""initialises rational instance"""

		#do not allow 0 denomiator 
		if bottom == 0:
			raise ZeroDivisionError,"cannot have 0 denominator"

		#raise attribute values
		self.numerator = abs(top)
		self.denominator = abs(bottom)
		self.sign = (top*bottom) / (self.numerator*self.denominator)

		self.simplify() #Rational represented in reduced form

	def __setitem__(self,name,value):
		"""Assign a value to an attribute"""
		if name == "numerator" or name == "denominator":
			self.__dict__["_numerator"] = value
			self.__dict__["_denominator"] = value
		else:
			raise ValueError,"Invalid name"

		self.sign1 = (top*bottom) / (self._numerator*self._denominator)

		if self.sign!= self.sign1:
			self._numerator = abs(self._numerator)
			self._denominator = abs(self.denominator)

	def __getitem__(self,name):
		if name =="numerator":
			return self._numerator
		if name == "denominator":
			return self._denominator

	# class interface method
	def simplify(self):
		"""simplies a rational number"""
		common = gcd(self.numerator,self.denominator)
		self.numerator /= common
		self.denominator /= common

	def __abs__(self):
		"""overload built in fxn abs"""
		return Rational(self.numerator,self.denominator)

	def __str__(self):
		"""string representation"""
		#determine sign display
		if self.sign == -1:
			signString ="-"
		else:
			signString = ""


		if self.numerator == 0:
			return "0"

		elif self.denominator == 1:
			return "%s%d"%(signString,self.numerator)
		else:
			return "%s%d/%d" %(signString,self.numerator,self.denominator)


	# overloaded binary arithmetic operators
	def __add__( self, other ):
		"""Overloaded addition operator"""
		return Rational(
		self.sign * self.numerator * other.denominator +
		other.sign * other.numerator * self.denominator,
		self.denominator * other.denominator )
	def __sub__( self, other ):
		"""Overloaded subtraction operator"""
		return self + ( -other )

	def __mul__( self, other ):
		"""Overloaded multiplication operator"""	
		return Rational( self.numerator * other.numerator,
		self.sign * self.denominator *
		other.sign * other.denominator)


#Test the program
#create objects of class Rational
rational1= Rational() # 1/1
rational2 = Rational(10,30) # reduce to 1/3
rational3 = Rational(-7,14)

#print objects of class Rational
print "rational1:",rational1

rational1.numerator = -6
rational1.denominator =12


print rational1






































































































