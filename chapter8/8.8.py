# Definition of class polynomial
#exponent=key,coefficient = value
import math
class Polynomail:
	"""class to make a polynomial behave like a dictionary"""
	def __init__(self,exponent = 1 ,coefficient = 1):
		self.__dict__[exponent] = coefficient
	#mapping special methods
	def __getitem__(self,exponent):
		"""overloaded key-value access"""
		if not self.__dict__[exponent]:#if coefficient doesnot exit,return 0
			return 0
		return self.__dict__[exponent]

	def __setitem__(self,exponent,coefficient):
		"""overloaded key-value assignment/creation"""
		self.__dict__[exponent] = coefficient

	def __str__(self):
		"""overloaded string representation"""
		return str(self.__dict__)

	def keys(self):
		"""return list of keys in dictionary"""
		return self.__dict__.keys()

	def values(self):
		return self.__dict__.values()

	def __len__(self):
		"""return length of dictionary"""
		self.length = self.keys()
		return max(self.length)


	#def __add__(self,other):
	#	"""overloaded add method"""
	#	self.__dict__[exponent] = self.__dict__[exponent]
	#	return self.__dict__[exponent] + other.__dict__[exponent]

	#def __sub__(self,other):
	#	"""overloaded subtract method"""
	#	return (self.__dict__[exponent] - other.__dict__[exponent])



#Test program
#create and print polynomial object
polynomial1 = Polynomail()
polynomial2 = Polynomail(6,7)
print "empty dictionary", polynomial1

#add values to polynomial 1(invokes simple.setitem)
polynomial1 [2] = 4
polynomial1 [3] = 6
polynomial1 [4] = 8
polynomial1 [6] = 3
 
polynomial2 [2] = 6
polynomial2 [3] =5
polynomial2 [4] = 2

print "dictionary after adding values :",polynomial1
print "dictionary after adding values :",polynomial2

print "length is from the highest exponent ie key",len(polynomial2)
print "coffiecient is",polynomial1[3]

#polynomial3 = polynomial1 + polynomial2
#print "Adding two poly",polynomial3






































