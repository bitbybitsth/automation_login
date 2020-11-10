class TooYoungException(Exception):

    def __init__(self, msg):
        self.__doc__ = msg

class TooOld(Exception):

    def __init__(self,msg):
        self.__doc__ = msg


class MatrimonyRegister:

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        if age<17:
            raise TooYoungException("Too young to get married")
        if age>60:
            raise TooOld("Too old chicha")
        self.age = age



def registration():
    name = input("Enter name:")
    height = float(input("Enter Height:"))
    age = int(input("Enter Age:"))

    return MatrimonyRegister(name,height,age)



try:
    ob = registration()
except (TooYoungException, TooOld) as tye:
    print(tye.__doc__)
else:
    print(ob.__dict__)
