from Ship import Ship
from Airplane import Airplane
from Driver import Driver

# SHIP CLASS
ship = [Ship() for i in range(0,5)]
ship[0].setShip("Ever Given", "Diesel", 1000, 22.8, 4, "Cargo Ship", "Japan")
ship[1].setShip("Symphony of the Seas", "Diesel", 5400, 22, 4, "Cruise Ship", "France")
ship[2].setShip("Mardi Gras", "Liquefied Natural Gas", 5200, 23, 1, "Cruise Ship", "Bahamas")
ship[3].setShip("Iona", "Liquefied Natural Gas", 5200, 17, 2, "Cruise Ship", "United Kingdom")
ship[4].setShip("Spectrum of the Seas", "Diesel", 4100, 22, 3, "Cruise Ship", "Germany")

print("                     SHIP DATA                     ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    ship[i].printShip()
    print("---------------------------------------------------")
print("===================================================")

print("                    VEHICLE DATA                   ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    ship[i].printVehicle()
    print("---------------------------------------------------")
print("===================================================")

# AIRPLANE CLASS
airplane = [Airplane() for i in range(0,5)]
airplane[0].setAirplane("Lockheed Martin F-35 Lightning II", "AVTUR", 1, 1042.771, 16, "Fighter Jet", 10.7)
airplane[1].setAirplane("Airbus A380-800", "Kerosene", 853, 593.4125, 4, "Commercial Aircraft", 80)
airplane[2].setAirplane("Boeing 747-8", "Kerosene", 467, 533.477, 12, "Commercial Aircraft", 68)
airplane[3].setAirplane("Boeing 777-300", "Jet Fuel", 394, 512.95, 29, "Commercial Aircraft", 61)
airplane[4].setAirplane("Airbus A350-900", "Aviation Kerosene", 350, 510.2, 12, "Commercial Aircraft", 65)

print("                   AIRPLANE DATA                   ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    airplane[i].printAirplane()
    print("---------------------------------------------------")
print("===================================================")

print("                    VEHICLE DATA                   ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    airplane[i].printVehicle()
    print("---------------------------------------------------")
print("===================================================")

# DRIVER CLASS
driver = [Driver() for i in range(0,5)]
driver[0].setDriver("1000412", "Johnny", True, "41265144", "PT. Wibu Sejahtera", "Employee", "1964126", "12-12-2025", "Motorcycle")
driver[1].setDriver("8764124", "Sins", False, "214165412", "PT. Gopud", "Employee", "241786412", "08-10-2027", "Motorcycle")
driver[2].setDriver("1905642", "Kang Galon", True, "412478641", "PT. Greb", "Employee", "24176414", "01-23-2024", "Truck")
driver[3].setDriver("4218461", "Kang Cilok", True, "124741541", "PT. Seblack Utama", "Employee", "12417641", "02-28-2023", "Car")
driver[4].setDriver("1276641", "Yuuka", False, "417654145", "Weebs Inc.", "CEO", "41274612", "10-25-2028", "Car")

print("                     DRIVER DATA                   ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    driver[i].printDriver()
    print("---------------------------------------------------")
print("===================================================")

print("                    PERSON DATA                    ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    driver[i].printPerson()
    print("---------------------------------------------------")
print("===================================================")

print("                      JOB DATA                     ")
print("===================================================")
print("---------------------------------------------------")
for i in range(0,5):
    driver[i].printJob()
    print("---------------------------------------------------")
print("===================================================")