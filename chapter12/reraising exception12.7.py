# program to reraise an exception
"""illustration of reraise an exception"""

class MyCustomException(Exception):
     pass

def foo():
    a = 1
    b = 0
    return a/b

def bar():
    try:
        foo()
    except ZeroDivisionError as e:
        raise # reraising the except here


bar()   