# program to display result ina tabular form
# info about the 5 products from the 4 salerpers
slip =[[10,52,60,10],
       [11,15,20,60],
       [20,15,10,18],
       [13,40,16,17],
       [17,10,20,23]] 


# to print total for each row and append to the list
totalrow = 0
productlist = []
for i in range (len(slip)):
	for j in range(len(slip[0])):
		totalrow += slip[i][j]
	productlist.append(totalrow)
	totalrow = 0

for i in range (len(slip)):
	slip[i].append(productlist[i])


# to print total for each column and append to the list
salepersonlist = []
totalcol = 0
for i in range (len(slip)):
	for j in slip:
		totalcol += j[i]
	salepersonlist.append(totalcol)	
	totalcol = 0

slip.append(salepersonlist)	

# get the number of products
product = len(slip)
# total number of salerperson
saleperson = len(slip[0])



print slip
#print table headers
print "The list is:"
print "saleperson",

for i in range (saleperson):
	if i == 4:
		print "Total"
	else :	
		print "[%d]" %i,

print

# print product by row
for i in range(product):
	if i == 5:
		print "    Total",
	else:	
		print "product[%d]" %i,
	for j in range (saleperson):
		print slip[i][j],'',

	print




