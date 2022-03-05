# kelas Driver adalah child dari kelas Person dan Job
from Person import Person
from Job import Job

class Driver(Person, Job):
    # constructor
    def __init__(self):
        super().__init__()
        self.__licenseID = ""   # menampung license id
        self.__activeUntil = "" # menampung tanggal aktif sampai
        self.__vehicleType = "" # menampung tipe kendaraan

    # setter and getter
    def setDriver(self, nik, name, isMale, nip, companyName, position, licenseID, activeUntil, vehicleType):
        self.setPerson(nik, name, isMale)
        self.setJob(nip, companyName, position)
        self.__licenseID = licenseID
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID

    def getLicenseID(self):
        return self.__licenseID

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    # method
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print("License ID       : " + str(self.__licenseID))
        print("Active Until     : " + str(self.__activeUntil))
        print("Vehicle Type     : " + str(self.__vehicleType))
        self.sleep()