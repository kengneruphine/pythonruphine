
class Rectangle:
	"""Rectangle class"""
	def __init__(self,x=0,y=0,x1=0,y1=0):
		self.x = 0 # for the upper right hand
		self.y = 0 # for the upper righr hand
		self.x1 = 0 #for the lower left hand
		self.y1=0 #for the lower left hand 

	# x is the length

	def setCoordinates(self,first,second):
		if   0< first[0] <20  and 0<first[1]<20:   # check to make sure they are in the first quadrant,ie +ve and less than 20
			self.x = first[0]
			self.y = first[1]
		else:
			raise ValueError,"Invalid values"
				
		if 0< second[0] <20 and 0<second[1] < 20:
			self.x1 = second[0]
			self.y1 = second[1]
			
		else:
			raise ValueError,"Invalid values"		

	def getWidth(self):    #width is gotten from x and x1
		if self.x > self.x1:
			self.width = self.x
		else:
			self.width=self.x1
		return self.width		

	def getLength(self):      #length is gotten from y and y1
		if self.y > self.y1:
			self.length=self.y
		else:
			self.length =self.y1
		return self.length		

	def perimeter(self):
		return 2 *(self.width + self.length)

	def area(self):
		return self.width * self.length

	def isSquare(self):
		if self.width == self.length:
			print "It is a square"
		else:
			print "It is not a square"			


rectangle = Rectangle(0,0)
#Enter the tuples
t1 = (3,4)
t2 = (3,4)

print rectangle.setCoordinates(t1,t2)
print "length is",rectangle.getLength()
print "width is",rectangle.getWidth()

print "Area is",rectangle.area()
print "Perimeter is",Rectangle.perimeter(rectangle)
print rectangle.isSquare()














			