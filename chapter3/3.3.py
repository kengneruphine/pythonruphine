# program to calculate the overall average
counter = 0
average1 = 0
 
gallons = raw_input("Enter the gallons used(-1 to end) :")
gallons = float(gallons)

while gallons != -1:
	miles = raw_input("Enter the miles driven:")
	miles = int(miles)
	average = miles / gallons
	print " The miles/gallons of the tank was %.6f"%average
	average1 = average1 + average
	counter = counter + 1
	gallons = raw_input("Enter the gallons used (-1 to end):")
	gallons = float(gallons)
   
print counter
if counter != 0:
      Average = average1 / counter
      print "the overall average miles/gallons was %.6f" %Average
else:
	print "exit"

