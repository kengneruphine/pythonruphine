#program to modify the class written in fig 7.13
class Time:
	"""class time with default constructor"""
	def __init__(self,hour=0,minute=0,second=0):
		"""Time constructor each data member to zero"""
	#self.setTime(hour,minute,second)

	def setTime(self,hour,minute,second):
		"""set values of hour,minute and second"""
		self.setHour(hour)
		self.setMinute(minute)
		self.setSecond(second)

	def setHour(self,hour):
		"""set hour value"""

		if 0<=hour <24:
			self.__hour = hour
		else:
			raise ValueError,"Invalid hour value:%d"%hour
	
	def setMinute(self,minute):
		if 0<=minute <60:
			self.__minute=minute
		else:
			raise ValueError,"Invalid minute value:%d"%minute
	
	def setSecond(self,second):
		if 0<=second < 60:
			self.__second=second
		else:
			raise ValueError,"Invalid second value:%d"%second

	#implementing the tick method
	def tick(self):
		if self.__hour ==23 and self.__minute==59 and self.__second ==59:
			print "The next day"
			self.__hour = 0
			self.__minute=00
			self.__second=00
			print "%.2d:%.2d:%.2d" %(self.__hour,self.__minute,self.__second)
		else:
			
			self.__second += 1
			if self.__second == 60:
				self.__minute +=1
			if self.__minute == 60:
				self.__hour += 1
		
			print "%.2d:%.2d:%.2d" %(self.__hour,self.__minute,self.__second)
		return ''	



	def getHour(self):
		return self.__hour
	def getMinute(self):
		return self.__minute
	def getSecond(self):
		return self.__second
	def printMilitary(self):
		print "%.2d:%.2d:%.2d" %(self.__hour,self.__minute,self.__second),
		return ''

	def printStandard(self):
		"""prints time object in standard format"""
		standardTime = ""

		if self.__hour ==0 or self.__hour ==12:
			standardTime += "12:"
		else:
			standardTime += "%d:" %(self.__hour%12)

		standardTime += "%.2d:%.2d" %(self.__minute,self.__second)	

		if self.__hour <12:
			standardTime += "AM"
		else:
			standardTime += "PM"

		print standardTime
		return ''			


time1 = Time(0,0,0)
hour =int(raw_input("Enter new hour:"))
time1.setHour(hour)
minute= int(raw_input("Enter new minute:"))
time1.setMinute(minute)
second = int(raw_input("Enter new second:"))
time1.setSecond(second)
print "new paramters are %d,%d,%d"%(time1.getHour(),time1.getMinute(), time1.getSecond())
print time1.printMilitary()
print time1.printStandard()
print "\n"
print "Implementing the method tick"
print Time.tick(time1)