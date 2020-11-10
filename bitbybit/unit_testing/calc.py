class AnythingMultipliedByZeroisZero(Exception):
    pass

def addition(a=0, b=0):
    if a and b:
        return a+b




def subtraction(a=0,b=0):
    if a and b:
        return a-b


def multiplication(a,b):
    if b==0:
        raise AnythingMultipliedByZeroisZero
    return a*b


def divide(a,b):
    return a/b


def modulo(a,b):
    return a%b
