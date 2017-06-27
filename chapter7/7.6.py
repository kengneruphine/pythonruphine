class Rectangle:
	"Rectangle class"
	def __init__(self,__length=1, __width=1):
		self.__length = __length
		self.__width = __width

	def setLength(self,__length):
		if 0 < __length < 20.0:
			self.__length = __length

		else:
			raise ValueError,"Invalid value for length:%f" %__length


	def setWidth(self,__width):
		if 0<__width <20.0:
			self.__width = __width

		else:
			raise ValueError,"Invalid value for width:%f" %__width

	def getLength(self):
		return self.__length

	def getWidth(self):
		return self.__width

	def area(self):
		return self.__length * self.__width

	def perimeter(self):
		return 2* (self.__length + self.__width)


rectangle = Rectangle(2,4)
print "The area is %f",Rectangle.area(rectangle)
print "The perimeter is %f",Rectangle.perimeter(rectangle)	

#print "Enter new value of length"
length= int(raw_input("Enter the new length:"))
rectangle.setLength(length)
width= int(raw_input("Enter the new width:"))
rectangle.setWidth(width)
print "The new length and width  is ",rectangle.getLength(),"and",rectangle.getWidth()
print "New area is ",Rectangle.area(rectangle)
print "New perimeter is ",Rectangle.perimeter(rectangle)

