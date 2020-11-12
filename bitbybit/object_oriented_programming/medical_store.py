from datetime import date

from object_oriented_programming.medicine import Medicine
from adavanced_concepts import MedicineExpired
from datetime import date


 class A:
#
#     def __init__(self, value, name):
#         self.value = value
#         self.name = name
#
#     def __add__(self, other):
#         self.name = self.name + other.name
#
#     def __gt__(self, other)

# class A:
#
#     def __init__(self, value, name):
#         self.value = value
#         self.name = name
#
#     def __add__(self, other):
#         self.name = self.name + other.name
#
#     def __gt__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#     def __le__(self, other):
#         pass
#
#     def __len__(self):
#         return len(self.name)
#

class MedicalStore:
    stock = []

    def display_stock(self):
        for item in MedicalStore.stock:
            print(item)

    def add_to_stock(self, med):
        st_med = self.get_medicine(med.mid)
        if st_med:
            st_med.quantity += med.quantity
        else:
            self.stock.append(med)

    def sell_medicine(self,mid, qty):
        st_med = self.get_medicine(mid)
        if st_med:
            today = date.today()
            if today>st_med.exp_date:
                raise MedicineExpired("medicine is expired",name=st_med.name, date=st_med.exp_date)
            elif st_med.quantity >= qty:
                st_med.quantity -=qty
                cost = st_med.price*qty
                return f"Have a Medicine and get well soon, please pay {cost}"
            else:
                return "Quantity not available"
        else:
            return "Medicine not available"

    def get_medicine(self, mid):
        for item in self.stock:
            if item.mid == mid:
                return item

    def stock_check(self):
        for item in self.stock:
            if item.quantity<5:
                return f"Order More {item.name} medicines"
            if item.exp_date<date.today():
                item.quantity = 0
                return f"{item.name} expired"

    def update_medicine(self, mid, med):
        st_med = self.get_medicine(mid)
        if st_med:
            st_med.price = med.price
            st_med.quantity +=med.quantity
        else:
            return "Not in stock"








ms = MedicalStore()

crocin = Medicine(mid=1, name="crocin", mfg_date=date(2020,5,15), exp_date=date(2019,5,14), contents=["A", "C"],
                  manufacturer="cipla", quantity=20, price=10)

ms.add_to_stock(crocin)

disprin = Medicine(mid=2, name="disprin", mfg_date=date(2020,2,15), exp_date=date(2020,7,14), contents=["D", "E"],
                  manufacturer="mankind", quantity=4, price=10)

ms.add_to_stock(disprin)

try:
    print(ms.sell_medicine(2,2))
except MedicineExpired as me:
    print(me.msg)
    print(me.medicine_name)
    print(me.expired_date)
    print(type(me))



# print(ms.stock)
# print(ms.stock[0].name)
# print(crocin)



# result = ms.sell_medicine(1,5)
# print(result)

# result = ms.stock_check()
# print(result)

# crocin2 = Medicine(mid=1, name="crocin", mfg_date=date(2020,5,15), exp_date=date(2019,5,14), contents=["A", "C"],
#                   manufacturer="cipla", quantity=20, price=15)
#
# result = ms.update_medicine(3,crocin2)
# print(result)
#
# ms.display_stock()
