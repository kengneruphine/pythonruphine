#program to implemement inheritance hierarchy for the class quadrilateral

import math

class Quadrilateral:
    '''class that represent quadrilateral'''
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.x4=x4
        self.y4=y4

    def __str__(self):
        return "4 endpoints data are \n A:(%s %s)\n B:(%s %s)\n C:(%s %s)\n D:(%s %s)" %(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3,self.x4,self.y4)

    def getDistance(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)**2 +(y2-y1)**2)

class Parallelogram(Quadrilateral):

    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):

        Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)

    def getPerimeter(self):
        A=self.getDistance(self.x1,self.y1,self.x2,self.y2)
        B= self.getDistance(self.x2,self.y2,self.x3,self.y3)
        C=self.getDistance(self.x3,self.y3,self.x4,self.y4)
        D=self.getDistance(self.x1,self.y1,self.x4,self.y4)
        return (A+B+C+ D)

    def __str__(self):
        return "Parallelogram has %s" %Quadrilateral.__str__(self) 

class Rectangle(Quadrilateral):
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):

        Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)

    def getArea(self):
        return (self.getDistance(self.x1,self.y1,self.x2,self.y2) * self.getDistance(self.x2,self.y2,self.x3,self.y3 ))    
    
    def getPerimeter(self):
        return (self.getDistance(self.x1,self.y1,self.x2,self.y2) + self.getDistance(self.x2,self.y2,self.x3,self.y3 ))*2

    def __str__(self):
        return "Rectangle has %s"%Quadrilateral.__str__(self)

class Square(Quadrilateral):
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):

        Quadrilateral.__init__(self,x1,y1,x2,y2,x3,y3,x4,y4)

    def getPerimeter(self):
        return (self.getDistance(self.x1,self.y1,self.x2,self.y2))*4

    def getArea(self):
        return (self.getDistance(self.x1,self.y1,self.x2,self.y2))**2

    def __str__(self):
        return "Square has %s"%Quadrilateral.__str__(self)



print "creating parallelogram object"
parallelogram= Parallelogram(1,7,3,4,6,7,8,9)
print parallelogram
print "it has a perimeter of %d" %parallelogram.getPerimeter()

print"\n"
print "creating rectangle object"
rectangle = Rectangle(2,4,2,3,5,6,5,8)
print rectangle
print "it has area as %d and perimeter %d"%(rectangle.getArea(),rectangle.getPerimeter())

print "\n"
print"creating square object"
square = Square(2,2,3,3,4,4,5,5)
print square
print "it has area as %d and perimeter %d" %(square.getArea(),square.getPerimeter()) 




