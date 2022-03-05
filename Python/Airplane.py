# kelas Airplane merupakan child dari kelas Vehicle
from Vehicle import Vehicle

class Airplane(Vehicle):
    # contructor
    def __init__(self):
        super().__init__()
        self.__age = 0          # umur pesawat (integer)
        self.__type = ""        # tipe pesawat (string)
        self.__wingsLength = 0  # panjang sayap pesawat (float) (dalam meter)

    # setter and getter
    def setAirplane(self, name, fuelType, maxPassengers, velocity, age, type, wingsLength):
        self.setVehicle(name, fuelType, maxPassengers, velocity)
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return self.__wingsLength

    # method
    def printAirplane(self):
        self.printVehicle()
        print("Airplane Age             : " + str(self.__age) + " Years Old")
        print("Airplane Type            : " + str(self.__type))
        print("Wings Length             : " + str(self.__wingsLength) + " Meters")
        self.move()