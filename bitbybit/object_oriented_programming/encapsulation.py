class Car:

    def __init__(self, brand, color, engine, pistons):
        self.brand = brand
        self.color = color
        self._engine = engine
        self.__pistons = pistons

    def get_pistons(self):
        return self.__pistons

    def set_pistons(self, nw_pi):
        print(self.__pistons)
        self.__pistons = nw_pi
        print(self.__pistons)

    def __repair_pistons(self):
        print("Repairing pistons")

    def service(self):
        self.__repair_pistons()






indica = Car(brand="tata", color="red", engine="v4", pistons=4)

print(indica._engine)
print(indica.color)
print(indica.__pistons)





