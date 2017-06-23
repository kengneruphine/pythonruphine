#program to implement a binary search

def binary_search(alist,item):
	first = 0
	last= len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1

	return found
	

blist = [2,3,1,6,5,7,8,9,4]
blist.sort()
print blist
item1 = int(raw_input("Enter the item to search :"))
isitfound = binary_search(blist,item1)
if isitfound:
	print "found at index" , blist.index(item1)
else:
	print "-1,not found"	