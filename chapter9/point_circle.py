#Writing the classes point,circle and cylinder using composition instead of inheritance

import math

class Point:

    def __init__(self,x=0,y= 0):
        '''condtructor for the point class'''
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x,self.y

    def setPoint(self,v1,v2):
        self.x = v1
        self.y = v2
        return self.x,self.y

    def __str__(self):
        return "%s, %s" %(self.x,self.y) 


class Circle:

    def __init__(self,x=0,y=0,radius=0.0):
        self.x =x
        self.y = y
        self.radius = radius
    
    def getPoint(self):
        return self.x,self.y    

    def setPoint(self,v1,v2):
        self.x = v1
        self.y = v2
        return self.x,self.y

    def getRadius(self):
        return self.radius

    def setRadius(self,value):
        self.radius=value 

    def area(self):
        return math.pi * self.radius **2

    def __str__(self):
        return "the center of circle is (%d,%d) and radius is %d" %(self.x,self.y,self.radius)

class Cylinder:

    def __init__(self,x=0,y=0,radius=0,height=0):
        self.x =x
        self.y =y
        self.radius = radius
        self.height = height

    def setPoint(self,v1,v2):
        self.x = v1
        self.y = v2
        return self.x,self.y 

    def getPoint(self):
        return self.x,self.y   
    
    def getRadius(self):
        return self.radius

    def setRadius(self,value):
        self.radius=value
        

    def getHeight(self):
        return self.height

    def setHeight(self,value):
        self.height=value

    def area(self):
        return 2 *math.pi *self.radius *self.height

    def volume(self):
        return math.pi * self.height * (self.radius**2)    
    
    def __str__(self):
        return "the center is (%d,%d),radius is %d and height is %d"%(self.x,self.y,self.radius,self.height)

# main program
#create point object
point = Point(5,9)
print "point object with value",point
print '\n'

 #create circle object
circle = Circle (2,4,6.0)
print circle
print "radius of the circle is ",circle.radius
print "area of the circle is ", circle.area()
print'\n'

#creating cylinder object
cylinder = Cylinder(2,2,5,8)
print cylinder
print "height of cylinder is ",cylinder.height
print "area of cylinder is",cylinder.area()
print "volume of cyliner is",cylinder.volume()