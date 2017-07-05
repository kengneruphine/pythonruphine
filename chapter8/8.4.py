#implementing the special overloading methods on class singlelist
class SingleList:

	def __init__(self,initialList = None):
		"""initializes singlelist instance"""
		self.__list = [] # internal list,contains no duplicates
		#process list passed to __init__.if necessary

		if initialList:
			for value in initialList:
				if value not in self.__list:
					self.__list.append(value) # add original value

	#string representation method
	def __str__(self):
		"""overloaded string representation"""
		tempString = ""
		i = 0
		#build output string
		for i in range(len(self)):
			tempString+= "%12d" %self.__list[i]

			if(i +1 )%4 == 0: #4 numbers per row of output
				tempString += "\n"

		if i % 4 !=0: # add newline,if necessary
			tempString+="\n"

		return tempString

	def __len__(self):
		return len(self.__list)

	def __getitem__(self,index):
		return self.__list[index]

	def __setitem__(self,index,value):
		"""overloaded sequence elt assignment"""
		if value in self.__list:
			raise ValueError,"List already contains value %s" %str(value)
		self.__list[index] = value

	def __len__(self):
		return len(self.__list)	
		
	def append(self,value):
		if value in self.__list:
			raise ValueError,"value already present"
		self.__list.append(value)

	def count(self,element):
		return self.__list.count(element)

	def index(self,element):
		return self.__list.index(element)

	def insert(self,index,element):	
		if element in self.__list:
			raise ValueError,"value already present %s" %str(element)
		self.__list.insert(index,element)

	def pop(self):
		return self.__list.pop()

	def remove(self,element):
		return self.__list.remove(element)

	def reverse(self):
		return self.__list.reverse()

	def sort(self):
		return self.__list.sort()

	def __delitem__(self,index):
		del self.__list[index]

	def __contains__(self):
		return self.__list



#driver program for the singlelist class

def getIntegers():
	size = int (raw_input("list size:"))
	returnList = [] # the list to return

	for i in range(size):
		returnList.append(int(raw_input("Integer %d:" %(i + 1))))

	return returnList

#print and create integers1 and intergers2
print "creating integers1..."
integers1 = SingleList(getIntegers())

print "creating integers2..."
integers2 = SingleList(getIntegers())

#print integers1 size and contents
print "\nSize of list integers1 is",len(integers1)
print "List:\n",integers1

#print integers2 size and contents
print "\nSize of list integers2 is",len(integers2)
print "List:\n",integers2

# using the append method
integers1.append(9)
print "After appending method",integers1

# using the count method
count1 = integers2.count(3)
print "occurrence of your element is :",count1

#using the index method
index1 = integers1.index(2)
print "index of the elt in integers1 is:",index1

#using the insert method
integers1.insert(1,20)
print " the new list after inserting in integers1 is:", integers1

#using the pop method
integers2.pop()
print "new list after popping in integers2:",integers2

# using the remove method
integers1.remove(9)
print "New list after removing in integers1 :",integers1

#using the reverse method
integers1.reverse()
integers2.reverse()
print "Reversed integers1 is:",integers1
print "Reversed integers2 is:",integers2

#using the sort method
integers1.sort()
integers2.sort()
print "Sorted integers1 is:",integers1
print "sorted integers2 is:",integers2

#using the delete method
del integers1[1]
print "integers1 is after deleting:",integers1

#using the contains method
#if 9 in integers1:
#	print " not found"
#else:
#	print "element present"	












    	






				
