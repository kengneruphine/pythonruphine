#creating the base class student

class Student:
    '''class that represent students'''

    def __init__(self,first,last):
        '''student constructor take first and lastname variables'''

        self.firstname = first
        self.lastname = last

    def __str__(self):
        '''string representation of student '''

        return "%s %s" %(self.firstname,self.lastname)


class UndergraduateStudent(Student):
    '''class that represent an undergraduate student'''

    def __init__(self,first,last,department):
        '''constructor for undergraduate takes firstname,lastname and department'''

        Student.__init__(self,first,last)
        self.department = department

    def __str__(self):
        '''string representation of undergraduate student'''

        print "%s is an undergraduate student" % Student.__str__(self)
        return "she is from the %s department" % self.department


 # creating the derived class Graduate student

class GraduateStudent(Student):
    '''class that represent a graduate student'''

    def __init__(self,first,last,degree):
        '''constructor for graduate takes firstname,lastname and degree'''

        Student.__init__(self,first,last)
        self.degree = degree

    def __str__(self):
        '''string representation of graduate student'''

        print "%s is a graduate student" % Student.__str__(self)
        return "He has a %s degree" % self.degree


# Main program
undergraduate = UndergraduateStudent('Grace', 'Ruphine','computer Engineering')
graduate = GraduateStudent ('Bob','Junior','Master')

print undergraduate

print '\n'

print graduate  





