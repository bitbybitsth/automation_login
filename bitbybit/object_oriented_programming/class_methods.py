# class methods
# static methods
# instance methods

class Employee:


    raise_amount = 1.05
    total_employees = 0

    def __init__(self, eid, name, pay, designation, joining_date):
        self.eid = eid
        self.name = name
        self.pay = pay
        self.designation = designation
        self.joining_date = joining_date
        Employee.total_employees += 1

    def display(self):
        print(self)
        print(f"{self.__dict__}")


    @classmethod
    def get_raise_amount(cls):
        print(cls)
        return cls.raise_amount

    # @classmethod
    # def get_raise_amount(cls):
    #     print(cls)
    #     return cls.raise_amount
    #
    # @classmethod
    # def annoucing_lockdown(cls):
    #     print(f"lockdown announced for {cls}")
    #
    # @classmethod
    # def give_diwali_bonus(cls):
    #     return 10000
    #
    # @classmethod
    # def set_raise_amount(cls, amt):
    #     print(cls)
    #     cls.raise_amount = amt
    #
    @staticmethod
    def get_joing_date(joing_date):
        x = joing_date.split(",")
        return x[0]




emp1 = Employee(1, "honu", 50000, "dev", joining_date = "10,2,2020")
# emp1.display()
x = emp1.get_joing_date("06,07,2020")
print(x)


emp1 = Employee(1, "honu", 50000, "dev", joining_date = "10,2,2020")
# emp1.display()
x = emp1.get_joing_date("06,07,2020")
print(x)


# emp1 = Employee(1, "honu", 50000, "dev", joining_date = "10,2,2020")
# emp2 = Employee(2, "nitesh", 50000, "test", joining_date = "10,2,2020")
# emp3 = Employee(3, "pankaj", 50000, "dev", joining_date = "10,2,2020")

# emp1.pay += Employee.give_diwali_bonus()
#
#
#
# emp1.display()
# emp2.display()
#
# emp1.get_raise_amount()
#
# emp1.set_raise_amount(1.1)
#
# Employee.get_raise_amount()
#
# Employee.annoucing_lockdown()
#
# emp1.modify_date(emp1.joining_date)
# emp2.modify_date("4,5,2020")
# emp3.modify_date(emp1.joining_date)




