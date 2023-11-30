from datetime import datetime, timedelta
from abc import ABC, abstractmethod


class Szoba(ABC):
    def __init__(self, szobaszam):
        self.szobaszam = szobaszam


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam)
        self.ar = ar
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam)
        self.ar = ar
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, kezdo_datum, veg_datum):
        self.szoba = szoba
        self.kezdo_datum = kezdo_datum
        self.veg_datum = veg_datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, kezdo_datum, veg_datum):
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas = Foglalas(szoba, kezdo_datum, veg_datum)
                self.foglalasok.append(foglalas)
                return f"A foglalás sikeres: {szobaszam}  {kezdo_datum}-tól {veg_datum}-ig. Az ár: {szoba.ar}"

        return f"Nincs ilyen szoba: {szobaszam}"

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return "Lemondás sikeres."

        return "Nincs ilyen foglalás."

    def listazas(self):
        return '\n'.join([f"Szoba: {foglalas.szoba.szobaszam}, Kezdő dátum: {foglalas.kezdo_datum}, Vég dátum: {foglalas.veg_datum}, Ár: {foglalas.szoba.ar}" for foglalas in self.foglalasok])


szoba1 = EgyagyasSzoba("1", 50)
szoba2 = KetagyasSzoba("2", 43)
szoba3 = EgyagyasSzoba("3", 80)

szalloda = Szalloda("HotelH")
szalloda.add_szoba(szoba1)
szalloda.add_szoba(szoba2)
szalloda.add_szoba(szoba3)

foglalas_kezelo = FoglalasKezelo(szalloda)

foglalas_kezelo.foglalas("1", datetime(2023, 6, 5), datetime(2023, 6, 6))
foglalas_kezelo.foglalas("2", datetime(2023, 3, 2), datetime(2023, 3, 3))
foglalas_kezelo.foglalas("3", datetime(2023, 8, 31), datetime(2023, 9, 1))
foglalas_kezelo.foglalas("1", datetime(2023, 11, 24), datetime(2023, 11, 25))
foglalas_kezelo.foglalas("2", datetime(2023, 12, 9), datetime(2023, 12, 10))


# print(foglalas_kezelo.listazas())

foglalas_kezelo.lemondas(foglalas_kezelo.foglalasok[0])

kezdes = int(input("1. Foglalások listázása, 2. Új foglalas, 3. Foglalas lemondása, 4. Kilépés "))

match kezdes:
    case 1:
        print("Jelenlegi foglalasok:")
        print(foglalas_kezelo.listazas())
    case 2:
        szobaszam = input("Adja meg a szobaszámot: ")
        erkezes_datuma = input("Adja meg a kezdő dátumát (yyyy-mm-dd): ")
        tavozas_datuma = input("Adja meg a távozás dátumát (yyyy-mm-dd): ")
        kezdo_datum = datetime.strptime(erkezes_datuma, '%Y-%m-%d')
        veg_datum = datetime.strptime(tavozas_datuma, '%Y-%m-%d')
        foglalas_kezelo.foglalas(szobaszam, kezdo_datum, veg_datum)
        print(foglalas_kezelo.foglalas(szobaszam, kezdo_datum, veg_datum))


    case 3:
        foglalszam = int(input("Adja meg a foglalási számot: "))
        foglalas_kezelo.lemondas(foglalas_kezelo.foglalasok[foglalszam])
        print(foglalas_kezelo.lemondas(foglalas_kezelo.foglalasok[foglalszam]))
        print(foglalas_kezelo.listazas())
    case 4:
        print("Viszlát!")

