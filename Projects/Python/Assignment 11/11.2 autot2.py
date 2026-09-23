autot = []
class Auto:
    def __init__(self, rekisteri, maxspd, spd=0, matka=0):
        self.rekisteri = rekisteri
        self.maxspd = maxspd
        self.spd = spd
        self.matka = matka
    def tulosta_tiedot(self):
        print(f"{auto.rekisteri}, {auto.maxspd}, {auto.spd}, {auto.matka}")

class Sähköauto(Auto):
    def __init__(self, rekisteri, maxspd, akkukwh, spd=0, matka=0):
        self.akkukwh = akkukwh
        super().__init__(rekisteri, maxspd, spd, matka)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akkukapasiteetti kw/h: {self.akkukwh}")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, maxspd, tankkilitrat, spd=0, matka=0):
        self.tankkilitrat = tankkilitrat
        super().__init__(rekisteri, maxspd, spd, matka)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Bensatankin koko litroina: {self.tankkilitrat}")

auto = Auto
sähkö = Sähköauto("ABC-15", 180, 52.5, 120)
poltto = Polttomoottoriauto("ACD-123", 165, 32.3, 150)
autot.append(sähkö)
autot.append(poltto)
for auto in autot:
    tunnit = 3
    auto.matka += tunnit * auto.spd
    auto.tulosta_tiedot()