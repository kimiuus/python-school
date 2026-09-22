import random
autot = []
reknum = 1
kilpailu = True
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
for i in range(10):
    rekisteri = f"ABC-{reknum}"
    maxnopeus = random.randint(100,200)
    autot.append(Auto(rekisteri, maxnopeus))
    reknum = reknum + 1
while kilpailu:
    for auto in autot:
        kiihdytys = random.randint(-10,15)
        auto.kiihdytä(kiihdytys)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu = False
print("Kilpailu päättynyt.")
autot.sort(key=lambda x: x.matka, reverse=True) 
for auto in autot:
    print(f"Rekisteri {auto.rekisteri}, Maksiminopeus {auto.maxspd} km/h, Lopullinen nopeus {auto.spd} km/h, Kuljettu matka {auto.matka} kilometriä")