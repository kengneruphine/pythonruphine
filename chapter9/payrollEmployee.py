#program to calculate the payroll of employees

import datetime
date=datetime.date.today()
month = date.month

class Date:
    '''class that represent date'''

    def __init__(self,day,month,year):
        '''date constructor '''
        self.day=day
        self.month=month
        self.year = year

    def __str__(self):
        '''representation of date object'''
        return "%d-%d-%d" %(self.day,self.month,self.year)


class Employee:

    def __init__(self,first,last,departcode):
        self.firstname=first
        self.lastname = last
        self.departcode=departcode

    def __str__(self):
        return "%s %s has code %d"%(self.firstname,self.lastname,self.departcode) 

class Boss(Date,Employee):
    
    def __init__(self,first,last,departcode,salary,day,month,year):
        Employee.__init__(self,first,last,departcode)
        Date.__init__(self,day,month,year)
        self.salary=salary

    def earning(self):
        if month==self.month:
            return self.salary + 1000
        else:
            return self.salary
    def __str__(self):
        return "%17s: %s and date %s" ("Boss",Employee.__str__(self),Date.__str__(self))

class CommissionWorker(Date,Employee):

    def __init__(self,first,last,departcode,salary,commission,quantity,day,month,year):
        Employee.__init__(self,first,last,departcode)
        date.__init__(self,day,month,year)
        self.salary=salary
        self.commission=commission
        self.quantity=quantity

    def earning(self):
        if month==self.month:
            return self.salary + self.commission * self.quantity + 1000
        else:
            return self.salary + self.commission * self.quantity

    def __str__(self):
        return "%17s: %s and date %s" % ( "Commission Worker",Employee.__str__(self),Date.__str__(self))    

class PieceWorker(Date,Employee):
    
    def __init__(self,first,last,wage,quantity,day,month,year,departcode):
        Employee.__init__(self,first,last,departcode)
        Date.__init__(self,day,month,year)
        self.wagePerPiece=wage
        self.quantity=quantity

    def earning(self):
        if month==self.month :
            return self.quantity * self.wagePerPiece + 1000
        else:
            return self.quantity * self.wagePerPiece

    def __str__(self):
        return "%17s: %s and date %s" % ( "PieceWorker",Employee.__str__(self),Date.__str__(self))

class HourlyWorker(Date,Employee):

    def __init__(self,first,last,departcode,day,month,year,wage,hour):
        Employee.__init__(self,first,last,departcode)
        Date.__init__(self,day,month,year)
        self.wage = wage
        self.hour = hour

    def earning(self):
        if month==self.month:
            if self.hour <= 40:
                return self.wage * self.hour + 1000
            else:
                return  1000 + 40 * self.wage + ( self.hour - 40 ) *\
                self.wage * 1.5            

        else:
            if self.hour <= 40:
                return self.wage * self.hours
            else:
                return 40 * self.wage + ( self.hour - 40 ) *\
                self.wage * 1.5

    def __str__(self):
        return "%17s: %s and date %s" % ( "Hourly Worker",Employee.__str__( self ),Date.__str__(self))


# main program
# create list of Employees
employees = [ Boss( "John", "Smith",885, 800.00,3,11,2012 ),
    #CommissionWorker( "Sue", "Jones",234, 3,11,2012,200.0, 3.0, 150 ),
    PieceWorker( "Bob", "Lewis",456, 2.5, 200,5,6,1994 ),
    HourlyWorker( "Karen", "Price",346, 13.75, 40,6,11,1996 ) ]    

for employee in employees:
    print " earned $%.2f" % (  employee.earning() )