# kelas Ship merupakan child dari kelas Vehicle
from Vehicle import Vehicle

class Ship(Vehicle):
    # constructor
    def __init__(self):
        super().__init__()
        self.__age = 0                      # umur kapal (integer)
        self.__type = ""                    # tipe kapal (string)
        self.__countryOfManufacture = ""    # negara pembuat (string)
    
    # setter and getter
    def setShip(self, name, fuelType, maxPassengers, velocity, age, type, countryOfManufacture):
        self.setVehicle(name, fuelType, maxPassengers, velocity)
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setCountryOfManufactur(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    # method
    def printShip(self):
        self.printVehicle()
        print("Ship Age                 : " + str(self.__age) + " Years Old")
        print("Ship Type                : " + str(self.__type))
        print("County of Manufacture    : " + str(self.__countryOfManufacture))
        self.move()