# kelas Person adalah parent dari kelas Driver
class Person:
    # constructor
    def __init__(self):
        self.__nik = ""      # menampung NIK (string)
        self.__name = ""     # menampung nama (string)
        self.__isMale = True   # menampung jenis kelamin (boolean, True untuk Male, False untuk Femail)

    # setter and getter
    def setPerson(self, nik, name, isMale):
        self.__nik = nik
        self.__name = name
        self.__isMale = isMale

    def setNIK(self, nik):
        self.__nik = nik

    def getNIK(self):
        return self.__nik

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setisMale(self, isMale):
        self.__isMale = isMale

    def getisMale(self):
        return self.__isMale

    # method
    def sleep(self):
        print(self.__name + " is sleeping right now.")

    def printPerson(self):
        print("NIK              : " + str(self.__nik))
        print("Name             : " + str(self.__name))
        print("Gender           :", end=" ")
        if self.__isMale is True:
            print("Male")
        else:
            print("Female")