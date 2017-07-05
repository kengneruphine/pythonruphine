#overloading mapping operators, for a dictionary
class SimpleDictionary:
	""" class to make an instance behave like a dictionary"""
	def __getitem__(self,key):
		"""overloaded key-value access"""
		return self.__dict__[key]

	def __setitem__(self,key,value):
		"""overloaded key-value assignment/creation"""
		self.__dict__[key] = value

	def clear(self):
		"""overloaded clear method"""
		return self.__dict__.clear()

	def update(self,other):
		"""overloaded update method"""
		return self.__dict__.update(other)

	def has_key(self,key):
		"""overloaded has_key method"""
		return self.__dict__.has_key(key)

	def copy(self):
		"""overloaded copy method"""
		return self.__dict__.copy()

	def get(self,key):
		"""overloaded get method"""
		return self.__dict__.get(key)

	def __str__(self):	
		return str(self.__dict__)	



#testing the class
simple = SimpleDictionary()
print "The empty dictionary:",simple

#add values to simple(invoke simple.__setitem__)
simple[1] = "one"
simple[2] = "two"
simple[3] = "three"

print "the dictionary after adding values:",simple
dict1 = {4:"four",5: "five",6:"six",1:"one"}
simple.update(dict1)

print "update dictionary:",simple
simple1 = simple.copy()
print "dict copy into this:",simple1

# test the has_key method
text = simple.has_key(6)
print text
text1 = simple.has_key(8)
print text1

# test the get method
textGet = simple.get(5)
print textGet

#testing the clear method
simple.clear()
print "removing all elements in the list",simple
print "see what you have in its copied:",simple1