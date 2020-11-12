class Employee:

    raise_amount = 1.05
    count_of_empl = 0

    def __init__(self, eid, name, pay, designation):
        self.eid = eid
        self.name = name
        self.pay = pay
        self.designation = designation
        Employee.count_of_empl +=1

    def __str__(self):
        return f"{self.__dict__}"

    def give_raise(self):
        self.pay = self.pay * self.raise_amount

class Employee:

    raise_amount = 1.05
    count_of_empl = 0

    def __init__(self, eid, name, pay, designation):
        self.eid = eid
        self.name = name
        self.pay = pay
        self.designation = designation
        Employee.count_of_empl +=1

    def __str__(self):
        return f"{self.__dict__}"

    def give_raise(self):
        self.pay = self.pay * self.raise_amount
#
emp1 = Employee(1, "honu", 50000, "dev")
emp2 = Employee(2, "nitesh", 50000, "dev")
emp3 = Employee(3, "pankaj", 50000, "dev")

print(Employee.count_of_empl)

#
emp1.raise_amount = 1.10
# emp3.raise_amount = 1.0
#
emp1.give_raise()
emp2.give_raise()
emp3.give_raise()
print(emp1)
print(emp2)
print(emp3)

# print("Using class name", Employee.raise_amount)




#
#
#
#
# # emp2.age = 27
# #
# emp1.raise_amount = 1.10
#
# print(emp1.pay)
#
# emp1.give_raise()
# emp2.give_raise()
# emp3.give_raise()
#
#
# print(emp1)
# print(emp2)
# print(emp3)
#
# # print(Employee.count_of_employees)
#
#
# class Employee:
#
#     raise_amount = 1.05
#     count_of_employees = 0
#
#     def __init__(self, eid, name, pay, designation):
#         self.eid = eid
#         self.name = name
#         self.pay = pay
#         self.designation = designation
#         Employee.count_of_employees +=1
#
#
#     def give_raise(self):
#         print(self)
#         self.pay = self.pay * self.raise_amount
#
#     @classmethod
#     def set_raise_amount(cls):
#         cls.raise_amount = 1.0
#
# emp1 = Employee(1, "honu", 50000, "dev")
# emp2 = Employee(2, "nitesh", 50000, "dev")
# emp3 = Employee(3, "pankaj", 50000, "dev")
#
# emp1.set_raise_amount()
# Employee.set_raise_amount()
# emp1.give_raise()

