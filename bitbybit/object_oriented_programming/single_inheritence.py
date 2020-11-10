from http import HTTPStatus
# P -> C

class Employee:

    def __init__(self, eid, name, last_name, pay):
        self.eid = eid
        self.name = name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f"{self.name}.{self.last_name}@organization.com"

    @property
    def U_ID(self):
        return f"PUN{self.eid}"

    def apply_leave(self):

        print("Your Leave is approved")

    def apply_raise(self, raise_percent= None):
        self.pay = self.pay * 1.15

    def __str__(self):
        return f"{self.name}\n{self.last_name}"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return self.pay + other.pay

    def __gt__(self, other):
        if self.pay > other.pay:
            return True
        return False

    def __lt__(self, other):
        if len(self.name) < len(other.name):
            return True
        return False


e1= Employee(eid=1,name="dayanand",last_name="j", pay=50000)
e2 = Employee(eid=1,name="dayana",last_name="j", pay=51000)

print(e1.U_ID)
e1.eid = 2
print(e1.U_ID)

# print(dayanand.pay + honu.pay)
print(e1 + e2)
print(e1 < e2)

# print(dayanand.email)
#
# dayanand.last_name = "jadhav"
# print(dayanand.email)
# dayanand.name = "daya"
# print(dayanand.email)

# aditya= Employee(eid=1,name="aditya",last_name="t", pay=50000)
#
class Developer(Employee):
    def __init__(self, eid, name, last_name, pay, task):
        self.task = task
        # super().__init__(eid, name, last_name, pay)
        Employee.__init__(self, eid, name, last_name, pay)

#
#
#
class Tester(Employee):
    def __init__(self, eid, name, last_name, pay, task):
        self.task = task
        super().__init__(eid, name, last_name, pay)
        # Employee.__init__(self, eid, name, last_name, pay)
#
#
# class Manger(Employee):
#
#     def apply_raise(self):
#         self.pay = self.pay *1.25
#
#
# dayanand = Developer(eid=1, name="dayanand", last_name="j", pay=50000, task="development")
# aditya = Tester(eid=1, name="aditya", last_name="t", pay=60000, task="development")
# manager = Manger(eid = 3, name="Prashat", last_name="shinde", pay=85000)
#
# print(manager.pay)
# manager.apply_raise()
# print(manager.pay)
#
# print(dayanand.pay)
# dayanand.apply_raise()
# print(dayanand.pay)
#
#
#
#
# # print(help(range))
#
# # print("Dayanand is Developer:", isinstance(dayanand,Developer))
# # print("Dayanand is Employee:", isinstance(dayanand,Employee))
# # print("Dayanand is Manager:", isinstance(dayanand,Manger))
#
# # print("Developer is child o
#
#
# # dayanand.apply_raise()
#
# #
# # dayanand1= Manger(eid=1,name="dayanand",last_name="j", pay=50000)
# # dayanand1.apply_raise()
# # print(dayanand.pay)
# #
# # aditya.apply_raise()
# # print(aditya.pay)
#
# # dayanand.apply_leave()
#
#
# #
# # dayanand.apply_leave()
# # print(dayanand.pay)
# # dayanand.apply_raise()
# # print(dayanand.pay)
# # aditya.apply_leave()
# # print(aditya.pay)
# # aditya.apply_raise()
# # print(aditya.pay)
# #
# # chinmay = Tester(eid=1,name="chinmay",last_name="s", pay=50000, task="testing")
# # print(chinmay.email)
# # sreenivas = Tester(eid=1,name="sreenivas",last_name="j", pay=55000, task ="testing")
# # print(sreenivas.email)
# # print(chinmay)
# # print(sreenivas)
# # #
# # # chinmay.apply_leave()
# # # print(chinmay.pay)
# # # chinmay.apply_raise()
# # # print(chinmay.pay)
# # # sreenivas.apply_leave()
# # # print(sreenivas.pay)
# # # sreenivas.apply_raise()
# # # print(sreenivas.pay)
