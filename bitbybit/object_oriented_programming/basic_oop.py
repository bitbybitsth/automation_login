class Car:
    """
    This class represents car, its data & operations
    """

    def __init__(self, mk, clr, amount, seats, type):
        self.make = mk
        self.color = clr
        self.price = amount
        self.seats = seats
        self.type = type
        self.repair = False

    def sell(self):
        if self.make == "tata":
            self.price -=20000
        print("Car sold")

    def service(self):
        print("Engine is healthy, Oil is filled to, Tyres are good")
        self.repair = True

    @property
    def is_serviced(self):
        if self.repair:
            return True
        else:
            return False




indica = Car(mk="tata", clr="black", amount=500000, seats=4, type="manual")

indica.service()


print("Car is serviced:", indica.is_serviced)

#
# class TataVehicle(Car):
#
#     def service(self):
#         print("service of tata is done")
#
#     def insurance(self):
#         print("You car is insured")
#
#
# class SpareParts:
#
#     def __init__(self, s):
#         self.spark_plug = s
#
# # t_car = TataVehicle(a="Tata", c=500000)
# # t_car.sell()
# # t_car.service()
# # t_car.insurance()
#
# # class Nexon(TataVehicle):
# #
# #     # def insurance(self):
# #     #     print("we are providing AXA insurance to car")
# #     #     super().insurance()
#
#
# # # nexon = Nexon(make="tata", price=500000)
# # nexon.sell()
# # nexon.service()
# # nexon.insurance()
#
#
# # def add(a, b):
# #     print("First add")
# #
# #
#
# # def add(a,b):
# #     print("second add")
#
# # add(10,20)
# # add("hi", "hello")
#
#
