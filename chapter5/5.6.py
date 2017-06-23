# program to implement the bubblesort

def bubble_sort(alist):
	moreswaps = True
	while moreswaps : 
		moreswaps = False
		for element in range(len(alist)-1):
			if alist[element] > alist [element + 1]:
				moreswaps = True
				temp = alist[element]
				alist[element] = alist[element + 1]
				alist[element +1] = temp

	return alist
	

mylist = [8,2,10,23,18,9,2,0,1,6,25,11]
sortedlist = bubble_sort(mylist)
print sortedlist				