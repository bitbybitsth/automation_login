

class Car:
    """
        User defined datatype, used to details of different cars, properties are id, color, brand, milegae
        operation are sell, service
    """


    def __init__(self, cid, brand, color, mileage, price, seats, type, fuel_capacity):
        self.cid = cid
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.price = price
        self.seats = seats
        self.type = type
        self.fuel_capacity = fuel_capacity


    def sell(self):
        self.price = self.price * 1.05
        print(f"Car sold for {self.price}")

    def service(self):
        print(f"{self.brand}'s {self.color} Car is serviced")

    def __str__(self):
        return f"\nBrand -> {self.brand}\n" \
               f"Color -> {self.color}\n" \
               f"Mileage -> {self.mileage}\n" \
               f"Price -> {self.price}\n" \
               f"Seats -> {self.seats}\n" \
               f"Type -> {self.type}"

    def __repr__(self):
        return str(self)


class Sedan:
    """
        User defined datatype, used to details of different cars, properties are id, color, brand, milegae
        operation are sell, service
    """


    def __init__(self, cid, brand, color, mileage, price, seats, type, fuel_capacity):
        self.cid = cid
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.price = price
        self.seats = seats
        self.type = type
        self.fuel_capacity = fuel_capacity


    def sell(self):
        self.price = self.price * 1.05
        print(f"Car sold for {self.price}")

    def service(self):
        print(f"{self.brand}'s {self.color} Car is serviced")

    def __str__(self):
        return f"\nBrand -> {self.brand}\n" \
               f"Color -> {self.color}\n" \
               f"Mileage -> {self.mileage}\n" \
               f"Price -> {self.price}\n" \
               f"Seats -> {self.seats}\n" \
               f"Type -> {self.type}"

    def __repr__(self):
        return str(self)

# indicia = Car(10, "tata", color="black", price=50000, seats=6, type="M", fuel_capacity=40, mileage=25)

# indicia.airbag = True


class CarCRUD:

    list_of_cars = []

    def add_car(self, car):
        self.list_of_cars.append(car)

    def get_car(self, cid):
        for car in self.list_of_cars:
            if car.cid == cid:
                return car

    def update_car(self, s_cid, new_car):
        for car in self.list_of_cars:
            if car.cid == s_cid:
                car.brand = new_car.brand
                car.color = new_car.color
                car.mileage = new_car.mileage
                car.price = new_car.price
                car.seats = new_car.seats
                car.type = new_car.type
                car.fuel_capacity = new_car.fuel_capacity

    def delete_car(self, cid):
        for car in self.list_of_cars:
            if car.cid == cid:
                self.list_of_cars.remove(car)

    def all_cars(self):
        for car in self.list_of_cars:
            print(car)

cc = CarCRUD()

indica = Car(cid=1, brand="Tata", color="White", price=600000, fuel_capacity=30, seats=5, type="manual", mileage=17)
nexon = Car(cid=2, brand="Tata", color="Blue-Lime", price=600000, fuel_capacity=30, seats=5, type="manual", mileage=17)
i20 = Car(cid=3, brand="Hundayi", color="Red", price=700000, fuel_capacity=30, seats=4, type="manual", mileage=14)

cc.add_car(indica)
cc.add_car(nexon)
cc.add_car(i20)

# old_car = cc.get_car(cid=2)
# print(old_car)
#
# new_car = Car(cid=2, brand="Tata", color="Black", price=700000, fuel_capacity=30, seats=4, type="manual", mileage=14)
# cc.update_car(s_cid=2, new_car=new_car)
#
# updated_car = cc.get_car(cid=2)
# print(updated_car)

cc.delete_car(2)
cc.all_cars()










# indica = Car(brand="Tata", color="White", price=600000, fuel_capacity=30, seats=5, type="manual", mileage=17)
# nexon = Car(brand="Tata", color="Blue-Lime", price=600000, fuel_capacity=30, seats=5, type="manual", mileage=17)

# indica.service()


