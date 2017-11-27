#Program using Exception and except
print "We want only proper function"

try:
    numerator = float(raw_input("enter the number1:"))
    denominator = float(raw_input('enter the number2:'))
    if denominator < numerator:
        raise Exception,"denominator must be greater than numerator for proper fraction"
    else:
        div = numerator/denominator


except Exception,exception:
    print exception

else:
    print div    
