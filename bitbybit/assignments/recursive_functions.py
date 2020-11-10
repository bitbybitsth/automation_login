
def function(n):

    if n == 0:
        return "Function execution complete"
    print("Calling my self")
    print(function(n-1))

# function(5)


def factorial(n):
    if n>=1:
        return n * factorial(n-1)
    elif n == 0:
        return 1
#
# print(factorial(5))
#
#
#
# fact = factorial(6)
# print(fact)



def outer(n):
    print("Entered in outer")

    def innner():
        print("entered in inner")
        print("exiting inner")

    print("Calling inner")
    return innner
    print("exiting outer")

#
# returned_function = outer(10)
# print(returned_function)

def addition(n1, n2):
    return n1+n2

print(addition(5,15))

une_addition = addition

print(une_addition(4,2))


