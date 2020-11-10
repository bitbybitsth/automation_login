import datetime

class Medicine:

    def __init__(self,mid, name, mfg_date, exp_date, contents, manufacturer, quantity,price):
        self.mid = mid
        self.name = name
        self.mfg_date = mfg_date
        self.exp_date = exp_date
        self.contents = contents
        self.manufacturer = manufacturer
        self.quantity = quantity
        self.price = price
        self.create = datetime.datetime.now()
        self.modified = datetime.datetime.now()


    def __str__(self):
        return f"Medicine ID ->{self.mid}\nMedicine Name ->{self.name}\nMfg. Date ->{self.mfg_date}\n" \
               f"Exp Date ->{self.exp_date}\nCintents ->{self.contents}\nManufacturer ->{self.manufacturer}" \
               f"\nQuantity ->{self.quantity}\nPrice -> {self.price}"

    def __add__(self, other):
        self.modified = datetime.datetime.now()
        self.quantity = self.quantity + other.quantity

    def __repr__(self):
        return str(self)


class A:

    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __add__(self, other):
        self.name = self.name + other.name

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __len__(self):
        return len(self.name)


#
# a = A(10, "good")
# b = A(20, "morning")
#
# print(len(b))
#
# # + -> __add__
# # > -> __gt__
# # >= -> __ge__
# # < -> __lt__
# # <=  -> __le__
#
# a+b
# print(a.__dict__)