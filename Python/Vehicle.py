# kelas Vehicle merupakan parent dari kelas Ship dan Airplane
class Vehicle:
    # constructor
    def __init__(self):
        self.__name = ""            # nama kendaraan (string)
        self.__fuelType = ""        # tipe bahan bakar kendaraan (string)
        self.__maxPassengers = 0    # maksimal jumlah penumpang kendaraan (integer)
        self.__velocity = 0         # kecepatan kendaraan (float)
    
    # setter and getter
    def setVehicle(self, name, fuelType, maxPassengers, velocity):
        self.__name = name
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
        self.__velocity = velocity

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType
    
    def getFuelType(self):
        return self.__fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def getMaxPassengers(self):
        return self.__maxPassengers

    def setVelocity(self, velocity):
        self.__velocity = velocity
    
    def getVelocity(self):
        return self.__velocity

    # method
    def move(self):
        print("The " + str(self.__name) + " is moving at " + str(self.__velocity) + " knots")

    def printVehicle(self):
        print("Name                     : " + str(self.__name))
        print("Fuel Type                : " + str(self.__fuelType))
        print("Max Passengers           : " + str(self.__maxPassengers) + " Passengers")
