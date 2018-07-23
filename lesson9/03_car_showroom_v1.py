class Car:

    def __init__(self, model, year, price, *Additional):
        super().__init__()
        self.model = model
        self.year = year
        self.price = price
        self.Additional = Additional

    def __str__(self):
        return "[" + self.model + "] [" + self.year + "] [" + self.price + "] [" + str(self.Additional) + "]"

    def __repr__(self):
        return  ("{}('{}' '{}' '{}' '{}')".format(self.__class__.__name__, self.model, self.year, self.price, self.Additional))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

# -------------------------------------------------------
class CarShowroom:

    def __init__(self, *cars):
        self.cars = list(cars)

    def __str__(self):
        return "[ " + self.__class__.__name__ + " ] [ " + str(self.cars) + " ]" 
        
    def __repr__(self):
        return  ("{}('{}')".format(self.__class__.__name__, self.cars))

    def add_car(self, name):
        self.cars.append(name)

    def show_cars(self):
        for car in self.cars:
            print(car)

    def sell(self, name):
        self.cars.remove(name)
        
# --------------------------------------------------------

bmw = Car("X3", "2016", "30000", "Full compl")
bmw1 = Car("X5", "2017", "50000", "Full compl+")

shop = CarShowroom(bmw, bmw1)
shop.show_cars()
print("--------------------------------------")
mazda = Car("3", "2015", "15000", "Base compl")
shop.add_car(mazda)
shop.show_cars()
print("--------------------------------------")
shop.sell(bmw)
shop.show_cars()
print("--------------------------------------")
print(shop)