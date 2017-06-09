#program to calculate the area of a circle
pie = 3.14159
radius = raw_input("Enter the radius of the circle \n")
radius = int(radius)

print "Diameter is" , 2 * radius
print "Area is " , (radius ** 2) * pie
print "circumference is ", 2 * pie * radius