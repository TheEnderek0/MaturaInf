from struct import Struct

class Adres():
    def __init__(self):
        self.miejscowosc = ""
        self.nrdomu = 0
        self.nrmieszkania = 0
        self.kodpocztowy = ""
        self.ulica = ""

    def __repr__(self):
        if self.nrmieszkania:
            return f"{self.kodpocztowy} {self.miejscowosc}, {self.ulica} {self.nrdomu}/{self.nrmieszkania}"
        else:
            return f"{self.kodpocztowy} {self.miejscowosc}, {self.ulica} {self.nrdomu}"

class Wpis():
    def __init__(self):
        self.numer = 0
        self.imie = ""
        self.nazwisko = ""
        self.adres: Adres = None

    def __repr__(self):
        return f"{self.numer} | {self.imie} {self.nazwisko} | {self.adres}"


    def Serialize(self, file):
        pass
