import random
autot = []
reknum = 1
class Auto:
    def __init__(self, rekisteri, maxspd: int, spd=0, matka=0):
        self.rekisteri = rekisteri
        self.maxspd = maxspd
        self.spd = spd
        self.matka = matka
    def kiihdytä(self, kmh):
        self.spd += kmh
        if self.spd > self.maxspd:
            self.spd = self.maxspd
        elif self.spd < 0:
            self.spd = 0
        return self.spd
    def kulje(self, hour):
        self.matka += hour * self.spd
class Kilpailu:
    def __init__(self, nimi, pituus):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = autot
        self.tunti = 0
    def tunti_kuluu(self):
        self.tunti += 1
        for auto in self.osallistujat:
            kiihdytys = random.randint(-10,15)
            auto.kiihdytä(kiihdytys)
            auto.kulje(1)
    def tulosta_tilanne(self):
        for auto in self.osallistujat:
            print(f"Rekisteri {auto.rekisteri}, Maksiminopeus {auto.maxspd} km/h, Lopullinen nopeus {auto.spd} km/h, Kuljettu matka {auto.matka} kilometriä")
    def kilpailu_ohi(self):
        for auto in self.osallistujat:
            if auto.matka >= self.pituus:
                return True
        return False
for i in range(10):
    rekisteri = f"ABC-{reknum}"
    maxnopeus = random.randint(100,200)
    autot.append(Auto(rekisteri, maxnopeus))
    reknum = reknum + 1
kilpailu = Kilpailu("Suuri romuralli", 8000)
kilpailu.tulosta_tilanne()
kilpailu_true = True
while kilpailu_true:
    kilpailu.tunti_kuluu()
    kilpailu.kilpailu_ohi()
    if kilpailu.kilpailu_ohi() == True:
        kilpailu_true = False
    if kilpailu.tunti % 10 == 0:
        print(f"Tunti {kilpailu.tunti}")
        kilpailu.tulosta_tilanne()
        print()
print("Kilpailu päättynyt")
print("Tulokset")
autot.sort(key=lambda x: x.matka, reverse=True) 
kilpailu.tulosta_tilanne()