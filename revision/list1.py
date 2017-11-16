#print the cumulative sum of a list

def cumulative_sum(t):
	total = [0]
	for i in range(len(t)):	
		total[0] += t[i]
		print total

t=[1,2,3]
cumulative_sum(t)
print '\n\n'

#fxn to remove the first and last letter from a list
print 'fxn to remove some element from a list'
def middle(t):
	x=t.pop(0)
	y = t.pop()
	return t

t =[1,2,4,5,6]
print middle(t)

print '\n'

# fxn to remove first and last letter and return None
def chop(t):
	x=t.remove(t[0])
	y= t.remove(t[-1])
	return 

t= [3,4,5,6]
print chop(t)

