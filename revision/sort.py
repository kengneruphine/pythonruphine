#Return true if a list is sorted
def is_sorted(t):
	i=0     
	j=len(t)-1      
	for i in range(j):
		if t[i]<t[i+1]:
			return True
		return False


t=['b','a','c']
print is_sorted(t)


#check if a list has duplicates
def has_duplicates(t):
	s=t.sort()
	for i in range(len(t)-1):
		if t[i]==t[i+1]:
			return 'duplicates found'
		return 'no duplicates'




t=[1,2,3,4,2,1]
print has_duplicates(t)


